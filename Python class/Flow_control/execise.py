from typing import Final

# Superhero attack power
IRON_MAN_POWER: Final = 300
CAPTAIN_AMERICA_POWER: Final = 295
THOR_POWER: Final = 300
DOCTOR_STRANGE_POWER: Final = 400

# Villain Power
thanos_life = 1600

# Attack pairs
pair_1 = 1
pair_2 = 2
pair_3 = 3
pair_4 = 4

# Helper variables
MOTIVATION = "The fate of humanity depends on our superheroes,\nchoose your pairs wisely. Avengers assemble! "
WIN: Final = "Our heroes have saved the planet"
LOSE: Final = "Our heroes don loose guard"

attack_count = 0

print(MOTIVATION)
while True:
    if thanos_life <= 0 and attack_count <= 3:  # Win
        print(WIN)
        break
    elif attack_count > 3:  # Lose
        print(LOSE)
        break

    attack_pair = int(input("attack with >> "))

    if attack_pair == pair_1:
        print("Thor and Captain America on the attack")
        thanos_life = thanos_life - THOR_POWER - CAPTAIN_AMERICA_POWER
    elif attack_pair == pair_2:
        print("Iron man and Doctor Strange on the attack")
        thanos_life = thanos_life - IRON_MAN_POWER - DOCTOR_STRANGE_POWER
    elif attack_pair == pair_3:
        print("Iron man and Captain America on the attack")
        thanos_life = thanos_life - IRON_MAN_POWER - CAPTAIN_AMERICA_POWER
    elif attack_pair == pair_4:
        print("Thor and Doctor Strange on the attack")
        thanos_life = thanos_life - THOR_POWER - DOCTOR_STRANGE_POWER

    attack_count += 1

a = 3
print(a)
a = "Hi"
print(a)