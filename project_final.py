def check_ice(ice):
    return ice.upper() == "SIM"

def check_delivery(order):
    return order.upper() == "DELIVERY"

def check_local(order):
    return order.upper() == "LOCAL"

def prepare_juice():
    print("Os sucos são servidos em copos de plástico.")
    flavor = input("Qual sabor ? Uva ou Laranja ? ")
    print(f"Sabor do suco {flavor}.")
    ice = input("Cliente quer gelo ? Digite sim ou não: ")
    if check_ice(ice):
       print("Colocar 12 pedras de gelo.")
    else:
       print("Não colocar gelo.")
    size = input("Qual tamanho do suco ? 300ml ou 500ml ? Digite apenas o número: ")
    print(f"Tamanho do copo de {size}ml.")
    order = input("Qual tipo do pedido ? Digite delivery ou local: ")
    if check_delivery(order):
       print("Cliente recebe uma tampa sem furo para o canudo.")
    if check_local(order):
       print("Cliente recebe uma tampa com furo para o canudo.")
    question = input("Deseja realizar um novo pedido ? Digite sim ou não: ").upper()
    if question == "SIM":
       prepare_drink()
    else:
       print("Finalizando ABS - Sistema automatizado de bebidas do McDonald's.")

def prepare_soda():
    print("Os refrigerantes são servidos em copos de papel.")
    flavor = input("Qual sabor ? Coca ou Guaraná ? ")
    print(f"Sabor do refrigerante {flavor}.")
    ice = input("Cliente quer gelo ? Digite sim ou não: ")
    if check_ice(ice):
       print("Colocar 6 pedras de gelo.")
    else: 
       print("Não colocar gelo.")
    size = input("Qual tamanho do refrigerante ? 300ml, 500ml ou 700ml ? Digite apenas o número: ")
    print(f"Tamanho do copo de {size}ml.")
    order = input("Qual tipo do pedido ? Digite delivery ou local: ")
    if check_delivery(order):
       print("Cliente recebe uma tampa com furo para o canudo.")
    if check_local(order):
       print("Cliente recebe uma tampa com furo para o canudo.")
    question = input("Deseja realizar um novo pedido ? Digite sim ou nao: ").upper()
    if question ==  "SIM":
       prepare_drink()
    else:
       print("Finalizando ABS - Sistema automatizado de bebidas do McDonald's")
    
def prepare_drink():
    print("Bem vindo ao BNS - Sistema automatizado de bebidas do McDonald's.")
    choice = input("Digite qual tipo de bebida ? Refrigerante ou Suco ? ").upper()
    match choice:
        case "SUCO":
            prepare_juice()

        case "REFRIGERANTE":       
            prepare_soda()

        case _:
            print("Opção incorreta. Retornando ao menu principal.")   
            prepare_drink()
                        
prepare_drink()
                 
