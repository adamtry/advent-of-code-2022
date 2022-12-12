def analyse_assignments(assignments):
    full_contains = 0
    overlaps = 0
    for cleanup_assignment in assignments:
        assignment_one = [int(assignment) for assignment in cleanup_assignment.split(",")[0].split("-")]
        assignment_two = [int(assignment) for assignment in cleanup_assignment.split(",")[-1].split("-")]

        range_one = set(range(assignment_one[0], assignment_one[-1] + 1))
        range_two = set(range(assignment_two[0], assignment_two[-1] + 1))

        overlap = not range_one.isdisjoint(range_two)
        full_contain = range_one.issubset(range_two) or range_two.issubset(range_one)

        if full_contain:
            full_contains += 1
        if overlap:
            overlaps += 1
    print(f"Full Contains (Part 1): {full_contains}\nOverlaps (Part 2): {overlaps}")

if __name__ == "__main__":
    with open("input.txt", "r") as outfile:
        cleanup_assignments = outfile.read().strip().splitlines()

    analyse_assignments(cleanup_assignments)
