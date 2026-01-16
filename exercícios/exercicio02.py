import pandas as pd

def analise_estoque_min (data:str)-> pd.DataFrame:
    
    estoque_minimo = 950
    df = pd.read_csv(data)
    produtos_estoque_minimo = df[df['Estoque'] < estoque_minimo]
    return produtos_estoque_minimo

if __name__=="__main__":
    dados = input("Informe o path do arquivo: ")
    resultado = analise_estoque_min(dados)
    print(resultado)

