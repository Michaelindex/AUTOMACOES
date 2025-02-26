# import csv

# csv_path = r"C:\Users\m.santos\OneDrive - Corporate\Área de Trabalho\oneitemimp_filtered.csv"

# with open(csv_path, mode='r', encoding='utf-8') as f:
#     reader = csv.reader(f)
#     header = next(reader)  # Ler a primeira linha (se for cabeçalho)
#     print("Cabeçalho (se existir):", header)
    
#     # Ler a segunda linha pra ver quantas colunas ela tem
#     second_line = next(reader)
#     print("Segunda linha tem", len(second_line), "colunas:", second_line)

# ACIMA SEM CÓD POR ;
#
# ABAIXO COM CÓD POR ,

import csv

csv_path = r"C:\Users\m.santos\OneDrive - Corporate\Área de Trabalho\oneitemimp_filtered.csv"

with open(csv_path, mode='r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=';')
    header = next(reader)
    print("Cabeçalho (se existir):", header)
    
    second_line = next(reader)
    print("Segunda linha tem", len(second_line), "colunas:", second_line)
