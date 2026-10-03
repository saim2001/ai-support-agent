import json
import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

from .tools import get_order_status

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def get_order_status_tool(order_id: str) -> dict:
    """Get the status and details of a customer order."""
    return get_order_status(order_id)


def run_agent(user_message: str) -> str:

    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=user_message,
        config=types.GenerateContentConfig(
            system_instruction=(
                "You are a customer support assistant. "
                "Use the available tool when you need order information. "
                "Never invent order information."
            ),
            tools=[get_order_status_tool],
        ),
    )

    return response.text