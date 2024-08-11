import os
import time
import autenticador
import msvcrt

def sleep():
    time.sleep(2)
def cls():
    os.system('cls')

def menu():
    print('''
========================
          
    Menu

    [1] - Fazer login
    [2] - Criar login
    [3] - Sair  

========================    
    ''')

def main():
    
    login_salvo = ""
    senha_salvo = ""

    while True: 
        cls()
        menu()
        try:
            choice = int(input("Escolha uma opção: "))
            
            match choice:
                case 1:
                    if login_salvo == "" or senha_salvo == "":
                        print("Não há conta cadastrada")
                        sleep()

                    else:
                        login = input("Insira o login: ")
                        senha = input("Insira a senha: ")

                        if senha_salvo != senha  or login_salvo != login:
                            print ('Login ou senha incorreta, voltando ao menu...')
                            sleep()

                        else:
                            print(autenticador.Autenticador.codigo.now())
                            codigo_usuario = input("Codigo de autenticação: ")

                            if autenticador.Autenticador.codigo.verify(codigo_usuario):
                                print('\nSua conta foi logada com sucesso.') 
                                print('Pressione qualquer tecla para voltar ao menu...')
                                msvcrt.getch() 
                            else:
                                print('Autenticação falhou, voltando ao menu...')
                                sleep()

                case 2:
                    login_salvo = input("Crie o login: ")
                    senha_salvo = input("Crie a senha: ")

                case 3:
                    break

                case _:
                    print ('Por favor, digite um valor válido. Tente novamente.')
                    sleep()

        except ValueError:
                print("Por favor, digite um valor válido. Tente novamente.")
                sleep()

if __name__ == "__main__":
    main()