# A ideia é criar uma playlist de filmes e séries

# Criar classe generalista para aplicar herança
class Midia:

    def __init__(self, name_midia, year_launch):
        self._name = name_midia.title()
        self.year = year_launch
        self._likes_number = 0

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name

    def set_likes(self):
        self._likes_number += 1

    def __str__(self):
        return f'Filme: {self._name} \n' f'Ano: {self.year}\n' f'Temporadas: {self.year}\n' f'Número de likes: {self._likes_number}\n'


# Criar uma classe que mostre o tamanho da minha playlist e retorne os nomes
class Playlist:
    def __init__(self, name_playlist, playlists):
        self.name_playlist = name_playlist
        self.playlists = playlists

    @property
    def get_return_name_playlist(self):
        return self.name_playlist

    @property
    def return_number_midias(self):
        return len(self.playlists)


# Criar classe filme deve ter os atributos nome do filme, ano, duração. Aplicar herança

class Movie(Midia):

    def __init__(self, name_midia, year_launch, time):
        super().__init__(name_midia, year_launch)
        self.time = time

    def __str__(self):
        return f'Filme: {self._name} \n' f'Ano: {self.year}\n' f'Temporadas: {self.year}\n' f'Número de likes: {self._likes_number}\n'


# Crie a classe das séries com nome, ano e temporada e aplicar herança

class Serie(Midia):

    def __init__(self, name_midia, year_launch, numbers_season):
        super().__init__(name_midia, year_launch)
        self.seasons = numbers_season

    def __str__(self):
        return f'Filme: {self._name} \n' f'Ano: {self.year}\n' f'Temporadas: {self.seasons}\n' f'Número de likes: {self._likes_number}\n'


# Settar as informações
vingadores = Movie('vingadores - guerra infinita', 2018, 160)
vingadores.set_likes()
vingadores.set_likes()
vingadores.set_likes()

atlanta = Serie('atlanta', 2018, 2)
atlanta.set_likes()
atlanta.set_likes()



# Aplicar Polimorfismo no módulo - implementando playlist

list_midias = [vingadores, atlanta]

# Criar o objeto playlist
minha_playlist = Playlist('fim de semana', list_midias)


for midia in minha_playlist.playlists:
    print(midia)

print(f'Playlist: {minha_playlist.name_playlist}. \n Possui: {minha_playlist.return_number_midias} séries/filmes')