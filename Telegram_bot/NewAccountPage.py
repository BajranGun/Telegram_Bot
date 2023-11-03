import sqlite3
import tkinter as tk

class NewAccountPage():
    def __init__(self, main_window):
        self.main_window = main_window
        self.window = tk.Toplevel()
        self.window.protocol("WM_DELETE_WINDOW", self.close_wo_submit)
        self.window.title("New Account")
        self.window.geometry("300x300")
        self.con = sqlite3.connect("accounts.db")

        self.window.rowconfigure(0, weight=1)
        self.window.rowconfigure(1, weight=1)
        self.window.rowconfigure(2, weight=1)
        self.window.rowconfigure(3, weight=1)
        self.window.columnconfigure(0, weight=1)

        self.new_account_label = tk.Label(self.window, text="NEW ACCOUNT", foreground="red")
        self.new_account_label.grid(row=0, column=0)

        self.entry_frame = tk.LabelFrame(self.window)
        self.entry_frame.grid(row=1, column=0)

        self.account_name_label = tk.Label(self.entry_frame, text="Enter Account Name")
        self.account_name_label.pack()

        self.account_name_entry = tk.Entry(self.entry_frame)
        self.account_name_entry.pack()

        self.api_hash_label = tk.Label(self.entry_frame, text="Enter API Hash")
        self.api_hash_label.pack()

        self.api_hash_entry = tk.Entry(self.entry_frame)
        self.api_hash_entry.pack()

        self.api_id_label = tk.Label(self.entry_frame, text="Enter API ID")
        self.api_id_label.pack()

        self.api_id_entry = tk.Entry(self.entry_frame)
        self.api_id_entry.pack()

        self.phone_label = tk.Label(self.entry_frame, text="Enter Phone Number")
        self.phone_label.pack()

        self.phone_entry = tk.Entry(self.entry_frame)
        self.phone_entry.pack()

        self.submit_button = tk.Button(self.window, text="Submit", command=lambda:self.submit_account(account_name=self.account_name_entry.get(),
                                                                                                      api_id=self.api_id_entry.get(),
                                                                                                      api_hash=self.api_hash_entry.get(),
                                                                                                      phone_number=self.phone_entry.get()))
        self.submit_button.grid(row=2, column=0)
    
    def create_table(self):
        self.con.execute('''CREATE TABLE Accounts IF NOT EXISTS
                         (Account_name TEXT NOT NULL)''')
        
        
    
    def insert_table(self, account_name, api_id, api_hash, phone_number):
        self.con.execute(f'''INSERT INTO accounts(Account_name, Api_ID, Api_hash, phone_number) VALUES ({account_name},
                                                                                                        {api_id}, 
                                                                                                        {api_hash}, 
                                                                                                        {phone_number})''')
        
        self.con.commit()
    
    def close_wo_submit(self):
        self.window.destroy()
        self.main_window.deiconify()
        
    def submit_account(self, account_name, api_id, api_hash, phone_number):
        self.create_table()
        self.insert_table(account_name, api_id, api_hash, phone_number)
        self.con.close()
        self.window.destroy()
        self.main_window.deiconify()