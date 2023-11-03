import tkinter as tk

class NewGroupPage():
    def __init__(self, main_window):
        self.window = tk.Toplevel()
        self.window.title("New Group")
        self.window.geometry("200x200")
        self.main_window = main_window
        self.window.protocol("WM_DELETE_WINDOW", self.submit_group)

        self.window.rowconfigure(0, weight=1)
        self.window.rowconfigure(1, weight=1)
        self.window.rowconfigure(2, weight=1)
        self.window.rowconfigure(3, weight=1)
        self.window.columnconfigure(0, weight=1)

        self.new_group_label = tk.Label(self.window, text="New Group", fg="red")
        self.new_group_label.grid(row=0, column=0)

        self.group_id_label = tk.Label(self.window, text="Enter Group Chat ID", fg="blue")
        self.group_id_label.grid(row=1, column=0)

        self.new_group_entry = tk.Entry(self.window)
        self.new_group_entry.grid(row=2, column=0)

        self.submit_button = tk.Button(self.window, text="Submit", command=self.submit_group)
        self.submit_button.grid(row=3, column=0)
    
    def submit_group(self):
        self.window.destroy()
        self.main_window.deiconify()
