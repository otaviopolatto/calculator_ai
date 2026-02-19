#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calculadora em Python
Suporta operações matemáticas básicas e avançadas
"""

import math


def exibir_menu():
    """Exibe o menu de operações disponíveis"""
    print("\n" + "="*50)
    print("           CALCULADORA PYTHON")
    print("="*50)
    print("\nOperações disponíveis:")
    print("  1. Adição (+)")
    print("  2. Subtração (-)")
    print("  3. Multiplicação (*)")
    print("  4. Divisão (/)")
    print("  5. Potenciação (^)")
    print("  6. Radiciação (raiz quadrada)")
    print("  7. Raiz cúbica")
    print("  8. Raiz n-ésima")
    print("  9. Módulo/Resto da divisão (%)")
    print(" 10. Logaritmo natural (ln)")
    print(" 11. Logaritmo na base 10 (log)")
    print(" 12. Seno (sin)")
    print(" 13. Cosseno (cos)")
    print(" 14. Tangente (tan)")
    print(" 15. Fatorial (!)")
    print("  0. Sair")
    print("="*50)


def obter_numero(mensagem="Digite um número: "):
    """Obtém um número válido do usuário"""
    while True:
        try:
            numero = float(input(mensagem))
            return numero
        except ValueError:
            print("Erro: Por favor, digite um número válido.")


def obter_numero_positivo(mensagem="Digite um número positivo: "):
    """Obtém um número positivo válido do usuário"""
    while True:
        try:
            numero = float(input(mensagem))
            if numero <= 0:
                print("Erro: O número deve ser positivo.")
                continue
            return numero
        except ValueError:
            print("Erro: Por favor, digite um número válido.")


def obter_numero_inteiro_positivo(mensagem="Digite um número inteiro positivo: "):
    """Obtém um número inteiro positivo válido do usuário"""
    while True:
        try:
            numero = int(input(mensagem))
            if numero < 0:
                print("Erro: O número deve ser positivo ou zero.")
                continue
            return numero
        except ValueError:
            print("Erro: Por favor, digite um número inteiro válido.")


def adicao():
    """Realiza a operação de adição"""
    print("\n--- ADIÇÃO ---")
    num1 = obter_numero("Digite o primeiro número: ")
    num2 = obter_numero("Digite o segundo número: ")
    resultado = num1 + num2
    print(f"\nResultado: {num1} + {num2} = {resultado}")
    return resultado


def subtracao():
    """Realiza a operação de subtração"""
    print("\n--- SUBTRAÇÃO ---")
    num1 = obter_numero("Digite o primeiro número: ")
    num2 = obter_numero("Digite o segundo número: ")
    resultado = num1 - num2
    print(f"\nResultado: {num1} - {num2} = {resultado}")
    return resultado


def multiplicacao():
    """Realiza a operação de multiplicação"""
    print("\n--- MULTIPLICAÇÃO ---")
    num1 = obter_numero("Digite o primeiro número: ")
    num2 = obter_numero("Digite o segundo número: ")
    resultado = num1 * num2
    print(f"\nResultado: {num1} × {num2} = {resultado}")
    return resultado


def divisao():
    """Realiza a operação de divisão"""
    print("\n--- DIVISÃO ---")
    num1 = obter_numero("Digite o dividendo: ")
    num2 = obter_numero("Digite o divisor: ")
    
    if num2 == 0:
        print("\nErro: Divisão por zero não é permitida!")
        return None
    
    resultado = num1 / num2
    print(f"\nResultado: {num1} ÷ {num2} = {resultado}")
    return resultado


def potenciacao():
    """Realiza a operação de potenciação"""
    print("\n--- POTENCIAÇÃO ---")
    base = obter_numero("Digite a base: ")
    expoente = obter_numero("Digite o expoente: ")
    resultado = base ** expoente
    print(f"\nResultado: {base} ^ {expoente} = {resultado}")
    return resultado


def raiz_quadrada():
    """Calcula a raiz quadrada"""
    print("\n--- RAIZ QUADRADA ---")
    numero = obter_numero_positivo("Digite o número: ")
    resultado = math.sqrt(numero)
    print(f"\nResultado: √{numero} = {resultado}")
    return resultado


def raiz_cubica():
    """Calcula a raiz cúbica"""
    print("\n--- RAIZ CÚBICA ---")
    numero = obter_numero("Digite o número: ")
    resultado = numero ** (1/3)
    print(f"\nResultado: ∛{numero} = {resultado}")
    return resultado


def raiz_nesima():
    """Calcula a raiz n-ésima"""
    print("\n--- RAIZ N-ÉSIMA ---")
    numero = obter_numero("Digite o número: ")
    indice = obter_numero_positivo("Digite o índice da raiz: ")
    resultado = numero ** (1/indice)
    print(f"\nResultado: {indice}√{numero} = {resultado}")
    return resultado


def modulo():
    """Calcula o resto da divisão (módulo)"""
    print("\n--- MÓDULO/RESTO DA DIVISÃO ---")
    num1 = obter_numero("Digite o primeiro número: ")
    num2 = obter_numero("Digite o segundo número: ")
    
    if num2 == 0:
        print("\nErro: Divisão por zero não é permitida!")
        return None
    
    resultado = num1 % num2
    print(f"\nResultado: {num1} % {num2} = {resultado}")
    return resultado


def logaritmo_natural():
    """Calcula o logaritmo natural"""
    print("\n--- LOGARITMO NATURAL (ln) ---")
    numero = obter_numero_positivo("Digite o número: ")
    resultado = math.log(numero)
    print(f"\nResultado: ln({numero}) = {resultado}")
    return resultado


def logaritmo_base10():
    """Calcula o logaritmo na base 10"""
    print("\n--- LOGARITMO NA BASE 10 (log) ---")
    numero = obter_numero_positivo("Digite o número: ")
    resultado = math.log10(numero)
    print(f"\nResultado: log({numero}) = {resultado}")
    return resultado


def seno():
    """Calcula o seno de um ângulo"""
    print("\n--- SENO ---")
    print("Nota: O ângulo deve ser em radianos")
    angulo = obter_numero("Digite o ângulo (em radianos): ")
    resultado = math.sin(angulo)
    print(f"\nResultado: sin({angulo}) = {resultado}")
    return resultado


def cosseno():
    """Calcula o cosseno de um ângulo"""
    print("\n--- COSSENO ---")
    print("Nota: O ângulo deve ser em radianos")
    angulo = obter_numero("Digite o ângulo (em radianos): ")
    resultado = math.cos(angulo)
    print(f"\nResultado: cos({angulo}) = {resultado}")
    return resultado


def tangente():
    """Calcula a tangente de um ângulo"""
    print("\n--- TANGENTE ---")
    print("Nota: O ângulo deve ser em radianos")
    angulo = obter_numero("Digite o ângulo (em radianos): ")
    resultado = math.tan(angulo)
    print(f"\nResultado: tan({angulo}) = {resultado}")
    return resultado


def fatorial():
    """Calcula o fatorial de um número"""
    print("\n--- FATORIAL ---")
    numero = obter_numero_inteiro_positivo("Digite um número inteiro não negativo: ")
    resultado = math.factorial(numero)
    print(f"\nResultado: {numero}! = {resultado}")
    return resultado


def main():
    """Função principal da calculadora"""
    print("\nBem-vindo à Calculadora Python!")
    
    while True:
        exibir_menu()
        
        try:
            opcao = input("\nEscolha uma operação (0-15): ").strip()
            
            if opcao == "0":
                print("\nObrigado por usar a Calculadora Python! Até logo!")
                break
            elif opcao == "1":
                adicao()
            elif opcao == "2":
                subtracao()
            elif opcao == "3":
                multiplicacao()
            elif opcao == "4":
                divisao()
            elif opcao == "5":
                potenciacao()
            elif opcao == "6":
                raiz_quadrada()
            elif opcao == "7":
                raiz_cubica()
            elif opcao == "8":
                raiz_nesima()
            elif opcao == "9":
                modulo()
            elif opcao == "10":
                logaritmo_natural()
            elif opcao == "11":
                logaritmo_base10()
            elif opcao == "12":
                seno()
            elif opcao == "13":
                cosseno()
            elif opcao == "14":
                tangente()
            elif opcao == "15":
                fatorial()
            else:
                print("\nOpção inválida! Por favor, escolha uma opção entre 0 e 15.")
            
            input("\nPressione Enter para continuar...")
            
        except KeyboardInterrupt:
            print("\n\nOperação cancelada pelo usuário.")
            print("Obrigado por usar a Calculadora Python! Até logo!")
            break
        except Exception as e:
            print(f"\nErro inesperado: {e}")
            input("\nPressione Enter para continuar...")


if __name__ == "__main__":
    main()
