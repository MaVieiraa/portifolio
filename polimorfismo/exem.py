class Pessoa: 
    def __init__ (self, nome):
        self.nome = nome
        
def apresentar(self):
    print(f'Ola, meu nome é', self.nome)
    
class Estudante(Pessoa):
    def __init__(self, nome, matricula):
        super().__init__(nome)
        self.matricula = matricula
        
        def apresentar(self):
            print(f'Oi, eu sou a estutante',self.nome,'e minha matricula é', self.matricula)
        
class Professor(Pessoa):
    def __init__(self, nome, disciplina):
        super().__init__(nome)
        self.nome = disciplina
        
        def apresentar(self):
         print(f'Olá, meu nome é', self.nome, 'e eu sou professor de', self.disciplina)
        

