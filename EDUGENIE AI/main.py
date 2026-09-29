import os
import sys

sys.path.insert(0,
os.path.dirname(os.path.abspath(__file__)))
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field

from explanation_module import explain_topic
from qna import answer_question
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import get_learning_recommendations
from config import APP_NAME, APP_VERSION


app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION
)


app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

templates = Jinja2Templates(directory="templates")


# -----------------------------
# Request Models
# -----------------------------

class TextRequest(BaseModel):
    text: str = Field(
        ...,
        min_length=1,
        max_length=50000
    )


class QARequest(BaseModel):
    question: str = Field(
        ...,
        min_length=1,
        max_length=10000
    )


# -----------------------------
# Home Page
# -----------------------------

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

   return templates.TemplateResponse(
    request=request,
    name="index.html",
    context={
        "app_name": APP_NAME,
        "version": APP_VERSION
    }
)


# -----------------------------
# Health Check
# -----------------------------

@app.get("/health")
async def health():

    return {
        "status": "ok",
        "app": APP_NAME,
        "version": APP_VERSION
    }


# -----------------------------
# Q&A API
# -----------------------------

@app.post("/qa")
async def qa(payload: QARequest):

    result = answer_question(
        payload.question
    )

    return {
        "success": True,
        "result": result
    }


# -----------------------------
# Explanation API
# -----------------------------

@app.post("/explain")
async def explain(payload: TextRequest):

    result = explain_topic(
        payload.text
    )

    return {
        "success": True,
        "result": result
    }


# -----------------------------
# Quiz API
# -----------------------------

@app.post("/quiz")
async def quiz(payload: TextRequest):

    result = generate_quiz(
        payload.text
    )

    return {
        "success": True,
        "result": result
    }


# -----------------------------
# Summary API
# -----------------------------

@app.post("/summarize")
async def summarize(payload: TextRequest):

    result = summarize_text(
        payload.text
    )

    return {
        "success": True,
        "result": result
    }


# -----------------------------
# Learning Path API
# -----------------------------

@app.post("/learn/recommendations")
async def recommendations(payload: TextRequest):

    result = get_learning_recommendations(
        payload.text
    )

    return {
        "success": True,
        "result": result
    }