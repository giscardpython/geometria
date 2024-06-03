# Crie um programa que o usuário possa escolher se deseja saber a área de um círculo, de um triângulo ou de um trapézio.

def calcular_circulo(pi, raio):
    area = pi * (raio * raio)
    return area

def calcular_triangulo(base, altura):
    area_triangulo = (base * altura) / 2
    return area_triangulo

def calcular_trapezio(altura, base_menor, base_maior):
    area_trapezio = (altura * (base_menor + base_maior) / 2)
    return area_trapezio

escolha = 1
opcao1 = 0

while escolha > 0:
    print ("\nQual área desejas saber? \n")
    print('1 - Área do Círculo')
    print('2 - Área do Triângulo')
    print('3 - Área do Trapézio')
    print('4 - Sair do programa')

    opcao1 = int(input('\nEscolha a opção desejada (1 a 4):\n'))
    
    match opcao1:
        case 1:
            pi = int(input('Informe o pi do círculo: '))
            raio = int(input('Informe o raio do círculo: '))

            print(f'Área do Círculo:  {calcular_circulo(pi, raio)}')
 
        case 2:
            base = int(input('Informe a base do retângulo: '))
            altura = int(input('Informe a altura do retângulo: '))

            print(f'Área do Triângulo:  {calcular_triangulo(base, altura)}')
 
        case 3:
            altura = int(input('Informe a altura do trapézio: '))
            base_menor = int(input('Informe a base menor do trapézio: '))
            base_maior = int(input('Informe a base maior do trapézio: '))
      
            print(f'Área do Trapézio:  {calcular_trapezio(altura, base_menor, base_maior)}')

        case 4:
            escolha = 0
            break    

        case _:
            print('Opção inváida! Digite uma opção de 1 a 7')
            continue      