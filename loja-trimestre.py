nome = input("Digite o nome da loja: ")
jan = float(input("Digite o valor da venda de janeiro: R$:"))
fev = float(input("Digite o valor da venda de fevereiro: R$:"))
mar = float(input("Digite o valor da venda de março: R$:"))
abr = float(input("Digite o valor da venda de abril: R$:"))
mai = float(input("Digite o valor da venda de maio: R$:"))
jun = float(input("Digite o valor da venda de junho: R$:"))
jul = float(input("Digite o valor da venda de julho: R$:"))
ago = float(input("Digite o valor da venda de agosto: R$:"))
set = float(input("Digite o valor da venda de setembro: R$:"))
out = float(input("Digite o valor da venda de outubro: R$:"))
nov = float(input("Digite o valor da venda de novembro: R$:"))
dez = float(input("Digite o valor da venda de dezembro: R$:"))
trim1= jan+fev+mar
trim2= abr+mai+jun
trim3= jul+ago+set
trim4= out+nov+dez
print("Total de vendas do primeiro trimestre: R$:",trim1)
print("Total de vendas do segundo trimestre: R$:",trim2)
print("Total de vendas do terceiro trimestre: R$:",trim3)
print("Total de vendas do quarto trimestre: R$:",trim4)
print("Total de vendas da loja: R$:",trim1+trim2+trim3+trim4)