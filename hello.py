import telegram

TELEGRAM_TOKEN = "1704418208:AAFj7~~"
bot = telegram.Bot(token=TELEGRAM_TOKEN)
updates = bot.getUpdates()
chat_id = updates[-1].message.chat_id

bot.sendMessage(chat_id=chat_id, text='메시지 발송')

for update in updates:
    print(update.message)

    