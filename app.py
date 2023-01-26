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


main_menu = Menu(name="Menu Principal", choices=content_type_list)
movies_menu = Menu(name="Films", choices=movies_type_list, parent=main_menu)
tvshows_menu = Menu(name="Séries", choices=tvshows_type_list, parent=main_menu)


def display_menu(item: object):
    print(f"{'#'*10} {item.name} {'#'*10}")
    for key, value in item.menu.items():
        print(f'{key}: {value}')

    if item.parent:
        print('R: Retour au menu précédent')
    print('Q: Quitter')

    user_choice = input('\nEntrez votre choix svp: ')
    available_options = [str(index) for index in range(1, len(item.menu) + 1)] + ['q']
    if item.parent:
        available_options.append('r')

    if user_choice not in available_options:
        print('Veuillez entrer une valeur valide svp!\n')
        display_menu(item=item)
    elif user_choice.lower() == 'r':
        display_menu(item.parent)
    elif user_choice.lower() == 'q':
        sys.exit(1)
    elif item.name == "main_menu" and user_choice == "1":
        print("toto")
        display_menu(movies_menu)
    elif item.name == "main_menu" and user_choice == "2":
        display_menu(tvshows_menu)


if __name__ == "__main__":
    display_menu(main_menu)
    # display_menu(movies_menu)
