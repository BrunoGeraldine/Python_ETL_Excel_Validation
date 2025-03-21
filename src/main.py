#import pandas as pd
#
#from ydata_profiling import ProfileReport
#
#df = pd.read_csv('../data-base/data.csv')
#profile = ProfileReport(df, title='Profiling Report')
#profile.to_file('../output.html')

import pandas as pd

# Lendo o arquivo CSV
df = pd.read_csv('../data-base/data_2025.csv')

# Dicionário de mapeamento das colunas (português -> inglês)
column_mapping = {
    'Organizador': 'Organizer',
    'Ano_Mes': 'Year_Month',
    'Dia_da_Semana': 'Day_of_Week',
    'Tipo_Dia': 'Day_Type',
    'Objetivo': 'Goal',
    'Date': 'Date',  # mantém igual pois já está em inglês
    'AdSet_name': 'AdSet_name',  # mantém igual pois já está em inglês
    'Amount_spent': 'Amount_spent',  # mantém igual pois já está em inglês
    'Link_clicks': 'Link_clicks',  # mantém igual pois já está em inglês
    'Impressions': 'Impressions',  # mantém igual pois já está em inglês
    'Conversions': 'Conversions',  # mantém igual pois já está em inglês
    'Tipo_de_Anúncio': 'Ad_Type',
    'Fase': 'Phase'
}

# Renomeando as colunas
df = df.rename(columns=column_mapping)

# Salvando o arquivo com as novas colunas
# Versão 1: Salvando com o mesmo nome mas com sufixo _en
df.to_csv('../data-base/data_2025_en.csv', index=False)