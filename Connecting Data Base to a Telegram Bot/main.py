import sqlite3
import telebot

bot = telebot.TeleBot("!YOUR TOKEN HERE!")

def create_table():
    connection = sqlite3.connect('bot.db')
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE users (
        id INTEGER NOT NULL,
        username TEXT  NOT NULL         
        )
    """)
    connection.commit()
    connection.close()

def add_user(id, username):
    connection = sqlite3.connect('bot.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (id, username) VALUES (?, ?)", (id, username))
    connection.commit()
    connection.close()

@bot.message_handler(commands=['start'])
def start(message):
    add_user(message.from_user.id, message.from_user.username)
    bot.send_message(message.from_user.id, f"Hello {message.from_user.username}")

bot.polling(none_stop=True)