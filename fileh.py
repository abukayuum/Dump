import requests,bs4,json,os,sys,random,time,re
import urllib3,rich,base64
from cfonts import render, say

# My Variables
id = [] 
Bes_Tok = [] 
uid = []
ses=requests.Session()
logo = render('File', colors=['white', 'green'], align='center')
cook = render('Cookies', colors=['white', 'yellow'], align='center')
# ------------[ My Colors ]--------------#
Bes_Red = '\033[1;31m'
Bes_Yell = '\033[1;33m'
Bes_Green = '\033[1;32m' 
Bes_Bl = '\033[1;34m'
Bes_White = '\033[0;97m'

def clear():
    os.system('clear')

# اتصال تسجيل دخول كوكيز تقدر تضيفه ب اداتك الفايس و تخليها من ايديات اتصال جديد
def login():
	try:
		clear()
		print(cook)
		cookie = input(f'{Bes_White} - Cookies : ')
		open("/sdcard/Besto/File_Ids/.cok.txt", "w").write(cookie)
		with requests.Session() as Besto:
			try:
				# تقدر تضيف يوزر اجنت عشوائي ادا تريد
				Besto.headers.update({'Accept-Language': 'id,en;q=0.9','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36','Referer': 'https://www.instagram.com/','Host': 'www.facebook.com','Sec-Fetch-Mode': 'cors','Accept': '*/*','Connection': 'keep-alive','Sec-Fetch-Site': 'cross-site','Sec-Fetch-Dest': 'empty','Origin': 'https://www.instagram.com','Accept-Encoding': 'gzip, deflate',})
				response = Besto.get('https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&redirect_uri=https://www.instagram.com/brutalid_/', cookies={'cookie':cookie})
				if '"access_token":' in str(response.headers):
					token = re.search('"access_token":"(.*?)"', str(response.headers)).group(1)
					open("/sdcard/Besto/File_Ids/.token.txt", "w").write(token)
					print(f"{Bes_Green} - Login Done √ {Bes_White}") 
				else:
					print(f'{Bes_Yellow} - Failed To Login ! ')
			except:
				print(f'{Bes_Red} - Failled To Get Token ! ')
		time.sleep(2)
		menu()
	except Exception as e:
		os.system("rm -f /sdcard/Besto/File_Ids/.token.txt")
		os.system("rm -f /sdcard/Besto/File_Ids/.cok.txt")
		print(f'{Bes_White} - Cookies Not Found')
		exit()
		
#------------------[ My Menu ]----------------#
def menu():
	try:
		token = open('/sdcard/Besto/File_Ids/.token.txt','r').read()
		cok = open('/sdcard/Besto/File_Ids/.cok.txt','r').read()
	except IOError:
		print(f'{Bes_White} - Cookies Not Found')
		time.sleep(2)
		login()
	os.system('clear')
	print(logo)
	print(f' [1] - Create File Ids ')
	print(f' [2] - Delete Double Ids ')
	print(f' [0] - Delete Cookies ')
	print('')
	Bes_H = input(f' - Choose : ')
	if Bes_H in ['1']:
		Bes_Menu_1()
	elif Bes_H in ['2']:
		Bes_Rev()
	elif Bes_H in ['0']:
		os.system('rm -rf /sdcard/Besto/File_Ids/.token.txt')
		os.system('rm -rf /sdcard/Bes/Bes_Login/.cookie.txt')
		print(f'{Bes_Yellow} - Cookies Was Deleted Done √ ')
		exit()
	else:
		print(f'{Bes_Red} - Choice Incorrect ')
		exit()
		
# Extract Ids H  - سحب ايديات 
def Bes_Menu_1():
	os.system('clear');print(logo)
	try:
		token = open('/sdcard/Besto/File_Ids/.token.txt','r').read()
		cok = open('/sdcard/Besto/File_Ids/.cok.txt','r').read()
	except IOError:
	    exit()
	try:
		Bes_File = input(' - Enter File Name [ For Save Ids ] : ')
		Bes_Tota_Id = int(input(f' - Enter Total Id : '))
		# ادا كان شيء غلط ب عدد
	except ValueError:
	    exit()
		# ادا كان ايديات اصغر من واحد او اكبر من 1000 خروج اداة
	if Bes_Tota_Id<1 or Bes_Tota_Id>1000:
	    exit()
	ses=requests.Session()
	# هاد مال ارقام 12345 الخ
	id_number = 0
	for Bes_H_H in range(Bes_Tota_Id):
		id_number+=1
		Enter_id = input(f' - Enter Id '+str(id_number)+' : ')
		uid.append(Enter_id)
	for user in uid:
	    try:
				# سحب من اصدقاء الايدي  اتصال بدون حضر 
	       head = ({"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"})
	       if len(id) == 0:
	           params = ({'access_token': token,'fields': "friends"})
	       else:
	           params = ({'access_token': token,'fields': "friends"})
	       url = requests.get('https://graph.facebook.com/{}'.format(user),params=params,headers=head,cookies={'cookies':cok}).json()
	       for Besto in url['friends']['data']:
	           try:
		# هدا يا صديقي مال يحط ايدي + | + اسم حساب
	               Besto_H = (Besto['id']+'|'+Besto['name']);open(f'%s'%(Bes_File),'a').write(Besto['id']+'|'+Besto['name']+'\n')
	               if Besto_H in id:pass
	               else:id.append(Besto_H)
	           except:continue
	    except (KeyError,IOError):
	      pass
	    except requests.exceptions.ConnectionError:
	        exit()
	try:
	      print('');print(f"{Bes_White} - Total Id Extracted : "+str(len(id))) 
	      print(f' - File Save As : {Bes_Green}{Bes_File}{Bes_White}')
	      time.sleep(5);menu()
	except requests.exceptions.ConnectionError:
	    exit()
	except (KeyError,IOError):
		exit()

def Bes_Rev():
    try:
        os.system('clear');print(logo)
        print('')
        filename = input(' - File : ')
        sd = '/sdcard/'
        file_path = os.path.join(sd, filename)
        with open(file_path, 'r') as file:
            lines = file.read().splitlines()
        lines = sorted(set(lines))
        with open(file_path, 'w') as file:
            for line in lines:
                file.write(line + '\n')
        print('')
        print(f'{Bes_Green} - Done Delete Doubles Ids ')
        print(f'{Bes_White} - Saved As Same File {Bes_Green}[{filename}]')
        exit()
    except:
    	print(' - Not Found a Doubles Ids ');exit()

#-----------------------[ End H Bye ]--------------------#
if __name__=='__main__':
	try:os.mkdir("/sdcard/Besto")
	except:pass
	try:os.mkdir("/sdcard/Besto/Besto_H")
	except:pass
	try:os.mkdir("/sdcard/Besto/File_Ids")
	except:pass
	login()
	
	# النهاية اداة برمجتي من 0 اخمط براحتك بس لا تنسى كلمة شكرا