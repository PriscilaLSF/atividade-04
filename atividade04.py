primeironome = input("Digite seu primeiro nome: ")
Dia = input("Digite o dia de nascimento: ")
mes = input("Digite o mês de nascimento: ")
ano = input("Digite o ano de nascimento: ")

primeiraletra=primeironome[0:1].upper()
restantenome = primeironome[1:].lower()
primeironomeformatado=primeiraletra+restantenome
mensagem= "{} nasceu em {}/{}/{}".format(primeironomeformatado,Dia,mes,ano)

print(mensagem)