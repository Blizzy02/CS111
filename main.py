# Aisultan Saliev

# DO NOT REMOVE
file_name = input("Enter the food web file name: ")
raw_file = open(file_name)
file_list = raw_file.readlines()

# Creating dictionary to store predator and prey relationships
relation = {}
relation_order = []
predator_set = set()
prey_set = set()

for line in file_list:
    line = line.strip()  # Removing trailing whitespace
    parts = line.split(",")  # Splitting the line into parts
    predator = parts[0]  # The first part is the predator
    prey = parts[1:]  # The other ones are prey

    predator_set.add(predator)
    prey_set.update(prey)

    if predator not in relation_order:
        relation_order.append(predator)
    if predator in relation:
        relation[predator].extend(prey)  # Adding prey to predators
    else:
        relation[predator] = prey  # New entry if predator doesn't exist

# Outputs
print("\nPredators and Prey:")
for predator in relation_order:
    prey = relation[predator]
    if len(prey) > 1:
        prey.sort()
        if len(prey) == 2:
            prey_str = ", ".join(prey[:-1]) + f" and {prey[-1]}"
        else:
            prey_str = ", ".join(prey[:-1]) + f", and {prey[-1]}"
        print(f"  {predator} eats {prey_str}")
    else:
        print(f"  {predator} eats {prey[0]}")

apex_predators = sorted(predator_set.difference(prey_set))
if apex_predators:
    if len(apex_predators) == 1:
        apex_predators_str = f"{apex_predators[0]}"
    elif len(apex_predators) == 2:
        apex_predators_str = f"{apex_predators[0]} and {apex_predators[1]}"
    else:
        apex_predators_str = ", ".join(apex_predators[:-1]) + f", and {apex_predators[-1]}"
    print("\nApex Predators:", apex_predators_str)
else:
    print("\nNo Apex Predators")

# Find producers (organisms that do not eat any other organisms)
producers = sorted(prey_set.difference(predator_set))
if producers:
    if len(producers) == 1:
        producers_str = f"{producers[0]}"
    elif len(producers) == 2:
        producers_str = f"{producers[0]} and {producers[1]}"
    else:
        producers_str = ", ".join(producers[:-1]) + f", and {producers[-1]}"
    print("\nProducers:", producers_str)
else:
    print("\nNo Producers")

# Close the file
raw_file.close()
