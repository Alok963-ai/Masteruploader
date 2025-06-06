import os
import asyncio
import logging
from config import Config
from pyrogram import Client as bot, idle

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S'
)
LOGGER = logging.getLogger(__name__)
LOGGER.info("Live log streaming to telegram.")

# Define plugins
plugins = dict(root="plugins")

# Main execution block
if __name__ == "__main__":
    # Ensure required environment variables are set
    try:
        bot = bot(
            "Bot",
            bot_token=Config.BOT_TOKEN,
            api_id=int(os.environ.get("API_ID", 0)),  # Default to 0 if not set
            api_hash=Config.API_HASH,
            sleep_threshold=120,
            plugins=plugins,
            workers=10,
        )
    except ValueError as e:
        LOGGER.error(f"Invalid API_ID: {e}")
        exit(1)  # Exit if API_ID is invalid

    async def main():
        await bot.start()
        bot_info = await bot.get_me()
        LOGGER.info(f"<--- @{bot_info.username} Started --->")
        
        # Send messages to authorized users
        for user_id in Config.AUTH_USERS:
            try:
                await bot.send_message(chat_id=user_id, text=f"__Congrats! You Are DRM member ... if You get any error then contact me -  {Config.CREDIT}__ ")
            except Exception as e:
                LOGGER.error(f"Failed to send message to user {user_id}: {e}")
                continue
        
        await idle()

    # Run the main function
    try:
        asyncio.get_event_loop().run_until_complete(main())
    except Exception as e:
        LOGGER.error(f"An error occurred: {e}")
    finally:
        LOGGER.info("<--- Bot Stopped --->")
