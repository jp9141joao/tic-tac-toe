import os
import random
import time

def Jogar_Sozinho(Dificuldade):

    if Dificuldade == 1:

        Placar1 = 0
        Placar2 = 0

        while True:
            os.system('cls')
            N1 = 1
            N2 = 2
            N3 = 3
            N4 = 4
            N5 = 5
            N6 = 6
            N7 = 7
            N8 = 8
            N9 = 9

            Placar = f'* Placar *\nVocê: {Placar1}\nRobo: {Placar2}\n\n'
            Layout = f' {N1}  |  {N2}  |  {N3} \n----------------\n {N4}  |  {N5}  |  {N6} \n----------------\n {N7}  |  {N8}  |  {N9} \n'

            print(Placar)
            print(Layout)

            Continuar = int(input('\nIniciar jogo:\n1- Sim\n2- Não\nR: '))
            while Continuar != 1 and Continuar != 2:
                Continuar = int(input('\nOpção Invalida!\nIniciar jogo:\n1- Sim\n2- Não\nR: '))

            if Continuar == 2:
                break

            while True: 
            
                while True:
                    
                    os.system('cls')

                    Placar = f'* Placar *\nVocê: {Placar1}\nRobo: {Placar2}\n\n'
                    Layout = f' {N1}  |  {N2}  |  {N3} \n----------------\n {N4}  |  {N5}  |  {N6} \n----------------\n {N7}  |  {N8}  |  {N9} \n'

                    print(Placar)
                    print(Layout)

                    Jogador1 = int(input('\nVez do jogador NUMERO UM\nR: '))
                    while Jogador1 > 9 and Jogador1 < 1:
                        Jogador1 = int(input('\nOpção Invalida! Digite um numero de 1 a 9\nVez do jogador NUMERO UM\nR: '))

                    if Jogador1 == N1 and N1 == 1:
                        N1 = 'X'
                        break

                    elif Jogador1 == N2 and N2 == 2:
                        N2 = 'X'
                        break

                    elif Jogador1 == N3 and N3 == 3:
                        N3 = 'X'
                        break

                    elif Jogador1 == N4 and N4 == 4:
                        N4 = 'X'
                        break

                    elif Jogador1 == N5 and N5 == 5:
                        N5 = 'X'
                        break

                    elif Jogador1 == N6 and N6 == 6:
                        N6 = 'X'
                        break

                    elif Jogador1 == N7 and N7 == 7:
                        N7 = 'X'
                        break

                    elif Jogador1 == N8 and N8 == 8:
                        N8 = 'X'
                        break

                    elif Jogador1 == N9 and N9 == 9:
                        N9 = 'X'
                        break

                    else:
                        Voltar = int(input('\nNão é possivel selecionar uma possição já utilizada!\nDigite "1" para voltar\nR: '))
                        while Voltar != 1:
                            Voltar = int(input('\nOpção Invalida!\nDigite "1" para voltar\nR: '))

                os.system('cls')

                Placar = f'* Placar *\nVocê: {Placar1}\nRobo: {Placar2}\n\n'
                Layout = f' {N1}  |  {N2}  |  {N3} \n----------------\n {N4}  |  {N5}  |  {N6} \n----------------\n {N7}  |  {N8}  |  {N9} \n'

                print(Placar)
                print(Layout)

                if (N1 == 'X' and N2 == 'X' and N3 == 'X') or (N4 == 'X' and N5 == 'X' and N6 == 'X') or (N7 == 'X' and N8 == 'X' and N9 == 'X') or (N1 == 'X' and N4 == 'X' and N7 == 'X') or (N2 == 'X' and N5 == 'X' and N8 == 'X') or (N3 == 'X' and N6 == 'X' and N9 == 'X') or (N1 == 'X' and N5 == 'X' and N9 == 'X') or (N3 == 'X' and N5 == 'X' and N7 == 'X'):
                    print('\n\n* Parabens *\nVocê 1 venceu!')
                    Placar1 += 1
                    
                    Voltar = int(input('\nDigite "1" para voltar\nR: '))
                    while Voltar != 1:
                        Voltar = int(input('Opção Invalida!\nDigite "1" para voltar\nR: '))

                    break
                    
                if (N1 == 'O' and N2 == 'O' and N3 == 'O') or (N4 == 'O' and N5 == 'O' and N6 == 'O') or (N7 == 'O' and N8 == 'O' and N9 == 'O') or (N1 == 'O' and N4 == 'O' and N7 == 'O') or (N2 == 'O' and N5 == 'O' and N8 == 'O') or (N3 == 'O' and N6 == 'O' and N9 == 'O') or (N1 == 'O' and N5 == 'O' and N9 == 'O') or (N3 == 'O' and N5 == 'O' and N7 == 'O'):
                    print('\n\n* Que azar! *\nRobo venceu!')
                    Placar2 += 1
                    
                    Voltar = int(input('\nDigite "1" para voltar\nR: '))
                    while Voltar != 1:
                        Voltar = int(input('\nOpção Invalida!\nDigite "1" para voltar\nR: '))

                    break

                if N1 != 1 and N2 != 2 and N3 != 3 and N4 != 4 and N5 != 5 and N6 != 6 and N7 != 7 and N8 != 8 and N9 != 9:
                    print('\nJogo empatado!')

                    Voltar = int(input('\nDigite "1" para voltar\nR: '))
                    while Voltar != 1:
                        Voltar = int(input('\nOpção Invalida!\nDigite "1" para voltar\nR: '))

                    break



                while True:
        
                    if (N1 == 'X' or N2 == 'X' or N3 == 'X') and (N1 != 'X' or N2 != 'X' or N3 != 'X'):
                        Jogador2 = random.randint(1,3)

                    elif (N4 == 'X' or N5 == 'X' or N6 == 'X') and (N4 != 'X' or N5 != 'X' or N6 != 'X'):
                        Jogador2 = random.randint(4,6)

                    elif (N4 == 'X' or N5 == 'X' or N6 == 'X') and (N4 != 'X' or N5 != 'X' or N6 != 'X'):
                        Jogador2 = random.randint(7,9)

                    elif (N1 == 'X' or N5 == 'X' or N9 == 'X') and (N1 != 'X' or N5 != 'X' or N9 != 'X'):
                        Numb = random.randint(1,3)
                        if Numb == 1:
                            Jogador2 = 1
                        elif Numb == 2:
                            Jogador2 = 5
                        else:
                            Jogador2 = 9

                    elif (N3 == 'X' or N5 == 'X' or N7 == 'X') and (N3 != 'X' or N5 != 'X' or N7 != 'X'):
                        Numb = random.randint(1,3)
                        if Numb == 1:
                            Jogador2 = 3
                        elif Numb == 2:
                            Jogador2 = 5
                        else:
                            Jogador2 = 7

                    elif (N1 == 'X' or N4 == 'X' or N7 == 'X') and (N1 != 'X' or N4 != 'X' or N7 != 'X'):
                        Numb = random.randint(1,3)
                        if Numb == 1:
                            Jogador2 = 1
                        elif Numb == 2:
                            Jogador2 = 4
                        else:
                            Jogador2 = 7

                    elif (N2 == 'X' or N5 == 'X' or N8 == 'X') and (N2 != 'X' or N5 != 'X' or N8 != 'X'):
                        Numb = random.randint(1,3)
                        if Numb == 1:
                            Jogador2 = 2
                        elif Numb == 2:
                            Jogador2 = 5
                        else:
                            Jogador2 = 8

                    elif (N3 == 'X' or N6 == 'X' or N9 == 'X') and (N3 != 'X' or N6 != 'X' or N9 != 'X'):
                        Numb = random.randint(1,3)
                        if Numb == 1:
                            Jogador2 = 3
                        elif Numb == 2:
                            Jogador2 = 6
                        else:
                            Jogador2 = 9
                    else:
                        Jogador2 = random.randint(1,9)

        

                    if Jogador2 == N1 and N1 == 1:
                        N1 = 'O'
                        break

                    elif Jogador2 == N2 and N2 == 2:
                        N2 = 'O'
                        break

                    elif Jogador2 == N3 and N3 == 3:
                        N3 = 'O'
                        break

                    elif Jogador2 == N4 and N4 == 4:
                        N4 = 'O'
                        break

                    elif Jogador2 == N5 and N5 == 5:
                        N5 = 'O'
                        break

                    elif Jogador2 == N6 and N6 == 6:
                        N6 = 'O'
                        break

                    elif Jogador2 == N7 and N7 == 7:
                        N7 = 'O'
                        break

                    elif Jogador2 == N8 and N8 == 8:
                        N8 = 'O'
                        break

                    elif Jogador2 == N9 and N9 == 9:
                        N9 = 'O'
                        break


                print(f'\nRobo escolheu a posição {Jogador2}')
                time.sleep(3)

                os.system('cls')

                Placar = f'* Placar *\nYou: {Placar1}\nRobo: {Placar2}\n\n'
                Layout = f' {N1}  |  {N2}  |  {N3} \n----------------\n {N4}  |  {N5}  |  {N6} \n----------------\n {N7}  |  {N8}  |  {N9} \n'

                print(Placar)
                print(Layout)

                if (N1 == 'X' and N2 == 'X' and N3 == 'X') or (N4 == 'X' and N5 == 'X' and N6 == 'X') or (N7 == 'X' and N8 == 'X' and N9 == 'X') or (N1 == 'X' and N4 == 'X' and N7 == 'X') or (N2 == 'X' and N5 == 'X' and N8 == 'X') or (N3 == 'X' and N6 == 'X' and N9 == 'X') or (N1 == 'X' and N5 == 'X' and N9 == 'X') or (N3 == 'X' and N5 == 'X' and N7 == 'X'):
                    print('\n\n* Parabens *\nVocê venceu!')
                    Placar1 += 1
                    
                    Voltar = int(input('\nDigite "1" para voltar\nR: '))
                    while Voltar != 1:
                        Voltar = int(input('Opção Invalida!\nDigite "1" para voltar\nR: '))

                    break
                    
                if (N1 == 'O' and N2 == 'O' and N3 == 'O') or (N4 == 'O' and N5 == 'O' and N6 == 'O') or (N7 == 'O' and N8 == 'O' and N9 == 'O') or (N1 == 'O' and N4 == 'O' and N7 == 'O') or (N2 == 'O' and N5 == 'O' and N8 == 'O') or (N3 == 'O' and N6 == 'O' and N9 == 'O') or (N1 == 'O' and N5 == 'O' and N9 == 'O') or (N3 == 'O' and N5 == 'O' and N7 == 'O'):
                    print('\n\n* Que azar! *\nRobo venceu!')
                    Placar2 += 1
                    
                    Voltar = int(input('\nDigite "1" para voltar\nR: '))
                    while Voltar != 1:
                        Voltar = int(input('Opção Invalida!\nDigite "1" para voltar\nR: '))

                    break

                if N1 != 1 and N2 != 2 and N3 != 3 and N4 != 4 and N5 != 5 and N6 != 6 and N7 != 7 and N8 != 8 and N9 != 9:
                    print('\nJogo empatado!')

                    Voltar = int(input('\nDigite "1" para voltar\nR: '))
                    while Voltar != 1:
                        Voltar = int(input('\nOpção Invalida!\nDigite "1" para voltar\nR: '))

                    break
        
    elif Dificuldade == 2:
        
        Placar1 = 0
        Placar2 = 0

        while True:
            os.system('cls')
            N1 = 1
            N2 = 2
            N3 = 3
            N4 = 4
            N5 = 5
            N6 = 6
            N7 = 7
            N8 = 8
            N9 = 9

            Placar = f'* Placar *\nVocê: {Placar1}\nRobo: {Placar2}\n\n'
            Layout = f' {N1}  |  {N2}  |  {N3} \n----------------\n {N4}  |  {N5}  |  {N6} \n----------------\n {N7}  |  {N8}  |  {N9} \n'

            print(Placar)
            print(Layout)

            Continuar = int(input('\nIniciar jogo:\n1- Sim\n2- Não\nR: '))
            while Continuar != 1 and Continuar != 2:
                Continuar = int(input('\nOpção Invalida!\nIniciar jogo:\n1- Sim\n2- Não\nR: '))

            if Continuar == 2:
                break

            while True: 
            
                while True:
                    
                    os.system('cls')

                    Placar = f'* Placar *\nVocê: {Placar1}\nBot: {Placar2}\n\n'
                    Layout = f' {N1}  |  {N2}  |  {N3} \n----------------\n {N4}  |  {N5}  |  {N6} \n----------------\n {N7}  |  {N8}  |  {N9} \n'

                    print(Placar)
                    print(Layout)

                    Jogador1 = int(input('\nSua vez\nR: '))
                    while Jogador1 > 9 and Jogador1 < 1:
                        Jogador1 = int(input('\nOpção Invalida! Digite um numero de 1 a 9\nSua vez\nR: '))

                    if Jogador1 == N1 and N1 == 1:
                        N1 = 'X'
                        break

                    elif Jogador1 == N2 and N2 == 2:
                        N2 = 'X'
                        break

                    elif Jogador1 == N3 and N3 == 3:
                        N3 = 'X'
                        break

                    elif Jogador1 == N4 and N4 == 4:
                        N4 = 'X'
                        break

                    elif Jogador1 == N5 and N5 == 5:
                        N5 = 'X'
                        break

                    elif Jogador1 == N6 and N6 == 6:
                        N6 = 'X'
                        break

                    elif Jogador1 == N7 and N7 == 7:
                        N7 = 'X'
                        break

                    elif Jogador1 == N8 and N8 == 8:
                        N8 = 'X'
                        break

                    elif Jogador1 == N9 and N9 == 9:
                        N9 = 'X'
                        break

                    else:
                        Voltar = int(input('\nNão é possivel selecionar uma possição já utilizada!\nDigite "1" para voltar\nR: '))
                        while Voltar != 1:
                            Voltar = int(input('\nOpção Invalida!\nDigite "1" para voltar\nR: '))


                os.system('cls')

                Placar = f'* Placar *\nVocê: {Placar1}\nRobo: {Placar2}\n\n'
                Layout = f' {N1}  |  {N2}  |  {N3} \n----------------\n {N4}  |  {N5}  |  {N6} \n----------------\n {N7}  |  {N8}  |  {N9} \n'

                print(Placar)
                print(Layout)

                if (N1 == 'X' and N2 == 'X' and N3 == 'X') or (N4 == 'X' and N5 == 'X' and N6 == 'X') or (N7 == 'X' and N8 == 'X' and N9 == 'X') or (N1 == 'X' and N4 == 'X' and N7 == 'X') or (N2 == 'X' and N5 == 'X' and N8 == 'X') or (N3 == 'X' and N6 == 'X' and N9 == 'X') or (N1 == 'X' and N5 == 'X' and N9 == 'X') or (N3 == 'X' and N5 == 'X' and N7 == 'X'):
                    print('\n\n* Parabens *\nVocê venceu!')
                    Placar1 += 1
                    
                    Voltar = int(input('\nDigite "1" para voltar\nR: '))
                    while Voltar != 1:
                        Voltar = int(input('Opção Invalida!\nDigite "1" para voltar\nR: '))

                    break
                    
                if (N1 == 'O' and N2 == 'O' and N3 == 'O') or (N4 == 'O' and N5 == 'O' and N6 == 'O') or (N7 == 'O' and N8 == 'O' and N9 == 'O') or (N1 == 'O' and N4 == 'O' and N7 == 'O') or (N2 == 'O' and N5 == 'O' and N8 == 'O') or (N3 == 'O' and N6 == 'O' and N9 == 'O') or (N1 == 'O' and N5 == 'O' and N9 == 'O') or (N3 == 'O' and N5 == 'O' and N7 == 'O'):
                    print('\n\n* Que azar! *\nRobo venceu!')
                    Placar2 += 1
                    
                    Voltar = int(input('\nDigite "1" para voltar\nR: '))
                    while Voltar != 1:
                        Voltar = int(input('\nOpção Invalida!\nDigite "1" para voltar\nR: '))

                    break

                if N1 != 1 and N2 != 2 and N3 != 3 and N4 != 4 and N5 != 5 and N6 != 6 and N7 != 7 and N8 != 8 and N9 != 9:
                    print('\nJogo empatado!')

                    Voltar = int(input('\nDigite "1" para voltar\nR: '))
                    while Voltar != 1:
                        Voltar = int(input('\nOpção Invalida!\nDigite "1" para voltar\nR: '))

                    break



                while True:
                
                    if ((N1 == 'X' and N2 == 'X' and N3 != 'O') or (N1 == 'X' and N3 == 'X' and N2 != 'O') or (N2 == 'X' and N3 == 'X' and N1 != 'O')) and (N1 != 'X' or N2 != 'X' or N3 != 'X'):
                        Jogador2 = random.randint(1,3)

                    elif ((N4 == 'X' and N5 == 'X' and N6 != 'O') or (N4 == 'X' and N6 == 'X' and N6 != 'O') or (N5 == 'X' and N6 == 'X' and N4 != 'O')) and (N4 != 'X' or N5 != 'X' or N6 != 'X'):
                        Jogador2 = random.randint(4,6)

                    elif ((N7 == 'X' and N8 == 'X' and N9 != 'O') or (N7 == 'X' and N9 == 'X' and N8 != 'O') or (N8 == 'X' and N9 == 'X' and N7 != 'O')) and (N7 != 'X' or N8 != 'X' or N9 != 'X'):
                        Jogador2 = random.randint(7,9)

                    elif ((N1 == 'X' and N4 == 'X' and N7 != 'O') or (N1 == 'X' and N7 == 'X' and N4 != 'O') or (N4 == 'X' and N7 == 'X' and N1 != 'O')) and (N1 != 'X' or N4 != 'X' or N7 != 'X'):
                        while True:
                            Numb = random.randint(1,3)
                            if Numb == 1 and N1 != 'X':
                                Jogador2 = 1
                                break
                            elif Numb == 2 and N4 != 'X':
                                Jogador2 = 4
                                break
                            elif Numb == 3 and N7 != 'X':
                                Jogador2 = 7
                                break
                            else:
                                break

                    elif ((N2 == 'X' and N5 == 'X' and N8 != 'O') or (N2 == 'X' and N8 == 'X' and N5 != 'O') or (N5 == 'X' and N8 == 'X' and N2 != 'O')) and (N2 != 'X' or N5 != 'X' or N8 != 'X'):
                        while True:
                            Numb = random.randint(1,3)
                            if Numb == 1 and N2 != 'X':
                                Jogador2 = 2
                                break
                            elif Numb == 2 and N5 != 'X':
                                Jogador2 = 5
                                break
                            elif Numb == 3 and N8 != 'X':
                                Jogador2 = 8
                                break
                            else:
                                break

                    elif ((N3 == 'X' and N6 == 'X' and N9 != 'O') or (N3 == 'X' and N9 == 'X' and N6 != 'O') or (N6 == 'X' and N9 == 'X' and N3 != 'O')) and (N3 != 'X' or N6 != 'X' or N9 != 'X'):
                        while True:
                            Numb = random.randint(1,3)
                            if Numb == 1 and N3 != 'X':
                                Jogador2 = 3
                                break
                            elif Numb == 2 and N6 != 'X':
                                Jogador2 = 6
                                break
                            elif Numb == 3 and N9 != 'X':
                                Jogador2 = 9
                                break
                            else:
                                break 

                    elif ((N1 == 'X' and N5 == 'X' and N9 != 'O') or (N1 == 'X' and N9 == 'X' and N5 != 'O') or (N5 == 'X' and N9 == 'X' and N1 != 'O')) and (N1 != 'X' or N5 != 'X' or N9 != 'X'):
                        while True:
                            Numb = random.randint(1,3)
                            if Numb == 1 and N1 != 'X':
                                Jogador2 = 1
                                break
                            elif Numb == 2 and N5 != 'X':
                                Jogador2 = 5
                                break
                            elif Numb == 3 and N9 != 'X':
                                Jogador2 = 9
                                break
                            else:
                                break

                    elif ((N3 == 'X' and N5 == 'X' and N7 != 'O') or (N3 == 'X' and N7 == 'X' and N5 != 'O') or (N7 == 'X' and N5 == 'X' and N3 != 'O')) and (N3 != 'X' or N5 != 'X' or N7 != 'X'):
                        while True:
                            Numb = random.randint(1,3)
                            if Numb == 1 and N3 != 'X':
                                Jogador2 = 3
                                break
                            elif Numb == 2 and N5 != 'X':
                                Jogador2 = 5
                                break
                            elif Numb == 3 and N7 != 'X':
                                Jogador2 = 7
                                break
                            else:
                                break

                    elif ((N1 == 'X' and N2 == 'X' and N3 == 'O') or (N1 == 'X' and N2 == 'O' and N3 == 'X') or (N1 == 'O' and N2 == 'X' and N3 == 'X')):
                        while True:
                            Numb = random.randint(1,6)

                            if Numb == 1 and N4 != 'X':
                                Jogador2 = 4
                                break
                            elif Numb == 2 and N5 != 'X':
                                Jogador2 = 5
                                break
                            elif Numb == 3 and N6 != 'X':
                                Jogador2 = 6
                                break
                            elif Numb == 4 and N7 != 'X':
                                Jogador2 = 7
                                break
                            elif Numb == 5 and N8 != 'X':
                                Jogador2 = 8
                                break
                            elif Numb == 6 and N9 != 'X':
                                Jogador2 = 9
                                break

                    elif ((N4 == 'X' and N5 == 'X' and N6 == 'O') or (N4 == 'X' and N5 == 'O' and N6 == 'X') or (N4 == 'O' and N5 == 'X' and N6 == 'X')):
                        while True:
                            Numb = random.randint(1,6)

                            if Numb == 1 and N1 != 'X':
                                Jogador2 = 1
                                break
                            elif Numb == 2 and N2 != 'X':
                                Jogador2 = 2
                                break
                            elif Numb == 3 and N3 != 'X':
                                Jogador2 = 3
                                break
                            elif Numb == 4 and N7 != 'X':
                                Jogador2 = 7
                                break
                            elif Numb == 5 and N8 != 'X':
                                Jogador2 = 8
                                break
                            elif Numb == 6 and N9 != 'X':
                                Jogador2 = 9
                                break 

                    elif ((N7 == 'X' and N8 == 'X' and N9 != 'O') or (N7 == 'X' and N8 == 'O' and N9 == 'X') or (N7 == 'O' and N8 == 'X' and N9 == 'X')):
                        while True:
                            Numb = random.randint(1,6)

                            if Numb == 1 and N1 != 'X':
                                Jogador2 = 1
                                break
                            elif Numb == 2 and N2 != 'X':
                                Jogador2 = 2
                                break
                            elif Numb == 3 and N3 != 'X':
                                Jogador2 = 3
                                break
                            elif Numb == 4 and N4 != 'X':
                                Jogador2 = 4
                                break
                            elif Numb == 5 and N5 != 'X':
                                Jogador2 = 5
                                break
                            elif Numb == 6 and N6 != 'X':
                                Jogador2 = 6
                                break 

                    elif ((N1 == 'X' and N4 == 'X' and N7 == 'O') or (N1 == 'X' and N4 == 'O' and N7 == 'X') or (N1 == 'O' and N4 == 'X' and N7 == 'X')):
                        while True:
                            Numb = random.randint(1,6)

                            if Numb == 1 and N2 != 'X':
                                Jogador2 = 2
                                break
                            elif Numb == 2 and N3 != 'X':
                                Jogador2 = 3
                                break
                            elif Numb == 3 and N4 != 'X':
                                Jogador2 = 4
                                break
                            elif Numb == 4 and N6 != 'X':
                                Jogador2 = 6
                                break
                            elif Numb == 5 and N7 != 'X':
                                Jogador2 = 7
                                break
                            elif Numb == 6 and N8 != 'X':
                                Jogador2 = 8
                                break

                    elif ((N3 == 'X' and N5 == 'X' and N7 == 'O') or (N3 == 'X' and N5 == 'O' and N7 == 'X') or (N3 == 'O' and N5 == 'X' and N7 == 'X')):
                        while True:
                            Numb = random.randint(1,6)

                            if Numb == 1 and N1 != 'X':
                                Jogador2 = 1
                                break
                            elif Numb == 2 and N2 != 'X':
                                Jogador2 = 2
                                break
                            elif Numb == 3 and N4 != 'X':
                                Jogador2 = 4
                                break
                            elif Numb == 4 and N6 != 'X':
                                Jogador2 = 6
                                break
                            elif Numb == 5 and N8 != 'X':
                                Jogador2 = 8
                                break
                            elif Numb == 6 and N9 != 'X':
                                Jogador2 = 9
                                break

                    elif (N1 == 'X' or N2 == 'X' or N3 == 'X') and (N1 != 'X' or N2 != 'X' or N3 != 'X'):
                        Jogador2 = random.randint(1,3)

                    elif (N4 == 'X' or N5 == 'X' or N6 == 'X') and (N4 != 'X' or N5 != 'X' or N6 != 'X'):
                        Jogador2 = random.randint(4,6)

                    elif (N4 == 'X' or N5 == 'X' or N6 == 'X') and (N4 != 'X' or N5 != 'X' or N6 != 'X'):
                        Jogador2 = random.randint(7,9)

                    elif (N1 == 'X' or N5 == 'X' or N9 == 'X') and (N1 != 'X' or N5 != 'X' or N9 != 'X'):
                        Numb = random.randint(1,3)
                        if Numb == 1:
                            Jogador2 = 1
                        elif Numb == 2:
                            Jogador2 = 5
                        else:
                            Jogador2 = 9

                    elif (N3 == 'X' or N5 == 'X' or N7 == 'X') and (N3 != 'X' or N5 != 'X' or N7 != 'X'):
                        Numb = random.randint(1,3)
                        if Numb == 1:
                            Jogador2 = 3
                        elif Numb == 2:
                            Jogador2 = 5
                        else:
                            Jogador2 = 7

                    elif (N1 == 'X' or N4 == 'X' or N7 == 'X') and (N1 != 'X' or N4 != 'X' or N7 != 'X'):
                        Numb = random.randint(1,3)
                        if Numb == 1:
                            Jogador2 = 1
                        elif Numb == 2:
                            Jogador2 = 4
                        else:
                            Jogador2 = 7

                    elif (N2 == 'X' or N5 == 'X' or N8 == 'X') and (N2 != 'X' or N5 != 'X' or N8 != 'X'):
                        Numb = random.randint(1,3)
                        if Numb == 1:
                            Jogador2 = 2
                        elif Numb == 2:
                            Jogador2 = 5
                        else:
                            Jogador2 = 8

                    elif (N3 == 'X' or N6 == 'X' or N9 == 'X') and (N3 != 'X' or N6 != 'X' or N9 != 'X'):
                        Numb = random.randint(1,3)
                        if Numb == 1:
                            Jogador2 = 3
                        elif Numb == 2:
                            Jogador2 = 6
                        else:
                            Jogador2 = 9
                    else:
                        Jogador2 = random.randint(1,9)

        

                    if Jogador2 == N1 and N1 == 1:
                        N1 = 'O'
                        break

                    elif Jogador2 == N2 and N2 == 2:
                        N2 = 'O'
                        break

                    elif Jogador2 == N3 and N3 == 3:
                        N3 = 'O'
                        break

                    elif Jogador2 == N4 and N4 == 4:
                        N4 = 'O'
                        break

                    elif Jogador2 == N5 and N5 == 5:
                        N5 = 'O'
                        break

                    elif Jogador2 == N6 and N6 == 6:
                        N6 = 'O'
                        break

                    elif Jogador2 == N7 and N7 == 7:
                        N7 = 'O'
                        break

                    elif Jogador2 == N8 and N8 == 8:
                        N8 = 'O'
                        break

                    elif Jogador2 == N9 and N9 == 9:
                        N9 = 'O'
                        break


                print(f'\nRobo escolheu a posição {Jogador2}')
                time.sleep(3)

                os.system('cls')

                Placar = f'* Placar *\nVocê: {Placar1}\nRobo: {Placar2}\n\n'
                Layout = f' {N1}  |  {N2}  |  {N3} \n----------------\n {N4}  |  {N5}  |  {N6} \n----------------\n {N7}  |  {N8}  |  {N9} \n'

                print(Placar)
                print(Layout)

                if (N1 == 'X' and N2 == 'X' and N3 == 'X') or (N4 == 'X' and N5 == 'X' and N6 == 'X') or (N7 == 'X' and N8 == 'X' and N9 == 'X') or (N1 == 'X' and N4 == 'X' and N7 == 'X') or (N2 == 'X' and N5 == 'X' and N8 == 'X') or (N3 == 'X' and N6 == 'X' and N9 == 'X') or (N1 == 'X' and N5 == 'X' and N9 == 'X') or (N3 == 'X' and N5 == 'X' and N7 == 'X'):
                    print('\n\n* Parabens *\nVocê venceu!')
                    Placar1 += 1
                    
                    Voltar = int(input('\nDigite "1" para voltar\nR: '))
                    while Voltar != 1:
                        Voltar = int(input('Opção Invalida!\nDigite "1" para voltar\nR: '))

                    break
                    
                if (N1 == 'O' and N2 == 'O' and N3 == 'O') or (N4 == 'O' and N5 == 'O' and N6 == 'O') or (N7 == 'O' and N8 == 'O' and N9 == 'O') or (N1 == 'O' and N4 == 'O' and N7 == 'O') or (N2 == 'O' and N5 == 'O' and N8 == 'O') or (N3 == 'O' and N6 == 'O' and N9 == 'O') or (N1 == 'O' and N5 == 'O' and N9 == 'O') or (N3 == 'O' and N5 == 'O' and N7 == 'O'):
                    print('\n\n* Que azar! *\nRobo venceu!')
                    Placar2 += 1
                    
                    Voltar = int(input('\nDigite "1" para voltar\nR: '))
                    while Voltar != 1:
                        Voltar = int(input('Opção Invalida!\nDigite "1" para voltar\nR: '))

                    break

                if N1 != 1 and N2 != 2 and N3 != 3 and N4 != 4 and N5 != 5 and N6 != 6 and N7 != 7 and N8 != 8 and N9 != 9:
                    print('\nJogo empatado!')

                    Voltar = int(input('\nDigite "1" para voltar\nR: '))
                    while Voltar != 1:
                        Voltar = int(input('\nOpção Invalida!\nDigite "1" para voltar\nR: '))

                    break
    
    else:
        
        Placar1 = 0
        Placar2 = 0

        while True:
            os.system('cls')
            N1 = 1
            N2 = 2
            N3 = 3
            N4 = 4
            N5 = 5
            N6 = 6
            N7 = 7
            N8 = 8
            N9 = 9

            Placar = f'* Placar *\nVocê: {Placar1}\nRobo: {Placar2}\n\n'
            Layout = f' {N1}  |  {N2}  |  {N3} \n----------------\n {N4}  |  {N5}  |  {N6} \n----------------\n {N7}  |  {N8}  |  {N9} \n'

            print(Placar)
            print(Layout)

            Continuar = int(input('\nIniciar jogo:\n1- Sim\n2- Não\nR: '))
            while Continuar != 1 and Continuar != 2:
                Continuar = int(input('\nOpção Invalida!\nIniciar jogo:\n1- Sim\n2- Não\nR: '))

            if Continuar == 2:
                break

            while True: 
            
                while True:
                    
                    os.system('cls')

                    Placar = f'* Placar *\nVocê: {Placar1}\nRobo: {Placar2}\n\n'
                    Layout = f' {N1}  |  {N2}  |  {N3} \n----------------\n {N4}  |  {N5}  |  {N6} \n----------------\n {N7}  |  {N8}  |  {N9} \n'

                    print(Placar)
                    print(Layout)

                    Jogador1 = int(input('\nSua vez\nR: '))
                    while Jogador1 > 9 and Jogador1 < 1:
                        Jogador1 = int(input('\nOpção Invalida! Digite um numero de 1 a 9\nSua vez\nR: '))

                    if Jogador1 == N1 and N1 == 1:
                        N1 = 'X'
                        break

                    elif Jogador1 == N2 and N2 == 2:
                        N2 = 'X'
                        break

                    elif Jogador1 == N3 and N3 == 3:
                        N3 = 'X'
                        break

                    elif Jogador1 == N4 and N4 == 4:
                        N4 = 'X'
                        break

                    elif Jogador1 == N5 and N5 == 5:
                        N5 = 'X'
                        break

                    elif Jogador1 == N6 and N6 == 6:
                        N6 = 'X'
                        break

                    elif Jogador1 == N7 and N7 == 7:
                        N7 = 'X'
                        break

                    elif Jogador1 == N8 and N8 == 8:
                        N8 = 'X'
                        break

                    elif Jogador1 == N9 and N9 == 9:
                        N9 = 'X'
                        break

                    else:
                        Voltar = int(input('\nNão é possivel selecionar uma possição já utilizada!\nDigite "1" para voltar\nR: '))
                        while Voltar != 1:
                            Voltar = int(input('\nOpção Invalida!\nDigite "1" para voltar\nR: '))


                os.system('cls')

                Placar = f'* Placar *\nVocê: {Placar1}\nRobo: {Placar2}\n\n'
                Layout = f' {N1}  |  {N2}  |  {N3} \n----------------\n {N4}  |  {N5}  |  {N6} \n----------------\n {N7}  |  {N8}  |  {N9} \n'

                print(Placar)
                print(Layout)

                if (N1 == 'X' and N2 == 'X' and N3 == 'X') or (N4 == 'X' and N5 == 'X' and N6 == 'X') or (N7 == 'X' and N8 == 'X' and N9 == 'X') or (N1 == 'X' and N4 == 'X' and N7 == 'X') or (N2 == 'X' and N5 == 'X' and N8 == 'X') or (N3 == 'X' and N6 == 'X' and N9 == 'X') or (N1 == 'X' and N5 == 'X' and N9 == 'X') or (N3 == 'X' and N5 == 'X' and N7 == 'X'):
                    print('\n\n* Parabens *\nVocê venceu!')
                    Placar1 += 1
                    
                    Voltar = int(input('\nDigite "1" para voltar\nR: '))
                    while Voltar != 1:
                        Voltar = int(input('Opção Invalida!\nDigite "1" para voltar\nR: '))

                    break
                    
                if (N1 == 'O' and N2 == 'O' and N3 == 'O') or (N4 == 'O' and N5 == 'O' and N6 == 'O') or (N7 == 'O' and N8 == 'O' and N9 == 'O') or (N1 == 'O' and N4 == 'O' and N7 == 'O') or (N2 == 'O' and N5 == 'O' and N8 == 'O') or (N3 == 'O' and N6 == 'O' and N9 == 'O') or (N1 == 'O' and N5 == 'O' and N9 == 'O') or (N3 == 'O' and N5 == 'O' and N7 == 'O'):
                    print('\n\n* Que azar! *\nRobo venceu!')
                    Placar2 += 1
                    
                    Voltar = int(input('\nDigite "1" para voltar\nR: '))
                    while Voltar != 1:
                        Voltar = int(input('\nOpção Invalida!\nDigite "1" para voltar\nR: '))

                    break

                if N1 != 1 and N2 != 2 and N3 != 3 and N4 != 4 and N5 != 5 and N6 != 6 and N7 != 7 and N8 != 8 and N9 != 9:
                    print('\nJogo empatado!')

                    Voltar = int(input('\nDigite "1" para voltar\nR: '))
                    while Voltar != 1:
                        Voltar = int(input('\nOpção Invalida!\nDigite "1" para voltar\nR: '))

                    break


    
                
                while True:
                
                    if (N1 == 'X' and N2 == 2 and N3 == 3 and N4 == 4 and N5 == 5 and N6 == 6 and N7 == 7 and N8 == 8 and N9 == 9) or (N1 == 1 and N2 == 2 and N3 == 'X' and N4 == 4 and N5 == 5 and N6 == 6 and N7 == 7 and N8 == 8 and N9 == 9) or (N1 == 1 and N2 == 2 and N3 == 3 and N4 == 4 and N5 == 5 and N6 == 6 and N7 == 'X' and N8 == 8 and N9 == 9) or (N1 == 1 and N2 == 2 and N3 == 3 and N4 == 4 and N5 == 5 and N6 == 6 and N7 == 7 and N8 == 8 and N9 == 'X'):
                        Jogador2 = 5

                
                    elif N1 == 'X' and N2 != 'X' and N3 != 'X' and N4 != 'X' and N5 != 'X' and N6 != 'X' and N7 != 'X' and N8 != 'X' and N9 == 'X':
                        Numb = random.randint(1,4)

                        if Numb == 1:
                            Jogador2 = 2
                        elif Numb == 2:
                            Jogador2 = 4
                        elif Numb == 3:
                            Jogador2 = 6
                        elif Numb == 4:
                            Jogador2 = 8
                    
                    elif N1 != 'X' and N2 != 'X' and N3 == 'X' and N4 != 'X' and N5 != 'X' and N6 != 'X' and N7 == 'X' and N8 != 'X' and N9 != 'X':
                        Numb = random.randint(1,4)

                        if Numb == 1:
                            Jogador2 = 2
                        elif Numb == 2:
                            Jogador2 = 6
                        elif Numb == 3:
                            Jogador2 = 4
                        elif Numb == 4:
                            Jogador2 = 8
                
                        
                    elif N5 == 'X' and N1 == 'X' and N3 == 3 and N7 == 7 and N9 == 9:
                        while True:
                            Numb = random.randint(1,2)
                            if Numb == 1:
                                Jogador2 = 3
                                break
                            elif Numb == 2:
                                Jogador2 = 7
                                break
                            else:
                                break
                    
                    elif N5 == 'X' and N1 == 1 and N3 == 'X' and N7 == 7 and N9 == 9:
                        while True:
                            Numb = random.randint(1,2)
                            if Numb == 1:
                                Jogador2 = 1
                                break
                            elif Numb == 2:
                                Jogador2 = 9
                                break
                            else:
                                break

                    elif N5 == 'X' and N1 == 1 and N3 == 3 and N7 == 'X' and N9 == 9:
                        while True:
                            Numb = random.randint(1,2)
                            if Numb == 1:
                                Jogador2 = 1
                                break
                            elif Numb == 2:
                                Jogador2 = 9
                                break

                    elif N5 == 'X' and N1 == 1 and N3 == 3 and N7 == 7 and N9 == 'X':
                        while True:
                            Numb = random.randint(1,2)
                            if Numb == 1:
                                Jogador2 = 3
                                break
                            elif Numb == 2:
                                Jogador2 = 7
                                break

                    elif N5 == 'X' and N1 == 1 and N3 == 3 and N7 == 7 and N9 == 9:
                        while True:
                            Numb = random.randint(1,4)

                            if Numb == 1:
                                Jogador2 = 1
                                break
                            elif Numb == 2:
                                Jogador2 = 3
                                break
                            elif Numb == 3:
                                Jogador2 = 7
                                break
                            elif Numb == 4:
                                Jogador2 = 9
                                break
                            else:
                                break
                    
                    elif ((N1 == 'O' and N2 == 'O' and N3 == 3) or (N1 == 'O' and N2 == 2 and N3 == 'O') or (N1 == 1 and N2 == 'O' and N3 == 'O') or (N4 == 4 and N5 == 'O' and N6 == 'O') or (N4 == 'O' and N5 == 5 and N6 == 'O') or (N4 == 'O' and N5 == 'O' and N6 == 6) or (N7 == 7 and N8 == 'O' and N9 == 'O') or (N7 == 'O' and N8 == 8 and N9 == 'O') or (N7 == 'O' and N8 == 'O' and N9 == 9)):                                    
                        while True:
                            Numb = random.randint(1,9)

                            if Numb == 1 and N1 == 1 and N2 == 'O' and N3 == 'O':
                                Jogador2 = 1
                                break
                            elif Numb == 2 and N1 == 'O' and N2 == 2 and N3 == 'O':
                                Jogador2 = 2
                                break
                            elif Numb == 3 and N1 == 'O' and N2 == 'O' and N3 == 3:
                                Jogador2 = 3
                                break
                            elif Numb == 4 and N4 == 4 and N5 == 'O' and N6 == 'O':
                                Jogador2 = 4
                                break
                            elif Numb == 5 and N4 == 'O' and N5 == 5 and N6 == 'O':
                                Jogador2 = 5
                                break
                            elif Numb == 6 and N4 == 'O' and N5 == 'O' and N6 == 6:
                                Jogador2 = 6
                                break
                            elif Numb == 7 and N7 == 7 and N8 == 'O' and N9 == 'O':
                                Jogador2 = 7
                                break
                            elif Numb == 8 and N7 == 'O' and N8 == 8 and N9 == 'O':
                                Jogador2 = 8
                                break
                            elif Numb == 9 and N7 == 'O' and N8 == 'O' and N9 == 9:
                                Jogador2 = 9
                                break
                            else:
                                break
                    
                    elif ((N1 == 'O' and N4 == 'O' and N7 == 7) or (N1 == 'O' and N4 == 4 and N7 == 'O') or (N1 == 1 and N4 == 'O' and N7 == 'O') or (N2 == 2 and N5 == 'O' and N8 == 'O') or (N2 == 'O' and N5 == 5 and N8 == 'O') or (N2 == 'O' and N5 == 'O' and N8 == 8) or (N3 == 3 and N6 == 'O' and N9 == 'O') or (N3 == 'O' and N6 == 6 and N9 == 'O') or (N3 == 'O' and N6 == 'O' and N9 == 9)):                                    
                        while True:
                            Numb = random.randint(1,9)

                            if Numb == 1 and N1 == 1 and N4 == 'O' and N7 == 'O':
                                Jogador2 = 1
                                break
                            elif Numb == 2 and N2 == 2 and N5 == 'O' and N8 == 'O':
                                Jogador2 = 2
                                break
                            elif Numb == 3 and N3 == 3 and N6 == 'O' and N9 == 'O':
                                Jogador2 = 3
                                break
                            elif Numb == 4 and N1 == 'O' and N4 == 4 and N7 == 'O':
                                Jogador2 = 4
                                break
                            elif Numb == 5 and N2 == 'O' and N5 == 5 and N8 == 'O':
                                Jogador2 = 5
                                break
                            elif Numb == 6 and N3 == 'O' and N6 == 6 and N9 == 'O':
                                Jogador2 = 6
                                break
                            elif Numb == 7 and N1 == 'O' and N4 == 'O' and N7 == 7:
                                Jogador2 = 7
                                break
                            elif Numb == 8 and N2 == 'O' and N5 == 'O' and N8 == 8:
                                Jogador2 = 8
                                break
                            elif Numb == 9 and N3 == 'O' and N6 == 'O' and N9 == 9:
                                Jogador2 = 9
                                break
                            else:
                                break

                    elif ((N1 == 'O' and N5 == 'O' and N9 == 9) or (N1 == 'O' and N5 == 5 and N9 == 'O') or (N1 == 1 and N5 == 'O' and N6 == 'O') or (N3 == 'O' and N5 == 'O' and N7 == 7) or (N3 == 'O' and N5 == 5 and N7 == 'O') or (N3 == 3 and N5 == 'O' and N7 == 'O')):
                        while True:
                            Numb = random.randint(1,6)

                            if Numb == 1 and N1 == 1:
                                Jogador2 = 1
                            elif Numb == 2 and N5 == 5:
                                Jogador2 = 5
                            elif Numb == 3 and N9 == 9:
                                Jogador2 = 9
                            elif Numb == 4 and N3 == 3:
                                Jogador2 = 3
                            elif Numb == 5 and N7 == 7:
                                Jogador2 = 7
                            else:
                                break

                    elif ((N1 == 'X' and N2 == 'X' and N3 != 'O') or (N1 == 'X' and N3 == 'X' and N2 != 'O') or (N2 == 'X' and N3 == 'X' and N1 != 'O')) and (N1 != 'X' or N2 != 'X' or N3 != 'X'):
                        Jogador2 = random.randint(1,3)

                    elif ((N4 == 'X' and N5 == 'X' and N6 != 'O') or (N4 == 'X' and N6 == 'X' and N6 != 'O') or (N5 == 'X' and N6 == 'X' and N4 != 'O')) and (N4 != 'X' or N5 != 'X' or N6 != 'X'):
                        Jogador2 = random.randint(4,6)

                    elif ((N7 == 'X' and N8 == 'X' and N9 != 'O') or (N7 == 'X' and N9 == 'X' and N8 != 'O') or (N8 == 'X' and N9 == 'X' and N7 != 'O')) and (N7 != 'X' or N8 != 'X' or N9 != 'X'):
                        Jogador2 = random.randint(7,9)

                    elif ((N1 == 'X' and N4 == 'X' and N7 != 'O') or (N1 == 'X' and N7 == 'X' and N4 != 'O') or (N4 == 'X' and N7 == 'X' and N1 != 'O')) and (N1 != 'X' or N4 != 'X' or N7 != 'X'):
                        while True:
                            Numb = random.randint(1,3)
                            if Numb == 1 and N1 != 'X':
                                Jogador2 = 1
                                break
                            elif Numb == 2 and N4 != 'X':
                                Jogador2 = 4
                                break
                            elif Numb == 3 and N7 != 'X':
                                Jogador2 = 7
                                break
                            else:
                                break

                    elif ((N2 == 'X' and N5 == 'X' and N8 != 'O') or (N2 == 'X' and N8 == 'X' and N5 != 'O') or (N5 == 'X' and N8 == 'X' and N2 != 'O')) and (N2 != 'X' or N5 != 'X' or N8 != 'X'):
                        while True:
                            Numb = random.randint(1,3)
                            if Numb == 1 and N2 != 'X':
                                Jogador2 = 2
                                break
                            elif Numb == 2 and N5 != 'X':
                                Jogador2 = 5
                                break
                            elif Numb == 3 and N8 != 'X':
                                Jogador2 = 8
                                break
                            else:
                                break

                    elif ((N3 == 'X' and N6 == 'X' and N9 != 'O') or (N3 == 'X' and N9 == 'X' and N6 != 'O') or (N6 == 'X' and N9 == 'X' and N3 != 'O')) and (N3 != 'X' or N6 != 'X' or N9 != 'X'):
                        while True:
                            Numb = random.randint(1,3)
                            if Numb == 1 and N3 != 'X':
                                Jogador2 = 3
                                break
                            elif Numb == 2 and N6 != 'X':
                                Jogador2 = 6
                                break
                            elif Numb == 3 and N9 != 'X':
                                Jogador2 = 9
                                break
                            else:
                                break 

                    elif ((N1 == 'X' and N5 == 'X' and N9 != 'O') or (N1 == 'X' and N9 == 'X' and N5 != 'O') or (N5 == 'X' and N9 == 'X' and N1 != 'O')) and (N1 != 'X' or N5 != 'X' or N9 != 'X'):
                        while True:
                            Numb = random.randint(1,3)
                            if Numb == 1 and N1 != 'X':
                                Jogador2 = 1
                                break
                            elif Numb == 2 and N5 != 'X':
                                Jogador2 = 5
                                break
                            elif Numb == 3 and N9 != 'X':
                                Jogador2 = 9
                                break
                            else:
                                break

                    elif ((N3 == 'X' and N5 == 'X' and N7 != 'O') or (N3 == 'X' and N7 == 'X' and N5 != 'O') or (N7 == 'X' and N5 == 'X' and N3 != 'O')) and (N3 != 'X' or N5 != 'X' or N7 != 'X'):
                        while True:
                            Numb = random.randint(1,3)
                            if Numb == 1 and N3 != 'X':
                                Jogador2 = 3
                                break
                            elif Numb == 2 and N5 != 'X':
                                Jogador2 = 5
                                break
                            elif Numb == 3 and N7 != 'X':
                                Jogador2 = 7
                                break
                            else:
                                break

                    elif ((N1 == 'X' and N2 == 'X' and N3 == 'O') or (N1 == 'X' and N2 == 'O' and N3 == 'X') or (N1 == 'O' and N2 == 'X' and N3 == 'X')):
                        while True:
                            Numb = random.randint(1,6)

                            if Numb == 1 and N4 != 'X':
                                Jogador2 = 4
                                break
                            elif Numb == 2 and N5 != 'X':
                                Jogador2 = 5
                                break
                            elif Numb == 3 and N6 != 'X':
                                Jogador2 = 6
                                break
                            elif Numb == 4 and N7 != 'X':
                                Jogador2 = 7
                                break
                            elif Numb == 5 and N8 != 'X':
                                Jogador2 = 8
                                break
                            elif Numb == 6 and N9 != 'X':
                                Jogador2 = 9
                                break
                            else:
                                break

                    elif ((N4 == 'X' and N5 == 'X' and N6 == 'O') or (N4 == 'X' and N5 == 'O' and N6 == 'X') or (N4 == 'O' and N5 == 'X' and N6 == 'X')):
                        while True:
                            Numb = random.randint(1,6)

                            if Numb == 1 and N1 != 'X':
                                Jogador2 = 1
                                break
                            elif Numb == 2 and N2 != 'X':
                                Jogador2 = 2
                                break
                            elif Numb == 3 and N3 != 'X':
                                Jogador2 = 3
                                break
                            elif Numb == 4 and N7 != 'X':
                                Jogador2 = 7
                                break
                            elif Numb == 5 and N8 != 'X':
                                Jogador2 = 8
                                break
                            elif Numb == 6 and N9 != 'X':
                                Jogador2 = 9
                                break
                            else:
                                break

                    elif ((N7 == 'X' and N8 == 'X' and N9 != 'O') or (N7 == 'X' and N8 == 'O' and N9 == 'X') or (N7 == 'O' and N8 == 'X' and N9 == 'X')):
                        while True:
                            Numb = random.randint(1,6)

                            if Numb == 1 and N1 != 'X':
                                Jogador2 = 1
                                break
                            elif Numb == 2 and N2 != 'X':
                                Jogador2 = 2
                                break
                            elif Numb == 3 and N3 != 'X':
                                Jogador2 = 3
                                break
                            elif Numb == 4 and N4 != 'X':
                                Jogador2 = 4
                                break
                            elif Numb == 5 and N5 != 'X':
                                Jogador2 = 5
                                break
                            elif Numb == 6 and N6 != 'X':
                                Jogador2 = 6
                                break 
                            else:
                                break

                    elif ((N1 == 'X' and N4 == 'X' and N7 == 'O') or (N1 == 'X' and N4 == 'O' and N7 == 'X') or (N1 == 'O' and N4 == 'X' and N7 == 'X')):
                        while True:
                            Numb = random.randint(1,6)

                            if Numb == 1 and N2 != 'X':
                                Jogador2 = 2
                                break
                            elif Numb == 2 and N3 != 'X':
                                Jogador2 = 3
                                break
                            elif Numb == 3 and N4 != 'X':
                                Jogador2 = 4
                                break
                            elif Numb == 4 and N6 != 'X':
                                Jogador2 = 6
                                break
                            elif Numb == 5 and N7 != 'X':
                                Jogador2 = 7
                                break
                            elif Numb == 6 and N8 != 'X':
                                Jogador2 = 8
                                break
                            else:
                                break

                    elif ((N3 == 'X' and N5 == 'X' and N7 == 'O') or (N3 == 'X' and N5 == 'O' and N7 == 'X') or (N3 == 'O' and N5 == 'X' and N7 == 'X')):
                        while True:
                            Numb = random.randint(1,6)

                            if Numb == 1 and N1 != 'X':
                                Jogador2 = 1
                                break
                            elif Numb == 2 and N2 != 'X':
                                Jogador2 = 2
                                break
                            elif Numb == 3 and N4 != 'X':
                                Jogador2 = 4
                                break
                            elif Numb == 4 and N6 != 'X':
                                Jogador2 = 6
                                break
                            elif Numb == 5 and N8 != 'X':
                                Jogador2 = 8
                                break
                            elif Numb == 6 and N9 != 'X':
                                Jogador2 = 9
                                break
                            else:
                                break
                        
                    elif ((N2 == 'X' and N6 == 'X' and N3 == 3 and N1 == 1 and N9 == 9) or (N2 == 'X' and N4 == 'X' and N1 == 1 and N7 == 7 and N3 == 3) or (N8 == 'X' and N4 == 'X' and N7 == 7 and N1 == 1 and N9 == 9) or (N8 == 'X' and N6 == 'X' and N7 == 7 and N3 == 3 and N9 == 9)):
                        
                        Numb = random.randint(1,3)
                        if N2 == 'X' and N6 == 'X' and N3 == 3 and N1 == 1 and N9 == 9:
                            if Numb == 1:
                                Jogador2 = 1
                            elif Numb == 2:
                                Jogador2 == 3
                            else:
                                Jogador2 == 7
                        elif N2 == 'X' and N4 == 'X' and N1 == 1 and N7 == 7 and N3 == 3:
                            if Numb == 1:
                                Jogador2 = 1
                            elif Numb == 2:
                                Jogador2 == 3
                            else:
                                Jogador2 == 9
                        elif N8 == 'X' and N4 == 'X' and N7 == 7 and N1 == 1 and N9 == 9:
                            if Numb == 1:
                                Jogador2 = 1
                            elif Numb == 2:
                                Jogador2 == 7
                            else:
                                Jogador2 == 9
                        elif N8 == 'X' and N6 == 'X' and N7 == 7 and N3 == 3 and N9 == 9:
                            if Numb == 1:
                                Jogador2 = 9
                            elif Numb == 2:
                                Jogador2 == 3
                            else:
                                Jogador2 == 7
                        
                    elif ((N1 == 1 and N2 == 'X' and N3 == 3) or (N2 == 'X' and N5 == 5 and N8 == 8) or (N1 == 1 and N4 == 'X' and N7 == 7) or (N4 == 'X' and N5 == 5 and N6 == 6) or (N2 == 2 and N5 == 5 and N8 == 'X')or (N7 == 7 and N8 == 'X' and N9 == 9) or (N4 == 4 and N5 == 5 and N6 == 'X') or (N3 == 3 and N6 == 'X' and N9 == 9)):
                        Numb = random.randint(1,2)
                        if N1 == 1 and N2 == 'X' and N3 == 3:
                            if Numb == 1:
                                Jogador2 = 1
                            else:
                                Jogador2 = 3
                        elif N2 == 'X' and N5 == 5 and N8 == 8:
                            if Numb == 1:
                                Jogador2 = 5
                            else:
                                Jogador2 = 8
                        elif N1 == 1 and N4 == 'X' and N7 == 7:
                            if Numb == 1:
                                Jogador2 = 1
                            else:
                                Jogador2 = 7
                        elif N4 == 'X' and N5 == 5 and N6 == 6:
                            if Numb == 1:
                                Jogador2 = 5
                            else:
                                Jogador2 = 6
                        elif N2 == 2 and N5 == 5 and N8 == 'X':
                            if Numb == 1:
                                Jogador2 = 2
                            else:
                                Jogador2 = 5
                        elif N7 == 7 and N8 == 'X' and N9 == 9:
                            if Numb == 1:
                                Jogador2 = 7
                            else:
                                Jogador2 = 9
                        elif N4 == 4 and N5 == 5 and N6 == 'X':
                            if Numb == 1:
                                Jogador2 = 4
                            else:
                                Jogador2 = 5
                        elif N3 == 3 and N6 == 'X' and N9 == 9:
                            if Numb == 1:
                                Jogador2 = 3
                            else:
                                Jogador2 = 9
                        
                    elif (N1 == 'X' or N2 == 'X' or N3 == 'X') and (N1 != 'X' or N2 != 'X' or N3 != 'X'):
                        Jogador2 = random.randint(1,3)

                    elif (N4 == 'X' or N5 == 'X' or N6 == 'X') and (N4 != 'X' or N5 != 'X' or N6 != 'X'):
                        Jogador2 = random.randint(4,6)

                    elif (N4 == 'X' or N5 == 'X' or N6 == 'X') and (N4 != 'X' or N5 != 'X' or N6 != 'X'):
                        Jogador2 = random.randint(7,9)

                    elif (N1 == 'X' or N5 == 'X' or N9 == 'X') and (N1 != 'X' or N5 != 'X' or N9 != 'X'):
                        Numb = random.randint(1,3)
                        if Numb == 1:
                            Jogador2 = 1
                        elif Numb == 2:
                            Jogador2 = 5
                        else:
                            Jogador2 = 9

                    elif (N3 == 'X' or N5 == 'X' or N7 == 'X') and (N3 != 'X' or N5 != 'X' or N7 != 'X'):
                        Numb = random.randint(1,3)
                        if Numb == 1:
                            Jogador2 = 3
                        elif Numb == 2:
                            Jogador2 = 5
                        else:
                            Jogador2 = 7

                    elif (N1 == 'X' or N4 == 'X' or N7 == 'X') and (N1 != 'X' or N4 != 'X' or N7 != 'X'):
                        Numb = random.randint(1,3)
                        if Numb == 1:
                            Jogador2 = 1
                        elif Numb == 2:
                            Jogador2 = 4
                        else:
                            Jogador2 = 7

                    elif (N2 == 'X' or N5 == 'X' or N8 == 'X') and (N2 != 'X' or N5 != 'X' or N8 != 'X'):
                        Numb = random.randint(1,3)
                        if Numb == 1:
                            Jogador2 = 2
                        elif Numb == 2:
                            Jogador2 = 5
                        else:
                            Jogador2 = 8

                    elif (N3 == 'X' or N6 == 'X' or N9 == 'X') and (N3 != 'X' or N6 != 'X' or N9 != 'X'):
                        Numb = random.randint(1,3)
                        if Numb == 1:
                            Jogador2 = 3
                        elif Numb == 2:
                            Jogador2 = 6
                        else:
                            Jogador2 = 9
                    else:
                        Jogador2 = random.randint(1,9)


                    if Jogador2 == N1 and N1 == 1:
                        N1 = 'O'
                        break
                    elif Jogador2 == N2 and N2 == 2:
                        N2 = 'O'
                        break
                    elif Jogador2 == N3 and N3 == 3:
                        N3 = 'O'
                        break
                    elif Jogador2 == N4 and N4 == 4:
                        N4 = 'O'
                        break
                    elif Jogador2 == N5 and N5 == 5:
                        N5 = 'O'
                        break
                    elif Jogador2 == N6 and N6 == 6:
                        N6 = 'O'
                        break  
                    elif Jogador2 == N7 and N7 == 7:
                        N7 = 'O'
                        break
                    elif Jogador2 == N8 and N8 == 8:
                        N8 = 'O'
                        break
                    elif Jogador2 == N9 and N9 == 9:
                        N9 = 'O'
                        break


                print(f'\nRobo escolheu a posição {Jogador2}')
                time.sleep(3)

                os.system('cls')

                Placar = f'* Placar *\nVocê: {Placar1}\nRobo: {Placar2}\n\n'
                Layout = f' {N1}  |  {N2}  |  {N3} \n----------------\n {N4}  |  {N5}  |  {N6} \n----------------\n {N7}  |  {N8}  |  {N9} \n'

                print(Placar)
                print(Layout)

                if (N1 == 'X' and N2 == 'X' and N3 == 'X') or (N4 == 'X' and N5 == 'X' and N6 == 'X') or (N7 == 'X' and N8 == 'X' and N9 == 'X') or (N1 == 'X' and N4 == 'X' and N7 == 'X') or (N2 == 'X' and N5 == 'X' and N8 == 'X') or (N3 == 'X' and N6 == 'X' and N9 == 'X') or (N1 == 'X' and N5 == 'X' and N9 == 'X') or (N3 == 'X' and N5 == 'X' and N7 == 'X'):
                    print('\n\n* Parabens *\nVocê venceu!')
                    Placar1 += 1
                    
                    Voltar = int(input('\nDigite "1" para voltar\nR: '))
                    while Voltar != 1:
                        Voltar = int(input('Opção Invalida!\nDigite "1" para voltar\nR: '))

                    break
                    
                if (N1 == 'O' and N2 == 'O' and N3 == 'O') or (N4 == 'O' and N5 == 'O' and N6 == 'O') or (N7 == 'O' and N8 == 'O' and N9 == 'O') or (N1 == 'O' and N4 == 'O' and N7 == 'O') or (N2 == 'O' and N5 == 'O' and N8 == 'O') or (N3 == 'O' and N6 == 'O' and N9 == 'O') or (N1 == 'O' and N5 == 'O' and N9 == 'O') or (N3 == 'O' and N5 == 'O' and N7 == 'O'):
                    print('\n\n* Que azar! *\nRobo venceu!')
                    Placar2 += 1
                    
                    Voltar = int(input('\nDigite "1" para voltar\nR: '))
                    while Voltar != 1:
                        Voltar = int(input('Opção Invalida!\nDigite "1" para voltar\nR: '))

                    break

                if N1 != 1 and N2 != 2 and N3 != 3 and N4 != 4 and N5 != 5 and N6 != 6 and N7 != 7 and N8 != 8 and N9 != 9:
                    print('\nJogo empatado!')

                    Voltar = int(input('\nDigite "1" para voltar\nR: '))
                    while Voltar != 1:
                        Voltar = int(input('\nOpção Invalida!\nDigite "1" para voltar\nR: '))

                    break
    

def Jogar_Amigo():
    Placar1 = 0
    Placar2 = 0

    while True:
        os.system('cls')
        N1 = 1
        N2 = 2
        N3 = 3
        N4 = 4
        N5 = 5
        N6 = 6
        N7 = 7
        N8 = 8
        N9 = 9

        Placar = f'* Placar *\nJ1: {Placar1}\nJ2: {Placar2}\n\n'
        Layout = f' {N1}  |  {N2}  |  {N3} \n----------------\n {N4}  |  {N5}  |  {N6} \n----------------\n {N7}  |  {N8}  |  {N9} \n'

        print(Placar)
        print(Layout)

        Continuar = int(input('\nIniciar jogo:\n1- Sim\n2- Não\nR: '))
        while Continuar != 1 and Continuar != 2:
            Continuar = int(input('\nOpção Invalida!\nIniciar jogo:\n1- Sim\n2- Não\nR: '))

        if Continuar == 2:
            break

        while True: 
            
            while True:
                
                os.system('cls')

                Placar = f'* Placar *\nJ1: {Placar1}\nJ2: {Placar2}\n\n'
                Layout = f' {N1}  |  {N2}  |  {N3} \n----------------\n {N4}  |  {N5}  |  {N6} \n----------------\n {N7}  |  {N8}  |  {N9} \n'

                print(Placar)
                print(Layout)

                Jogador1 = int(input('\nVez do jogador NUMERO UM\nR: '))
                while Jogador1 > 9 and Jogador1 < 1:
                    Jogador1 = int(input('\nOpção Invalida! Digite um numero de 1 a 9\nVez do jogador NUMERO UM\nR: '))

                if Jogador1 == N1 and N1 == 1:
                    N1 = 'X'
                    break
                elif Jogador1 == N2 and N2 == 2:
                    N2 = 'X'
                    break
                elif Jogador1 == N3 and N3 == 3:
                    N3 = 'X'
                    break
                elif Jogador1 == N4 and N4 == 4:
                    N4 = 'X'
                    break
                elif Jogador1 == N5 and N5 == 5:
                    N5 = 'X'
                    break
                elif Jogador1 == N6 and N6 == 6:
                    N6 = 'X'
                    break
                elif Jogador1 == N7 and N7 == 7:
                    N7 = 'X'
                    break
                elif Jogador1 == N8 and N8 == 8:
                    N8 = 'X'
                    break
                elif Jogador1 == N9 and N9 == 9:
                    N9 = 'X'
                    break
                else:
                    Voltar = int(input('\nNão é possivel selecionar uma possição já utilizada!\nDigite "1" para voltar\nR: '))
                    while Voltar != 1:
                        Voltar = int(input('\nOpção Invalida!\nDigite "1" para voltar\nR: '))

            os.system('cls')

            Placar = f'* Placar *\nJ1: {Placar1}\nJ2: {Placar2}\n\n'
            Layout = f' {N1}  |  {N2}  |  {N3} \n----------------\n {N4}  |  {N5}  |  {N6} \n----------------\n {N7}  |  {N8}  |  {N9} \n'

            print(Placar)
            print(Layout)

            if (N1 == 'X' and N2 == 'X' and N3 == 'X') or (N4 == 'X' and N5 == 'X' and N6 == 'X') or (N7 == 'X' and N8 == 'X' and N9 == 'X') or (N1 == 'X' and N4 == 'X' and N7 == 'X') or (N2 == 'X' and N5 == 'X' and N8 == 'X') or (N3 == 'X' and N6 == 'X' and N9 == 'X') or (N1 == 'X' and N5 == 'X' and N9 == 'X') or (N3 == 'X' and N5 == 'X' and N7 == 'X'):
                print('\n\n* Parabens *\nJogador 1 venceu!')
                Placar1 += 1
                
                Voltar = int(input('\nDigite "1" para voltar\nR: '))
                while Voltar != 1:
                    Voltar = int(input('Opção Invalida!\nDigite "1" para voltar\nR: '))

                break
                
            if (N1 == 'O' and N2 == 'O' and N3 == 'O') or (N4 == 'O' and N5 == 'O' and N6 == 'O') or (N7 == 'O' and N8 == 'O' and N9 == 'O') or (N1 == 'O' and N4 == 'O' and N7 == 'O') or (N2 == 'O' and N5 == 'O' and N8 == 'O') or (N3 == 'O' and N6 == 'O' and N9 == 'O') or (N1 == 'O' and N5 == 'O' and N9 == 'O') or (N3 == 'O' and N5 == 'O' and N7 == 'O'):
                print('\n\n* Parabens *\nJogador 2 venceu!')
                Placar2 += 1
                
                Voltar = int(input('\nDigite "1" para voltar\nR: '))
                while Voltar != 1:
                    Voltar = int(input('\nOpção Invalida!\nDigite "1" para voltar\nR: '))

                break

            if N1 != 1 and N2 != 2 and N3 != 3 and N4 != 4 and N5 != 5 and N6 != 6 and N7 != 7 and N8 != 8 and N9 != 9:
                print('\nJogo empatado!')

                Voltar = int(input('\nDigite "1" para voltar\nR: '))
                while Voltar != 1:
                    Voltar = int(input('\nOpção Invalida!\nDigite "1" para voltar\nR: '))

                break



            while True:
                Jogador2 = int(input('\nVez do jogador NUMERO DOIS\nR: '))
                while Jogador2 > 9 and Jogador2 < 1:
                    Jogador2 = int(input('\nOpção Invalida! Digite um numero de 1 a 9\nVez do jogador NUMERO DOIS\nR: '))
        
                if Jogador2 == N1 and N1 == 1:
                    N1 = 'O'
                    break
                elif Jogador2 == N2 and N2 == 2:
                    N2 = 'O'
                    break
                elif Jogador2 == N3 and N3 == 3:
                    N3 = 'O'
                    break
                elif Jogador2 == N4 and N4 == 4:
                    N4 = 'O'
                    break
                elif Jogador2 == N5 and N5 == 5:
                    N5 = 'O'
                    break
                elif Jogador2 == N6 and N6 == 6:
                    N6 = 'O'
                    break
                elif Jogador2 == N7 and N7 == 7:
                    N7 = 'O'
                    break
                elif Jogador2 == N8 and N8 == 8:
                    N8 = 'O'
                    break
                elif Jogador2 == N9 and N9 == 9:
                    N9 = 'O'
                    break
                else:
                    Voltar = int(input('\nNão é possivel selecionar uma possição já utilizada!\nDigite "1" para voltar\nR: '))
                    while Voltar != 1:
                        Voltar = int(input('\nOpção Invalida!\nDigite "1" para voltar\nR: '))

            os.system('cls')

            Placar = f'* Placar *\nJ1: {Placar1}\nJ2: {Placar2}\n\n'
            Layout = f' {N1}  |  {N2}  |  {N3} \n----------------\n {N4}  |  {N5}  |  {N6} \n----------------\n {N7}  |  {N8}  |  {N9} \n'

            print(Placar)
            print(Layout)

            if (N1 == 'X' and N2 == 'X' and N3 == 'X') or (N4 == 'X' and N5 == 'X' and N6 == 'X') or (N7 == 'X' and N8 == 'X' and N9 == 'X') or (N1 == 'X' and N4 == 'X' and N7 == 'X') or (N2 == 'X' and N5 == 'X' and N8 == 'X') or (N3 == 'X' and N6 == 'X' and N9 == 'X') or (N1 == 'X' and N5 == 'X' and N9 == 'X') or (N3 == 'X' and N5 == 'X' and N7 == 'X'):
                print('\n\n* Parabens *\nJogador 1 venceu!')
                Placar1 += 1
                
                Voltar = int(input('\nDigite "1" para voltar\nR: '))
                while Voltar != 1:
                    Voltar = int(input('Opção Invalida!\nDigite "1" para voltar\nR: '))

                break
                
            if (N1 == 'O' and N2 == 'O' and N3 == 'O') or (N4 == 'O' and N5 == 'O' and N6 == 'O') or (N7 == 'O' and N8 == 'O' and N9 == 'O') or (N1 == 'O' and N4 == 'O' and N7 == 'O') or (N2 == 'O' and N5 == 'O' and N8 == 'O') or (N3 == 'O' and N6 == 'O' and N9 == 'O') or (N1 == 'O' and N5 == 'O' and N9 == 'O') or (N3 == 'O' and N5 == 'O' and N7 == 'O'):
                print('\n\n* Parabens *\nJogador 2 venceu!')
                Placar2 += 1
                
                Voltar = int(input('\nDigite "1" para voltar\nR: '))
                while Voltar != 1:
                    Voltar = int(input('Opção Invalida!\nDigite "1" para voltar\nR: '))

                break

            if N1 != 1 and N2 != 2 and N3 != 3 and N4 != 4 and N5 != 5 and N6 != 6 and N7 != 7 and N8 != 8 and N9 != 9:
                print('\nJogo empatado!')

                Voltar = int(input('\nDigite "1" para voltar\nR: '))
                while Voltar != 1:
                    Voltar = int(input('\nOpção Invalida!\nDigite "1" para voltar\nR: '))

                break


def Main():
    while True:
        os.system('cls')
        Menu = int(input('\n* Menu Jogo da Velha *\n1- Jogar sozinho\n2- Jogar com um amigo\n3- Sair\nR: '))
        
        if Menu == 3:
            print('\nPrograma encerrado!')
            break
        elif Menu == 1:
            os.system('cls')
            Dificuldade = int(input('\nSelecione a dificuldade do jogo\n1- Facil\n2- Medio\n3- Dificil\nR: '))
            while Dificuldade > 3 and Dificuldade < 1:
                Dificuldade = int(input('\nValor invalido!\nSelecione a dificuldade do jogo\n1- Facil\n2- Medio\n3- Dificil\nR: '))

            Jogar_Sozinho(Dificuldade)
            print('\nJogo encerrado!')
            Voltar = int(input('\nDigite "1" para voltar\nR: '))
            while Voltar != 1:
                Voltar = int(input('Opção Invalida!\nDigite "1" para voltar\nR: '))

        elif Menu == 2:
            os.system('cls')
            Jogar_Amigo()
            print('\nJogo encerrado!')
            Voltar = int(input('\nDigite "1" para voltar\nR: '))
            while Voltar != 1:
                Voltar = int(input('Opção Invalida!\nDigite "1" para voltar\nR: '))

        else:
            os.system('cls')
            print('\nOpção Invalida!')

            Voltar = int(input('\nDigite "1" para voltar\nR: '))
            while Voltar != 1:
                Voltar = int(input('Opção Invalida!\nDigite "1" para voltar\nR: '))


Main()