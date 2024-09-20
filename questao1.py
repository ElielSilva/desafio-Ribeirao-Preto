
def isFibonacci(num):
    if (num < 0):
        return "não é Fibonacci"
    if ( num >= 0 and num <= 3):
        return "é Fibonacci"
    ant = 2
    atual = 3
    resultado = 'não é Fibonacci'
    
    while (num >= atual):
        if(num == atual):
            resultado = "é Fibonacci"
            return resultado
        atual = atual + ant
        ant = atual - ant
    return resultado

print(isFibonacci(-5))
print(isFibonacci(2))
print(isFibonacci(8))
print(isFibonacci(13))
print(isFibonacci(15))