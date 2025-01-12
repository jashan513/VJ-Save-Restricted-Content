import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7776870492:AAHglTpmX4OCbEPS8CpIpyYGhj3OmD6Wv84")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "20988890"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "c48d0549a594dbd7ce61caf3c604e05d")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "7461799540"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://rs92573993688:pVf4EeDuRi2o92ex@cluster0.9u29q.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", Cluster0"")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
