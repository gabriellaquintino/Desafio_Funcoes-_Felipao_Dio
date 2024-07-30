def victory_defeat(num_vict,num_def):
    balance_rank = num_vict - num_def
    if balance_rank <= 10:
        balance = "Ferro"
    elif 11<= balance_rank <= 20:
        balance = "Bronze"
    elif 21<= balance_rank <= 50:
        balance = "Prata"
    elif 51<= balance_rank <= 80:
        balance = "Ouro"
    elif 81<= balance_rank <= 90:
        balance = "Diamante"
    elif 91<= balance_rank <= 100:
        balance = "Lendário"
    elif balance_rank >= 100:
        balance = "Imortal"

        return print(f"O Herói tem um saldo de {balance_rank} e está no nível de {balance}")
    

result =  victory_defeat(500,60)
print(result)