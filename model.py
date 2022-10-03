import numpy as np

NUM_RUNS = 100
NUM_BETTER_PEOPLE = np.empty((NUM_RUNS), dtype=int)

for k in range(NUM_RUNS):

    total_pop = np.arange(1, 501)
    np.random.shuffle(total_pop)
    selection_pool = total_pop[:100]
    sorted_selection_pool = np.sort(selection_pool, kind="mergesort")

    final_selection = 0
    checked_people = []

    for i in range(len(selection_pool)):

        # Adds the new person to the list of checked people
        # sorted by ranking from least to greatest
        for j in range(len(checked_people) + 1):
            if len(checked_people) == 0:
                checked_people.append(selection_pool[i])
                break

            if selection_pool[i] < checked_people[j]:
                checked_people.insert(j, selection_pool[i])
                break

            if j == len(checked_people) - 1:
                checked_people.append(selection_pool[i])
                break

        # First Model!!!!
        if i > 50:
            if selection_pool[i] == checked_people[i]:
                final_selection = selection_pool[i]
                break
        if i == len(selection_pool) - 1:
            final_selection = selection_pool[i]
        # End first Model!!!!

    # Count how many people are better than the one the model found
    num_better_people = 0
    for i in range(len(sorted_selection_pool)):
        if sorted_selection_pool[i] == final_selection:
            num_better_people = len(sorted_selection_pool) - 1 - i
            break

    # Just here to ensure the model is working correctly
    if k == 0:
        print(selection_pool)
        print(final_selection)
        print(sorted_selection_pool)
        print(num_better_people)

    NUM_BETTER_PEOPLE[k] = num_better_people

# Get stats!
avg_better_people = np.average(NUM_BETTER_PEOPLE)
median_better_people = np.median(NUM_BETTER_PEOPLE)
std_better_people = np.std(NUM_BETTER_PEOPLE)
worst_performance = np.max(NUM_BETTER_PEOPLE)
best_performance = np.min(NUM_BETTER_PEOPLE)
num_best_match = np.bincount(NUM_BETTER_PEOPLE)

print(NUM_BETTER_PEOPLE)
print(
    "The model found the best available match",
    num_best_match[0],
    "out of",
    NUM_RUNS,
    "times",
)
print("For the model's best performance, there were", best_performance, "better people")
print(
    "For the model's worst performance, there were", worst_performance, "better people"
)
print(
    "The AVERAGE number of people better than what the model found is",
    avg_better_people,
)
print(
    "The MEDIAN number of people better than what the model found is",
    median_better_people,
)
print(
    "The STANDARD DEVIATION of number of people better than what the model found is",
    std_better_people,
)
