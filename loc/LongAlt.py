import time
import requests
from geopy.geocoders import Nominatim

# Função para obter a localização atual
def get_location():
    geolocator = Nominatim(user_agent='my_location')
    location = geolocator.geocode('')
    return location

# Função para enviar mensagem para o bot do Telegram
def send_message(chat_id, text):
    bot_token = '6258166876:AAHFOyYvt0zKgyLQSBYQ54bhYbpnq_79NlQ'
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': text
    }
    response = requests.post(url, json=payload)
    return response.json()

# Função principal que executa o script
def main():
    while True:
        try:
            location = get_location()
            if location:
                latitude = location.latitude
                longitude = location.longitude
                chat_id = '5212651576'  # Substitua pelo ID do chat do Telegram
                message = f'Localização atual: Latitude {latitude}, Longitude {longitude}'
                send_message(chat_id, message)
        except Exception as e:
            print(f'Erro: {str(e)}')

        time.sleep(225)

if __name__ == '__main__':
    main()
