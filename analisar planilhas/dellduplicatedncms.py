import pandas as pd

def remove_duplicatas_por_impostos():
    # Ajuste o caminho do CSV se necessário
    input_csv = r"C:\Users\m.santos\OneDrive - Corporate\Área de Trabalho\oneitemimp.csv"
    output_csv = r"C:\Users\m.santos\OneDrive - Corporate\Área de Trabalho\oneitemimp_filtered.csv"
    
    # Ler o CSV, assumindo delimitador ; e encoding UTF-8
    df = pd.read_csv(input_csv, sep=';', encoding='utf-8')
    
    # Converter DATA REGISTRO para datetime (ajuste o formato se necessário)
    df['DATA REGISTRO'] = pd.to_datetime(df['DATA REGISTRO'], format='%d/%m/%Y')
    
    # Ordenar pela data (do mais antigo ao mais recente)
    df.sort_values('DATA REGISTRO', inplace=True)
    
    # Remover duplicatas mantendo apenas o último registro de cada combinação
    # (NCM, %ICMS, % I.P.I., %PIS, % I.I)
    df.drop_duplicates(
        subset=['NCM', '% ICMS', '% I.P.I.', '% PIS', '% I.I'],
        keep='last',
        inplace=True
    )
    
    # Salvar o resultado em um novo CSV
    df.to_csv(output_csv, sep=';', encoding='utf-8', index=False)
    print(f"Arquivo '{output_csv}' gerado com sucesso!")

if __name__ == '__main__':
    remove_duplicatas_por_impostos()
