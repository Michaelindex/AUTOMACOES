import csv
from openpyxl import load_workbook

csv_path = r"C:\Users\m.santos\OneDrive - Corporate\Área de Trabalho\oneitemimp_filtered.csv"
xlsx_path = r"C:\Users\m.santos\OneDrive - Corporate\Área de Trabalho\template.xlsx"

wb = load_workbook(xlsx_path)
ws = wb.active  # ou wb["NomeDaAba"] se quiser uma aba específica

with open(csv_path, mode='r', newline='', encoding='utf-8') as f:
    # Note o delimiter=';' aqui
    reader = csv.reader(f, delimiter=';')
    
    # Ler a primeira linha (cabeçalho) e descartar
    next(reader)
    
    # Vamos começar a escrever na linha 3 da planilha final
    row_in_template = 3
    
    for row in reader:
        # Agora cada "row" deve ter colunas separadas corretamente
        # Verifique se há colunas suficientes antes de acessar índices altos:
        if len(row) < 36:
            # Se alguma linha tiver menos colunas, você pode decidir
            # pular a linha ou tratar de outra forma
            continue
        
        # Exemplo de preenchimento (ajuste se os índices forem diferentes):
        # CSV col J (índice 9) => planilha final col B
        ws.cell(row=row_in_template, column=2).value = row[9]
        
        # CSV col P (índice 15) => planilha final col G
        ws.cell(row=row_in_template, column=7).value = row[15]
        
        # CSV col AJ (índice 35) => planilha final col I
        ws.cell(row=row_in_template, column=9).value = row[35]
        
        # CSV col AA (índice 26) => planilha final col Q
        ws.cell(row=row_in_template, column=17).value = row[26]
        
        # CSV col AD (índice 29) => planilha final col X
        ws.cell(row=row_in_template, column=24).value = row[29]
        
        # CSV col AF (índice 31) => planilha final col AE
        ws.cell(row=row_in_template, column=31).value = row[31]
        
        # CSV col Y (índice 24) => planilha final col AS
        ws.cell(row=row_in_template, column=45).value = row[24]
        
        row_in_template += 1

wb.save(xlsx_path)
