n1 = input('Digite o nome de uma cidade: ')
print('O nome da cidade começa com "SANTO"?')
frase = n1.split()
frase2 = n1.upper()
localizar = frase[0].upper().find("SANTO")
if localizar == 0:
    resp = 'sim'
else:
    resp = 'não'
print(f'Resp.: {resp}')
print(f'Resp.: {localizar}')#funciona também, apenas para primeiro
print(f'Resp.: {"SANTO" in frase2}')
