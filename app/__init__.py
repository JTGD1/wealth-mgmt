import os
from dotenv import load_dotenv
from flask import Flask

load_dotenv()

CLIENT_NAME = os.getenv("CLIENT_NAME", default="Sir or Madam")
