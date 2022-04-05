
# Essa vai ser a nossa Classe Mãe

class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome (self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self):
        return (self._nome, self.ano, self._likes, 'Likes')


# Colocamos a classe Mãe entre parenteses para que a nova classe herde as funcoes e da classe Mãe
# Também não podemos usar variaveis privadas com __, pois as classes filhas nao conseguiram acessar, por convenção entao usamos apenas 1 _, assim indicamos que nao devemos mexer, mas conseguimos herdar nas classes filhas

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        # essa função super() tras o init da classe mãe, trazendo os atributos e evitando duplicação e pontos de falha
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return (self._nome, self.ano, self.duracao, self._likes, 'Likes')
        

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)       
        self.temporadas = temporadas

    def __str__(self):
        return (self._nome, self.ano, self.temporadas, self._likes, 'Likes')
        

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]
    
    @property
    def listagem(self):
        return self._programas


    def __len__(self):
        return len(self._programas)






vingadores = Filme('vingadores', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme('Todo mundo em panico', 1999, 100)
demolidor = Serie('Demolidor', 2016, 2)


vingadores.dar_like()
atlanta.dar_like()
atlanta.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
demolidor.dar_like()
demolidor.dar_like()
demolidor.dar_like()

filme_e_series = [vingadores, atlanta, tmep, demolidor]

playlist_fds = Playlist('fim de semana', filme_e_series)

for programa in playlist_fds:
    print(programa)