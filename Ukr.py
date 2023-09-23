import os
import webbrowser
import time


import Lan
import prog


def init_commands_Ukr():
    os.system('CLS')
    print("No errors found_UKR\n")
    commands_Ukr()


def commands_Ukr():
    print("Напишіть help для отримання списку команд")
    t = input()

    if t.lower() == "help":
        print("lanchg - Змінює мову")
        print("tim - Показує час")
        print("open - Відкриває вибраний файл (ВАЖЛИВО щоб файл був у тій самій директорії, що й програма) open nameUKR.txt <--можете спробувати цю команду")
        print("exit0 - Вимикає програму")
        print("System - відкриває додаткові функції пов'язані з системою")
        print("run - Запускає вказану програму (run + назва програми)")
        print("openweb - Відкриває веб-сторінку (openweb + url)")
        print("cls - Очищає екран")
        return commands_Ukr()
    elif t.lower() == "System" or t.lower() == "system":
        prog.system_UKR()


    elif t.lower() == "Tim" or t.lower() == "tim":
        prog.show_time()
        return commands_Ukr()

    elif t.lower() == "Exit" or t.lower() == "Exit0" or t.lower() == "exit0" or t.lower() == "exit":
        print("Програма вимкнеться через 5 секунд")
        time.sleep(5)
        exit(0)
    elif t.lower() == "Cls" or t.lower() == "cls":
        os.system('CLS')
        return commands_Ukr()

    elif t.lower() == "Lanchg" or t.lower() == "lanchg":
        Lan.lan()

    elif t.lower().startswith("open "):
        filename = t[5:]
        try:
            with open(filename, 'r') as f:
                content = f.read()
                print("Вміст файлу:")
                print(content)
        except FileNotFoundError:
            print("Файл не знайдено")
        return commands_Ukr()


    elif t.lower().startswith("run "):
        program_name = t[4:]
        try:
            os.system(program_name)
            print(f"Програма '{program_name}' була запущена.")
        except Exception as e:
            print(f"Помилка: {e}")
        return commands_Ukr()


    elif t.lower().startswith("openweb "):
        url = t[8:]
        webbrowser.open(url)
        print(f"Opening web page: {url}")
        return commands_Ukr()

    else:
        print("Немає такої команди.")
        return commands_Ukr()