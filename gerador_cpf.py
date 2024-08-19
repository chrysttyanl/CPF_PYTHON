import random, re

def gerador_cpf(func):
    def gerando_cpf():    
        cpf =''
        for _ in range(9):
            cpf += str(random.randrange(9))
        return func(cpf)
    return gerando_cpf

@gerador_cpf
def calcular_digito(numero):
    cpf = numero
    if len(cpf) <= 9:
        cont = 10   
        soma = 0         
        for num in cpf:
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
    return cpf_formatado(cpf) 

def cpf_formatado(numero):
    return re.sub(r'(\d{3})(\d{3})(\d{3})(\d{2})', r'\1.\2.\3-\4', numero)
    # return f'{numero[:3]}.{numero[3:6]}.{numero[6:9]}-{numero[9:]}' 

def app():
    cpf = ''
    print(f'CPF: {calcular_digito()}')
    # print(f'cpf: {cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}')
    # print('cpf: ' + re.sub(r'(\d{3})(\d{3})(\d{3})(\d{2})', r'\1.\2.\3-\4', cpf_gerado))    
################################################################################################
app()