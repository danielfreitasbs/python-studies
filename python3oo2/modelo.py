class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    def dar_like(self):
        self._likes += 1

    @property
    def likes(self):
        return self._likes

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self):
        return f'Nome: {self.nome} - {self.ano} - {self.likes} likes'


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'Nome: {self.nome} - {self.ano} - {self.duracao} min - {self.likes} likes'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome: {self.nome} - {self.ano} - {self.temporadas} temporadas - {self.likes} likes'


class Playlist(list):
    def __init__(self, nome, programas):
        self.nome = nome
        super().__init__(programas)

    def tamanho(self):
        return len(self.programas)


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme('Todo mundo em pânico', 1999, 100)
demolidor = Serie('Demolidor', 2016, 2)

vingadores.dar_likes()
tmep.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()
atlanta.dar_likes()
atlanta.dar_likes()
atlanta.dar_likes()

filmes_e_series = [vingadores, atlanta, demolidor, tmep]

playlist_fim_de_semana = Playlist('Fim de semana', filmes_e_series)

print(f'Tamanho do playlist: {len(playlist_fim_de_semana)}')

for programa in playlist_fim_de_semana.programas:
    print(programa)

print(demolidor in playlist_fim_de_semana)
