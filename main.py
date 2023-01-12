from flask import Flask, request
import requests
import json

token = 'YOUR-TOKEN'

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        a = request.json
        body = a["items"][0]["body"] 
        title = a["items"][0]["title"] 
        tags = a["items"][0]["tags"][0] 
        id = a["items"][0]["id"] 
        name = a["items"][0]["name"] 
        user = a["items"][0]["author"]["name"] 
        url = 'https://answers.ton.org/question/' + a["items"][0]["id"] + '/' 

        link1 = '[' + name + '](' + url + ')'
        link2 = '[Answer on TON Overflow](' + url + ')'
        
        n = 1 # number of groups
        arr = ['-000000000'] # array of IDs of all groups 
        for i in range(n):
            requests.get('https://api.telegram.org/bot{}/sendMessage'.format(token), params=dict(
                chat_id = arr[i],
                text = '🔔 ' + link1 + '\n' + '*from *' + '*' + user + '*' + '\n\n' + body  + '\n\n' + '🔗 ' + link2,
                parse_mode= 'markdown'
            )) 
        return 'GOOD!'
    else:
        return 'BAD!'

app.run(host='0.0.0.0', port=5000) # port can be changed
