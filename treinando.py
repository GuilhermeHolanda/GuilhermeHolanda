from xmlrpc.client import boolean


nome = input("Digite seu nome para começar o calculo: ")

# Entrada de dados 1 "sh" Sálario hora

salario_hora = int(input(f"{nome}, Quanto você ganha por hora ? \nR= ".title()))
horas_trabalhadas_mes = int(input("E quantas horas você trabalha no mês ? \nR= "))

# Processamento

salario_bruto = salario_hora * horas_trabalhadas_mes
ir = salario_bruto * 11/100
inss = salario_bruto * 8/100
sindicato = salario_bruto * 5/100

salario_liquido = salario_bruto - ir - inss - sindicato

#saida

print (f"salário bruto: {salario_bruto}!")
print (f"Quanto pagou ao INSS: {inss}!")
print (f"Quanto pagou ao sindicato: {sindicato}!")
print (f"Seu Salário Liquido: {salario_liquido}!! ")



