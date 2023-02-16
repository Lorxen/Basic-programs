# Program that sends an automated sms to a number on schedule

import requests
import schedule
import time

# Uses request library to send a message to a phone number
def send_message():

    resp = requests.post('https://textbelt.com/text', {
        'phone': 555555555,
        'message': 'Hey!!! Good morning buddy!!',
        'key': 'textbelt'
    })

    print(resp.json())

# Uses time and schedule libraries to schedule the sms
#schedule.every().day.at('08:00').do(send_message)
schedule.every(10).seconds.do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)