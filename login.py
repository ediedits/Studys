def joguinho():
    import random
    from time import sleep
    contador = 0
    while True:
        choice = str(input('Digite  Se vc quer par ou impa[P/I]?: ')).upper().strip()
        num = int(input('Digite o numero que vc vai jogar: '))
        computer = random.randint(1, 10)
        game = num + computer
        if choice == 'P':
            choice = 'Par'
        elif choice == 'I':
            choice = 'Impar'
        if game % 2 == 0:
            print(f'Vc jogou {num} e o computador {computer} | a soma dos 2 é {game}')
            print(f'Vc jogou {choice}')
            sleep(3)
            if choice == 'Par':
                print('E o computador jogou impa')
                sleep(2)
                print(f'Vc ganhou :D {game} é par ')
                contador += 1
                sleep(2)
            if choice == 'Impar':
                print('E o computador jogou impa')
                sleep(2)
                print(f'Vc perdeu :/ {game} é par')
                sleep(2)
                break
        if game % 2 != 0:
            print(f'Vc jogou {num} e o computador {computer} | a soma dos 2 é {game}')
            sleep(1)
            print(f'Vc jogou {choice}')
            sleep(1)
            if choice == 'Par':
                print('E o computador jogou par')
                sleep(2)
                print(f'Vc perdeu :/ {game} é impar ')
                sleep(2)
                break
            if choice == 'Impar':
                print('E o computador jogou par')
                sleep(2)
                print(f'Vc ganhou :D {game} é impar')
                contador += 1
                sleep(2)
    print(f'Fim, com um total de {contador} acertos')


from time import sleep
print('Abaixo, irá aparecer a tela de login, a cada opção, terá um numero. ')
login = ''
senha = ''
reallogin = ''
realsenha = ''
cont = ''
sleep(5)
while True:
    print('Digite o numero para acessar a função')
    res = int(input(f"""
    [1]Login[{login}]
    [2]Senha[{cont}]
    
        [3]CONFIRMAR
    
    [4]Novo? se cadastre agora!
    
Digite sua solicitação:
    """))
    if res == 1:
        login = str(input('Digite o login: ')).lower().strip()
        print('Login Cadastrado!...')
        sleep(3)
    elif res == 2:
        senha = str(input('Digite a Sua senha:')).lower().strip()
        contn = len(senha)
        cont = '*'*contn
        print('Senha cadastrada!')
        sleep(3.0)
    elif res == 3:
        if login == '' and senha == '':
            print('Nenhum valor digitado digite o login e senha ou crie uma nova conta!')
            sleep(4)
        elif login == reallogin and senha == realsenha:
            print('Vc está logado!')
            print('E terá acesso a um joguinho!!')
            print('.')
            sleep(1)
            print('..')
            sleep(1)
            print('...')
            joguinho()
            break
        else:
            print("Hey, esta conta não está cadastrada.")
            sleep(3)
    elif res == 4:
        print('Olá, digite suas credenciais para ser salvas!')
        reallogin = str(input('Digite seu login: ')).lower().strip()
        realsenha = str(input('Digite sua senha: ')).lower().strip()


