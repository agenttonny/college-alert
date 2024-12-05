import requests

def send_message(chat_id):
    bot_token = ''
    chat_id = ''
    message = 'Hello, this is a message from my bot!'
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': message
    }
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print(f"Failed to send message. Error: {response.status_code}")

def get_updates():
    bot_token = '7831706178:AAExsJpMIbhQz5RYGeA6H5VvRDqn62AMoDI'
    chat_id = 'YOUR_CHAT_ID'
    url = f'https://api.telegram.org/bot{bot_token}/getUpdates'
    response = requests.get(url)
    updates = response.json()
    if updates["result"]:
        return updates["result"]
    return []


def get_chat_ids(chat_list):
    users = []
    for chat in chat_list:
        chatId = chat.get('message').get('from').get('id')
        full_name = chat['message']['from']['first_name'] + ' ' + chat['message']['from']['last_name']
        users.append({'chat_id': chatId, 'full_name': full_name})

    unique_users = {user['chat_id']: user for user in users}
    
    unique_users_list = list(unique_users.values())
    print(unique_users_list)
    # return unique_users_list

get_chat_ids(get_updates())