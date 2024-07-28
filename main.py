import random
import time

import mesop as me
import mesop.labs as mel
from app import get_response

def on_load(e: me.LoadEvent):
    pass

@me.page(
    title="Mesop Demo Chat",
    on_load=on_load,
)
def page():
    mel.chat(transform, title="LLM Bot Chat", bot_user="LLM Bot")

def transform(input: str, history: list[mel.ChatMessage]):
    yield get_response(input)
