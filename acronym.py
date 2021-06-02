
def generate_acronym():
    full_meaning = input('Enter meaning to get acronym: ')
    split_meaning = full_meaning.split(' ')
    acronym = ''

    for i in split_meaning:
        acronym += i[0]

    print(acronym.upper(), sep='')






