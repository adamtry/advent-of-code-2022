import string

def part_one(rs_data):
    score = 0
    for rucksack in rs_data:
        next_rucksack = False
        compartment1 = rucksack[ 0 : len(rucksack)//2 ]
        compartment2 = rucksack[ len(rucksack)//2 : ]
        for component in compartment1:
            if component in compartment2:
                score += int(priority_dictionary[component])
                next_rucksack = True
            if next_rucksack:
                break
    print(score)

def part_two(rs_data):
    score = 0
    for i in range(0, len(rs_data), 3):
        next_rucksack_group = False
        rucksack_group = rs_data[i:i+3]
        for component in rucksack_group[0]:
            if component in rucksack_group[1] and component in rucksack_group[2]:
                score += priority_dictionary[component]
                next_rucksack_group = True
            if next_rucksack_group:
                break
    print(score)

if __name__ == "__main__":
    priority_dictionary = {}
    for i, letter in enumerate(string.ascii_lowercase):
        priority_dictionary[letter] = i + 1  # Start at 1
    for i, letter in enumerate(string.ascii_uppercase):
        priority_dictionary[letter] = i + 1 + 26

    with open("input.txt", "r") as outfile:
        rucksack_data: list[str] = outfile.read().strip().splitlines()

    part_one(rucksack_data)
    part_two(rucksack_data)
