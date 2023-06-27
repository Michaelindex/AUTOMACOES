from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

def obter_latitude_longitude_por_ip():
    geolocator = Nominatim(user_agent="my_app")  # Defina um nome de usuário para sua aplicação

    try:
        # Use o método geocode do geolocator com o parâmetro 'timeout' definido para 5 segundos
        localizacao = geolocator.geocode("45.174.238.1", timeout=5)
    except GeocoderTimedOut:
        return obter_latitude_longitude_por_ip()  # Em caso de timeout, tente novamente

    if localizacao:
        latitude = localizacao.latitude
        longitude = localizacao.longitude
        return latitude, longitude
    else:
        return None

# Chamada da função para obter a latitude e longitude com base no endereço IP
resultado = obter_latitude_longitude_por_ip()

if resultado:
    latitude, longitude = resultado
    print("Latitude:", latitude)
    print("Longitude:", longitude)
else:
    print("Não foi possível obter a latitude e longitude.")
