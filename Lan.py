import Eng
import Ukr
import time
import os

def error_lan():
    print("Language file not found. What language will we use? (This data can be changed)")
    print("Мовний файл не знайдено. Якою мовою ми будемо користуватися? (Ці дані можуть бути змінені)")
    time.sleep(5)
    os.system('CLS')
    return error_text()


def lan():
    ukr = 'Ukr'
    eng = 'Eng'

    print("Choose a language / Виберіть мову")
    print("1 - English")
    print("2 - Ukrainian")

    lan = input()

    if lan == "1":
        Eng.init_commands_Eng()
        with open('Lan.txt', 'w') as f:
            f.write(eng)
    elif lan == "2":
        Ukr.commands_Ukr()
        with open('Lan.txt', 'w') as f:
            f.write(ukr)






def error_text():
    ukr = 'Ukr'
    eng = 'Eng'
    print("1 - English")
    print("2 - Ukrainian")
    a = input()

    if a == "1":
        with open('Lan.txt', 'w') as f:
            f.write(eng)
        return eng
    elif a == "2":
        with open('Lan.txt', 'w') as f:
            f.write(ukr)
        return ukr
    else:
        print("Invalid choice. Please choose '1' for English or '2' for Ukrainian")
        print("Невірний вибір. Виберіть «1» для англійської мови або «2» для української.")
        return error_text()