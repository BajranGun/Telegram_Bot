import tkinter as tk

class CodePage():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Code Confirmation")
        self.window.geometry("300x100")

        self.window.rowconfigure(0, weight=1)
        self.window.rowconfigure(1, weight=1)
        self.window.columnconfigure(0, weight=2)
        self.window.columnconfigure(1, weight=1)

        self.code_label = tk.Label(self.window, text="Please Enter Your Code")
        self.code_label.grid(row=0, column=0)

        self.code_entry = tk.Entry(self.window)
        self.code_entry.grid(row=1, column=0)

        self.submit_button = tk.Button(self.window, text="Submit")
        self.submit_button.grid(row=1, column=1)

    def run(self):
        self.window.mainloop()

MyCodePage = CodePage()
MyCodePage.run()