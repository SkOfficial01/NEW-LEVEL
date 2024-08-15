from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_DB_URI
from ..logging import LOGGER

logger = LOGGER(__name__)

logger.info("Connecting to your Mongo Database...")
try:
    # Create the client instance
    _mongo_async_ = AsyncIOMotorClient(MONGO_DB_URI)
    
    # Access the desired database
    mongodb = _mongo_async_.get_database()  # Update this to your database name if needed

    # Test connection by executing a simple command
    asyncio.run(mongodb.command('m'))  # Ensure MongoDB is reachable

    logger.info("Connected to your Mongo Database.")
except Exception as e:
    logger.error(f"Failed to connect to your Mongo Database: {e}")
    exit()
    
