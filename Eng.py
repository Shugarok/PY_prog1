import os
import webbrowser
import time


import Lan
import prog


def init_commands_Eng():
    print("No errors found_ENG\n")
    commands_Eng()


def commands_Eng():
    print("Type help for a list of commands")
    t = input()

    if t.lower() == "help":
        print("lanchg - Changes the language")
        print("tim - Shows the time")
        print("open - Opens the selected file (IMPORTANT that the file is in the same directory as the program) open nameENG.txt <--you can try this command")
        print("exit0 - Turns off the program")
        print("System - opens additional functions related to the system")
        print("run - Runs the specified program (run + program name)")
        print("openweb  - Opens a web page(openweb + url)")
        print("cls - Clears the screen")
        return commands_Eng()


    elif t.lower() == "System" or t.lower() == "system":
        prog.system_ENG()

    elif t.lower() == "Cls" or t.lower() == "cls":
        os.system('CLS')
        return commands_Eng()

    elif t.lower() == "Tim" or t.lower() == "tim":
        prog.show_time()
        return commands_Eng()


    elif t.lower() == "Lanchg" or t.lower() == "lanchg":
        Lan.lan()

    elif t.lower() == "Exit" or t.lower() == "Exit0" or t.lower() == "exit0" or t.lower() == "exit":
        print("The program will turn off after 5 seconds")
        time.sleep(5)
        exit(0)


    elif t.lower().startswith("open "):
        filename = t[5:]
        try:
            with open(filename, 'r') as f:
                content = f.read()
                print("File contents:")
                print(content)
        except FileNotFoundError:
            print("File not found")
        return commands_Eng()


    elif t.lower().startswith("run "):
        program_name = t[4:]
        try:
            os.system(program_name)
            print(f"Program '{program_name}' has been run.")
        except Exception as e:
            print(f"Error: {e}")
        return commands_Eng()

    elif t.lower().startswith("openweb "):
        url = t[8:]
        webbrowser.open(url)
        print(f"Opening web page: {url}")
        return commands_Eng()

    else:
        print("Unknown command")
        return commands_Eng()