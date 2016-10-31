arq = open("teste.txt" ,"r")
dados = arq.readlines()
nome = str(input('Digite seu nome...\n'))
idade = str(input('Digite sua idade...\n'))
escola = str(input('Digite sua escola...\n'))

arq = open("teste.txt", "w")
arq.writelines(dados)
arq.write("\n")
arq.writelines(nome + "|" + idade + "|" + escola)
arq.close()
print('Cadastro realizado com sucesso!!')

