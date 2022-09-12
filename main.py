import botogram
#import os

#API_KEY = os.getenv("API_KEY")
API_KEY = "5456357833:AAGApPbodcGhshTBr9_InNuBBzCaNVzKes4"
bot = botogram.create(API_KEY)

@bot.command("hello")
def sayHi(chat, message, arg):
  chat.send("hi clown")

#if __name__ == "__main__":
bot.run()