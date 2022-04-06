def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
             print('\033[0;31mTipo de dado incorreto\033[m')
             continue
        except KeyboardInterrupt:
            print('O usuario preferiu nao digitar um numero')
            return 0
        else:
            return n


inteiro = leiaInt("Digite um numero inteiro: ")
print(f"O numero digitado foi: {inteiro}")

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mTipo de dado incorreto\033[m')
            continue
        except (KeyboardInterrupt):
            print('O usuario preferiu nao digitar um numero')
            break
        else:
            return n

floaat = leiaFloat("Digite um float: ")
print(f'O float digitado foi {floaat}')

print(f"O inteiro digitado foi {inteiro} e o float foi {floaat}")