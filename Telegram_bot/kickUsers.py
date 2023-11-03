from telethon.sync import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
import pandas as pd
import requests

api_id = "29728474"
api_hash = "6957e0462a33c2125a47f8007c5efbbb"
phone = "+905372076039"

client = TelegramClient(phone, api_id, api_hash)
client.start()

target_groups = ["https://t.me/+CPF5JyWFiq5lY2M0"]


user_list = []
for group in target_groups:
    all_participants = client.get_participants(group, aggressive=True)
    for user in all_participants:
        userr={}
        user_id = user.id
        user_name = user.username
        user_hash = user.access_hash
        userr["user_id"] = user_id
        userr["user_name"] = user_name
        userr["user_hash"] = user_hash
        user_list.append(userr)

user_list.remove(user_list[0])

for user in user_list:
    reciever = client.get_input_entity(user["user_id"])
    message = "deneme"
    client.kick_participant(-1001905718366, reciever)

client.log_out()