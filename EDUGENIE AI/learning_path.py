from gemini_client import generate_text


def get_learning_recommendations(topic: str) -> str:
    topic = topic.strip()

    if not topic:
        raise ValueError("Topic cannot be empty.")

    prompt = f"""
You are EduGenie, a personalized learning assistant.

Create a structured learning path for:
{topic}

Use the following structure:

1. Learning Goal

2. Beginner Level
   - Topics to learn
   - Practice activities

3. Intermediate Level
   - Topics to learn
   - Practice activities

4. Advanced Level
   - Topics to learn
   - Practice activities

5. Suggested Timeline

6. Recommended Learning Resources
   - Books
   - Videos
   - Documentation
   - Courses

7. Progress Check

Make the path practical and easy to follow.
Do not invent specific URLs.
"""

    return generate_text(prompt)