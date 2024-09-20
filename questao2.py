palavra = "dnfeinqwertyuiopasdghdlfpminocwuiwinawuiawun"
letra = 'a'

repetiçoes = 0

for x in range(len(palavra)):
  if (palavra[x] == letra):
    repetiçoes = repetiçoes + 1

print(repetiçoes)

# forma 2 

path = input('digite o caminho')
caracter = input('digite o caracter')

arquivo = open(path, "r+")

repetições = 0

for linha in arquivo.readlines():
  repetições = repetições + linha.count(caracter)

print(f"repetiçoes: {repetições}")

arquivo.close()