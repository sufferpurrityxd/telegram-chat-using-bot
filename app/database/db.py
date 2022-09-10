import os
import dotenv
dotenv.load_dotenv("../.env")
DATABASE_NAME = os.getenv("database_name")
DATABASE_PASSWORD = os.getenv("database_password")
DATABASE_USER = os.getenv("database_user")
DATABASE_HOST = os.getenv("database_host")
DATABASE_PORT = os.getenv("database_port")
