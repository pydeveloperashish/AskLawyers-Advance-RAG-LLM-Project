from FlagEmbedding import LLMEmbedder, FlagReranker # Al document present here https://github.com/FlagOpen/FlagEmbedding/tree/master
import os
import lancedb
import re
import pandas as pd
import random
from datasets import load_dataset
import torch
import gc
import lance
from lancedb.embeddings import with_embeddings
from data_retrieval import get_excerpt

task = "qa" # Encode for a specific task (qa, icl, chat, lrlm, tool, convsearch)
embed_model = LLMEmbedder('BAAI/llm-embedder', use_fp16=False) # Load model (automatically use GPUs)

reranker_model = FlagReranker('BAAI/bge-reranker-base', use_fp16=True) # use_fp16 speeds up computation with a slight performance degradation

# Re-rank Search Results using Re-ranker from BGE Reranker
# Pass all the results to a stronger model to give them the similarity ranking

def get_reranked_docs(query):
  old_docs = get_excerpt(query) 
  df_old_docs = pd.DataFrame(old_docs, columns=["Excerpts"])
  torch.cuda.empty_cache()
  gc.collect()
  df_old_docs["new_scores"] = reranker_model.compute_score([[query,chunk] for chunk in df_old_docs['Excerpts']]) # Re compute ranks
  df_old_docs.sort_values(by = "new_scores", ascending = False).reset_index(drop = True)
  return df_old_docs['Excerpts']

# print("get_reranked_docs: ", get_reranked_docs(query = "what is indian panel code?"))