
valor_salario = float(input('Qual o valor do salário ? R$: '))
porcentagem_aumento =  float (input('Qual a porcentagem de aumento ? %: '))
valor_aumento = (valor_salario / 100) * porcentagem_aumento
novo_salario =  valor_salario + valor_aumento
print('O funcionario que ganhava R${:.2f}'.format(valor_salario), 'com um aumento de {:.0f}'.format(porcentagem_aumento),'% passará a receber R${:.2f}'.format(novo_salario))