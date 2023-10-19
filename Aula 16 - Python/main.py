# import datetime

# data atual -> datetime.date.now()
# apenas a data -> datetime.datetime.today()
# setar uma data -> data = datetime.datetime(2023,10,2,10,15,0)

# data_atual = datetime.datetime.now()
# data_futura = data_atual + timedelta(days=10)
# print(data_futura)


# obtendo a diferença entre as datas:
# date1 = datetime.date(2023,9,10)
# date2 = datetime.date(2023,9,20)
# diferenca = date2 - date1
# print(diferenca)


# método strftime -- método de formatação de data em string

# data_hora = datetime.datetime(2023, 9, 5, 15, 30, 0)
# data_hora_formatada = data_hora.strftime('%y, %B, %A')
# print(data_hora_formatada)

# 1 - Peça ao usuário que insira seu ano de nascimento e calcule sua idade.
# import datetime

# ano_atual = datetime.datetime.now().year

# ano_nascimento = int(input("Digite seu ano de nascimento: "))

# idade = ano_atual - ano_nascimento

# print("Sua idade é", idade)

# 2 - Calcule e exiba a data e hora exatas daqui a 7 dias a partir de agora.

# import datetime
# from datetime import timedelta
# data_atual = datetime.datetime.now()
# data_futura = data_atual + timedelta(days=7)
# print(data_futura)

# 3 - Peça ao usuário para inserir um ano e, em seguida, exiba o ano atual.

# mport datetimei

# data_user = int(input("Digite um ano: "))
# data_atual = datetime.datetime.now()
# print(f"A data digitada pelo úsuario é: {data_user}, e a data atual é: {data_atual}")

# 4 - Calcule e exiba a data e hora atuais em um formato personalizado(utilize diretivas).

# import datetime

# data_atual = datetime.datetime.now()
# data_personalizada = data_atual.strftime('%y, %B, %A')
# print(data_personalizada)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# metodo .isoformat
# from datetime import datetime, timezone
# data_iso = datetime.now() .isoformat()
# print(data_iso)







