import sys

# Movies
movies_action_list = ["Matrix", "Bad Boys", "L'arme fatale", "Bloodsport", "Rambo 3", "Terminator 2"]
movies_romance_list = ["N'oublie jamais", "Dirty Dancing", "Ghost", "Coupe de foudre à Notting Hill", "P.S: I love you"]
movies_history_list = ["Le roi Arthur", "La vie est belle", "La liste de Schindler", "Indigènes"]
movies_comedy_list = ["OSS 117", "Les trois frères", "La cité de la peur", "Mon beau-père et moi"]

# TV Shows
tvshows_action_list = ["Vikings", "24 heures chrono", "Game of thrones", "Sons of anarchy", "The boys"]
tvshows_humour_list = ["Friends", "How I met your mother", "Malcolm", "Kaamelott", "Seinfield"]
tvshows_police_list = ["Esprits criminels", "NCIS: Los Angeles", "Elementary", "Mentalist"]
tvshows_horror_list = ["American horror history", "Channel zero"]

movies_type_list = ["Comedy", "History", "Romance", "Action"]
tvshows_type_list = ["Horror", "Police", "Humour", "Action"]

# Content type
content_type_list = ["Movies", "TvShows"]


class Menu:
    def __init__(self, name: str, choices: list, parent: object = None) -> None:
        self.name = name
        self.choices = choices
        self.parent = parent

    @property
    def menu(self) -> dict:
        choices_dict = {}
        for index, item in enumerate(self.choices, 1):
            choices_dict[index] = item
        return choices_dict


main_menu = Menu(name="Main Menu", choices=content_type_list)
movies_menu = Menu(name="Movies", choices=movies_type_list, parent=main_menu)
tvshows_menu = Menu(name="TvShows", choices=tvshows_type_list, parent=main_menu)
for movie_type in movies_type_list:
    globals()[movie_type.lower()] = Menu(name=movie_type, choices=[f'movies_{movie_type}_list'])
for tvshow_type in tvshows_type_list:
    globals()[tvshow_type.lower()] = Menu(name=tvshow_type, choices=[f'tvshows_{tvshow_type}_list'])


def display_menu(item: object):
    user_choice = ''
    available_options = [str(index) for index in range(1, len(item.menu) + 1)] + ['q']
    if item.parent:
        available_options.append('r')

    while user_choice not in available_options:
        print(f"{'#'*10} {item.name} {'#'*10}")
        for key, value in item.menu.items():
            print(f'{key}: {value}')

        if item.parent:
            print('B: Back to the previous menu')
        print('Q: Quit')

        user_choice = input('\nEntrez votre choix svp: ')

    if user_choice.lower() == 'r':
        display_menu(item.parent)
    elif user_choice.lower() == 'q':
        sys.exit(1)
    elif item.name == "Main Menu" and user_choice == "1":
        display_menu(movies_menu)
    elif item.name == "Main Menu" and user_choice == "2":
        display_menu(tvshows_menu)
    else:
        print(f'{item.name.split("_")[0].lower()}_{item.menu[int(user_choice)].lower()}_list')
        display_menu(f'{item.name.split("_")[0].lower()}_{item.menu[int(user_choice)].lower()}_list')


if __name__ == "__main__":
    display_menu(main_menu)
