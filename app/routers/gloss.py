from fastapi import APIRouter, Request
from google import genai
from google.genai import types
from utils.config import settings

router = APIRouter(
    prefix="/generate_gloss"
)

client = genai.Client(
    api_key=settings.GEMINI_API_KEY
)

def generate_response(question: str) -> str | None:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""You are an expert translator specializing in Indian Sign Language (ISL) gloss.
        Your primary goal is to provide ONLY the ISL gloss translation. Do not add any extra explanations.
        Don't use any punctuation marks and Special Symbols, and do not include any additional text.

        USER'S SENTENCE:
        {question}

        ISL GLOSS TRANSLATION:""",
        config={
            "thinking_config": {
                "thinking_budget": 1024,
                "include_thoughts": False
        }
        }
    )

    return response.text

@router.post("/")
async def generate_gloss(request: Request) -> str | None:
    body = await request.json()
    response: str | None = generate_response(body['text'])
    return response