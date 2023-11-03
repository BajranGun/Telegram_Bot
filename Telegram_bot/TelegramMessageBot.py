from telethon.sync import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
import os, time, random
import requests

class TelegramMessageBot():
    def __init__(self, api_id, api_hash):
        self.api_id = api_id
        self.api_hash = api_hash
        self.target_groups = ["https://t.me/vfs_globa1"]
        self.user_list = []
    
    def generate_otp(self, phone):
        client = TelegramClient("session", self.api_id, self.api_hash)
        self.phone = phone
        client.connect()
        result = client.send_code_request(self.phone)
        self.phone_hash = result.phone_code_hash
        print(result)
    
    def verify_otp(self, code):
        client = TelegramClient("session", self.api_id, self.api_hash)
        client.connect()
        client.sign_in(self.phone,
                        code=code,
                        phone_code_hash=self.phone_hash)

    def send_message(self, message):
        client = TelegramClient("session", self.api_id, self.api_hash)
        client.connect()
        for group in self.target_groups:
            all_participants = client.get_participants(group, aggressive=True)
            for user in all_participants:
                userr={}
                user_id = user.id
                user_name = user.username
                user_hash = user.access_hash
                userr["user_id"] = user_id
                userr["user_name"] = user_name
                userr["user_hash"] = user_hash
                self.user_list.append(userr)
        

        for user in self.user_list:
            reciever = client.get_input_entity(user["user_id"])
            client.send_message(reciever, message)
            time.sleep(random.randrange(1, 3))

        client.log_out()