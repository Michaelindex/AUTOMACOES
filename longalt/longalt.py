from geopy.geocoders import Nominatim

geolacalizador = Nominatim(user_agent="teste-palancacode")
lugar_input = input("Digite o nome do lugar: ")
lacalizacao = geolacalizador.geocode(lugar_input)
print(lacalizacao)