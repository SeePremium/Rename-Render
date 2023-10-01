# Don't Remove Credit @seesmovies
# Subscribe YouTube Channel For Amazing Bot @thetechsup
# Ask Doubt on telegram @sunnyseee


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "29264299")

API_HASH = os.environ.get("API_HASH", "01715c2876c152106ceab149e4764ec5")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6362584126:AAHS8q9gogOuTAPY_b-p8nH7pWK3FxRARWI") 

FORCE_SUB = os.environ.get("FORCE_SUB", "Seerenamer") 

             # Don't Remove Credit @seesmovies
             # Subscribe YouTube Channel For Amazing Bot @thetechsup
             # Ask Doubt on telegram @sunnyseee

DB_NAME = os.environ.get("DB_NAME", "renamevjbot")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://tufanbhaix24:sunny12@cluster0.vrwi05k.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/file/a63662da0e85342651531.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5505094097').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @seesmovies
# Subscribe YouTube Channel For Amazing Bot @thetechsup
# Ask Doubt on telegram @sunnyseee
