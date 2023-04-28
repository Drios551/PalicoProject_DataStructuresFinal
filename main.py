import discord
import os
import random
import time
import csv
import pandas
from replit import db

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

test_List = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
troll_List = ["Why don't you play with some friends"]

csv = pandas.read_csv('GameItems.csv')
items = {'name': [], 'descriptions': []}

for index, item in csv.iterrows():
  items['name'].append(str(item[13]).lower())
  items['descriptions'].append(str(item[14]).lower())





def update_game_list(game_List):
  if "games" in db.keys():
    games = db["games"]
    games.append(game_List)
    db["games"] = games
  else:
    db["games"] = [game_List]

def delete_game_list(index):
  games = db["games"]
  print(games)
  index = int(index)
  if len(games) > index:
    del games[index]
    db["games"] = games

@client.event
async def on_ready():
    print('We have sucessfully logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
      
    if message.content.startswith('$hello'):
      start = time.time()
      await message.channel.send('Hello!')
      end = time.time()
      total = end - start
      print('%.2f' % total, 'Seconds')

    if message.content.startswith("$help"):
      start = time.time()
      await message.channel.send('To add a game to the list just say, $add followed by the name of the game you want to add. To delete a game off the list, just type $del followed by the name of the game in the list')
      end = time.time()
      total = end - start
      print('%.2f' % total, 'Seconds')

    if message.content.startswith('$progress'):
      start = time.time()
      await message.channel.send('I am fully working!')
      end = time.time()
      total = end - start
      print('%.2f' % total, 'Seconds')

    if message.content.startswith('palico tell me a joke'):
      start = time.time()
      await message.channel.send('Here is a joke from where I come from. What do you call a hunting squad full of hunting horns? An orcestra. XD')
      end = time.time()
      total = end - start
      print('%.2f' % total, 'Seconds')
      
    if message.content.startswith('random number'):
      start = time.time()
      await message.channel.send(random.choice(test_List))
      end = time.time()
      total = end - start
      print('%.2f' % total, 'Seconds')

    options = troll_List
    if "games" in db.keys():
      options = options + list(db["games"])

    if message.content.startswith('palico tell me what to play'):
      start = time.time()
      await message.channel.send(random.choice(options))
      end = time.time()
      total = end - start
      print('%.2f' % total, 'Seconds')
      
    if message.content.startswith('$add'):
      start = time.time()
      game_List = message.content.split('$add')[1].strip().upper()
      update_game_list(game_List)
      await message.channel.send('Game has been added to list')
      end = time.time()
      total = end - start
      print('%.2f' % total, 'Seconds')

    if message.content.startswith('$del'):
      start = time.time()
      games = []
      if "games" in db.keys():
        game = str(message.content).split('$del')[1].strip().upper()
        index = db['games'].index(game)
        delete_game_list(int(index))
        index = db["games"]
      await message.channel.send('Game has been deleted')
      end = time.time()
      total = end - start
      print('%.2f' % total, 'Seconds')

    if message.content.startswith('$game list'):
      start = time.time()
      listOrder = 'Game list in order:\n'
      for game in db['games']:
        listOrder = listOrder + f'{db["games"].index(game)}: {game}\n'
      await message.channel.send(listOrder)
      end = time.time()
      total = end - start
      print('%.2f' % total, 'Seconds')

    if message.content.startswith('$item info'):
      start = time.time()
      UserInput = message.content.split('$item info')[1].strip()
      try:
        index = items['name'].index(str(UserInput).lower())
        await message.channel.send(items['descriptions'] [index])
      except:
        suggest = f'Sorry I do not recognize "{UserInput}". Did you mean to say any of the following?'
        row = 0
        for item in items['name']:
          if str(UserInput).lower() in str(item).lower():
            row += 1
            suggest += f'\n{row}) {item}'
        await message.channel.send(suggest)
      end = time.time()
      total = end - start
      print('%2f' % total, 'Seconds')

    if message.content.startswith('$monster info '):

      csv2 = pandas.read_csv('MonsterInfo.csv')
      monsters = {
          'mname': [], 'weakness': [], 'resistance':[]
        }
      
      def element_status(order):
        if order == 0:
          return 'Fire'
        elif order == 1:
          return 'Water'
        elif order == 2:
          return 'Thunder'
        elif order == 3:
          return 'Ice'
        elif order == 4:
          return 'Dragon'
        elif order == 5:
          return 'Poison'
        elif order == 6:
          return 'Sleep'
        elif order == 7:
          return 'Paralysis'
        elif order == 8:
          return 'Blast'
        elif order == 9:
          return 'Stun'
      
      for index, row in csv2.iterrows():
        
        name =row[0]
        form = row[2]
        fire = row[3]
        water = row[4]
        thunder = row[5]
        ice = row[6]
        dragon = row[7]
        poison = row[8]
        sleep = row[9]
        paralysis = row[10]
        blast = row[11]
        stun = row[12]
        mlist = 0
      
      elements = [fire, water, thunder, ice, dragon, poison, sleep, paralysis, blast, stun]
      
      if len(str(form)) > 3:
        mweak = f'Weak to "{form}":\n'
        mresistance = f'Resistant against "{form}":\n'
      else:
        mweak = f'Weak to:\n'
        mresistance = f'Resistant to:\n'
      for element in elements:
        try:
          if int(element) < 2:
            mresistance += f'- {element_status(mlist)}\n'
          elif int(element) >= 2:
            mweak += f'- {element_status(mlist)}\n'
          mlist += 1
        except:
          mlist += 1
      monsters['mname'].append(str(name).lower())
      monsters['resistance'].append(mresistance)
      monsters['weakness'].append(mweak)

      
      print(monsters['mname'])
      UserInput2 = message.content.split('$monster info')[1].strip().lower()
      

      for name in monsters['mname']:
        if UserInput2 == name:
          await message.channel.send(monsters['mname']['weakness'][mlist])
          mlist += 1
      else:
        await message.channel.send("monster not found")
          

my_secret = os.environ['token']      
client.run(os.getenv("token"))


