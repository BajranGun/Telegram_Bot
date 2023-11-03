import tkinter as tk
import time
from TelegramMessageBot import TelegramMessageBot as TMBot

class API_ID_Hash_Window():
    def __init__(self):
        #General setup
        self.users_path = "users"

        #Setup window
        self.window = tk.Tk()
        self.window.geometry("300x300")
        self.window.title("Telegram Mesaj Botu")

        #Font
        font = "Calibri 16 bold"
        self.api_id_label = tk.Label(self.window, text="API ID giriniz.", font=font)
        self.api_id_label.pack()

        self.api_id_entry = tk.Entry(self.window)
        self.api_id_entry.pack()

        self.api_hash_label = tk.Label(self.window, text="API Hash giriniz.", font=font)
        self.api_hash_label.pack()

        self.api_hash_entry = tk.Entry(self.window)
        self.api_hash_entry.pack()

        self.ok_button = tk.Button(self.window, text="OK", command=self.phone_popup)
        self.ok_button.pack()

    
    def phone_popup(self):
        MyTMBot = TMBot(api_id=self.api_id_entry.get(),
                        api_hash=self.api_hash_entry.get())
        
        popup = tk.Tk()
        popup.geometry("300x300")
        popup.title("Hesap Onaylama")

        phone_label = tk.Label(popup, text="Telefon Numarası")
        phone_label.pack()

        phone_entry = tk.Entry(popup)
        phone_entry.pack()

        ok_button = tk.Button(popup, text="OK", command=lambda:self.auth_phone(MyTMBot, phone_entry))
        ok_button.pack()

        code_label = tk.Label(popup, text="Onay Kodunu Giriniz")
        code_label.pack()

        code_entry = tk.Entry(popup)
        code_entry.pack()

        message_label = tk.Label(popup, text="Mesajınızı Giriniz")
        message_label.pack()

        message_entry = tk.Entry(popup)
        message_entry.pack()

        ok_button_2 = tk.Button(popup, text="OK", command=lambda:self.auth_code(MyTMBot,
                                                                                code=code_entry.get(),
                                                                                message=message_entry.get()
                                                                                ))
        ok_button_2.pack()

    
    def auth_phone(self, Bot, phone_entry):
        Bot.generate_otp(phone=phone_entry.get())

    def auth_code(self, Bot, code, message):
        Bot.verify_otp(code)
        time.sleep(60)
        Bot.send_message(message)

    def run(self):
        self.window.mainloop()

UW = API_ID_Hash_Window()
UW.run()