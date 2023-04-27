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

my_secret = os.environ['token']      
client.run(os.getenv("token"))


