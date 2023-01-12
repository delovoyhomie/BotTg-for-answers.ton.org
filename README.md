# BotTg-for-answers.ton.org

## ✍️ What you need to get started
Install [Python](https://www.python.org/) if you haven't yet.

Also you need these Python libraries:
 - flask
 - requests

You can install them with one command in the terminal.
```bash
pip install flask requests
```
## 🚀 Let's get started!

First we initialize the libraries
```bash
from flask import Flask, request
import requests
import json
```

Set the bot token in the telegram
```bash
token = 'YOUR-TOKEN'
```

The app works with a webhooks. 
* Receives information 
* Processes it
* Sends it to Telegram

Therefore, with the flask we create a server
```bash
app = Flask(__name__)
```

Then we set the handle, where we get a webhook in the form of a json object
```bash
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
        arr = ['-800000000'] # array of IDs of all groups
        for i in range(n):
            requests.get('https://api.telegram.org/bot{}/sendMessage'.format(token), params=dict(
                chat_id = arr[i],
                text = '🔔 ' + link1 + '\n' + '*from *' + '*' + user + '*' + '\n\n' + body  + '\n\n' + '🔗 ' + link2,
                parse_mode= 'markdown'
            )) 
        return 'GOOD!'
    else:
        return 'BAD!'
```

Next, we get the components we need from the json file and use requests to send a message to the chats.

## 📨Setting up mailing lists

```bash
n = 1 # number of groups
arr = ['-800000000'] # array of IDs of all groups
```
You enter the group IDs into the array and the variable n indicates the number of the first groups in the array that will be involved in the mailing list

## ⚙️Configuring a webhooks 

When you start the project, you will see a private (localhost) and public ip. You need to choose public (second).

![image](/img/ip.png)

1) Copy the ip and go to https://answers.ton.org/admin to set the webhook. Example: http://127.0.0.1:5000/webhook

2) Also you have to select the event trigger `question.create`.

## 🚀 Start the server and that's it

```bash
app.run(host='0.0.0.0', port=5000)
```
