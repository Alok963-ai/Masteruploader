#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "26572696"))
API_HASH = environ.get("API_HASH", "67a8947a3e1b15f9ef9684286baa34cb")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
AUTH_USER = os.environ.get('AUTH_USERS', '7903596276').split(',') 
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
HOST = "https://drm-api-six.vercel.app"
CREDIT = " 𝙎𝘼𝙄𝙉𝙄 𝘽𝙊𝙏𝙎"
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
