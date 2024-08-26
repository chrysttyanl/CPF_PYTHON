from cpf import CPF

if __name__ == '__main__':
    cpf = CPF()
    gerador_de_CPF = cpf.gerador_de_CPF()
    validador_de_CPF = cpf.validador_de_CPF

    print(gerador_de_CPF)
    print(validador_de_CPF('374.574.558-25'))
