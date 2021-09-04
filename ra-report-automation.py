from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from datetime import datetime, timedelta
import time
import enquiries
import os
import platform

# OPTIONS
name = "Kyungbae Min"

floor = "C17"

mainhall_time = {"start_hour":"08", "start_meridiem":"PM", "end_hour":"00", "end_meridiem":"AM"}
staying_time = {"start_hour":"09", "start_meridiem": "PM", "end_hour": "11", "end_meridiem": "PM"}
weekend_time = {"start_hour": "00", "start_meridiem": "AM", "end_hour": "00", "end_meridiem": "AM"}
holyday_time = {"start_hour": "00", "start_meridiem": "AM", "end_hour": "00", "end_meridiem": "AM"}

duty_dates = {"Main Hall Rounding": "Thu", "Staying":"Tue", "Weekend":"Fri", "Holyday":""}

delay = 0.7

# Color codes
DEFAULT= '\033[0m'
ERROR = '\033[31m'
BLUE = '\033[34m'

duty_time = {"Main Hall Rounding":mainhall_time, "Staying":staying_time, "Weekend":weekend_time, "Holyday":holyday_time}

duty_types = {"Main Hall Rounding":1, "Staying":2, "Weekend":3, "Holyday":4}

dates = {"Mon":0, "Tue":1, "Wed":2, "Thu":3, "Fri":4, "Sat":5, "Sun":6}

code2date = {0:"Mon", 1:"Tue", 2:"Wed", 3:"Thu", 4:"Fri", 5:"Sat", 6:"Sun"}

dorm_id = {"A5":3, "A6":4, "A7":5, "A11":6, "B6":7, "B9":8, "B11":9, "B15":10, "B19":11, "B20":12, "C8":13, "C9":14, "C10":15, "C14":16, "C16":17, "C17":18}

while True:
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

    duty_type = enquiries.choose('Choose duty-type: ', duty_types.keys())

    resident1_info = duty_type
    resident2_info = duty_type
    resident_issue = 'N/A'
    duty_date = duty_dates[duty_type]
    
    # incidentReport = False
    # facilityIssue = "None"
    # facilityIssue_sol = ""

    if duty_date == "":
        duty_date = enquiries.choose('Choose duty-date: ', dates.keys())
    report_date = datetime.today() - timedelta(days=(datetime.today().weekday()-dates[duty_dates[duty_type]]))

    year = str(report_date.year) 
    month = '{0:02d}'.format(report_date.month)
    day = '{0:02d}'.format(report_date.day)

    # duty = ""
    phone_duty = enquiries.confirm("Phone duty?")

    if duty_type == "Staying":
        resident1_info = enquiries.freetext('Resident #1: ')
        resident2_info = enquiries.freetext('Resident #2: ')
    
    if enquiries.confirm("Issue about residents?"):
        resident_issue = enquiries.freetext('Details about issue: ')
 

    # if input("Incident report?(y/n): ").lower() == "y":
    #     incidentReport = True
    # if input("Facility issues?(y/n): ").lower() == "y":
    #     facilityIssue = input("Provide any details: ")
    #     facilityIssue_sol = input("Your solution: ")
    # commentsRHD = input("Comments to RHDs?: ")
    # if commentsRHD == "":
    #     commentsRHD = "None"

    #
    # duty_time[duty_types[duty_num]].start_hour
    # duty_time[duty_types[duty_num]].start_meridiem
    # duty_time[duty_types[duty_num]].end_hour
    # duty_time[duty_types[duty_num]].end_meridiem

    result = DEFAULT + "============== Your Responses ==============\n"+ DEFAULT + "Name: " + BLUE + name + '\n' + DEFAULT + "Floor: " + BLUE + floor + '\n' + DEFAULT+"Report type: " + BLUE +  duty_type + '\n' + DEFAULT + "Date: " + BLUE + year + "/" + month + "/" + day + "(" + duty_date + ")" + '\n' + DEFAULT + "Time: " + BLUE + duty_time[duty_type]["start_hour"] + ":00 "+duty_time[duty_type]["start_meridiem"]+" ~ " + duty_time[duty_type]["end_hour"] + ":00 "+duty_time[duty_type]["end_meridiem"] + '\n' +DEFAULT+"Resident #1: " + BLUE + resident1_info+ '\n' +DEFAULT+"Resident #2: " + BLUE + resident2_info+ '\n' +DEFAULT+"Issue about residents: " + BLUE + resident_issue+ '\n' +DEFAULT+"============================================"
    print(result)
    # def YoN(response):
    #     if response:
    #         return BLUE+"Yes"
    #     return error_+"No"

    # print(default_+"Phone duty?: " + YoN(phoneDuty))
    # print(default_+"Incident report: " + YoN(incidentReport))
    # if facilityIssue == "None":
    #     print(default_+"Facility issues: " + error_+"None")
    # else:
    #     print(default_+"Facility issues: " + BLUE + facilityIssue)
    #     print(default_+"Your solution: " + BLUE + facilityIssue_sol)
    # if commentsRHD == "None":
    #     print(default_+"Comments to RHD: " + error_ + commentsRHD)
    # else:
    #     print(default_+"Comments to RHD: " + BLUE + commentsRHD)

   
    if enquiries.confirm("Continue?", default = True):
        break
        

print(DEFAULT+"Opening the browser...")
driver = webdriver.Chrome("./chromedriver")
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfNkJ-7hAAs9hug1T1v-OyIw1ioC-of0V1PpEs6xE9GWL_O8A/viewform")
time.sleep(1)

# Name
driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(name)

# Floor
driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div[1]').click()
time.sleep(delay)
driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div['+str(dorm_id[floor])+']').click()
time.sleep(delay)

# Date
driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input').send_keys(year+month+day)

# Start time
driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/input').send_keys(duty_time[duty_type]["start_hour"])
driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[3]/div/div[1]/div/div[1]/input').send_keys('00')
if duty_time[duty_type]["start_meridiem"]=='PM':
    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[4]/div[1]/div[1]/div[1]').click()
    time.sleep(delay)
    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[4]/div[2]/div[2]').click()
    time.sleep(delay)

#End time
driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/input').send_keys(duty_time[duty_type]["end_hour"])
driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[3]/div/div[1]/div/div[1]/input').send_keys('00')
if duty_time[duty_type]["end_meridiem"]=='PM':
    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[4]/div[1]/div[1]/div[1]').click()
    time.sleep(delay)
    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[4]/div[2]/div[2]').click()
    time.sleep(delay)


# Phone duty check
if phone_duty:
    button = driver.find_element_by_xpath('//*[@id="i26"]/div[3]')
    driver.execute_script("arguments[0].click();", button)
else:
    button = driver.find_element_by_xpath('//*[@id="i29"]/div[3]')
    driver.execute_script("arguments[0].click();", button)

# Duty type check
driver.find_element_by_xpath('//*[@id="i{0}"]/div[2]'.format(34+3*duty_types[duty_type])).click()

# Next
button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/div[2]')
driver.execute_script("arguments[0].click();", button)
time.sleep(delay)

# Community Building
driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/textarea').send_keys(resident1_info)
driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/textarea').send_keys(resident2_info)
driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea').send_keys(resident_issue)

# Next
button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div[2]/span')
driver.execute_script("arguments[0].click();", button)
time.sleep(delay)


# Date
# driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input").send_keys(date)

# Time
# driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/input").send_keys(DutyHour_start)
# driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[3]/div/div[1]/div/div[1]/input").send_keys("00")
# if DutyHour_start != "00":
#     driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[4]/div[1]/div[2]").click()
#     time.sleep(0.3)
#     driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[4]/div[2]/div[2]").click()
#     time.sleep(0.3)
# driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/input").send_keys(DutyHour_end)
# driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[3]/div/div[1]/div/div[1]/input").send_keys("00")
# if DutyHour_end != "00":
#     driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[4]/div[1]/div[2]").click()
#     time.sleep(0.3)
#     driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[4]/div[2]/div[2]").click()
#     time.sleep(0.3)

# Incident report
# if incidentReport:
#     driver.find_element_by_xpath("//*[@id='i56']/div[3]/div").click()
# else:
#     driver.find_element_by_xpath("//*[@id='i59']/div[3]/div").click()

# Facility issues
# driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div[1]/div[2]/textarea").send_keys(facilityIssue)
# driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div[1]/div[2]/textarea").send_keys(facilityIssue_sol)

# Duty
# driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[11]/div/div/div[2]/div/div[1]/div[2]/textarea").send_keys(duty)

# To RHD
# driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[12]/div/div/div[2]/div/div[1]/div[2]/textarea").send_keys(commentsRHD)