notas = []
digite_nota=0

while digite_nota >=0:
    if digite_nota ==-1:
        break
    digite_nota = float(input('Digite sua nota: '))
    notas.append(digite_nota)
    quantidade = len(notas)

    print(f'A sua quantidade de números lidos foram: {quantidade}')
    print(f'Os valores informados são: {notas}')
    print('')

    print('Print dos números invertidos')
    notas.reverse()
    for i in notas:
        print(i)    
        print
    
    soma = sum(notas)
    print('')
    print(f'A soma foi {soma}')
    print("")

    media = soma/quantidade
    print(f'A média dos números foram{media}')
    print("")
    maiores = []

    for m in notas:
        if m > media:
            maiores.append(m)
            print(F'Os números maiores que a média foram: {maiores}')
    print("")
    menores = []
    for m in notas:
        if int(m) < 7:
            menores.append(m)
            print(F'Os números menores que a média 7 foram: {menores}')
    print('Progamando Encerrando...')
    
