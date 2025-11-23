import os
import subprocess
from dotenv import load_dotenv

load_dotenv()

FOLDER_URL = os.getenv("FOLDER_URL")
OUTPUT_DIR = "images"

subprocess.run([
    "gdown",
    "--folder",
    "--remaining-ok",
    FOLDER_URL,
    "-O",
    OUTPUT_DIR
])


print("Downloaded successfully!")