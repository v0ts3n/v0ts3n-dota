#B_Votson Dota Bot
#Все права на бота пренадлежат B_Votson Team. В случае нарушения авторским прав автор в праве набить вам ебальник
#Создано совмесно с системой умного дома Nerif Project.
#Офф. сайт: http://bvotsonteam.alwaysdata.net
#Офф. сайт Nerif Project: http://nerifproject.22web.org
#805124040 - Illya
#1175804570 - антон
#1266375880 - ya dotqa
#775842886 - danya
#854861902 - Akk dani
#1118900219 - Akk Antona


#ACCOUNTS INFO
#CHANGE IT IF YOU WANT TO USE BOT IN YOUR GROUP
account_userName = ['@hallgheen', '@Kob2n4ik', '@B_Votson', '@Vots0n']
accounts_list = [854861902, 1118900219, 1266375880, 1520830298]
chatId_list = [775842886, 1175804570, 936106535, 805124040]
is_alive = [False, False, False, False]


from threading import Thread
from io import BytesIO
import ranktier
import emoji
import logging
import requests
import json
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message, ParseMode, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import executor


matchidDota = ''
logging.basicConfig(level=logging.INFO)
datadoto = ''
API_TOKEN = '5965011484:AAFCpplJfAzio6Eieapdbl1PZxhVfxUnyZU'
#pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
#Мертвая функция старого определения игры. Не использовать.
def getmatchid():
    image = pyautogui.screenshot("screen.png", region=(235, 651, 60, 50))

    image = Image.open("screen.png")
    matchpre = pytesseract.image_to_string(image, config='digits')
    print(matchpre)
    return matchpre

def changePollingForChat_Id(id):
    for i in chatId_list:
        if i == id:
            nowsNum = chatId_list.index(i)
            is_alive[nowsNum] = not is_alive[nowsNum]
            print(nowsNum)
            return nowsNum

#Получить айди аккаунта стим из чат_ида
def checknamefromid(id):
    for i in chatId_list:
        if i == id:
            nowsNum = chatId_list.index(i)
            
            return account_userName[nowsNum]
#Получить чат_ид из тегерама ника
def checkidfromname(username):
    for i in account_userName:
        if i == username:
            nowsNum = account_userName.index(i)
            print(chatId_list[nowsNum])
            return chatId_list[nowsNum]
#Получить айди аккаунта стим из чат_ида
def checkids(chatid):
    for i in chatId_list:
        #print(i)
        if i == chatid:
            nowsNum = chatId_list.index(i)
            return accounts_list[nowsNum]

async def send_photo_by_url(chat_id, photo_url):
    
    response = requests.get(photo_url)
    photo = BytesIO(response.content)
    await bot.send_photo(chat_id, photo)
    
def startpolling(mode, id):
    
    if mode == True: 
        global datadoto
        ids = getmatchid()

        match_id = ids
        url = 'https://api.opendota.com/api/matches/'+ str(match_id)

        response = requests.get(url)
        #print(response.json())
        #print(response.json()['replay_url'])

        first_blood = str(int(response.json()['first_blood_time'])//60) + ":" + str(int(response.json()['first_blood_time'])%60)
        allKill = str(response.json()['radiant_score']) + " - " + str(response.json()['dire_score'])
        allTime = str(int(response.json()['duration'])//60) + ":" + str(int(response.json()['duration'])%60)
        if response.json()['radiant_win'] == True:
            teamwin = "Сил света"
        if response.json()['radiant_win'] == False:
            teamwin = "Сил тьмы"



        datadoto = "B_Votson Team \nМатч №"+str(match_id)+"\nВремя первой крови: " + str(first_blood) + "\nСчет игры: " + str(allKill) + "\nДлительность матча: " + str(allTime) + "\nРезультат: победа " + teamwin
    if mode == False:
        
        userId = id
        url = 'https://api.opendota.com/api/players/' + str(userId) + '/recentMatches'

        response = requests.get(url)
        matchidNeed = response.json()[0]['match_id']
        slotPlay = response.json()[0]['player_slot']
        
        if slotPlay >= 128:
            teamPlayer = "Силы Тьмы"
        if slotPlay <= 127:
            teamPlayer = "Силы Света"
        url = 'https://api.opendota.com/api/matches/'+ str(matchidNeed)

        response = requests.get(url)
        
        first_blood = str(int(response.json()['first_blood_time'])//60) + ":" + str(int(response.json()['first_blood_time'])%60)
        allKill = str(response.json()['radiant_score']) + " - " + str(response.json()['dire_score'])
        allTime = str(int(response.json()['duration'])//60) + ":" + str(int(response.json()['duration'])%60)
        allTime2 = str(int(response.json()['duration'])//60)
        if response.json()['radiant_win'] == True:
            teamwin = "Сил света"
        if response.json()['radiant_win'] == False:
            teamwin = "Сил тьмы"
        url = 'https://api.opendota.com/api/players/' + str(userId) + '/recentMatches'
        response = requests.get(url)
        id_hero = response.json()[0]['hero_id']
        url = 'https://bvotsonteam.alwaysdata.net/heroes.json'
        res = requests.get(url)
        new_id = res.json()[str(id_hero)]["localized_name"]

        
        url = 'https://api.opendota.com/api/players/' + str(userId) + '/recentMatches'
        response = requests.get(url)
        
        tower_dmg = response.json()[0]['tower_damage']
        hero_dmg = response.json()[0]['hero_damage']
        gpm = response.json()[0]['gold_per_min']
        networse = int(gpm)*int(allTime2)
        kda = str(response.json()[0]['kills']) + "/" + str(response.json()[0]['deaths']) + "/" + str(response.json()[0]['assists'])
        global matchidDota
        matchidDota = matchidNeed
        print(matchidDota)
        datadoto = str(emoji.emojize(":check_mark_button:")) + "B_Votson Team" + str(emoji.emojize(":check_mark_button:")) + "\n" + str(emoji.emojize(":ID_button:")) + "Матч №"+str(matchidNeed)+"\n" + str(emoji.emojize(":timer_clock:")) + "Время первой крови: " + str(first_blood) + "\n" + str(emoji.emojize(":skull:")) + "Счет игры: " + str(allKill) + "\n" + str(emoji.emojize(":timer_clock:")) + "Длительность матча: " + str(allTime) + "\n" + str(emoji.emojize(":loudspeaker:")) + "Играл за: " + teamPlayer + "\n"  + str(emoji.emojize(":loudspeaker:")) + "Результат: победа " + teamwin + "\n" + str(emoji.emojize(":man_superhero:")) + "На герое: " + str(new_id) + "\n" + str(emoji.emojize(":baby_dark_skin_tone:")) + "Урон по героям игрока: " + str(hero_dmg) + "\n" + str(emoji.emojize(":Tokyo_tower:")) + "Урон по постройкам: " + str(tower_dmg) + "\n" + str(emoji.emojize(":check_mark_button:") + "КДА: " + str(kda) + "\n" + str(emoji.emojize(":money_bag:")) + "ГПМ: " + str(gpm) + "\n" + str(emoji.emojize(":money_bag:")) + "НЕТВОРС: " + str(networse))
        return matchidNeed




def start_pollingProfile(mode, id):
    if mode == True:
        url = 'https://api.opendota.com/api/players/' + str(id)

        response = requests.get(url)
        rankTier = ranktier.Rank(int(response.json()['rank_tier']))
        profile_name = response.json()['profile']['personaname']
        lastLogin_time = response.json()['profile']['last_login']
        full_avatar_link = response.json()['profile']['avatarfull']
        countryName = response.json()['profile']['loccountrycode']
        return rankTier, profile_name, lastLogin_time, full_avatar_link, countryName

def createNewPoller(mode, id, chatid):
    if mode == True:
        id_in_list = changePollingForChat_Id(id)
        lastmatchbefore = startpolling(False, id)
        while is_alive[id_in_list] == True:
            url = 'https://api.opendota.com/api/players/' + str(userId) + '/recentMatches'
            response = requests.get(url)
            matchid_last_Poller = response.json()[0]['match_id']
            if matchid_last_Poller != lastmatchbefore:
                #await bot.send_message(chatid, "У пользователя №" + str(id) + " был сыгран новый матч. Быстрее апросите его обработку")
                pass
            
            
        

        



@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Ура, все работает!!!!")

@dp.message_handler(commands=['startpolling'])
async def send_welcome(msg: types.Message):
    command = msg.get_full_command()
    await msg.answer("Создаеться запрос на автоматическое обновление профиля. Ожидайте")
    command = msg.get_full_command()
    idNeed = checkidfromname(command[1])
    profile_id = checkids(idNeed)

    t1 = Thread(target=createNewPoller, args = (True, profile_id, checkidfromname(str(command[1]))))
    t1.start()
    await msg.answer("Автоматическое обновление включено. ")
    
@dp.message_handler(commands=['stoppolling'])
async def send_welcome(msg: types.Message):
    
    command = msg.get_full_command()
    await msg.answer("Создаеться запрос на отключение автоматического обновления профиля.")
    command = msg.get_full_command()
    idNeed = checkidfromname(command[1])
    profile_id = checkids(idNeed)
    id_in_list = changePollingForChat_Id(checkidfromname(str(command[1])))
    await msg.answer("Автоматическое обновление матчей отключено.")
    

    


    



@dp.message_handler(commands=['checkProfile'])
async def send_profile(msg: types.Message):
    command = msg.get_full_command()
    print(msg.get_full_command())
    idNeed = checkidfromname(command[1])
    profile_id = checkids(idNeed)
    await msg.reply("Обработка профиля №" + str(profile_id) + "\n" + "(Тестовая функция)")
    rank, profileName, lastLogin, linkAvatar, country = start_pollingProfile(True, profile_id)
    await send_photo_by_url(msg.chat.id, linkAvatar)
    await msg.reply(emoji.emojize(":check_mark_button:") + "B_Votson Team" + str(emoji.emojize(":check_mark_button:")) + "\n" + "Имя профиля: " + str(profileName) + "\n" + "RANK: " + str(rank) + "\n" + "Входил в сеть последний раз: " + str(lastLogin))



@dp.message_handler(commands=['lastmatchfrom'])
async def send_last_match(message: types.Message):
    
    command = message.get_full_command()
    print(message.get_full_command())
    idNeed = checkidfromname(command[1])
    profile_id = checkids(idNeed)
    global datadoto
    await message.reply("Обработка профиля №" + str(profile_id))
    startpolling(False, profile_id)
    global matchidDota
    button = InlineKeyboardButton(text='DOTABUFF', url='https://www.dotabuff.com/matches/' + str(matchidDota))
    keyboard = InlineKeyboardMarkup().add(button)
    button2 = InlineKeyboardButton(text='OPENDOTA', url='https://www.opendota.com/matches/' + str(matchidDota))
    keyboard.add(button2)
    
    await message.reply("Ваш последний матч: \n" + datadoto, reply_markup=keyboard)
@dp.message_handler(commands=['lastmatch'])
async def send_last_match(message: types.Message):
    profile_id = checkids(message.from_user.id)
    print(profile_id)
    global datadoto
    await message.reply("Обработка профиля №" + str(profile_id))
    startpolling(False, profile_id)
    global matchidDota
    button = InlineKeyboardButton(text='DOTABUFF', url='https://www.dotabuff.com/matches/' + str(matchidDota))
    keyboard = InlineKeyboardMarkup().add(button)
    button2 = InlineKeyboardButton(text='OPENDOTA', url='https://www.opendota.com/matches/' + str(matchidDota))
    keyboard.add(button2)
    
    
    await message.reply("Ваш последний матч: \n" + datadoto, reply_markup=keyboard)

@dp.message_handler(commands=['newRoshan'])
async def send_roshan(msg: types.Message):
    await msg.reply("Создаються новые тайминги роши, ожидайте....")
    
    upom = checknamefromid(msg.from_user.id)
    
    
    
    await msg.reply("Рошан создан. Ожидайте упоминания ботом. ")
    await asyncio.sleep(420)
    await msg.reply("Возможный тайминг рошана(минимальный тайминг) " + upom + " " + upom + " " + upom + " " + upom)
    await asyncio.sleep(540)
    await msg.reply("Возможный тайминг рошана(Средний тайминг) " + upom + " " + upom + " " + upom + " " + upom)
    await asyncio.sleep(660)
    await msg.reply("Возможный тайминг рошана(Конечный тайминг) " + upom + " " + upom + " " + upom + " " + upom)

        











#@dp.message_handler(content_types=['text'])
#async def echo_message(message: types.Message):
    # не отправляем сообщение при каждом нажатии клавиши
#    if not keyboard.is_pressed('insert'):
#        return
#    await bot.send_message(-1001571677403, "Начата обработка матча, ожидайте....")
#    startpolling()
#        #photo eshe
#    await bot.send_message(-1001571677403, datadoto)
        
#s = requests.get("https://api.telegram.org/bot5965011484:AAFCpplJfAzio6Eieapdbl1PZxhVfxUnyZU/sendMessage?chat_id=-1001571677403&text=Бот успешно запущен на хостинге. Добавлено: тайминг рошана и все)))")   

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
 





