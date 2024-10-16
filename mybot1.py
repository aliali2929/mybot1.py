from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler
import logging

# توکن ربات و نام کانال را وارد کنید
BOT_TOKEN = '7630593934:AAHIx7ePwrSlecXo413ye1lk9vfMWZqYUOk'  # توکن ربات خود را از BotFather وارد کنید
CHANNEL_USERNAME = '@Literally_Me7'  # نام کاربری کانالی که می‌خواهید کاربران عضو آن شوند

# تنظیمات لاگینگ
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

# تابعی که به درخواست /start پاسخ می‌دهد
async def start(update: Update, context):
    user_id = update.message.from_user.id
    
    try:
        # بررسی وضعیت کاربر در کانال
        chat_member = await context.bot.get_chat_member(chat_id=CHANNEL_USERNAME, user_id=user_id)
        
        if chat_member.status in ['member', 'administrator', 'creator']:
            # ارسال ویدیو اگر کاربر عضو کانال باشد
            video_url = "https://www.learningcontainer.com/wp-content/uploads/2020/05/sample-mp4-file.mp4"  # لینک مستقیم ویدیو را اینجا قرار دهید
            await context.bot.send_video(chat_id=user_id, video=video_url)
            await update.message.reply_text("ویدیو با موفقیت ارسال شد!")
        else:
            await update.message.reply_text(f"لطفاً ابتدا عضو کانال {'@Literally_Me7'} شوید تا ویدیو را دریافت کنید.")
    
    except Exception as e:
        logger.error(f"Error: {e}")
        await update.message.reply_text("زاهد ببین بزار فردا برم مدرسه")

if __name__ == '__main__':
    # ساخت اپلیکیشن و اضافه کردن هندلرها
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("ربات در حال اجراست...")
    app.run_polling()
