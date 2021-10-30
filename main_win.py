# Copyright (C) 2021, Kyungbae Min <kyungbae.min@stonybrook.edu>

from selenium import webdriver
from datetime import datetime, timedelta
import time
import os
import platform

"""CONFIGS"""

# Basic Info
email="kyungbae.min@stonybrook.edu"
name = "Kyungbae Min"
floor = "C17"
commitee = "Snapshot" # "IGC Committee", "Hangout", "Pop Up", "Re-Building"

# Duty Time & Date
duty_dates = {"Main Hall Rounding": "Thu", "Staying":"Tue", "Weekend":"Fri", "Holyday":"", "Adjustment Day":""}
mainhall_time = {"start_hour":"08", "start_meridiem":"PM", "end_hour":"00", "end_meridiem":"AM"}
staying_time = {"start_hour":"09", "start_meridiem": "PM", "end_hour": "11", "end_meridiem": "PM"}
weekend_time = {"start_hour": "00", "start_meridiem": "AM", "end_hour": "00", "end_meridiem": "AM"}
holyday_time = {"start_hour": "00", "start_meridiem": "AM", "end_hour": "00", "end_meridiem": "AM"}
adjustmentday_time = {"start_hour": "00", "start_meridiem": "AM", "end_hour": "00", "end_meridiem": "AM"}

# Delay
delay = 0.7


"""CONSTANT & VARIABLES"""

# Color Codes
DEFAULT= '\033[0m'
ERROR = '\033[31m'
BLUE = '\033[34m'
DIM = '\033[2;37m'

# Dictionaries
duty_time = {"Main Hall Rounding":mainhall_time, "Staying":staying_time, "Weekend":weekend_time, "Holyday":holyday_time, "Adjustment Day":adjustmentday_time}
duty_types = {"Main Hall Rounding":0, "Staying":1, "Weekend":2, "Holyday":3, "Adjustment Day":4}
dates = {"Mon":0, "Tue":1, "Wed":2, "Thu":3, "Fri":4, "Sat":5, "Sun":6}
commitees = {"Snapshot":0, "IGC Committee":1, "Hangout":2, "Pop Up":3, "Re-Building":4}
commitee_events = {"Snapshot":["Entertainment Recommendation", "Mental Health"], "IGC Committee":[], "Hangout":["Internship Panel", "Academic Success"], "Pop Up":["LOL/Battle Ground/OverWatch Tournament", "Thanksgiving"], "Re-Building":["Freshman Welcoming", "Check-In"]}
dorm_id = {"A5":3, "A6":4, "A7":5, "A11":6, "B6":7, "B9":8, "B11":9, "B15":10, "B19":11, "B20":12, "C8":13, "C9":14, "C10":15, "C14":16, "C16":17, "C17":18}
feelings = {"Happy":0, "Excited":1, "Hopeful":2, "Confident":3, "Bored":4, "Exhausted":5, "Upset":6, "Fightened":7, "Disgusted":8, "Enraged":9, "Stressed":10}

# Functions
def print_result(category, value):
    return print(DEFAULT + category+ ":" + BLUE, value)

def freetext(question):
    result = input(question)
    while len(result) == 0:
        result = input(question)
    return result

def choose_one(question, lst):
    dic={}
    for i in range(1, len(lst)+1):
        dic.setdefault(str(i), list(lst)[i-1])
    print(question)
    for k, v in dic.items():
        print(" "+ k + '. ' + v)
    result = input("Enter the number: ")
    while result not in dic.keys():
        result = input("Enter the number(again): ")
    return dic[result]

def confirm(question, default=False):
    print(question, end='')
    result = default
    if default:
        ans = input('[Y/n]')
        if ans.lower() == 'n':
            result=False
    else:
        ans = input('[y/N]')
        if ans.lower() == 'y':
            result=True
    print(result)
    return result

def clear():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')
    print(DIM+"Copyright (C) 2021, Kyungbae Min <kyungbae.min@stonybrook.edu>"+DEFAULT)
    

"""MAIN LOOP"""

while True:
    # Clear prompt
    clear()

    # Duty type
    duty_type = choose_one('Choose duty-type: ', duty_types.keys())

    # Duty date
    if duty_dates[duty_type] == "":
        duty_date = choose_one('Choose duty-date: ', dates.keys())
    else:
        duty_date = duty_dates[duty_type]
    report_date = datetime.today() - timedelta(days=(datetime.today().weekday()-dates[duty_date]))

    year = str(report_date.year) 
    month = '{0:02d}'.format(report_date.month)
    day = '{0:02d}'.format(report_date.day)

    # Phone duty
    clear()
    phone_duty = confirm("Phone duty?")

    # Community Building
    clear()
    resident_issue = freetext('Info about residents: ')

    # Committee event
    clear()
    if len(commitee_events[commitee]) > 0:
        commitee_event = choose_one('Choose upcoming committee event('+commitee+'): ', commitee_events[commitee])
    else:
        commitee_event = freetext('Provide upcoming committee event('+commitee+'): ')

    # Committee event progress
    event_progress = freetext("Current progress of preparation for the event: ")

    # Committee event issue
    clear()
    if confirm("Any issues on event preparation process?"):
        event_issue = freetext("Details(event preparation issues): ")
    else:
        event_issue = "Everything is okay:)"

    # Maintenance issue
    clear()
    maintenance_issue = confirm("Any maintenance issues?")

    # Maintenance detail
    if maintenance_issue:
        maintenance_detail = freetext("Details(maintenance issues): ")
    else:
        maintenance_detail = "N/A"
    
    # Feeling
    clear()
    feeling = [choose_one('Your feeling on duty day: ', feelings.keys())]
    while len(feeling) == 0:
        feeling = [choose_one('Your feeling on duty day: ', feelings.keys())]
 
    # Result print
    clear()
    print(DEFAULT + "=============== Your Responses ===============")
    print_result("E-mail", email)
    print_result("Name", name)
    print_result("Floor", floor)
    print_result("Duty type",duty_type)
    print_result("Date", year + "/" + month + "/" + day + "(" + duty_date + ")")
    print_result("Time", duty_time[duty_type]["start_hour"] + ":00 "+duty_time[duty_type]["start_meridiem"]+" ~ " + duty_time[duty_type]["end_hour"] + ":00 "+duty_time[duty_type]["end_meridiem"])
    print()
    print_result("Issue about residents", resident_issue)
    print()
    print_result("Committee", commitee)
    print_result("Upcoming event", commitee_event)
    print_result("Event preparation", event_progress)
    print_result("Issues on event preparation", event_issue)
    print()
    print_result("Maintenance issue", maintenance_detail)
    print_result("Feelings", feeling)
    print(DEFAULT+"==============================================")
    
    if confirm("Continue?", default = True):
        break


"""BROWSER AUTOMATION"""

print(DEFAULT+"Opening the browser...")
driver = webdriver.Chrome("./chromedriver")
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfNkJ-7hAAs9hug1T1v-OyIw1ioC-of0V1PpEs6xE9GWL_O8A/viewform")
time.sleep(1)
start = time.time()
# E-mail
driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div[1]/input').send_keys(email)

# Name
driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(name)

# Floor
driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]').click()
time.sleep(delay)
driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[2]/div['+str(dorm_id[floor])+']').click()
time.sleep(delay)

# Date
driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input').send_keys(year+month+day)

# Start time
driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/input').send_keys(duty_time[duty_type]["start_hour"])
driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[3]/div/div[1]/div/div[1]/input').send_keys('00')
if duty_time[duty_type]["start_meridiem"]=='PM':
    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[4]/div[1]/div[1]/div[1]').click()
    time.sleep(delay)
    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[4]/div[2]/div[2]').click()
    time.sleep(delay)

#End time
driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/input').send_keys(duty_time[duty_type]["end_hour"])
driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[3]/div/div[1]/div/div[1]/input').send_keys('00')
if duty_time[duty_type]["end_meridiem"]=='PM':
    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[4]/div[1]/div[1]/div[1]').click()
    time.sleep(delay)
    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[4]/div[2]/div[2]').click()
    time.sleep(delay)

# Phone duty check
if phone_duty:
    button = driver.find_element_by_xpath('//*[@id="i30"]/div[3]')
    driver.execute_script("arguments[0].click();", button)
else:
    button = driver.find_element_by_xpath('//*[@id="i33"]/div[3]')
    driver.execute_script("arguments[0].click();", button)

# Duty type check
driver.find_element_by_xpath('//*[@id="i{0}"]/div[2]'.format(41+3*duty_types[duty_type])).click()

# Next
button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/div[2]')
driver.execute_script("arguments[0].click();", button)
time.sleep(delay)

# Community Building
driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/textarea').send_keys(resident_issue)

# Next
button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span')
driver.execute_script("arguments[0].click();", button)
time.sleep(delay)

# Committee
button = driver.find_element_by_xpath('//*[@id="i{0}"]/div[3]'.format(9+3*commitees[commitee]))
driver.execute_script("arguments[0].click();", button)

# Upcoming committee event
driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(commitee_event)

driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div[2]/textarea').send_keys(event_progress)

driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div[2]/textarea').send_keys(event_issue)

# Next
button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div[2]/span')
driver.execute_script("arguments[0].click();", button)
time.sleep(delay)

# Maintenance issue
if maintenance_issue:
    button = driver.find_element_by_xpath('//*[@id="i12"]/div[3]')
    driver.execute_script("arguments[0].click();", button)
else:
    button = driver.find_element_by_xpath('//*[@id="i9"]/div[3]')
    driver.execute_script("arguments[0].click();", button)

driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea').send_keys(maintenance_detail)

# Next
button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div[2]/span')
driver.execute_script("arguments[0].click();", button)
time.sleep(delay)

# Feelings
for item in feeling:
    driver.find_element_by_xpath('//*[@id="i{}"]/div[2]'.format(10+3*feelings[item])).click()

print("DONE... %.2fs" % (time.time()-start))