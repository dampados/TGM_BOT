import telepot
token = "897908672:AAHcu05tJ6OizzQFo2zx8AeM1ffSisJF6fM"
TelegramBot = telepot.Bot(token)
print(TelegramBot.getMe())