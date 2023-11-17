import re

def atualizar():
    return "um email sera enviado para que você possa atualizar suas informações de pagamento"
def status():
    return "seu pedido  esta atualmente na rua Faz da cidade O do estado L"



def main():
    intencoes  = {
        "atualizar": "(?:pagamento){1}|(?:atualiz(ar|o)){1}|(?:cart[ãa]o){1}|(?:cr[eé]dito){1}|(?:d[eé]bito){1}",
        "status": "(?:status){1}|(?:rastre(ar|io)){1}|(?:onde){1}|(?:consultar){1}|(?:encontr(ar|e)){1}"

    }
    acoes = {
        "atualizar":  atualizar,
        "status":status
    }

    while True:
        text =input("olá aqui você pode acompanhar seu pedido ou atualizar sua forma de pagamento, se quiser sair digite sair: ").strip().lower()
        
        if text=="sair":
            break


                                        
        has_match = False
        for key in intencoes.keys():
            regex = intencoes[key]
            
            match = re.search(regex, text)
            if match:
                has_match = True
                print(acoes[key]())
                continue


        
        if not has_match:
            print("não entendi o que você disse")
        


if __name__ == '__main__':
    main()  