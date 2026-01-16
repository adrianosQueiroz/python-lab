# Crie uma função chamada verificar_ruptura(estoque_atual: int, estoque_minimo: int) -> bool.
# Se o estoque atual for menor que o mínimo, 
#a função deve retornar True (alerta de ruptura).
# Adicione uma Docstring explicando os parâmetros.

def verificar_ruptura(estoque_atual: int, estoque_minimo: int) -> bool:
    """
    Função para verificar se o estoque do produto está com rutpura ou não.
    """
    if estoque_atual < estoque_minimo:
        resultado: str
        resultado = "Alerta de Ruptura"
    else:
        resultado = "Estoque Ok"
    return resultado        


if __name__ == "__main__":
    atual = input("informe o estoque atual: ")
    minimo = input("Informe o estoque mínimo: ")
    retorno = verificar_ruptura(atual, minimo)
    print(retorno)
    
