list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

playersCounter = (len(list_players) // 2)
firstTeam = list_players[0: playersCounter]
secondTeam = list_players[playersCounter: (playersCounter * 2)]

print(firstTeam,'\n',secondTeam)
