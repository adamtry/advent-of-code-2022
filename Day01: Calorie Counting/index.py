class Elf():
    def __init__(self, fruit_calories_list):
        self.fruit_calories_list = fruit_calories_list
    
    def get_total_calories(self):
        return sum(self.fruit_calories_list)

with open("input.txt", "r") as outfile:
    elf_input=outfile.read()
elf_fruit_list = elf_input.split("\n\n")

elf_sums = []
for fruit_calories in elf_fruit_list:
    elf = Elf(
        fruit_calories_list=[int(item) for item in fruit_calories.split("\n")]
        )
    elf_sums.append(elf.get_total_calories())

elf_sums.sort()

print(max(elf_sums)) # Part 1
print(sum(elf_sums[-3:])) # Part 2
