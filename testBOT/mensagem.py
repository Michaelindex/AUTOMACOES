import requests

def send_message(chat_id, text):
    bot_token = ''
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': text
    }
    response = requests.post(url, json=payload)
    return response.json()

def main():
    chat_id = ''  # Substitua pelo ID do chat do Telegram
    message = 'Olá, eu sou um exemplo de mensagem enviada por um bot do Telegram!'
    response = send_message(chat_id, message)
    if response['ok']:
        print('Mensagem enviada com sucesso!')
    else:
        print('Falha ao enviar a mensagem.')

if __name__ == '__main__':
    main()