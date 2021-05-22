"""
Nome: Caio Sampaio Oliveira
TIA: 32195621
Turma: 01N12
Atividade: Exercício do pptx da aula do dia 06/04
"""

#Entradas

##Tabela de Produtos
print("\nTabela de Produtos:")
print("\nCódigo\t\tEspecificação\t\tPreço")
print("------------------------------------------------")
print("1\t\tCachorro Quente\t\tR$ 4,00")
print("2\t\tX-Salada\t\tR$ 4,50")
print("3\t\tX-Bacon\t\t\tR$ 5,00")
print("4\t\tTorrada Simples\t\tR$ 2,00")
print("5\t\tRefrigerante\t\tR$ 1,50")
##Tabela de Produtos

codigo_produto = int(input("\nDigite o código do produto (conforme a tabela acima): "))

quantidade_produto = int(input("Digite do quantidade do produto selecionado: "))

catch_erro = 0

#Valor dos produtos
opcao_1 = 4.00
opcao_2 = 4.50
opcao_3 = 5.00
opcao_4 = 2.00
opcao_5 = 1.50
                      
#Processamento

if(quantidade_produto == 0):
    print("\nERRO: Você não pode colocar a quantidade de produtos como zero")
    catch_erro = 1
else:
    if(codigo_produto == 1):
        valor_total = (opcao_1 * quantidade_produto)
    elif(codigo_produto == 2):
        valor_total = (opcao_2 * quantidade_produto)
    elif(codigo_produto == 3):
        valor_total = (opcao_3 * quantidade_produto)
    elif(codigo_produto == 4):
        valor_total = (opcao_4 * quantidade_produto)
    elif(codigo_produto == 5):
        valor_total = (opcao_5 * quantidade_produto)
    else:
        print("\nERRO: Digite o código do produto respeitando a Tabela de Produtos")
        catch_erro = 1

#Saídas
        
if(catch_erro == 0):
    print("\n\n\tNota Fiscal")
    print("_____________________________")
    print("\nTotal: R$ %2.2f"%valor_total)
else:
    print("\nErro em gerar a Nota Fiscal")
