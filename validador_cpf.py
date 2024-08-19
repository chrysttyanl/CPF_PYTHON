###################################################################################################
# Criar um gerador de CPF válido
# 1) Distribua os 9 primeiros dígitos em um quadro colocando os pesos 10, 9, 8, 7, 6, 5, 4, 3, 2 
# abaixo da esquerda para a direita, conforme representação abaixo:
# 1 	1 	1 	4 	4 	4 	7 	7 	7
# 10 	9 	8 	7 	6 	5 	4 	3 	2
# 2) Multiplique os valores de cada coluna:
# 1 	1 	1 	4 	4 	4 	7 	7 	7
# 10 	9 	8 	7 	6 	5 	4 	3 	2
# 10 	9 	8 	28 	24 	20 	28 	21 	14
# 3) Calcule o somatório dos resultados (10+9+...+21+14) = 162
# 4) O resultado obtido (162) será divido por 11. Considere como quociente apenas o valor inteiro,
# o resto da divisão será responsável pelo cálculo do primeiro dígito verificador.
# Resto = 162%11 = 8; se for menor que (<) 2 = 0; senão divisão inteiro menos o resto(11 - 8 = 3)
# Inteiro da divisão = 162//11 = 11
# O primeiro digito será 3
##################################################################################################
# 1) Distribua os 9 primeiros dígitos em um quadro colocando os pesos 11,10, 9, 8, 7, 6, 5, 4, 3, 2 
# abaixo da esquerda para a direita, conforme representação abaixo:
# 1 	1 	1 	4 	4 	4 	7 	7 	7 	3
# 11 	10 	9 	8 	7 	6 	5 	4 	3 	2
# 2) Multiplique os valores de cada coluna:
# 1 	1 	1 	4 	4 	4 	7 	7 	7 	3
# 11 	10 	9 	8 	7 	6 	5 	4 	3 	2
# 11 	10 	9 	32 	28 	24 	35 	28 	21 	6
# 3) Calcule o somatório dos resultados (11+10+...+21+6) = 204
# 4) O resultado obtido (204) será divido por 11. Considere como quociente apenas o valor inteiro,
# o resto da divisão será responsável pelo cálculo do primeiro dígito verificador.
# Resto = 204%11 = 6; se for menor que (<) 2 = 0; senão divisão inteiro menos o resto(11 - 6 = 5)
# Inteiro da divisão = 204//11 = 18
#################################################################################################

from re import sub
from os import system

def verificar_cpf(func):
    def verificando_numero(numero):
        cpf = sub(r'\D','',numero)
        cpf_informado = numero

        if cpf.isdigit() and len(cpf) == 11:
            cpf = cpf[:9]
            if len(cpf):
                cont = 10   
                soma = 0         
                for num in cpf[:9]:
                    num = int(num)            
                    soma += (num * cont)
                    cont -= 1
                resto = soma % 11
                cpf += str(11 - resto) if resto > 2 else str(0) 
                if len(cpf) == 10:
                    cont = 11   
                    soma = 0        
                    for num in cpf:
                        num = int(num)
                        soma += (num * cont)            
                        cont -= 1
                    resto = soma % 11
                    cpf += str(11 - resto) if resto > 2 else str(0)    
                    cpf = sub(r'(\d{3})(\d{3})(\d{3})(\d{2})', r'\1.\2.\3-\4', cpf)
                    cpf = (cpf, cpf_informado)
                return func(cpf)        
        raise ValueError()
    return verificando_numero  

@verificar_cpf
def cpf_verificado(numero):
    if numero[0] == numero[1]:
        cpf =f'cpf: {numero[0]} é válido!'
        return cpf             
    else:
        cpf = f'cpf: {numero[0]} não é válido!'
        return cpf   

def sair():
    check = input('Deseja sair? [S]air ou [C]ontinuar:')
    if check == 'C' or check == 'c':
        return ''
    return exit()

def app():
    while True:
        try:
            cpf = input('cpf: ')
            print(cpf_verificado(cpf)) 
            sair()
            system('cls')     
        except (ValueError, TypeError):
            print('Digite um cpf válido!')        
        except Exception as e:
            print(type(e).__name__)
################################################################################################
print(app())