import sys
from colorama import Fore, Style, init
import subprocess
import platform
import os
from rich import print as rich_print
from datetime import datetime
init(autoreset=True)
def main():
    compatibility_test()
# rich_print("[bold red][link=https://github.com/Luciusharsh]GITHUB PROFILE[/link][/bold red]")
def log_record(text):
    with open("installer_py.log", "a") as file:
        text = f"########################################{text}##########################################\n"
        file.write(text)
def compatibility_test():
    print(Fore.GREEN + "Checking your system Compatibility...")
    system_name = platform.system()
    if system_name == "Darwin":
        print("This is a Mac (macOS).")
        log_record(system_name)
    elif system_name == "Linux":
        print("This is a Linux system.")
    else:
        print(Fore.BLUE + "The program is not made for windows, but don't worry in future a windows version will be released!!")
        sys.exit()
if __name__ == "__main__":
    main()
