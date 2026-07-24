import os
from dotenv import load_dotenv
from google import genai
import json

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_question(topic, difficulty, style):

    prompt = f"""
You are an expert technical interviewer.

Topic: {topic}
Difficulty: {difficulty}
Interview Style: {style}

Generate exactly ONE interview question.

Do not provide the answer.
Only return the question.
"""

    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=prompt,
    )

    return response.text

def generate_next_question(previous_question, user_answer):

    prompt = f"""
You are an expert technical interviewer.

Previous Question:
{previous_question}

Candidate's Answer:
{user_answer}

Analyze the candidate's answer.

If the answer is partially correct or incorrect, ask a follow-up question based on the same topic.

If the answer is good, ask the next interview question on the same topic.

Only return the next interview question.
Do not explain.
Do not give feedback.
Do not use bullet points.
"""

    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=prompt,
    )

    return response.text


def generate_report(interview_history):

    prompt = f"""
You are an expert technical interviewer.

Below is the complete interview history.

{json.dumps(interview_history, indent=2)}

Evaluate the candidate and return ONLY valid JSON.

Use this format exactly:

{{
  "overall": 78,
  "recommendation": "Lean Hire",
  "technical": 82,
  "communication": 74,
  "problem_solving": 80,
  "confidence": 65,

  "strengths": [
    "...",
    "...",
    "..."
  ],

  "weaknesses": [
    "...",
    "...",
    "..."
  ],

  "feedback": "Overall feedback about the candidate."
}}

Return ONLY JSON.
No markdown.
No explanation.
"""

    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=prompt,
    )

    text = response.text.strip()

    # Remove Markdown fences if Gemini adds them
    text = text.replace("```json", "").replace("```", "").strip()

    return json.loads(text)