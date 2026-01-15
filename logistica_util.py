from datetime import datetime

def calcular_lead_time(data_expedicao: str, data_entrega: str) -> int:
    """
    Calcula o lead time em dias entre a expedição e a entrega.
    As datas devem estar no formato 'AAAA-MM-DD'.
    
    Args:
        data_expedição (str): Data em que o pedido foi expedido.
        data_entrega (str): Data em que o pedido foi entregue.
        
    Returns:
        int: Quantidade de dias que o pedido levou para ser entregue.
    """
    formato = "%Y-%m-%d"
    
    try:
        inicio = datetime.strptime(data_expedicao, formato)
        fim = datetime.strptime(data_entrega, formato)
        
        # Calcula a diferença e retorna apenas os dias
        diferenca = fim - inicio
        return abs(diferenca.days)
    
    except ValueError:
        print("Erro: Use o formato de data AAAA-MM-DD")
        return 0

# Teste da função
print(f"Lead Time: {calcular_lead_time('2026-01-01', '2026-01-05')} dias")