from gemini_client import generate_text


def answer_question(question: str) -> str:
    question = question.strip()

    if not question:
        raise ValueError("Question cannot be empty.")

    prompt = f"""
You are EduGenie, an educational question-answering assistant.

Answer this question:
{question}

Rules:
- Give the direct answer first.
- Explain the answer clearly.
- Use simple student-friendly language.
- Use bullet points when useful.
- If the question is ambiguous, state the assumption.
- Do not invent sources or facts.
- Keep the answer educational and concise.
"""

    return generate_text(prompt)