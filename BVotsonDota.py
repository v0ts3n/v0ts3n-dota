#B_Votson Dota Bot v3.6.8
#Все права на бота пренадлежат B_Votson Team. В случае нарушения авторских прав автор в праве набить вам ебальник
#Офф. сайт: http://bvotsonteam.alwaysdata.net
#Офф. сайт Nerif Project: http://nerifproject.22web.org

#ACCOUNTS INFO
#CHANGE IT IF YOU WANT TO USE BOT IN YOUR GROUP
import configparser
import os
# Создаем объект configparser
config = configparser.ConfigParser()



file_path = "BVotsonDota.ini"

if not os.path.isfile(file_path):


    print("1")
    account_userName = ['@B_Vatsan']
    accounts_list = [123123123]
    chatId_list = [123321]
    is_alive = [False, False, False, False, False, False]
    groups_register = []
    config['DotaPlayers'] = {'account_userName': str(account_userName), 'accounts_list': str(accounts_list), "chatId_list": str(chatId_list), "is_alive": str(is_alive)}
    # Сохраняем изменения в файле
    with open('BVotsonDota.ini', 'w') as configfile:
        config.write(configfile)
if os.path.isfile(file_path):
    config.read('BVotsonDota.ini')

    account_userName = eval(config.get('DotaPlayers', 'account_userName'))
    accounts_list = eval(config.get('DotaPlayers', 'accounts_list'))
    chatId_list = eval(config.get('DotaPlayers', 'chatId_list'))
    is_alive = eval(config.get('DotaPlayers', 'is_alive'))
    groups_register = eval(config.get('DotaPlayers', 'groups_register'))



import urllib
import json
from threading import Thread
from io import BytesIO
import ranktier
import emoji
import logging
import requests
import json
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message, ParseMode, InlineKeyboardButton, InlineKeyboardMarkup,WebAppInfo
from aiogram.utils import executor


matchidDota = ''
logging.basicConfig(level=logging.INFO)
datadoto = ''
API_TOKEN = 'YOUR-BOT-TOKEN'
#pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
'''==========================================ВОЗМОЖНА ПЕРЕРАБОТКА
def check_mmrs():
    url1 = 'https://api.opendota.com/api/players/' + str(accounts_list[0])
    url2 = 'https://api.opendota.com/api/players/' + str(accounts_list[1])
    url3 = 'https://api.opendota.com/api/players/' + str(accounts_list[2])
    url4 = 'https://api.opendota.com/api/players/' + str(accounts_list[3])
    

    response1 = requests.get(url1)
    response2 = requests.get(url2)
    response3 = requests.get(url3)
    response4 = requests.get(url4)
    
    rankTier1 = str(ranktier.Rank(int(response1.json()['rank_tier'])))
    rankTier2 = str(ranktier.Rank(int(response2.json()['rank_tier'])))
    rankTier3 = str(ranktier.Rank(int(response3.json()['rank_tier'])))
    rankTier4 = "Herald 5"#str(ranktier.Rank(int(response4.json()['rank_tier'])))
    print(rankTier1, rankTier2, rankTier3, rankTier4)
    return rankTier1, rankTier2, rankTier3, rankTier4
    #except Exception:
    #    print("[Coused Error] Coused error in mmr updater function. Error: " + str(Exception))
async def ranks_update():
    halgheen_pre, koban_pre, bv_pre, votson_pre = check_mmrs()
    while True:
        print(check_mmrs())
        hallgheen, kobanchik, bv, votson = check_mmrs()
        if hallgheen != halgheen_pre:
            halgheen_pre = hallgheen
            s = requests.get("https://api.telegram.org/bot5965011484:AAFCpplJfAzio6Eieapdbl1PZxhVfxUnyZU/sendMessage?chat_id=-1001571677403&text=У пользователя @hallgheen новый ранг! Поздравляем его!")   
        if kobanchik != koban_pre:
            koban_pre = kobanchik            
            s = requests.get("https://api.telegram.org/bot5965011484:AAFCpplJfAzio6Eieapdbl1PZxhVfxUnyZU/sendMessage?chat_id=-1001571677403&text=У пользователя @Kob2n4ik новый ранг! Поздравляем его!")   
        if bv != bv_pre:
            bv_pre = bv
            s = requests.get("https://api.telegram.org/bot5965011484:AAFCpplJfAzio6Eieapdbl1PZxhVfxUnyZU/sendMessage?chat_id=-1001571677403&text=У пользователя @B_Votson новый ранг! Поздравляем его!")
        if votson != votson_pre:
            votson_pre = votson
            s = requests.get("https://api.telegram.org/bot5965011484:AAFCpplJfAzio6Eieapdbl1PZxhVfxUnyZU/sendMessage?chat_id=-1001571677403&text=У пользователя @Vots0n новый ранг! Поздравляем его!")
        asyncio.sleep(5)        
'''


#Пооверить соотвествие чатида к аккаунту стима

def isYourAccount(chatid, steamid):
    for i in chatId_list:
        if i == chatid:
            nowsNum = chatId_list.index(i)
            for j in accounts_list:
                if steamid == j:
                    nowsNumSteam = accounts_list.index(j)
    if nowsNum == nowsNumSteam:
        return True
    else:
        return False

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

def checksteamidfromusername(user):
    for i in account_userName:
        if i == user:
            nowsNum = account_userName.index(i)
            return accounts_list[nowsNum]

#Constructing data for table with recent matches
def recentmatches(steamid):
    res1 = requests.get("https://api.opendota.com/api/players/" + str(steamid) + "/recentMatches")
    matchesjson = res1.json()
    reentmatchesid = []
    for i in matchesjson:
        reentmatchesid.insert(len(reentmatchesid), str(i['match_id']))
    reentmatchesid = reentmatchesid[:9]
    return reentmatchesid

async def send_photo_by_url(chat_id, photo_url):
    
    response = requests.get(photo_url)
    photo = BytesIO(response.content)
    await bot.send_photo(chat_id, photo)


def startpollingpre(mode, id):
    #get match id 
    if mode == True: 
        pass
    if mode == False:
        global datadoto2
        userId = id
        url = 'https://api.opendota.com/api/players/' + str(userId) + '/recentMatches'

        response = requests.get(url)
        matchidNeed = response.json()[1]['match_id']
        slotPlay = response.json()[1]['player_slot']
        
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
        id_hero = response.json()[1]['hero_id']
        url = 'https://bvotsonteam.alwaysdata.net/heroes.json'
        res = requests.get(url)
        new_id = res.json()[str(id_hero)]["localized_name"]

        
        url = 'https://api.opendota.com/api/players/' + str(userId) + '/recentMatches'
        response = requests.get(url)
        
        tower_dmg = response.json()[1]['tower_damage']
        hero_dmg = response.json()[1]['hero_damage']
        gpm = response.json()[1]['gold_per_min']
        networse = int(gpm)*int(allTime2)
        kda = str(response.json()[1]['kills']) + "/" + str(response.json()[1]['deaths']) + "/" + str(response.json()[1]['assists'])
        global matchidDota
        matchidDota = matchidNeed
        print(matchidDota)
        datadoto2 = str(emoji.emojize(":check_mark_button:")) + "B_Votson Team" + str(emoji.emojize(":check_mark_button:")) + "\n" + str(emoji.emojize(":ID_button:")) + "Матч №"+str(matchidNeed)+"\n" + str(emoji.emojize(":timer_clock:")) + "Время первой крови: " + str(first_blood) + "\n" + str(emoji.emojize(":skull:")) + "Счет игры: " + str(allKill) + "\n" + str(emoji.emojize(":timer_clock:")) + "Длительность матча: " + str(allTime) + "\n" + str(emoji.emojize(":loudspeaker:")) + "Играл за: " + teamPlayer + "\n"  + str(emoji.emojize(":loudspeaker:")) + "Результат: победа " + teamwin + "\n" + str(emoji.emojize(":man_superhero:")) + "На герое: " + str(new_id) + "\n" + str(emoji.emojize(":baby_dark_skin_tone:")) + "Урон по героям игрока: " + str(hero_dmg) + "\n" + str(emoji.emojize(":Tokyo_tower:")) + "Урон по постройкам: " + str(tower_dmg) + "\n" + str(emoji.emojize(":check_mark_button:") + "КДА: " + str(kda) + "\n" + str(emoji.emojize(":money_bag:")) + "ГПМ: " + str(gpm) + "\n" + str(emoji.emojize(":money_bag:")) + "НЕТВОРС: " + str(networse))
        
def checkmatch(matchid, playerid):
    try:
        
        global datadoto
        userId = playerid
        res1 = requests.get("https://api.opendota.com/api/matches/" + str(matchid))
        for i in res1.json()['players']:
            if i['account_id'] == playerid:
                slotPlay = i['player_slot']
                playergameslot = i
        matchidNeed = matchid
    
        
        
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
        res1 = requests.get("https://api.opendota.com/api/matches/" + str(matchid))
        
        id_hero = res1.json()['players'][playergameslot]['hero_id']
        url = 'https://bvotsonteam.alwaysdata.net/heroes.json'
        res = requests.get(url)
        new_id = res.json()[str(id_hero)]["localized_name"]

        
        url = 'https://api.opendota.com/api/players/' + str(userId) + '/recentMatches'
        response = requests.get(url)
        
        #tower_dmg = response.json()[0]['tower_damage']
        #hero_dmg = response.json()[0]['hero_damage']
        #gpm = response.json()[0]['gold_per_min']
        #networse = int(gpm)*int(allTime2)
        #kda = str(response.json()[0]['kills']) + "/" + str(response.json()[0]['deaths']) + "/" + str(response.json()[0]['assists'])
        global matchidDota
        matchidDota = matchidNeed
        print(matchidDota)
        print("HUI")
        datadoto = str(emoji.emojize(":check_mark_button:")) + "B_Votson Team" + str(emoji.emojize(":check_mark_button:")) + "\n" + str(emoji.emojize(":ID_button:")) + "Матч №"+str(matchidNeed)+"\n" + str(emoji.emojize(":timer_clock:")) + "Время первой крови: " + str(first_blood) + "\n" + str(emoji.emojize(":skull:")) + "Счет игры: " + str(allKill) + "\n" + str(emoji.emojize(":timer_clock:")) + "Длительность матча: " + str(allTime) + "\n" + str(emoji.emojize(":loudspeaker:")) + "Играл за: " + teamPlayer + "\n"  + str(emoji.emojize(":loudspeaker:")) + "Результат: победа " + teamwin + "\n" + str(emoji.emojize(":man_superhero:")) + "На герое: " + str(new_id) + "\n" + str(emoji.emojize(":baby_dark_skin_tone:")) + "Урон по героям игрока: "
        print(datadoto)
        return datadoto
    except Exception:
        pass

#return matchidNeed, first_blood, allKill, allTime, allTime2, teamwin, new_id, tower_dmg, hero_dmg, gpm, networse, kda
def startpolling(mode, id):
    #get match id 
    if mode == True: 
        pass
    if mode == False:
        global datadoto
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
        party_size = response.json()[0]['party_size']
        tower_dmg = response.json()[0]['tower_damage']
        hero_dmg = response.json()[0]['hero_damage']
        gpm = response.json()[0]['gold_per_min']
        networse = int(gpm)*int(allTime2)
        kda = str(response.json()[0]['kills']) + "/" + str(response.json()[0]['deaths']) + "/" + str(response.json()[0]['assists'])
        kda2 = (response.json()[0]['kills']  +  response.json()[0]['assists']) / response.json()[0]['deaths']
        global matchidDota
        matchidDota = matchidNeed
        print(matchidDota)
        datadoto = str(emoji.emojize(":check_mark_button:")) + "B_Votson Team" + str(emoji.emojize(":check_mark_button:")) + "\n" + str(emoji.emojize(":ID_button:")) + "Матч №"+str(matchidNeed)+"\n" + str(emoji.emojize(":timer_clock:")) + "Время первой крови: " + str(first_blood) + "\n" + str(emoji.emojize(":skull:")) + "Счет игры: " + str(allKill) + "\n" + str(emoji.emojize(":timer_clock:")) + "Длительность матча: " + str(allTime) + "\n" + str(emoji.emojize(":loudspeaker:")) + "Играл за: " + teamPlayer + "\n"  + str(emoji.emojize(":loudspeaker:")) + "Результат: победа " + teamwin + "\n" + str(emoji.emojize(":man_superhero:")) + "На герое: " + str(new_id) + "\n" + str(emoji.emojize(":baby_dark_skin_tone:")) + "Урон по героям игрока: " + str(hero_dmg) + "\n" + str(emoji.emojize(":Tokyo_tower:")) + "Урон по постройкам: " + str(tower_dmg) + "\n" + str(emoji.emojize(":check_mark_button:") + "КДА: " + str(kda) + "\n" + str(emoji.emojize(":money_bag:")) + "ГПМ: " + str(gpm) + "\n" + str(emoji.emojize(":money_bag:")) + "НЕТВОРС: " + str(networse) + str(emoji.emojize(":money_bag:")) + "\n" + str(emoji.emojize(":check_mark_button:")) + str("Размер Пати: ") + str(party_size) + str(emoji.emojize(":check_mark_button:")))
        
        return gpm, kda2



#return rankTier, profile_name, lastLogin_time, full_avatar_link, countryName
def start_pollingProfile(mode, id):
    if mode == True:
        url = 'https://api.opendota.com/api/players/' + str(id)

        response = requests.get(url)
        try:
            rankTier = ranktier.Rank(int(response.json()['rank_tier']))
        except Exception:
            rankTier = "Нету"
        profile_name = response.json()['profile']['personaname']
        lastLogin_time = "Неизвестно"   #response.json()['profile']['last_login']
        full_avatar_link = response.json()['profile']['avatarfull']
        countryName = response.json()['profile']['loccountrycode']
        return rankTier, profile_name, lastLogin_time, full_avatar_link, countryName

#return last match and hero from profile id
def get_lastmatch(accountid):
    url = 'https://api.opendota.com/api/players/' + str(accountid) + '/recentMatches'

    response = requests.get(url)
    matchidNeed = response.json()[0]['match_id']
    id_hero = response.json()[0]['hero_id']
    url = 'https://bvotsonteam.alwaysdata.net/heroes.json'
    res = requests.get(url)
    hero = res.json()[str(id_hero)]["localized_name"]
    return hero, matchidNeed
        
def checkifmatch(matchid):
    res = requests.get("https://api.opendota.com/api/matches/" + str(matchid))
    try:
        if res.json()['error'] == "Not Found":
            return True
    except Exception:
        return False


def checkcurrentmatch(username):
    
    res = requests.get("http://bvotsonteam.alwaysdata.net/currentmatch.php?user=" + username)
    arr = {
            "time": res.json()['time'],
            'hero_name': res.json()['hero_name'],
            'matchid': res.json()['matchid'],
            'rad_score': res.json()['rad_score'],
            'dire_score': res.json()['dire_score'],
            'kda': res.json()['kda'],
            'last_hits': res.json()['last_hits']

    }
    if checkifmatch(arr['matchid']) == True:
        time = int(int(arr["time"])/60)
        data = "B_Votson Team" + "\nТекущее время: " + str(time) + " минута. \nГерой: " + arr["hero_name"] + "\nАйди матча: " + arr["matchid"] + "\nСчет сил света: " + arr["rad_score"] + "\nСчет сил тьмы: " + arr["dire_score"] + "\nЛастхит: " + arr["last_hits"] + "\nK/D/A: " + arr["kda"]
        return data
    if checkifmatch(arr['matchid']) == False:
        return "На данный момент пользователь не играет или выключен обработчик. "

@dp.message_handler(commands=['offabot'])
async def send_welcome(message: types.Message):
    if message.chat.id == 936106535:
        await message.answer("Бот был выключен.")
        exit()
    else:
        await message.answer("Команда доступна только администраторам. ")
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    
    button = InlineKeyboardButton(text='Сайт разработчика', url='http://bvotson.byethost7.com')
    button2 = InlineKeyboardButton(text='Сайт команды', url='http://bvotsonteam.alwaysdata.net')
    button3 = InlineKeyboardButton(text='GITHUB', url='https://github.com/BVotson')
    keyboard = InlineKeyboardMarkup().add(button)
    keyboard.add(button2)
    keyboard.add(button3)

    await message.reply("Dota Bot v3.6.7 \nBy B_Votson Team", reply_markup=keyboard)

@dp.message_handler(commands=['recentmatches'])
async def recent(msg: types.Message):
    command = msg.get_full_command()
    id = checksteamidfromusername(command[1])
    keyboard = InlineKeyboardMarkup()
    lastmatches = recentmatches(id)
    if id == None:
        await msg.answer_sticker(r'CAACAgIAAxkBAAEIi1hkNXDw3Cb42bhbthJqGSRRwo_2JwACYwEAAntOKhBTVm71ygpsCy8E')
        await msg.reply("Вы указали неправильный username либо же его не существует")
    else:
        for i in lastmatches:
            button = InlineKeyboardButton(text=str(i) + " (" + str(lastmatches.index(i) + 1) + ")", url='https://www.opendota.com/matches/' + str(i))
            keyboard.add(button)
        await msg.reply("Последние игры " + str(command[1]), reply_markup=keyboard)
        


@dp.message_handler(commands=['matchinfo'])
async def new_player(msg: types.Message):
    command = msg.get_full_command()
    matchid = command[1]
    print(command, matchid)
    global datadoto
    datadoto = checkmatch(matchid, checknamefromid(msg.from_user.id))
    await msg.reply(datadoto)



@dp.message_handler(commands=['addnewgroup'])
async def new_player(msg: types.Message):
    #groups_register.insert
    
    groups_register.insert(len(groups_register), int(msg.chat.id))
    config['DotaPlayers'] = {'account_userName': str(account_userName), 'accounts_list': str(accounts_list), "chatId_list": str(chatId_list), "is_alive": str(is_alive), "groups_register": str(groups_register)}
            # Сохраняем изменения в файле
    with open('BVotsonDota.ini', 'w') as configfile:
        config.write(configfile)
    await msg.answer("В базу данных добавлена новая группа.")
    
    

@dp.message_handler(commands=['recend'])
async def new_player(msg: types.Message):
    global groups_register
    if msg.from_user.id == 936106535:
        command = msg.get_full_command()
        text = command[1]
        #words = text.replace('_', ' ')

        for i in chatId_list:
            
            try:
                await bot.send_message(i, text)
            except Exception as e:
                await msg.answer("Не удалось отправить сообщение " + str(i) + str(e))
            
        for j in groups_register:
            #print(j)
            #await msg.answer(groups_register)  
            try:

                await bot.send_message(j, text)
            except Exception:
                await msg.answer("Не удалось отправить " + str(j) + str(e))
        
        await msg.answer("Рассылка создана.")
    else:
        await msg.answer("У вас нет прав для испольхования этой команды.")



@dp.message_handler(commands=['addnewplayer'])
async def new_player(msg: types.Message):
    command = msg.get_args().split()

    print(command)
    if len(command) < 2:
        await msg.reply("Введите достаточное количество аргументов.\nШаблон: /addnewplayer [@username] [chat_id] [steam_profile] \nПример: /addnewplayer @B_Votson 93612732 10273721")
    else:
        account_userName.insert(len(account_userName), command[0])
        chatId_list.insert(len(chatId_list), int(command[1]))
        accounts_list.insert(len(accounts_list), int(command[2]))
        config['DotaPlayers'] = {'account_userName': str(account_userName), 'accounts_list': str(accounts_list), "chatId_list": str(chatId_list), "is_alive": str(is_alive)}
        # Сохраняем изменения в файле
        with open('BVotsonDota.ini', 'w') as configfile:
            config.write(configfile)
        await msg.reply("Добавлен новый игрок в базу данных.")


@dp.message_handler(commands=['prelastmatchfrom'])
async def prematchsend(msg: types.Message):
    command = msg.get_full_command()
    print(msg.get_full_command())
    idNeed = checkidfromname(command[1])
    profile_id = checkids(idNeed)
    await msg.reply("Обработка профиля №" + str(profile_id))
    if profile_id != None:
        startpollingpre(False, profile_id)
        global datadoto2
        await msg.answer(datadoto2)
    if profile_id == None:
        await msg.answer_sticker(r'CAACAgIAAxkBAAEIi1hkNXDw3Cb42bhbthJqGSRRwo_2JwACYwEAAntOKhBTVm71ygpsCy8E')
        await msg.reply("Вы указали неправильный username либо же его не существует")

"""
@dp.message_handler(commands=['mmrpolling'])
async def start_polingmmrs(msg: types.Message):
    t1 = Thread(target=ranks_update)
    t1.start()
    await msg.answer("Начата авто-обработка рангов. ")
"""

@dp.message_handler(commands=["createupdater"])
async def create_updater(msg: types.Message):
    command = msg.get_full_command()
    
    whoUpdate = msg.from_user.id
    
    #create_profile_updater(whoUpdate)
    

@dp.message_handler(commands=['checkProfile'])
async def send_profile(msg: types.Message):
    command = msg.get_full_command()
    print(msg.get_full_command())
    idNeed = checkidfromname(command[1])
    profile_id = checkids(idNeed)
    if profile_id != None:
        await msg.reply("Обработка профиля №" + str(profile_id) + "\n" + "(Тестовая функция)")
        rank, profileName, lastLogin, linkAvatar, country = start_pollingProfile(True, profile_id)
        await send_photo_by_url(msg.chat.id, linkAvatar)
        
        res = requests.get("https://api.opendota.com/api/players/" + str(profile_id) + "/wl?limit=20")
        wrlast = int(res.json()["win"]) / 20 * 100
        

        wrlast = int(wrlast)
        ishisaccount = isYourAccount(msg.from_user.id, profile_id)
        
        button = InlineKeyboardButton(text='Коментарий к профилю BVotson Dota', web_app=WebAppInfo(url="https://bvotsonteam.alwaysdata.net/profile_dota.php?profile=" + str(profile_id)))
        keyboard = InlineKeyboardMarkup().add(button)

        await msg.reply(emoji.emojize(":check_mark_button:") + "B_Votson Team" + str(emoji.emojize(":check_mark_button:")) + "\n" + "Имя профиля: " + str(profileName) + "\n" + "RANK: " + str(rank) + "\n" + "Входил в сеть последний раз: " + str(lastLogin) + "\nВинрейт за последние 20 игр: " + str(wrlast) + "%", reply_markup=keyboard)
        hero, match_id = get_lastmatch(profile_id)
        await bot.send_message(msg.chat.id, "Последний сыграный матч: №" + str(match_id) + ", на герое " + str(hero))
    
    if profile_id == None:
        await msg.reply("Вы указали неправильный username либо же его не существует")

@dp.message_handler(commands=['lastmatchfrom'])
async def send_last_match(message: types.Message):
    
    command = message.get_full_command()
    print(message.get_full_command())
    idNeed = checkidfromname(command[1])
    profile_id = checkids(idNeed)
    if profile_id != None:
        
        await message.reply("Обработка профиля №" + str(profile_id))
        gpm, kda = startpolling(False, profile_id)
        global matchidDota
        button = InlineKeyboardButton(text='DOTABUFF', url='https://www.dotabuff.com/matches/' + str(matchidDota))
        keyboard = InlineKeyboardMarkup().add(button)
        button2 = InlineKeyboardButton(text='OPENDOTA', url='https://www.opendota.com/matches/' + str(matchidDota))
        keyboard.add(button2)
        global datadoto
        print(datadoto)
        await message.reply("Ваш последний матч: \n" + datadoto, reply_markup=keyboard)
        print(gpm, kda)
        if gpm <= 500:
            #CAACAgIAAxkBAAEIi2hkNXKNztUFEiyZpW24bMnhGSwutAACICcAAs0eKEgAAZtRGNXVf7UvBA
            #await message.answer_sticker(r'CAACAgIAAxkBAAEIi2hkNXKNztUFEiyZpW24bMnhGSwutAACICcAAs0eKEgAAZtRGNXVf7UvBA')
            await message.reply("Че по гпму, ало")
        if kda < 2:
            await message.reply("Че по кда, чучело")
            #await message.answer_sticker(r'CAACAgIAAxkBAAEIi2xkNXQKVPXUX7jppqxlXAGMH00ikgACvycAArLU0UocBE2-dWq6LC8E')
    if profile_id == None:
        await message.answer_sticker(r'CAACAgIAAxkBAAEIi1hkNXDw3Cb42bhbthJqGSRRwo_2JwACYwEAAntOKhBTVm71ygpsCy8E')
        await message.reply("Вы указали неправильный username либо же его не существует")
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
'''=====================УДАЛЕННАЯ ФУНКЦИЯ, ВОЗМОЖНА ПЕРЕРАБОТКА В НОВЫХ ВЕРСИЯХ
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
'''
def checkwinrate(id, hero):
    res = requests.get("https://api.opendota.com/api/players/" + str(id) + "/heroes")
    
    res2 = requests.get("http://bvotsonteam.alwaysdata.net/heroes.json")
    
    for i in res2.json():
        if res2.json()[str(i)]["localized_name"] == str(hero):
            heroid = i
            heroname = res2.json()[str(i)]["name"]
            
    


    for i in res.json():
    
        if i["hero_id"] == heroid:
            games = i['games']
            last_played = i['last_played']
            wingames = i['win']
            if games != 0:
                winrate = wingames/games*100
            else:
                return 0, "none", 999
            print(int(winrate))

    
    
    return winrate, heroname, games, last_played, heroid

@dp.message_handler(commands=['winrate'])
async def checkwr(msg: types.Message):
    command = msg.get_full_command()
    if len(command) == 3:
        hero = command[1] + command[2]
    if len(command) == 2:
        hero = command[1]
    if len(command) == 1:
        pass
    wr, heronamed, games, lastgame, heroid2 = checkwinrate(checkids(msg.from_user.id), hero)
    if heronamed != "none":
        wr = int(wr)
        imagehero = heronamed + ".webm"
        print("https://studio.bazar.kr.ua/heroes/" + imagehero)
        #print("http://nerifdoto.22web.org/" + imagehero)
        
        #with open(imagehero, "wb") as f:
        #    f.write(requests.get("http://studio.bazar.kr.ua/heroes/" + imagehero).content)
        #    f.close()


        #await bot.send_photo(msg.chat.id, imagehero)
        button = InlineKeyboardButton(text='Статистика героя ' + hero, url='https://www.opendota.com/players/' + str(checkids(msg.from_user.id)) + '/heroes?hero_id=' + str(heroid2))
        keyboard = InlineKeyboardMarkup().add(button)
        await msg.reply(str(emoji.emojize(":check_mark_button:")) + "B_Votson Team" + str(emoji.emojize(":check_mark_button:")) + "\nПрофиль №" + str(msg.from_user.id // 1) + "\nВинрейт на " + hero + ": " + str(wr) + "%" + "\nВсего игр: " + str(games), reply_markup=keyboard)
    if heronamed == "none":
        await msg.reply("Похоже что у вас нет игр на этом герое, если это не так значит проблемы на стороне бота")
    
@dp.message_handler(commands='currentmatch')
async def send_notification(msg: types.Message):
    command = msg.get_full_command()
    username = command[1]

    data = checkcurrentmatch(username)
    await msg.reply(data)


@dp.message_handler(commands=['betatest'])
async def send_notification(msg: types.Message):
    button = InlineKeyboardButton(text='Зарегестрироваться', url='https://forms.gle/Tbkzx6xfT2UzY4Vk9')
    keyboard = InlineKeyboardMarkup().add(button)
    await msg.answer("На данный момент открыт бета-тест интеграции в игру бота. Для тестирования нужно зарегестрироваться. Вы можете сделать это по ссылкеЮ после чего ожидайте пока вам напишет бот.",reply_markup=keyboard)
    



@dp.message_handler(commands=['all'])
async def send_notification(msg: types.Message):
    users = ""
    for i in account_userName:
        users += " " + i
    await msg.reply(users)
    



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