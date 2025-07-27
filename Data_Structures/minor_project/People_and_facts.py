#This program creates a dictionary of people with one interesting fact about each person.
# It first displays the list, then changes one fact, adds another person with a fact, and finally displays the updated list.

people_facts = {
    "Jeff": "Is afraid of Dogs.",
    "David": "Plays the piano.",
    "Jason": "Can fly an airplane."
}

print("Original List:")
for person in people_facts:
    print(person + ": " + people_facts[person])

people_facts["Jeff"] = "Is afraid of heights."
people_facts["Jill"] = "Can hula dance."

print()
print("Updated List:")
for person in people_facts:
    print(person + ": " + people_facts[person])
