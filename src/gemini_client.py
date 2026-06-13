import os

import dotenv
from google import genai
from google.genai import types
from google.genai.chats import Chat

from src.models.response_model import ResponseModel

dotenv.load_dotenv()


def get_chat_config() -> types.GenerateContentConfig:
    return types.GenerateContentConfig(temperature=0.9, top_p=0.95, top_k=40, max_output_tokens=8192,
                                       response_schema=ResponseModel, response_mime_type="application/json")


class GeminiClient:
    def __init__(self):
        self.client = genai.Client(
            api_key=os.environ["GEMINI_API_KEY"],
            enterprise=False
        )

    def create_chat(self) -> Chat:
        chat = self.client.chats.create(model=os.environ["GEMINI_MODEL"],
                                        config=get_chat_config())
        return chat

    @staticmethod
    def send_message(chat: Chat, message: str):
        return chat.send_message(message)
