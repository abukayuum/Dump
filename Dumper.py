import requests
import random
import sys
import json
import os
import re
from time import sleep as slp
from os import system as cmd
import os

try:
    os.remove('temp.txt')
except:
    pass

try:
    token = open('token.txt', 'r').read()
except Exception as error:
    exit(error)
try:
    cookie = open('cookie.txt', 'r').read()
except Exception as error:
    exit(error)

ua = 'Mozilla/5.0 (Linux; Android 14; moto g64 5G Build/U1TDS34.100-46-7-2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.104 Mobile Safari/537.36'

cod = []
cod1 = []
cod2 = []
oO = []
totaldmp = 0
count = 0

def grep(f):
    o = input('\033[0;97m[->] Save As : ')
    try:
        ask_link = int(input('\n[->] Enter Grip ID Limit: '))
    except:
        ask_link = 1
        completed = 0
    for links in range(ask_link):
        li = input('[✓] Separate Object : ')
        os.system('cat '+f+' | grep "'+li+'" >> '+o)
    print("")

    print("[->] Separating Successful ")
    print("[->] New File Save " + o)
    input("\n[>>] Press Inter to go Back < ")
    p_dump()


tokenlist = []
cookielist = []
tokenlist.append(token)
def login2():
    try:
        req = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenlist[0], cookies={'cookie': cookie}).json()
        Name = req['name']
        Uid = req['id']
    except Exception as error:
        print(error)


def p_dump():
    login2()
    global totaldmp, count
    try:
        os.system('clear')
        head = {
            "User-Agent": ua
        }
        params = {
            'access_token': token,
            'fields': "friends"}
        try:
            fbbuid = input("[->] Enter Public UID: ")
            dmp = requests.get("https://graph.facebook.com/"+fbbuid, headers = head, params = params, cookies={"cookie": fbcokis}).json()
            apnd = open('temp.txt', 'a')
            for idnm in dmp['friends']['data']:
                totaldmp += 1
                apnd.write(idnm['id']+'\n')
            print(apnd)
        except KeyError:
            print("\n\x1b[1;91m[!] UID WAS NOT PUBLIC")
            p_dump()
        apnd.close()
        filepath = input("\n[->] Enter File Path: ")
        ch_x2 = input("\n[->] Do You Want to Use UID Separator (n/y) LIKE 100084_100083: ")
        if ch_x2 in ["yes", "Yes", "YES", "Y", "y"]:
            oO.append('Ya')
            code = input('[-] SEP LINK1: ')
            code1 = input('[-] SEP LINK2: ')
            code2 = input('[-] SEP LINK3: ')
            cod.append(code)
            cod1.append(code1)
            cod2.append(code2)
        else:
            oO.append('No')
        apnd = open(filepath, 'a')
        fbidz = open('temp.txt', 'r').read().splitlines()
        for fbuid in fbidz:
            count += 1
            try:
                dmp = requests.get("https://graph.facebook.com/"+fbuid, headers = head, params = params, cookies={"cookie": cookie}).json()
                for idnm in dmp['friends']['data']:
                    totaldmp += 1
                    apnd.write(idnm['id']+"|"+idnm['name']+'\n')
                if 'Ya' in oO:
                    os.system('cat '+filepath+' | grep "'+cod[0]+'" >> Hmm')
                    os.system('cat '+filepath+' | grep "'+cod1[0]+'" >> Hmm')
                    os.system('cat '+filepath+' | grep "'+cod2[0]+'" >> Hmm')
                    os.system('sort -r Hmm | uniq > '+filepath)
                    os.system('rm -rf Hmm')
                    print("\x1b[1;92m Dumping UID From: " + fbuid)
                else:
                    print("\x1b[1;92m Dumping UID From: " + fbuid)
            except KeyError:
                print('\x1b[1;91m Dumping UID From: ' + fbuid)
        apnd.close()
        ch_x1 = input("[->] Do You Want to Use Without Duplicate UID(n/y): ")
        if ch_x1 in ["yes", "Yes", "YES", "Y", "y"]:
            newfile = input("\n[->] File Path Without Duplicate UID Save As: ")
            os.system('sort -r '+filepath+' | uniq > '+newfile)
            if 'ouoo' == 'oo':
                os.system('rm -rf akakajh')
            else:
                print(47*'-')
                print(
                    f"\x1b[0;37m Your Dump File Save As:\x1b[1;92m {newfile} \x1b[0;37m")
                print(47*'-')
                print('\n')
                input("\n[->] Press Inter to go Back << ")
                p_dump()
        else:
            print(47*'-')
            print(f"\x1b[0;37m Total ID Dump :\x1b[1;92m {totaldmp}")
            print(f"\x1b[0;37m Your Dump File Save As :\x1b[1;92m {filepath} ")
            print(47*'-')
            input("\n[>>] Press Inter to go Back < ")
            p_dump()
    except Exception as e:
        print("[>>] Error: %s" % e)
        exit("")


if __name__ == '__main__':
    p_dump()
