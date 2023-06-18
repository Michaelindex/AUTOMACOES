import time
from geopy.geocoders import Nominatim

# Função para obter a localização atual
def get_location():
    geolocator = Nominatim(user_agent='my_location')
    location = geolocator.geocode('NomeDaRua, Número, Cidade, Estado, País', timeout=5)
    return location

# Função principal que obtém e imprime a localização
def main():
    while True:
        try:
            location = get_location()
            if location:
                latitude = location.latitude
                longitude = location.longitude
                message = f'Localização atual: Latitude {latitude}, Longitude {longitude}'
                print(message)  # Exibe a mensagem no terminal
        except Exception as e:
            print(f'Erro: {str(e)}')

        time.sleep(30)

if __name__ == '__main__':
    main()
