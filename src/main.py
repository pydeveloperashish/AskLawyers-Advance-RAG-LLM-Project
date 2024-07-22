from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from src.generate_answers import generate_answer
import os 

app = FastAPI()
template_folder_path = os.path.join(os.path.dirname(__file__), '..', 'templates')
static_folder_path = os.path.join(os.path.dirname(__file__), '..', 'static')

templates = Jinja2Templates(directory=template_folder_path)
# Mount static files
app.mount("/static", StaticFiles(directory=static_folder_path), name="static")


@app.get("/", response_class=HTMLResponse)
async def get_data(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/", response_class=HTMLResponse)
async def post_data(request: Request, Input: str = Form(...)):
    response = generate_answer(query = Input)
    data = {"message": response}
    return templates.TemplateResponse("index.html", {"request": request, "data": data})



# uvicorn main:app --reload