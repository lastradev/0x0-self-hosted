import os

SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")

if os.getenv("MAX_SIZE"):
    MAX_CONTENT_LENGTH = int(os.getenv("MAX_SIZE")) * 1024 * 1024
