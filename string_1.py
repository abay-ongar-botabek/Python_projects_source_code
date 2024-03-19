def ulttyq_qurama(firstName, lastName, **kwargs):
    kwargs['first_name'] = firstName
    kwargs['last_name'] = lastName
    return kwargs

player_profile = ulttyq_qurama('Kyle', 'Waker', club = 'MC', playerNumber = 3, apps = 34)

print(player_profile)