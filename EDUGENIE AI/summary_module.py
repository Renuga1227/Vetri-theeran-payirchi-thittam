from gemini_client import generate_text


def summarize_text(text: str) -> str:
    text = text.strip()

    if not text:
        raise ValueError("Text cannot be empty.")

    prompt = f"""
You are EduGenie, an educational summarization assistant.

Summarize the following educational passage.

Passage:
{text}

Requirements:
- Keep the important information.
- Remove repetition.
- Use simple language.
- Make it useful for quick revision.
- Use a short heading.
- Use bullet points where appropriate.
- Do not add unsupported facts.
"""

    return generate_text(prompt)