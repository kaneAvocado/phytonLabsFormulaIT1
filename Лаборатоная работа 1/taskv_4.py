users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
usersDict = {
    'Общее количество' : None, 'Уникальные посещения' : None
}

usersDict['Общее количество'] = len(users)
usersDict['Уникальные посещения'] = len(set(users))

print(usersDict)
# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
