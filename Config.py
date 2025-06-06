import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    API_ID = int(os.environ.get("20288951"))
    API_HASH = os.environ.get("e8cb5fb7a475b5f5eb3b0ef0e6ca03a8")
    AUTH_USER = os.environ.get('AUTH_USERS', '7833842279').split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
    HOST = "https://drm-api-six.vercel.app"
    CREDIT = " Kakabots"
