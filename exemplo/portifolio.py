class Pessoa: 
    def __init__ (self, email):
        self.email = email
        
def login(self):
    print(f'{p2.nome} está fazendo login com o email {p2.email}')
    
class Estudante(Pessoa):
    def __init__(self, email, nome):
        super().__init__(email, nome)
        self.nome = nome
        
class Professor(Pessoa):
    def __init__(self, email, nome, materia):
        super().__init__(email, nome, materia)
        self.nome = nome
        self.materia = materia 
        
p2 = Professor
p2.email = 'Luisa@gmail.com'
p2.nome = 'Luisa'
p2.materia ='Artes'
print(f'A {p2.nome} professora de {p2.materia}, está fazendo login com o email:{p2.email}')

e1 = Estudante
e1.email = 'maria@gmail.com'
e1.nome = 'maria'
print(f'A aluna {e1.nome} está fazendo login com o email:{e1.email}')





