import json
import re

from gemini_client import generate_text


def clean_json_block(text: str) -> str:
    text = text.strip()
    text = re.sub(r"^```(?:json)?\s*", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\s*```$", "", text)
    return text.strip()


def validate_quiz(data):
    if not isinstance(data, dict):
        raise ValueError("Quiz response must be an object.")

    if "questions" not in data:
        raise ValueError("Quiz response must contain questions.")

    questions = data["questions"]

    if not isinstance(questions, list):
        raise ValueError("Questions must be a list.")

    if len(questions) != 3:
        raise ValueError("Quiz must contain exactly 3 questions.")

    for question in questions:
        required_fields = [
            "question",
            "options",
            "correct_answer",
            "explanation"
        ]

        for field in required_fields:
            if field not in question:
                raise ValueError(f"Missing quiz field: {field}")

        if len(question["options"]) != 4:
            raise ValueError("Each question must contain 4 options.")

        if question["correct_answer"] not in question["options"]:
            raise ValueError("Correct answer must match an option.")

    return data


def generate_quiz(passage: str) -> dict:
    passage = passage.strip()

    if not passage:
        raise ValueError("Passage cannot be empty.")

    prompt = f"""
Create exactly 3 multiple-choice questions
from the educational material below.

Material:
{passage}

Return ONLY valid JSON.

Use exactly this structure:

{{
    "questions": [
        {{
            "question": "Question text",
            "options": [
                "Option A",
                "Option B",
                "Option C",
                "Option D"
            ],
            "correct_answer": "Option A",
            "explanation": "Short explanation"
        }}
    ]
}}

Rules:
- Exactly 3 questions.
- Exactly 4 options per question.
- Questions must be based on the supplied material.
- Distractors should be plausible.
- correct_answer must exactly match one option.
"""

    raw_response = generate_text(prompt, json_mode=True)

    cleaned = clean_json_block(raw_response)

    try:
        data = json.loads(cleaned)
        return validate_quiz(data)
    except (json.JSONDecodeError, ValueError, TypeError) as error:
        raise RuntimeError(f"Could not parse quiz response: {error}")