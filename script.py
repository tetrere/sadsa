import json
from notifier_botty import login_to_chegg, refresh_chegg, telegram_both_sendtext
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime, timedelta
import pytz
import requests
import multiprocessing
import base64
from io import StringIO



x = 1  # Starting row index (inclusive) Row starts from 0 x=2 means Row 3
y = 7  # Ending row index (exclusive) 15 Row pomints to 14 row, but since it starts from 0 it points to 15 row


# Access secrets from environment variables


login_admin_bohit_token= '8131045025:AAEXVM5EpcSWGAL75leGo3lT7ccECa2JisU'
admin_chatID = '6966110728'





accounts = [
    {"username": "himanshubardwajsunnyh@gmail.com", "password": "p0lin528500@D", "user_bot_chatID": '1437550690', "account_name": "Vikas Calculus", "user_bot_token" : "8131045025:AAE9_BMb5i2pk479mubtilbSIUilPA25jWM"},
    {"username": "himanshubharwaj528500@gmail.com", "password": "p0lin528500@D", "user_bot_chatID": '1437550690', "account_name": "Ankit Calculus", "user_bot_token" : "8131045025:AAE9_BMb5i2pk479mubtilbSIUilPA25jWM"},
    {"username": "amitsaroaji990@gmail.com", "password": "p0lin528500@D", "user_bot_chatID": '1437550690', "account_name": "Amit advance", "user_bot_token" : "8131045025:AAE9_BMb5i2pk479mubtilbSIUilPA25jWM"},
    {"username": "kunduarshant06@gmail.com", "password": "p0lin528500@D", "user_bot_chatID": '1437550690', "account_name": "Nitin advance", "user_bot_token" : "8131045025:AAE9_BMb5i2pk479mubtilbSIUilPA25jWM"},
    {"username": "sunny90766@gmail.com", "password": "Sunny@19", "user_bot_chatID": '1437550690', "account_name": "Sunny Advance", "user_bot_token" : "8131045025:AAE9_BMb5i2pk479mubtilbSIUilPA25jWM"},
    {"username": "vinaykudu17@gmail.com", "password": "Vinayk@15", "user_bot_chatID": '5697608903', "account_name": "Vinay", "user_bot_token" : "8131045025:AAE9_BMb5i2pk479mubtilbSIUilPA25jWM"},
    {"username": "inncentvermagi@gmail.com", "password": "Chegg@123", "user_bot_chatID": '5697608903', "account_name": "Deepak", "user_bot_token" : "8131045025:AAE9_BMb5i2pk479mubtilbSIUilPA25jWM"},
    {"username": "shabagrohya@gmail.com", "password": "Chegg@123", "user_bot_chatID": '5697608903', "account_name": "Nitesh", "user_bot_token" : "8131045025:AAE9_BMb5i2pk479mubtilbSIUilPA25jWM"},
    {"username": "cheggexprt271@gmail.com", "password": "Chegg@123", "user_bot_chatID": '5697608903', "account_name": "Shekar", "user_bot_token" : "8131045025:AAE9_BMb5i2pk479mubtilbSIUilPA25jWM"},
    {"username": "devilagrohya@gmail.com", "password": "Chegg@123", "user_bot_chatID": '5697608903', "account_name": "Ajay", "user_bot_token" : "8131045025:AAE9_BMb5i2pk479mubtilbSIUilPA25jWM"},
    # Add more accounts if necessary
]


def refresh_account(account):
    username = account["Username"]
    password = account["Password"]
    user_both_chatID = str(account["user_both_chatID"])
    account_name = account["Account_name"]
    user_both_token = account["user_both_token"]  # Same token for all accounts
    start_time = account["start_time"]
    end_time = account["end_time"]
    accept_option = account["accept_option"]
    
    
    # Set up Chrome WebDriver for this account
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    # Each account gets its own Chrome instance
    driver = webdriver.Chrome(options=options)

    # Attempt to log in
    flag_login = True
    while flag_login:
        flag_login = login_to_chegg(username, password, driver)
    login_texts = f"both currently active on {account_name}"
    #telegram_both_sendtext(login_texts,user_both_token,user_both_chatID)
    telegram_both_sendtext(login_texts,login_admin_bohit_token,admin_chatID)


    # Start refreshing for the account
    refresh_chegg(driver, accept_option, start_time, end_time, user_both_token, user_both_chatID, account_name)
    #exit_texts = f"Loop exit on {account_name}"
    #telegram_both_sendtext(exit_texts,user_both_token,user_both_chatID)  
if __name__ == "__main__":
    # Create a process for each account
    processes = []
    for account in accounts:
        process = multiprocessing.Process(target=refresh_account, args=(account,))
        processes.append(process)
        process.start()

    # Optionally join the processes to ensure the script waits for all to finish
    for process in processes:
        process.join()
