import os

DEV = os.environ.get("DEV", True)
HOST = os.environ.get("HOST", "::")
PORT = os.environ.get("PORT", "8080")