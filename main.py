import asyncio
from tgbot.services.scheduler import start_scheduler
from tgbot.publicating import articles
from config import dp, bot

from tgbot.handlers import start
import tgbot.handlers.ad_pic_handler
import tgbot.handlers.ad_text_handler
import tgbot.handlers.ad_pubtime_handler
import tgbot.handlers.ad_type_handler
import tgbot.handlers.ad_top_hours_handler
import tgbot.handlers.calendar_handler
import tgbot.handlers.pay_handler


async def main():
    dp.include_router(articles.router)  # Регистрируем router из articles.py
    await start_scheduler()
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
