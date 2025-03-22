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
def homebrew_installer(install_cmd):
    now = datetime.now()
    formatted = now.strftime("%Y-%m-%d %H:%M:%S")
    date_time = f"[{formatted} --->]"
    with open("installer_py.log", "a", buffering=1) as file:
        try:
            subprocess.run(install_cmd, shell=True, capture_output=True, text=True)
            date_time = "✅ Homebrew was installed" + date_time
            print("✅ Homebrew was installed")
            file.write(date_time+"\n")
        except subprocess.CalledProcessError:
            print(Fore.RED + "Some error occured, please retry. If the problem persists please report the issue in github")
            rich_print("[bold red][link=https://github.com/Luciusharsh]GITHUB PROFILE[/link][/bold red]")

def homebrew_test(system_name):
    print(Fore.BLUE + f"So you have {system_name}!. Lets's get started with the installation then!☺️")
    print(Fore.BLUE + "Following upcomming steps will be easy!")
    try:
        homebrew = subprocess.run(["brew","--version"],check=True,capture_output=True)
        print("✅ Homebrew")
        install_cmd = '/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" -- --unattended'
        homebrew_installer(install_cmd)
    except subprocess.CalledProcessError:
        print("❌ Homebrew not found!")
        print(Fore.RED + "Homebrew is recomended to use this project!")
        tries = 5
        while(tries):
            reponse = str(input(Fore.LIGHTGREEN_EX + "Install homebrew? (y/n) : "))
            if reponse=="y":
                print("Installing homebrew in your system!")
                homebrew_installer()
                break  
            elif reponse=="no":
                print("NO PROBLEM!!, we have other ways too make it work")
                break
            else:
                tries-=1
                print("Please choose a valid option...and try again")
                print(f"Tries left = {tries}")
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
        homebrew_test(system_name)
    elif system_name == "Linux":
        print("This is a Linux system.")
        homebrew_test(system_name)
        install_cmd = "/bin/bash -c '$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)' -- --unattended"
        homebrew_installer(install_cmd)
    else:
        print(Fore.BLUE + "The program is not made for windows, but don't worry in future a windows version will be released!!")
        sys.exit()
if __name__ == "__main__":
    main()
