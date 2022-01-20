import discord
import os
import json
import requests
import random

client = discord.Client()

nono_words = ["nincompoop", "booger", "depressed", "blob sucks", "boogers"]
great_words = ["i am awesome", ""]

nono_msg = [
  "Don't say nono words! :<",
  "Don't do that again!",
  "You are not pog :<"
]
yes_msg = [
  "Great! You are now super pog!",
  "You are now super famous!",
  "Awww, no you don't! You're awesome!"
]

PREFIX = "-"

def thync():
  res = requests.get("https://thync-API.jbloves27.repl.co/toggle")
  return res.content

@client.event
async def on_ready():
  print(f"Bot logged in as {client.user}")

@client.event
async def on_message(msg):
  if msg.author == client.user:
    return

  MSG = msg.content

  if MSG.startswith(f"{PREFIX}help"):
    await msg.channel.send(f"""
    ```Commands:
    Syntax: {PREFIX}command [optional text]
    Prefix: `{PREFIX}`

    `{PREFIX}help [optional text]`: Helps with bot commands.
    `{PREFIX}search [text]`: Searches google.
    `{PREFIX}thync [on/off]`: Turns on/off thync.
    `{PREFIX}memes [optional text]`: Memes.
    ```""")
  
  if any(word in MSG for word in nono_words):
    await msg.channel.send(random.choice(nono_msg))


client.run(os.environ["TOKEN"])