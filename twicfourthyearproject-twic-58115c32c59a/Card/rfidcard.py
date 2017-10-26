import serial
import requests
import json
serial = serial.Serial("/dev/ttyUSB0", baudrate=9600)

card1 = '18004865AB9E'
card2 = '19007E5E4970'



'''
Data is read from the card as individual symbols/variables
'''
firebase_url = 'https://twic-polymer.firebaseio.com/'

def post_to_db(card_id):
    data={'id':card_id, 'number of times tapped': 0}
    sent = json.dumps(data)
    result = requests.post(firebase_url+'/cards.json', sent)
    print 'Success!' + str(result.status_code) + ',' + result.text


def check_card(code):
    if code.find(card1) > 0:
        print('victory')
    else:
        print('failure')

def read_card():
    code = ''
    while True:
            data = serial.read()
            if data == '\r':
                    print(code)
                    print(type(code))
                    check_card(code)
                    post_to_db(code)
                    code = ''
            else:
                    code = code + data
read_card()
