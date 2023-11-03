import tkinter as tk
from PIL import Image, ImageTk
from NewAccountPage import NewAccountPage
from NewGroupPage import NewGroupPage

class WelcomePage():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Welcome!")
        self.window.geometry("300x300")
        self.window.configure(bg="light green")

        self.welcome_frame = tk.LabelFrame(self.window,
                                           background="light blue",
                                           foreground="light blue")
        self.welcome_frame.pack(pady=15)

        self.welcome_label = tk.Label(self.welcome_frame, text="WELCOME!",
                                      background="light grey",
                                      foreground="blue")
        self.welcome_label.pack()

        self.account_dropbox_frame = tk.LabelFrame(self.window)
        self.account_dropbox_frame.configure(bg="light blue",
                                             fg="light blue")
        
        self.account_dropbox_frame.pack(pady=15)

        self.account_dropbox_var = tk.StringVar(self.window)
        self.account_dropbox_var.set("one")
        self.account_dropbox = tk.OptionMenu(self.account_dropbox_frame, self.account_dropbox_var,
                                             "one", "two", "three")
        
        self.account_dropbox.configure(bg="light blue",
                                       fg="blue",
                                       highlightbackground="light blue")
        self.account_dropbox.pack()

        self.group_dropbox_frame = tk.LabelFrame(self.window)
        self.group_dropbox_frame.configure(bg="light blue",
                                           fg="light blue")
        
        self.group_dropbox_frame.pack(pady=15)

        self.group_dropbox_var = tk.StringVar()
        self.group_dropbox_var.set("one")
        self.group_dropbox = tk.OptionMenu(self.group_dropbox_frame,
                                           self.group_dropbox_var,
                                           "one", "two", "three")
        
        self.group_dropbox.configure(bg="light blue",
                                     fg="blue",
                                     highlightbackground="light blue")
        self.group_dropbox.pack()

        self.button_frame = tk.LabelFrame(self.window)
        self.button_frame.configure(bg="light blue")
        self.button_frame.pack()

        self.button_frame.columnconfigure(0, weight=1)
        self.button_frame.columnconfigure(1, weight=1)
        self.button_frame.rowconfigure(0, weight=1)

        self.new_account_button = tk.Button(self.button_frame,
                                            text="New Account",
                                            command=self.start_account_page,
                                            foreground="blue",
                                            background="light blue")
        
        self.new_group_button = tk.Button(self.button_frame,
                                          text="New Group",
                                          command=self.start_group_page,
                                          foreground="blue",
                                          background="light blue")

        self.new_account_button.grid(row=0, column=0)
        self.new_group_button.grid(row=0, column=1)

        self.load = Image.open(r"C:\Users\pc\Desktop\Telegram_bot\right_arrow.jpg").convert("RGBA")
        self.resized_img = self.load.resize((25,25))
        
        self.render = ImageTk.PhotoImage(self.resized_img)
        self.click_btn = tk.Button(self.window, image=self.render)
        self.click_btn.place(relx= 0.90, rely=0.90)
    
    def start_account_page(self):
        self.window.withdraw()
        NewAccountPage(main_window=self.window)

    def start_group_page(self):
        self.window.withdraw()
        NewGroupPage(main_window=self.window)

    def run(self):
        self.window.mainloop()