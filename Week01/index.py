with open("aoc_input.txt", "r") as outfile:
    elf_input=outfile.read()
elf_fruit = elf_input.split("\n\n")

elf_sums = []
for fruit_calories in elf_fruit:
    elf_fruit = [int(item) for item in fruit_calories.split("\n")]
    elf_sum = sum(fruit_calories)
    elf_sums.append(elf_sum)

elf_sums.sort()

print(max(elf_sums)) # Part 1
print(sum(elf_sums[-3:])) # Part 2
