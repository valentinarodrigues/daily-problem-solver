import requests
from datetime import datetime, timedelta


# Return current date in dd-mm-YYYY format
def get_todays_date():
	current_time = datetime.now()+ timedelta(days=1) 
	return current_time.strftime('%d-%m-%Y')

def send_message(message, priority=0):
	print('message')
	
_message('Error occured in script:'+str(e))

import json
r = requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode=400053&date='+get_todays_date())

resp = r.json()
# print(resp['sessions'])
for session in resp['sessions']:
    if((session['name'] == 'Lokhandwala Aditi Puri Trust' or session['name'] == 'Indian Oil Nagar' or session['name'] == 'BANANA LEAF DISPENSARY')
    and session['fee_type'] == 'Free' and session['available_capacity_dose1']>0):
        print('boooook')
        r = requests.post('', data=json.dumps({'text': f'Slot Available {session["name"]} {session["available_capacity_dose1"]} https://selfregistration.cowin.gov.in'}))        
# /usr/local/bin/python3 vaccine.py

# */5 * * * * /usr/local/bin/python3 /Users/Projects/Valentina/daily-problem-solver/vaccine.py