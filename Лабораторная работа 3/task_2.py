def find_common_participants(firstGroup, secondGroup, separator=","):
    firstGroupSplit = firstGroup.split(separator)
    secondGroupSplit = secondGroup.split(separator)

    commonParticipants = set(firstGroupSplit) & set(secondGroupSplit)

    return sorted(commonParticipants)


# Пример использования:
participants_first_group = "Иванов,Петров,Сидоров"
participants_second_group = "Петров,Сидоров,Смирнов"

common_participants = find_common_participants(participants_first_group, participants_second_group)
print(common_participants)
