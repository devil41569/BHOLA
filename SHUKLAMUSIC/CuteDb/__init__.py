from motor.motor_asyncio import AsyncClient
from config import MONGO_DB_URI

DBNAME = "CUTIEXMUSICBOTPT"

mongo = AsyncClient(MONGO_DB_URI)
dbname = mongo[DBNAME]
