# Provam8

## Descrição

A atividade requer o desenvolvimento de uma cli que use regex para descobrir se a mensagem contem uma de duas intenções:

- atualizar forma de pagamento.
- verificar status do pedido.

## Regex desenvolvido

Foram desenvolvidos 2 regex para a resolução do problema:

1. (?:pagamento){1}|(?:atualiz(ar|o)){1}|(?:cart[ãa]o){1}|(?:cr[eé]dito){1}|(?:d[eé]bito){1}
2. (?:status){1}|(?:rastre(ar|io)){1}|(?:onde){1}|(?:consultar){1}|(?:encontr(ar|e)){1}

O primeiro regex captura se há intenção de atualizar as informações de pagamento procurando por palavras como: pagamento,atualizar,cartão,crédito,débito. O segundo regex procura palavras como: status,rastrear,onde,consultar e encontar.

## Utilização do sistema

Para executar o sistema o usuário deve simplesmente rodar:

```bash
git clone https://github.com/angrysine/provam8.git
cd provam8
python3 cli.py
```

O usuário pode terminar a aplicação digitando "sair no terminal".
