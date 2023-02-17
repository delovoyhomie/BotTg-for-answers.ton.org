from flask import Flask, request
import requests
import json

token = 'YOUR-TOKEN'

app = Flask(name)

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
        

        flag = True
        body_count = body.count('*')
        if body_count % 2 != 0:
            body_count -= 1

        for i in range(body_count):
            if flag:
                body = body.replace('*', '_', 1)
                flag = False
            else:
                body = body.replace('*', '_', 1)
                flag = True
        print(body)

        flag = True
        body_count = body.count('')
        if body_count % 2 != 0:
            body_count -= 1

        for i in range(body_count):
            if flag:
                body = body.replace('', '*', 1)
                flag = False
            else:
                body = body.replace('**', '*', 1)
                flag = True
        print(body)

        flag = True
        body_count = body.count('')
        if body_count % 2 != 0:
            body_count -= 1

        for i in range(body_count):
            if flag:
                body = body.replace('', '*', 1)
                flag = False
            else:
                body = body.replace('__', '*', 1)
                flag = True
        print(body)

        n = 2 # number of groups
        # first - test; second - ton dev chat
        arr = ['-1001884593590', '-1001516541544'] # array of IDs of all groups 
        for chat_id in arr:
            response = requests.get('https://api.telegram.org/bot{}/sendMessage'.format(token), params=dict(
                chat_id = chat_id,
                text = link1 + '\n' + '*from *' + '*' + user + '*' + '\n\n' + body  + '\n\n' + '🔗 ' + link2,
                parse_mode= 'markdown'
            )) 
            print(response.text)
        return 'GOOD!'
    else:
        return 'BAD!'

app.run(host='0.0.0.0', port=5000) # port can be changed
