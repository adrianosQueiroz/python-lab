def classificar_curva_abc(porcentagem_acumulada: float) -> str:
    """
    Classifica um item na curva ABC com base na sua representatividade acumulada.
    """
    if porcentagem_acumulada <= 80:
        return "A"
    elif porcentagem_acumulada <= 95:
        return "B"
    else:
        return "C"

# --- Bloco de teste interativo ---
if __name__ == "__main__":
    print("--- Sistema de Classificação ABC ---")
    
    produto = input("Digite o nome do produto/marca: ")
    ocupacao = input(f"Digite a ocupação acumulada de '{produto}' (em %): ")
    
    # Converte a entrada de texto para número decimal (float)
    try:
        valor_float = float(ocupacao.replace(',', '.')) # Aceita vírgula ou ponto
        categoria = classificar_curva_abc(valor_float)
        
        print(f"\nResultado:")
        print(f"O produto '{produto}' pertence à Categoria: {categoria}")
        
    except ValueError:
        print("Erro: Por favor, digite um número válido para a ocupação.")