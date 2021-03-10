# This is a program that will autofill the STEM attendance form every day
#Prerequisite's you must pip install: pyautogui, pillow, selenium, and pyscreenshot
# Also must download chromdriver online at http://chromedriver.chromium.org/downloads. Current build is on 89.0.4389.23 as of 3/10/21.
#Current Chrome version: Version 89.0.4389.82 (Official Build) (64-bit)
# Written by:
# Derrick Clarke
# Jakob Langtry

# Imports of select packages for proper execution
from email.message import EmailMessage
from datetime import datetime
import pyscreenshot
import pyautogui
import smtplib
import imghdr
import time
import sys


# Grabs current date and assigns the month, day and year to strings
current_time: datetime = datetime.now()
month: str = str(current_time.month)
day: str = str(current_time.day)
year: str = str(current_time.year)

# The code will pass to the end and exit if the current date we grabbed earlier is a Saturday or Sunday.
if current_time.weekday() == 5 or current_time.weekday() == 6:
    pass

# Else it will run the code below
else:
    # Imports the chrome webdriver and opens chrome
    from selenium import webdriver
    web = webdriver.Chrome()

    # Opens the attendance form URL
    web.get('[ATTENDANCE LINK')

    # This section is pretty self explanatory: it simply presses tab and enter given answers into the fields
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.typewrite(month)  # Types out the current month
    pyautogui.write('/')
    pyautogui.typewrite(day)  # Types out the current day
    pyautogui.write('/')
    pyautogui.typewrite(year)  # Types out the current year

    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.write('Clarke, Derrick')

    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('down')

    pyautogui.press('tab')
    pyautogui.press('tab')
    # If The weekday is MWF then it prints my MWF classes
    if current_time.weekday() == 0 or current_time.weekday() == 2 or current_time.weekday() == 4:
        pyautogui.write('CSCS, CSNT, CSNS')
    # If it is tuesday, it will list my tuesday classes
    elif current_time.weekday() == 1:
        pyautogui.write('CSNS')
    # If it is thursday, it will list my thursday classes
    else:
        pyautogui.write('CSCS')

    # Continuation of literal type commands
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.write('Unfortunately, I couldn\'t make the time')

    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.write('I did not')

    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.write('No help with anything thank you though')

    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.write('Yes')

    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.write('CSNS QUIZ, CSNT QUIZ')

    # Submits and exits chrome
    pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(1)
    im = pyscreenshot.grab()
    im.save('DerrickSubmit.png')
    pyautogui.hotkey('alt','f4')

    # Email to send from, password, and email to send to
    Sender_Email = "[SENDER EMAIL]"
    Password = ('[PASSWORD] ')
    Reciever_Email = "[RECIEVER EMAIL]"

    # Contents of email to be sent
    newMessage = EmailMessage()
    newMessage['Subject'] = "Morning, Sir!"
    newMessage['From'] = Sender_Email
    newMessage['To'] = Reciever_Email
    newMessage.set_content('I\'ve done your Attendance Form!\nHave a Great Day!\n\n -Jasper The Robot')

    # Picture file to be sent
    files = ['DerrickSubmit.png']

    # Reads file specified, decides the type, adds a name in a loop
    for file in files:
        with open(file, 'rb') as f:
            image_data = f.read()
            image_type = imghdr.what(f.name)
            image_name = f.name
        newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)

    # Uploads it to smtp, which is what actually sends the email.
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(Sender_Email, Password)
        smtp.send_message(newMessage)

# Exits
sys.exit()