import psycopg2

from dotenv import load_dotenv
import os

load_dotenv()

conn = psycopg2.connect(
    database=os.getenv("database"),
    user=os.getenv("user"),
    password=os.getenv("password"),
    host='172.26.0.2',
    port='5432'
)

# Creating a cursor object using the cursor() method
cursor = conn.cursor()



