import time
import requests
from geopy.geocoders import Nominatim
from urllib.error import URLError

# Função para obter a localização atual
def get_location():
    geolocator = Nominatim(user_agent='my_location')
    location = geolocator.geocode('NomeDaRua, Número, Cidade, Estado, País', timeout=5)
    return location

# Função para enviar mensagem para o bot do Telegram
def send_message(chat_id, text):
    bot_token = ''
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
                chat_id = ''  # Substitua pelo ID do chat do Telegram
                message = f'Localização atual: Latitude {latitude}, Longitude {longitude}'
                print(message)  # Exibe a mensagem no terminal
                send_message(chat_id, message)
        except URLError as e:
            print(f'Erro de conexão: {str(e)}')
        except Exception as e:
            print(f'Erro: {str(e)}')

        time.sleep(30)

if __name__ == '__main__':
    main()
