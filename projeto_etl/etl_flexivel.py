import pandas as pd
import json

# --- PARTE 1: EXTRAÇÃO (Leitura) ---
def extrair_dados_json(caminho_arquivo: str) -> pd.DataFrame:
    """Lê arquivos JSON e transforma em DataFrame."""
    with open(caminho_arquivo, 'r') as f:
        dados = json.load(f)
    return pd.DataFrame(dados)

# --- PARTE 2: TRANSFORMAÇÃO ---
def transformar_dados(df: pd.DataFrame) -> pd.DataFrame:
    """Aplica regras de negócio (limpeza, novos cálculos)."""
    # Padronizar
    df['Produto'] = df['Produto'].str.strip().str.title()
    return df

# --- PARTE 3: CARREGAMENTO (Saída) ---
def salvar_dados(df: pd.DataFrame, formato: str, nome_arquivo: str):
    """Decisão de saída baseada no parâmetro 'formato'."""
    if formato.lower() == 'csv':
        df.to_csv(f"{nome_arquivo}.csv", index=False)
        print(f"✅ Salvo com sucesso em CSV!")
    elif formato.lower() == 'parquet':
        df.to_parquet(f"{nome_arquivo}.parquet", index=False)
        print(f"✅ Salvo com sucesso em Parquet!")

# --- FLUXO PRINCIPAL (Onde a mágica acontece) ---
if __name__ == "__main__":
    # 1. Iniciar ETL e Leitura
    arquivo: str = input("Informe o path do arquivo: ").strip()
    df_inicial = extrair_dados_json(arquivo)
    
    # 2. Transformação
    df_final = transformar_dados(df_inicial)
    
    # 3. Decisão de Saída (Aqui você resolve o desafio da imagem!)
    formato_escolhido = input("Deseja salvar em CSV ou Parquet? ").strip()
    salvar_dados(df_final, formato_escolhido, "resultado_processado")