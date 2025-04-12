# Telegram Imges Download from a channel
#import telethon library
# Run as pyhon script
import os
import asyncio
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from telethon import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.types import InputMessagesFilterPhotos

api_id = 'your_api_id'#don't use quotations
api_hash = 'your api hash'
phone_number = 'your phone number in international format'
# Example: +14155552671
channel_username = 'target telegram UserName'
download_folder = 'C:\\Users\\Public\\Downloads'
#for Windows

os.makedirs(download_folder, exist_ok=True)

client = TelegramClient('my_session', api_id, api_hash)

async def download_photos():
    try:
        await client.start(phone_number)
        print("✅ Client connected successfully.")

        channel = await client.get_entity(channel_username)
        print(f"📢 Fetched channel: {channel.title}")

        # Fetch the latest 10 photos for debugging
        messages = await client.get_messages(channel, limit=30, filter=InputMessagesFilterPhotos)
        
        if not messages:
            print("❌ No photos found.")
            return

        print(f"📸 Found {len(messages)} photo messages.")

        for message in messages:
            print(f"➡️ Downloading photo from message ID: {message.id}")
            try:
                photo_path = await message.download_media(file=download_folder)
                if photo_path:
                    print(f"✅ Photo saved to: {photo_path}")
                else:
                    print(f"❌ Failed to download photo (Empty path).")
            except Exception as e:
                print(f"❌ Error downloading message {message.id}: {e}")

    except Exception as e:
        import traceback
        print(f"❌ Exception: {traceback.format_exc()}")
if __name__ == "__main__":
    asyncio.run(download_photos())
