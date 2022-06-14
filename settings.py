import os
from dotenv import load_dotenv

load_dotenv()

ACCESS_KEY = str(os.getenv("ACCESS_KEY"))
SECRET_KEY = str(os.getenv("SECRET_KEY"))