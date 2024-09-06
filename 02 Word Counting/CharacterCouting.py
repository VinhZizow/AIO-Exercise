# CHARACTER COUNTING
def character_count(word):
    character_statistic = {}

    for character in word:
        if character in character_statistic:
            character_statistic[character] += 1
        else:
            character_statistic[character] = 1
    return character_statistic


assert character_count("Baby") == {'B': 1, 'a': 1, 'b': 1, 'y': 1}

print(character_count('Sssmiles'))
print(character_count('Tonight I cel'))
