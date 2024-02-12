import time
import random
import string

try:
    import requests
    import colorama
    from colorama import Fore, Back, Style
    import json
except ModuleError:
    pass


headers = {
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
}


def main():

    while(True):
        print(f"{Fore.YELLOW}=" * 100)
        print()
        print(f"{Fore.YELLOW}░██████╗░█████╗░████████╗██╗░░░██╗██████╗░███╗░░██╗  ██████╗░░█████╗░██████╗░██╗░░░░░░█████╗░██╗░░██╗")
        print(f"██╔════╝██╔══██╗╚══██╔══╝██║░░░██║██╔══██╗████╗░██║  ██╔══██╗██╔══██╗██╔══██╗██║░░░░░██╔══██╗╚██╗██╔╝")
        print(f"╚█████╗░███████║░░░██║░░░██║░░░██║██████╔╝██╔██╗██║  ██████╔╝██║░░██║██████╦╝██║░░░░░██║░░██║░╚███╔╝░")
        print(f"░╚═══██╗██╔══██║░░░██║░░░██║░░░██║██╔══██╗██║╚████║  ██╔══██╗██║░░██║██╔══██╗██║░░░░░██║░░██║░██╔██╗░")
        print(f"██████╔╝██║░░██║░░░██║░░░╚██████╔╝██║░░██║██║░╚███║  ██║░░██║╚█████╔╝██████╦╝███████╗╚█████╔╝██╔╝╚██╗")
        print(f"╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░░╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝  ╚═╝░░╚═╝░╚════╝░╚═════╝░╚══════╝░╚════╝░╚═╝░░╚═╝")
        print()
        print(f"██╗░░░██╗░██████╗███████╗██████╗░███╗░░██╗░█████╗░███╗░░░███╗███████╗")
        print(f"██║░░░██║██╔════╝██╔════╝██╔══██╗████╗░██║██╔══██╗████╗░████║██╔════╝")
        print(f"██║░░░██║╚█████╗░█████╗░░██████╔╝██╔██╗██║███████║██╔████╔██║█████╗░░")
        print(f"██║░░░██║░╚═══██╗██╔══╝░░██╔══██╗██║╚████║██╔══██║██║╚██╔╝██║██╔══╝░░")
        print(f"╚██████╔╝██████╔╝███████╗██║░░██║██║░╚███║██║░░██║██║░╚═╝░██║███████╗")
        print(f"░╚═════╝░╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝")
        print()
        print(f"░██████╗░███████╗███╗░░██╗███████╗██████╗░░█████╗░████████╗░█████╗░██████╗░")
        print(f"██╔════╝░██╔════╝████╗░██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗")
        print(f"██║░░██╗░█████╗░░██╔██╗██║█████╗░░██████╔╝███████║░░░██║░░░██║░░██║██████╔╝")
        print(f"██║░░╚██╗██╔══╝░░██║╚████║██╔══╝░░██╔══██╗██╔══██║░░░██║░░░██║░░██║██╔══██╗")
        print(f"╚██████╔╝███████╗██║░╚███║███████╗██║░░██║██║░░██║░░░██║░░░╚█████╔╝██║░░██║")
        print(f"░╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝")
        print()
        print(f"{Fore.YELLOW}=" * 100)
        print()
        print(f"{Fore.WHITE}[Saturn Roblox Username Generator is a generator for roblox to make usernames for any length you want!]")
        print()
        print(f"{Fore.WHITE}[The generator can tell you if the name is valid or invaild or even inappropriate, and will make a 3 text files for valid users and invalid ones!]")
        print()
        print(f"{Fore.WHITE}[In order to start generating type a length number for the username. (Min 3, Max 20) ]")
        print()
        input1 = int(input(f"{Fore.CYAN}[>] "))
        if(input1 > 20):
            input(f"{Fore.RED}Number shouldn't be above 20. [PRESS ENTER] ")
        elif(input1 < 3):
            input(f"{Fore.RED}Number shouldn't be lower than 3. [PRESS ENTER] ")
        else:
            break

    print(f"{Fore.WHITE}[Write how many times do you want to generate usernames]")
    print()
    input2 = int(input(f"{Fore.CYAN}[>] "))
    print()
    for i in range(input2):
        userNameGen = "".join(random.choices(string.ascii_letters + string.digits, k=input1))
        url = requests.get(f"https://auth.roblox.com/v1/usernames/validate?Username=" + userNameGen + "&Birthday=8%2F13%2F2000&Context=1", headers=headers)
        urljson = json.loads(url.text)
        print()
        if(urljson['code'] == 0):
            print(f"{Fore.GREEN}[VALID]: {userNameGen}")
            with open("ValidUsernames.txt", "a") as f:
                f.write(userNameGen + "\n")
        elif(urljson['code'] == 1):
            print(f"{Fore.RED}[INVALID]: {userNameGen}")
            with open("InvalidUsernames.txt", "a") as f:
                f.write(userNameGen + "\n")
        elif(urljson['code'] == 2):
            print(f"{Fore.RED}[USERNAME IS INAPPROPRIATE]: {userNameGen}")
            with open("InappropriateUsernames.txt", "a") as f:
                f.write( userNameGen+ "\n")

    print()
    input(f"{Fore.GREEN}Finished generating usernames! [PRESS ENTER TO CONTINUE] ")
    main()

# Runs the main function

if __name__ == "__main__":
    main()
