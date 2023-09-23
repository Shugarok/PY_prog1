
import Lan
import Eng
import Ukr


def start_kernel():
    print("Starting up...")

    try:
        with open('Lan.txt', 'r') as q:
            content = q.read().strip()
    except FileNotFoundError:
        content = Lan.error_lan()

    if content == "Ukr":
        Ukr.init_commands_Ukr()

    elif content == "Eng":
        Eng.init_commands_Eng()




start_kernel()