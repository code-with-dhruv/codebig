from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ( CommandHandler, Filters, MessageHandler, Updater)
from message import Editmessage, Sendmessage, logger, sendfile, Deletemessage
import os
import telepot
import urllib.request
from PIL import Image
import requests
from bs4 import BeautifulSoup
import random
import string
import requests
import time
import json
import math
import html5lib

os.environ['TZ'] = 'America/Buenos_Aires'

gods=["21951A6626","21951A6637","21951A6627","21951A6614"]
members =[2141450636,809309749,2045746007,1257359605,2113380774,1134323688,2040610087]
bot_token = os.environ.get('TG_BOT_TOKEN')
startmessage = [[
		InlineKeyboardButton(
			"Dev",
			url='https://t.me/dheeraj2324'
		),
        InlineKeyboardButton(
			"Channel",
			url='https://t.me/aboutdheeraj'
		)
        ]]


def start(update, context):
    info = update.effective_user
    print(info)
    chat_id = info.id
    print(chat_id)
    userid= info['username']
    text = f'<b>Welcome</b> @{userid}<b>, to maths calculator bot and also private stuff!</b>\n<b>To know more use-</b> /help\n<code>This bot is provided for educational use!!</code>\n<code>ENTER IN YOUR OWN RISK!!</code>\n<code>YOU ARE RESPONSIBLE FOR YOUR OWN ACTION!.</code>'
    Sendmessage(chat_id, text, reply_markup=InlineKeyboardMarkup(startmessage))
    return
def cmds(update, context):
    chat_id = update.message.chat_id
    text = "<b>Available cmds available:</b>/login <code>username</code> <code>password</code>\n<code>username -- replace with Roll no.</code>\n<code>password -- replace with password</code>"
    Sendmessage(chat_id, text, reply_markup= InlineKeyboardMarkup(startmessage))
def help(update, context):
    chat_id = update.message.chat_id
    text = "<b>Hey, welcome to this Bot! Sorry to say cmds of the bots have been taken to private!!</b>\n<code>Some cmds are listed here:</code> /cmds"
    Sendmessage(chat_id, text)

######################################################################################################################
def login(update, context):
    chat_id = update.message.chat_id
    info = update.effective_user
    userid= info['username']
    text =  update.message.text.split(' ',2)
    username=text[1]
    password=text[2]
    logger.info(text)
    print(info)
    Deletemessage(chat_id, update.message.message_id)
    text = "<b>Logged in as</b> -- <code>{} </code>".format(username)
    Sendmessage(chat_id,text)
    if True:
        if False:
            text = "Gods data not available"
            Sendmessage(chat_id,text)
        else:
            try:
                data={'username':username,'password':password}
                headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': '_ga=GA1.3.361214083.1658147021',
    'Origin': 'http://buildit.iare.ac.in',
    'Referer': 'http://buildit.iare.ac.in/login',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}
                response = requests.post('http://buildit.iare.ac.in/login_', headers=headers, data=data, verify=False)
                #print(response)
                cook=(response.headers['Set-Cookie'])
                cookk=cook.split(";")
                finc=cookk[0][6:]
                #print(finc)
                us=(cookk[-2]).split("=")
                userr=us[-1]
                #print(userr)
                text=userr
                Sendmessage(chat_id,text)
                br=(cookk[-3]).split("=")
                bran=br[-1]
            except:
                text = "Incorrect password"
                Sendmessage(chat_id,text)
                
    else:
        text = "Gods do not permit your entry!" 
        Sendmessage(chat_id,text)


                
def solve(update,context):
    chat_id = update.message.chat_id
    info = update.effective_user
    userid= info['username']
    text =  update.message.text.split(' ',2)
    pot=text[1]
    ccode=text[2]
    logger.info(text)
    print(info)
    Deletemessage(chat_id, update.message.message_id)
    text = "<b>Solving as</b> -- <code>{} </code>".format(userr[:-2])
    Sendmessage(chat_id,text)
    if True:
        if False:
            text = "Gods data not available"
            Sendmessage(chat_id,text)
        else:
            try:
                
                cookies = {
   # '_ga': 'GA1.3.361214083.1658147021',
    'token':finc,
    'username': username,
    'branch': bran,
    'user': userr,
    'contestId': 'POTD{}'.format(),
}
                headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # Requests sorts cookies= alphabetically
    # 'Cookie': '_ga=GA1.3.361214083.1658147021; token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IjIxOTUxYTY2MjYiLCJpc1ZlcmlmaWVkIjp0cnVlLCJpYXQiOjE2NTgyNDY5MzMsImV4cCI6MTY2MDg3NDkzM30._bMpds30eHVYk-P2igs_U9yEODqK0GhR6aYa0W8z8KM; username=21951A6626; branch=cse; user=21951A662661; contestId=POTD91',
    'Pragma': 'no-cache',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}
                response = requests.get('http://buildit.iare.ac.in/contests/POTD91',cookies=cookies, headers=headers, verify=False)
                aa=str(response.content[12600:])
                ke=(aa.find("#5"))
                qii=aa[ke+1:ke+7]
                text=qii
                Sendmessage(chat_id,text)
                headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    # Already added when you pass json=
    # 'Content-Type': 'application/json',
    'Origin': 'http://buildit.iare.ac.in',
    'Referer': 'http://buildit.iare.ac.in/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'authorization': finc,
}
                json_data = {
    'source_code': ccode,
    'language_id': '34',
    'stdin': '',
    'contestId': pot.upper(),
    'courseId': '',
    'user': userr,
    'questionId': qii,
}
                response = requests.post('http://13.234.234.30:5000/validateSubmission', headers=headers, json=json_data, verify=False)
                print(response)
                p=str(response.json())
                text=p
                Sendmessage(chat_id,text)

            except:
                text = "Incorrect password"
                Sendmessage(chat_id,text)
                
    else:
        text = "Gods do not permit your entry!" 
        Sendmessage(chat_id,text)

        

#####################################################################################################################################################################


def main():
    updater = Updater(
        bot_token,
        use_context=True
    )
    dp = updater.dispatcher
    #dp.add_handler(MessageHandler(Filters.text & ~Filters.command, duty))
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("cmds", cmds))
    dp.add_handler(CommandHandler("login", login))
    dp.add_handler(CommandHandler("solve", solve))

    logger.info("Bot Started!!!")
    updater.start_polling()
    updater.idle()
if __name__ == "__main__":
    main()
