import os
from PyPDF2 import PdfReader, PdfWriter

def split_pdf(input_pdf, chunk_size):
    input_path = input_pdf
    input_basename = os.path.basename(input_path)
    input_name, input_ext = os.path.splitext(input_basename)
    
    output_folder = os.path.join(os.path.dirname(input_path), input_name + '_chunks')
    os.makedirs(output_folder, exist_ok=True)
    
    with open(input_path, 'rb') as input_file:
        pdf_reader = PdfReader(input_file)
        num_pages = len(pdf_reader.pages) 
        
        for i in range(0, num_pages, chunk_size):
            pdf_writer = PdfWriter()
            chunk_start = i
            chunk_end = min(i + chunk_size, num_pages)
            
            for page_num in range(chunk_start, chunk_end):
                pdf_writer.add_page(pdf_reader.pages[page_num])
            
            output_pdf = os.path.join(output_folder, f'{input_name}_chunk_{i//chunk_size + 1}.pdf')
            with open(output_pdf, 'wb') as output_file:
                pdf_writer.write(output_file)
    
    print(f'PDF split into {num_pages // chunk_size + 1} chunks in folder: {output_folder}')

# Example usage:
input_pdf = r'D:\LLM Projects\dataset\Indian Penal Code Book (2).pdf'
chunk_size = 10  # Number of pages per chunk
split_pdf(input_pdf, chunk_size)
