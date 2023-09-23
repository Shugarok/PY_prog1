import tkinter as tk
import time
import os

import Ukr
import Eng
import Lan




def show_time():
    root = tk.Tk()
    root.title('TIME')

    time_label = tk.Label(root, font=('calibri', 40, 'bold'), background='purple', foreground='white')
    time_label.pack(anchor='center')

    def update_time():
        current_time = time.strftime('%H:%M:%S %p')
        time_label.config(text=current_time)
        time_label.after(1000, update_time)

    update_time()
    root.mainloop()




def system_UKR():
    os.system('CLS')
    print('CH - checking files')
    print("Back - Повернутися")
    a = input()

    if a == "Back":
        os.system('CLS')
        Ukr.init_commands_Ukr()

    if a == "CH":


        try:
            print("Перевірка файлу - Lan.txt")
            with open('Lan.txt', 'r') as q:
                content = q.read().strip()
                print("Файл знайдено")
                time.sleep(2)
        except FileNotFoundError:
            content = Lan.error_lan()



        try:
            print("Перевірка файлу - main.py")
            with open('main.py', 'r') as q:
                q.read().strip()
                print("Файл знайдено")
                time.sleep(2)
        except FileNotFoundError:
            print("Критична помилка")
            print("Спробуйте завантажити програму ще раз")

        if content == "Ukr":
            Ukr.init_commands_Ukr()
        elif content == "Eng":
            Eng.init_commands_Eng()






def system_ENG():
    os.system('CLS')
    print('CH - checking files')
    print("Back - Back")
    a = input()

    if a == "Back":
        os.system('CLS')
        Eng.init_commands_Eng()

    if a == "CH":

        try:
            print("Checking the file - Lan.txt")
            with open('Lan.txt', 'r') as q:
                content = q.read().strip()
                print("File found")
                time.sleep(3)
                os.system('CLS')
        except FileNotFoundError:
            Lan.error_lan()


        try:
            print("Checking the file - main.py")
            with open('main.py', 'r') as q:
                q.read().strip()
                print("File found")
                time.sleep(2)
        except FileNotFoundError:
            print("Critical error")
            print("Try downloading the app again")
            time.sleep(4)
            exit(0)


        try:
            print("Checking the file - prog.py")
            with open('prog.py', 'r') as q:
                q.read().strip()
                print("File found")
                time.sleep(2)
        except FileNotFoundError:
            print("Critical error")
            print("Try downloading the app again")
            time.sleep(4)
            exit(0)



        if content == "Ukr":
            Ukr.init_commands_Ukr()
        elif content == "Eng":
            Eng.init_commands_Eng()
