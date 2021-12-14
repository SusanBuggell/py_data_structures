"""Functions to parse a file containing student data."""


def all_houses(filename):
    """Return a set of all house names in the given file.

    For example:
      >>> unique_houses('cohort_data.txt')
      {"Dumbledore's Army", 'Gryffindor', ..., 'Slytherin'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """

    houses = set()

    # TODO: replace this with your code

    str_cohort_data=open(filename)
    for wiz in str_cohort_data:
        wiz = wiz.split('|')
        if wiz[2] != '':
          houses.add(wiz[2])
    str_cohort_data.close()
    return houses


def students_by_cohort(filename, cohort='All'):
    """Return a list of students' full names by cohort.

    Names are sorted in alphabetical order. If a cohort isn't
    given, return a list of all students. For example:
      >>> students_by_cohort('cohort_data.txt')
      ['Adrian Pucey', 'Alicia Spinnet', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Fall 2015')
      ['Angelina Johnson', 'Cho Chang', ..., 'Terence Higgs', 'Theodore Nott']

      >>> students_by_cohort('cohort_data.txt', cohort='Winter 2016')
      ['Adrian Pucey', 'Andrew Kirke', ..., 'Roger Davies', 'Susan Bones']

      >>> students_by_cohort('cohort_data.txt', cohort='Spring 2016')
`      ['Cormac McLaggen', 'Demelza Robins', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Summer 2016')
      ['Alicia Spinnet', 'Dean Thomas', ..., 'Terry Boot', 'Vincent Crabbe']

    Arguments:
      - filename (str): the path to a data file
      - cohort (str): optional, the name of a cohort

    Return:
      - list[list]: a list of lists
    """

    students = []

    # TODO: replace this with your code
    str_cohort_data=open(filename)
    for wiz in str_cohort_data:
        wiz=wiz.rstrip()
        wiz=wiz.split('|')
        # print(f'wiz: {wiz}')
        # print(f'wiz0:{wiz[0]}, wiz1:{wiz[1]}, wiz2:{wiz[2]}, wiz3:{wiz[3]}, wiz4:{wiz[4]}')
        if wiz[4] != 'I' and wiz[4] != 'G':
          if cohort == "All" or wiz[4] == f'{cohort}':
            students.append(f'{wiz[0]} {wiz[1]}')
    str_cohort_data.close()
    return sorted(students)


def all_names_by_house(filename):
    """Return a list that contains rosters for all houses, ghosts, instructors.

    Rosters appear in this order:
    - Dumbledore's Army
    - Gryffindor
    - Hufflepuff
    - Ravenclaw
    - Slytherin
    - Ghosts
    - Instructors

    Each roster is a list of names sorted in alphabetical order.

    For example:
      >>> rosters = hogwarts_by_house('cohort_data.txt')
      >>> len(rosters)
      7

      >>> rosters[0]
      ['Alicia Spinnet', ..., 'Theodore Nott']
      >>> rosters[-1]
      ['Filius Flitwick', ..., 'Severus Snape']

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[list]: a list of lists
    """

    dumbledores_army = []
    gryffindor = []
    hufflepuff = []
    ravenclaw = []
    slytherin = []
    ghosts = []
    instructors = []

    # TODO: replace this with your code
    str_cohort_data=open(filename)
    for wiz in str_cohort_data:
        wiz=wiz.rstrip()
        wiz=wiz.split('|')
        # print(f'wiz: {wiz}')
        # print(f'wiz0:{wiz[0]}, wiz1:{wiz[1]}, wiz2:{wiz[2]}, wiz3:{wiz[3]}, wiz4:{wiz[4]}')
        if wiz[2] == "Dumbledore's Army":
          dumbledores_army.append(f'{wiz[0]} {wiz[1]}')
        elif wiz[2] == "Gryffindor":
          gryffindor.append(f'{wiz[0]} {wiz[1]}')
        elif wiz[2] == "Hufflepuff":
          hufflepuff.append(f'{wiz[0]} {wiz[1]}')
        elif wiz[2] == "Ravenclaw":
          ravenclaw.append(f'{wiz[0]} {wiz[1]}')
        elif wiz[2] == "Slytherin":
          slytherin.append(f'{wiz[0]} {wiz[1]}')
        elif wiz[4] == "G":
          ghosts.append(f'{wiz[0]} {wiz[1]}')
        elif wiz[4] == "I":
          instructors.append(f'{wiz[0]} {wiz[1]}')

    str_cohort_data.close()
    return [sorted(dumbledores_army), sorted(gryffindor), sorted(hufflepuff), sorted(ravenclaw), sorted(slytherin), sorted(ghosts), sorted(instructors) ]


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (full_name, house, advisor, cohort)

    Iterate over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)

    For example:
      >>> all_student_data('cohort_data.txt')
      [('Harry Potter', 'Gryffindor', 'McGonagall', 'Fall 2015'), ..., ]

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[tuple]: a list of tuples
    """

    all_data = []

    # TODO: replace this with your code
    str_cohort_data=open(filename)
    for wiz in str_cohort_data:
        wiz=wiz.rstrip()
        wiz=wiz.split('|')
        wiz=(f'{wiz[0]} {wiz[1]}', f'{wiz[2]}', f'{wiz[3]}', f'{wiz[4]}')
        all_data.append(wiz)
    str_cohort_data.close()
    return all_data


def get_cohort_for(filename, name):
    """Given someone's name, return the cohort they belong to.

    Return None if the person doesn't exist. For example:
      >>> get_cohort_for('cohort_data.txt', 'Harry Potter')
      'Fall 2015'

      >>> get_cohort_for('cohort_data.txt', 'Hannah Abbott')
      'Winter 2016'

      >>> get_cohort_for('cohort_data.txt', 'Someone else')
      None

    Arguments:
      - filename (str): the path to a data file
      - name (str): a person's full name

    Return:
      - str: the person's cohort or None
    """

    # TODO: replace this with your code
    str_cohort_data=open(filename)
    for wiz in str_cohort_data:
        wiz=wiz.rstrip()
        wiz=wiz.split('|')
        if name in f'{wiz[0]} {wiz[1]}': 
            wiz=wiz[4]
            return wiz  
    str_cohort_data.close()


def find_duped_last_names(filename):
    """Return a set of duplicated last names that exist in the data.

    For example:
      >>> find_name_duplicates('cohort_data.txt')
      {'Creevey', 'Weasley', 'Patil'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """

    # TODO: replace this with your code
    single_names=set()
    dupe_names=set()

    str_cohort_data=open(filename)
    for wiz in str_cohort_data:
        wiz=wiz.rstrip()
        wiz=wiz.split('|')
        wiz=wiz[1]
        bef_len=len(single_names)
        # print(f'bef_len: {bef_len}')
        single_names.add(wiz)
        # print(f'single_names: {single_names}')
        aft_len=len(single_names)
        # print(f'aft_len: {aft_len}')
        if bef_len == aft_len:
          dupe_names.add(wiz)
          # print(f'dupe_names: {dupe_names}')
    str_cohort_data.close()
    return dupe_names

def get_housemates_for(filename, name):
    """Return a set of housemates for the given student.

    Given a student's name, return a list of their housemates. Housemates are
    students who belong to the same house and were in the same cohort as the
    given student.

    For example:
    >>> get_housemates_for('cohort_data.txt', 'Hermione Granger')
    {'Angelina Johnson', ..., 'Seamus Finnigan'}
    """

    # TODO: replace this with your code
    housemates = set()
    house=str()
    cohort=str()
    str_cohort_data=open(filename)
    for wiz in str_cohort_data:
        wiz=wiz.rstrip()
        wiz=wiz.split('|')
        if name in f'{wiz[0]} {wiz[1]}':
          house=wiz[2]
          # print(f'house: {house}')
          cohort=wiz[4]
          #  print(f'cohort: {cohort}')
    str_cohort_data.close()
    str_cohort_data=open(filename)
    for house_wiz in str_cohort_data:
        house_wiz=house_wiz.rstrip()
        house_wiz=house_wiz.split('|')
      # print('TEST')
        if name not in f'{house_wiz[0]} {house_wiz[1]}' and  house == f'{house_wiz[2]}' and cohort == f'{house_wiz[4]}':
          # house_wiz=f'{house_wiz[0]} {house_wiz[1]}, {house_wiz[2]}, {house_wiz[3]}, {house_wiz[4]}'
          # if house == f'{house_wiz[1]}' and cohort == f'{house_wiz[3]}':
            # print(f'{house_wiz[0]} {house_wiz[1]}')print('house_wiz: ',house_wiz)
          housemates.add(f'{house_wiz[0]} {house_wiz[1]}')
    #     # print(f'housemates_after: {housemates}')  
    
    # print(f'housemates: {housemates}')
    str_cohort_data.close()
    return housemates
    #   # if wiz[4] != 'I' and wiz[4] != 'G':
    #   #     if cohort == "All" or wiz[4] == f'{cohort}':
    #   #       students.append(f'{wiz[0]} {wiz[1]}')
##############################################################################
# END OF MAIN EXERCISE.  Yay!  You did it! You Rock!
#

if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')
