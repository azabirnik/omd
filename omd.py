# Guido van Rossum <guido@python.org>
# Updates from Aleksei Zabirnik <azabirnik@gmail.com>

def step2_umbrella():
    print('Зонтик был большой и в бар зайти не получилось.')
    print('Так и ходила весь день трезвая и злая...')


def step2_no_umbrella():
    print('Пошел дождь, но в баре её ждал горячий глинтвейн.')
    print('Хорошо...')


def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


if __name__ == '__main__':
    step1()
