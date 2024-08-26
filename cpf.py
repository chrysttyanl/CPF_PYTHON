from random import randint
from re import sub, compile

class CPF:
    '''
        Contém um gerador de CPF de automático e um validador de CPF para verificar um CPF
        válido.
    '''
    def __init__(self) -> None:
        _cpf_formatado: str
        _cpf: str 
        _cpf9: str
        _cpf10: str
        _cpf11: str
        _cpf_gerado: str
        _cpf_validado: str
        _validador: bool
        _digito: int
        _resto: int
        _contador: int

    def gerador_de_CPF(self) -> str:
        """
            Gerando o CPF automático.
        """
        self._contador = 1
        self._cpf_gerado = ''
        _cpf_gerado_formatado = CPF()._formatar_CPF
        while self._contador < 10:
            self._cpf_gerado += str(randint(0,9))
            self._contador += 1
        self._cpf_validado = CPF().validador_de_CPF(self._cpf_gerado)
        
        return CPF()._formatar_CPF(self._cpf_validado)
    
    def _validador(self, cpf, cpf_validador):
        if cpf != cpf_validador:
            return f'CPF: {cpf} não é válido'
        return f'CPF: {cpf} é válido'
    
    def _formatar_CPF(self,cpf) -> str:
        _formatando_cpf = sub(r'(\d{3})(\d{3})(\d{3})(\d{2})', r'\1.\2.\3-\4',cpf)
        return _formatando_cpf         

    def converter_para_cpf9(func) -> str:
        def convertendo_cpf9(self, cpf) -> str:
            try:
                self._cpf = cpf
                self._cpf9 = ''
                self._cpf_formatado = str(sub(r'\D','', self._cpf))                              
                if len(self._cpf_formatado) == 11 or len(self._cpf_formatado) == 9 :
                    self._cpf9 = self._cpf_formatado[:9]  
                    return func(self, self._cpf9)
                else:                                        
                    raise TypeError                
            # except TypeError as e:
            #     return "Digite um CPF com 11 digitos.", self._cpf
            except Exception as e:
                return f'{e}'
        return convertendo_cpf9             
 
    @converter_para_cpf9
    def validador_de_CPF(self, cpf9):
        ############### Descobrir o décimo(10º) digito ######################################
        self._cpf_formatado = CPF()._formatar_CPF
        self._cpf9 = cpf9
        self._cpf10 = ''
        self._cpf11 = ''
        self._contador = 10
        self._digito = 0    

        for soma in self._cpf9:
            self._digito += int(soma) * self._contador
            self._contador -= 1
        self._resto = self._digito % 11

        if self._resto > 0:
            self._cpf10 = self._cpf9 + str(11 - self._resto)
        else:
            self._cpf10 += '0'
        ############### Descobrir o décimo(11º) digito ######################################
        self._digito = 0
        self._contador = 11
        self._resto = 0
        
        for soma in self._cpf10:           
            self._digito += int(soma) * self._contador
            self._contador -= 1
        self._resto = self._digito % 11        

        if self._resto > 0:
            self._cpf11 = self._cpf_formatado(self._cpf10 + str(11 - self._resto))
            if len(self._cpf) == 9:
                self._cpf = self._cpf11
        else:
            self._cpf11 = self._cpf10 + '0'
            self._cpf11 = self._cpf_formatado(self._cpf11)
            if len(self._cpf) == 9:
                self._cpf = self._cpf11
              

        return CPF()._validador(self._cpf, self._cpf11)
        



    
        


############################################################################################
if __name__ == '__main__':
    gerando_cpf9 = CPF().gerador_de_CPF
    validador_cpf = CPF().validador_de_CPF    

    # print(gerando_cpf9())
    print(gerando_cpf9())
    # print(validador_cpf(gerando_cpf9()))
