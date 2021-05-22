"""
Nome: Caio Sampaio Oliveira
TIA: 32195621
Turma: 01N12
"""

#Variáveis
conversao_celsius = 0

#Início código do Cabeçalho

print("\nTabela de Conversão de ºF para ºC")
print("---------------------------------")
print("  Fahrenheit  |     Celsius      ")
print("---------------------------------")

#Fim do código do Cabeçalho

#Início código do Corpo da Tabela

for temperatura in range(50,100,1): #1ª Parte da tabela
    conversao_celsius = ((5/9)*(temperatura - 32))
    print("    ",temperatura,"ºF    |     %2.2f"%conversao_celsius,"ºC")
    print("---------------------------------")
    
#Tabela divida em duas partes por estética (melhor alinhamento do itens)
    
for temperatura in range(100,151,1): #2ª Parte da tabela (para alinhar a tabela a partir do 100ºF)
    conversao_celsius = ((5/9)*(temperatura - 32))
    print("   ",temperatura,"ºF    |     %2.2f"%conversao_celsius,"ºC")
    print("---------------------------------")

#Fim do código do Corpo da Tabela
