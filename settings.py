import os
from dotenv import load_dotenv

load_dotenv()

TIMEDOCTOR_EMAIL = os.getenv("TIMEDOCTOR_EMAIL") if os.getenv("TIMEDOCTOR_EMAIL") != '' else None
TIMEDOCTOR_PASSWORD = os.getenv("TIMEDOCTOR_PASSWORD") if os.getenv("TIMEDOCTOR_PASSWORD") != '' else None