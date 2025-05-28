import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    API_ID = int(os.environ.get("26572696"))
    API_HASH = os.environ.get("67a8947a3e1b15f9ef9684286baa34cb")
    AUTH_USER = os.environ.get('AUTH_USERS', '7903596276').split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
    HOST = "https://drm-api-six.vercel.app"
    CREDIT = " Kakabots"
