import time
import requests
from geopy.geocoders import Nominatim

# Função para obter a localização atual
def get_location():
    geolocator = Nominatim(user_agent='my_location')
    location = geolocator.geocode('NomeDaRua, Número, Cidade, Estado, País')
    return location

# Função para enviar mensagem para o bot do Telegram
def send_message(chat_id, text):
    bot_token = 'SEU_TOKEN_DO_BOT'
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
                print(message)  # Exibe a mensagem no terminal
                send_message(chat_id, message)
        except Exception as e:
            print(f'Erro: {str(e)}')

        time.sleep(10)

if __name__ == '__main__':
    main()
