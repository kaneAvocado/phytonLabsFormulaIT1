import json


FILENAME = "input.json"
def task() -> float:
    total_data=0

    with open(FILENAME, 'r') as file:
        data = json.load(file)

    for item in data:
        if "score" in item and "weight" in item:
            score = item["score"]
            weight = item["weight"]
            total_data += score * weight
    return round(total_data, 3)


print(task())
