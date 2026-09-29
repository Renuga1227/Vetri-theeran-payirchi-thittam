import os
from dotenv import load_dotenv

load_dotenv()

MODEL_NAME = os.getenv(
    "LOCAL_MODEL_NAME",
    "MBZUAI/LaMini-Flan-T5-783M"
)


def explain_topic(topic: str) -> str:
    if not topic or not topic.strip():
        return "Please enter a topic to explain."

    try:
        from transformers import pipeline

        generator = pipeline(
            "text2text-generation",
            model=MODEL_NAME
        )

        prompt = (
            f"Explain the topic '{topic}' in simple and easy language. "
            "Give a short definition, important points, and one simple example."
        )

        result = generator(
            prompt,
            max_new_tokens=256,
            do_sample=False
        )

        return result[0]["generated_text"]

    except Exception as e:
        return f"Explanation error: {str(e)}"