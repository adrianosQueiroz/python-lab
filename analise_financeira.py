def calcular_media_movel_simples(precos: list, janela: int) -> float:
    """
    Calcula a média móvel simples de uma lista de preços.
    
    Args:
        precos (list): Lista com os valores (ex: fechamentos de Bitcoin ou AZZA3).
        janela (int): Quantidade de períodos para a média (ex: 50 para SMA50).
        
    Returns:
        float: O valor da média móvel.
    """
    if len(precos) < janela:
        return 0.0
    
    ultimos_precos = precos[-janela:]
    media = sum(ultimos_precos) / janela
    return round(media, 2)

# Exemplo de teste
precos_btc = [42000, 43500, 44000, 41000, 45000]
print(f"Média Móvel: {calcular_media_movel_simples(precos_btc, 3)}")
