import json
import os
import re

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY not found in .env")

client = OpenAI(api_key=api_key)


def parse_llm_json(content: str) -> dict:
    """
    Cleans and parses JSON returned by the LLM.
    Removes markdown code fences if present.
    """

    text = content.strip()

    # Remove ```json ... ```
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?\s*", "", text)
        text = re.sub(r"\s*```$", "", text.strip())

    try:
        return json.loads(text)

    except json.JSONDecodeError as e:
        raise ValueError(
            f"Failed to parse LLM JSON.\n\nResponse:\n{text}"
        ) from e