from motor.motor_asyncio import AsyncIOMotorClient

from config import MONGO_DB_URI

DBNAME = "CUTIEXMUSICBOTPT"

mongo = AsyncIOMotorClient(MONGO_DB_URI)
dbname = mongo[DBNAME]
