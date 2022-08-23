# Escreva um progama que leia um valor em metros e o exiba convertido em centímetros e milímetros

mt = float(input('Digite o valor em metros: '))
km = mt / 1000 # Kilometros
hm = mt / 100 # Hectometros
dam = mt / 10 # Decametros
dm = mt * 10 # Decímetos
cm = mt * 100 #centímetros
mm = mt * 1000 #milímetros

print('Valor em kilometros: {:.3f}Km. \nValor em hectometros: {:.3f}hm. \nValor em decametros: {:.3f}dam. \nValor em metros: {}m. \nValor em decímetros: {:.0f}dm. \nValor em centímetros: {:.0f}cm. \nValor em milímetros: {:.0f}mm.'.format(km, hm, dam, mt, dm, cm, mm))

