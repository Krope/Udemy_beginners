
def display_facts(facts):
    """Display facts"""

    for fact in facts:
        print('{}: {}'.format(fact, facts[fact]))
    print()

facts = {
    'Jeff': ' Is afraid of clowns',
    'David': 'Plays the piano',
    'Jason': 'Can fly an airplane'
}

display_facts(facts)

facts['Jeff'] = 'Is afraid of heights.'
facts['Jill'] = 'Can hula dance.'

display_facts(facts)
