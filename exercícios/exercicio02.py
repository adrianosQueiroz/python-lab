import pandas as pd

def analise_estoque_min (data:str, estoque_minimo: int = 950)-> pd.DataFrame:

    """
    Função para verificar se produtos listados estão com estoque mínimo. 
    """

    df = pd.read_csv(data)
    produtos_estoque_minimo = df[df['Estoque'] < estoque_minimo]
    return produtos_estoque_minimo

if __name__=="__main__":
    dados = input("Informe o path do arquivo: ").strip().replace('"','').replace("'",'')
    resultado = analise_estoque_min(dados)
    if not resultado.empty:
        print("\n--- Produtos com ruptura no estoque ---")    
        print(resultado)
    else:
        print("\nNenhum produto com ruptura")    

