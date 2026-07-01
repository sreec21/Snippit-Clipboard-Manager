from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))

db = client["snippit_ai"]

users = db["users"]

snippets = db["snippits"]   # use this if you keep current collection name