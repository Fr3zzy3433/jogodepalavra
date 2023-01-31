import os 

palavra_secreta = 'perfume'
letras_acertadas = ''
tentativa = 0

while True:
    
    letra_digitada = input('Digite uma letra: ')
    tentativa += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra: ')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
            

    print(palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print(f'Você acertou na {tentativa} tentativa')
        print('A palavra era', palavra_formada)
        tentativa = 0
        letras_acertadas = ''
        break