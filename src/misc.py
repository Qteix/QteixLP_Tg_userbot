from pyrogram import Client
from src.config import api_id, api_hash

app = Client("my_account",api_id=api_id, api_hash=api_hash)