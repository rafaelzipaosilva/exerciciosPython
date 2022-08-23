# Operadores matemáticos
# + adição
# - subtração
# * multiplicação
# / divisão
# ** potência
# // divisão inteira
# % resto da divisão

# Ordem de precedência
# 1. ()
# 2. **
# 3. * / // %
# 4. + -

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
a = n1 + n2
s = n1 - n2
m = n1 * n2
d = n1 / n2
e = n1 ** n2
di = n1 // n2
rd = n1 % n2
print('A soma vale {}, a subtração vale {}, a multiplicação vale {}, a divisão vale {:.2f}'.format(a, s, m, d), end=' >> ')
print('A potência vale {}, a divisão inteira vale {} e o resto da divisão vale {}'.format(e, di, rd))