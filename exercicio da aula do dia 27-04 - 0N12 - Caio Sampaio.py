"""
Nome: Caio Sampaio Oliveira
TIA: 32195621
Turma: 01N12
Atividade: Exercício 1 da aula do dia 27/04
"""

#Entradas (variáveis)

numero_notas_otimo = 0
numero_notas_ruim = 0
numero_notas_pessimo = 0
idade_notas_ruim = 0
media_idade_ruim = 0
total_notas = 0
maior_idade_bom = 0
lista_idade_bom = []
lista_idade_regular = []
lista_idade_ruim = []

#Processamento

while True: #Verifica a ocupação do cinema e permite receber um valor de ocupação menor que 100, para testes
    
        ocupacao = input("\nA ocupação do cinema está completa? (digite S para Sim e N para Não) ")

        if (ocupacao.upper() == "S"):
            limite_while = 100
            break
        elif(ocupacao.upper() == "N"):
            while True:
                limite_while = int(input("\nDigite a quantidade de espectadores presentes (entre 1 e 99): "))
                if ((limite_while >= 1) and (limite_while <= 99)):
                    break
                else:
                    print("\n *** Por favor digite um valor entre 1 e 99 pessoas *** ")
            break
        else:
            print("\n *** Por favor digite S para Sim e N para Não *** ")
            
while (limite_while != 0):

    print("\nEspectador nº",limite_while)
    
    while True:
        idade = int(input("\nDigite a sua idade (deve ser maior ou igual a 14 anos): "))
        if ((idade >= 14)):
            break
        else:
            print("\n *** Por favor digite uma idade maior ou igual a 14 anos *** ")
            
    while True:
        
        # Tabela de Notas
        print("\n Tabela de Notas para o Filme ")
        print("\nNota\t\tSignificado")
        print("\nA\t\tÓtimo")
        print("\nB\t\tBom")
        print("\nC\t\tRegular")
        print("\nD\t\tRuim")
        print("\nE\t\tPéssimo")
        
        nota = input("\nDigite a nota do filme (conforme a tabela de notas acima): ")
        if ((nota.upper() == "A") or (nota.upper() == "B") or (nota.upper() == "C") or (nota.upper() == "D") or (nota.upper() == "E")):
            total_notas += 1
            break
        else:
            print("\n *** Por favor digite a nota do filme conforme a tabela de notas *** \n")

    if(nota.upper() == "A"):
        numero_notas_otimo += 1
    elif(nota.upper() == "B"):
        lista_idade_bom.append(idade)
    elif(nota.upper() == "C"):
        lista_idade_regular.append(idade)
    elif(nota.upper() == "D"):
        idade_notas_ruim = (idade_notas_ruim + idade)
        numero_notas_ruim += 1
        lista_idade_ruim.append(idade)
    else:
        numero_notas_pessimo += 1

    limite_while -= 1
            
if(numero_notas_ruim == 0):
    media_idade_ruim = 0
else:
    media_idade_ruim = (idade_notas_ruim / numero_notas_ruim)

if(numero_notas_pessimo == 0):
    porcentagem_pessimo = 0
else:
    porcentagem_pessimo = ((numero_notas_pessimo * 100) / total_notas)

if(not lista_idade_bom):
    maior_idade_bom = 0
else:
    maior_idade_bom = max(lista_idade_bom)

if(not lista_idade_regular):
    diferenca_regular_ruim = 0
elif(not lista_idade_regular):
    diferenca_regular_ruim = (0 - min(lista_idade_ruim))
elif(not lista_idade_ruim):
    diferenca_regular_ruim = (min(lista_idade_regular) - 0)
else:
    diferenca_regular_ruim = (min(lista_idade_regular) - min(lista_idade_ruim))

#Saídas
        
print("\n_____________________________")
print("\nQuantidade de respostas 'Ótimo': ",numero_notas_otimo)
print("\nMédia da idade das pessoas quem responderam 'Ruim': ",media_idade_ruim)
print("\nPorcentagem de respostas 'Péssimo':",porcentagem_pessimo,"%")
print("\nMaior idade entre as pessoas que responderam 'Bom': ",maior_idade_bom)
print("\nDiferença entre a menor idade que respondeu 'Regular' e a menor idade que respondeu 'Ruim': ",diferenca_regular_ruim)
