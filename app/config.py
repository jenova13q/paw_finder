import os
from dotenv import load_dotenv

load_dotenv()

#postgres
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_DB = os.getenv('POSTGRES_DB')
POSTGRES_HOST = os.getenv('POSTGRES_HOST', 'db')
POSTGRES_PORT = os.getenv('POSTGRES_PORT', 5432)

DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

#rabbitmq

#rabbitmq queue

#JWT
# SECRET_KEY = os.getenv('SECRET_KEY')
# ALGORITHM = os.getenv('ALGORITHM')
# ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES')

#bot
# BOT_TOKEN = os.getenv('BOT_TOKEN')
# BOT_PORT = os.getenv('BOT_PORT')

#model
# PREDICTION_COST = 50
# MODEL_PATH = os.getenv('MODEL_PATH')

#
DEBUG_MODE = os.getenv('DEBUG_MODE')