import discord
import os
import random
from replit import db

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


test_List = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
troll_List = ["Why don't you play with some friends"]

def update_game_list(game_List):
  if "games" in db.keys():
    games = db["games"]
    games.append(game_List)
    db["games"] = games
  else:
    db["games"] = [game_List]


def delete_game_list(index):
  games = db["games"]
  index = int(float(index))
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
        await message.channel.send('Hello!')

    if message.content.startswith("$help"):
        await message.channel.send('To add a game to the list just say, $add followed by the name of the game you want to add. To delete a game off the list, just type $del followed by the number of the positon of the game in the list starting at 0')

    if message.content.startswith('$progress'):
        await message.channel.send('I am fully working!')

    if message.content.startswith('palico tell me a joke'):
        await message.channel.send('Here is a joke from where I come from. What do you call a hunting squad full of hunting horns? An orcestra. XD')

    if message.content.startswith('random number'):
        await message.channel.send(random.choice(test_List))

    options = troll_List
    if "games" in db.keys():
      options = options + list(db["games"])

    if message.content.startswith('palico tell me what to play'):
      await message.channel.send(random.choice(options))
      
    if message.content.startswith('$add'):
      game_List = message.content.split('$add ',1)[1]
      update_game_list(game_List)
      await message.channel.send('Game has been added to list')

  #for some reason it doesnt let me delete the games off the list will work on a fix
    if message.content.startswith('$del'):
      games = []
      if "games" in db.keys():
        index = message.content.split('$del', 1)[1]
        delete_game_list(index)
        index = db["games"]
      await message.channel.send(games)

    if message.content.startswith('$game list'):
      await message.channel.send(options)




      
      
        

        
                                   
      
my_secret = os.environ['token']      
client.run(os.getenv("token"))


