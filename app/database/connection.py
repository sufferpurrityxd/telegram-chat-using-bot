import asyncpg
from database.db import DATABASE_NAME, DATABASE_HOST, DATABASE_USER, DATABASE_PASSWORD, DATABASE_PORT


async def get_connection():
    connection = await asyncpg.connect(
        host=DATABASE_HOST,
        port=DATABASE_PORT,
        user=DATABASE_USER,
        database=DATABASE_NAME,
        password=DATABASE_PASSWORD
    )
    return connection
