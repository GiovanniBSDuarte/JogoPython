from random import randint

enimiesList = []

def create_enemy():
    level = randint(1,50)

    newEnemy = {
        "name": f"Enemy #{level}",
        "level": level,
        "damege": 5 * level,
        "hp": 100* level,
    }

    enimiesList.append(newEnemy)
