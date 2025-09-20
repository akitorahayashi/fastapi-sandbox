import os
import sys
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Add the project root to sys.path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
