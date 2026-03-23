#Estrutura de repetição Dor para listas
#Lista: Estrutura de dados compostas (armazena vários valores)

nomes = ["Pietro", "Ryan", "Maria", "Gabriela", "Sophia"]

#imprime toda a lista
print(nomes)
print("\n")

#imprime um nome individualmente (Maria)
for i in range(5):
    print(nomes[0])
    print(nomes[1])
    print(nomes[2])
    print(nomes[3])
    print(nomes[4])

print("\n")

#imprime todos os nomes utilizando for - range
for i in range(5):
    print(nomes[i])

for nome in nomes:
#outra opção para interar(percorrer de 1 em 1) sobre as listas
    print(nome)
print("\n")