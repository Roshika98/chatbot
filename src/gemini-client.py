import os

from google import genai
from google.genai import types
from models.response_model import ResponseModel


def get_chat_config() -> types.GenerateContentConfig:
    return types.GenerateContentConfig(temperature=0.9, top_p=0.95, top_k=40, max_output_tokens=8192,
                                       response_schema=ResponseModel)


class GeminiClient:
    def __init__(self):
        self.client = genai.Client(
            api_key=os.environ["GEMINI_API_KEY"],
            enterprise=False
        )

    def create_chat(self, prompt: str):
        chat = self.client.chats.create(model="", config=get_chat_config())
        chat.send_message(prompt)
        return chat
