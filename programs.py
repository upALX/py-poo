# Criar duas classes [filme e serie]com atributos e métodos para seus conteúdos

#Criar classe generalista para aplicar herança
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

# Criar classe filme deve ter os atributos nome do filme, ano, duração. Aplicar herança

class Movie(Midia):

    def __init__(self, name_midia, year_launch, time):
        super().__init__(name_midia, year_launch)
        self.time = time

    def show_movie(self):
        print(f'Filme: {self._name} \n'
              f'Ano: {self.year}\n'
              f'Duração: {self.time}\n'
              f'Número de likes: {self._likes_number}')

#Crie a classe das séries com nome, ano e temporada e aplicar herança

class Serie(Midia):

    def __init__(self, name_midia, year_launch, numbers_season):
        super().__init__(name_midia, year_launch)
        self.seasons = numbers_season

    def show_series(self):
        print(f'Filme: {self._name} \n'
              f'Ano: {self.year}\n'
              f'Temporadas: {self.seasons}\n'
              f'Número de likes: {self._likes_number}')

#Settar as informações
vingadores = Movie('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
vingadores.set_likes()
vingadores.set_likes()
vingadores.set_likes()

atlanta.set_likes()
atlanta.set_likes()

#Chamar o programa
print(f'Nome: {vingadores._name} - Likes: {vingadores._likes_number}')
print(f'Nome: {atlanta._name} - Likes: {atlanta._likes_number}')