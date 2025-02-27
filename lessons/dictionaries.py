"""Demonstrations of dictionary capabilities."""


# Declaring the type of a dictionary
schools: dict[str, int]

# Initialize to an empty dictionary
schools = dict()

# Set a key-value pairing in the dictionary
schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150

# Print a dictionary literal representation
print(schools)

# Access a value by its key -- "lookup"
print(f"UNC has {schools['UNC']} students")

# Remove a key-value pair from a dictionary
# by its key
schools.pop("Duke")

# Test for existence of a key
if "Duke" in schools:
    print("Found the key 'Duke' in schools")
else:
    print("No key 'Duke' in schools")

# Update / reassign a key-value pair
schools["UNC"] = 20000
schools["NCSU"] += 200

print(schools)

# Demonstration of dictionary literals

# empty dictionary literal
schools = {} # same as dict()

# Alternatively, initialize key-value pairs
schools = {"UNC": 19400, "Dukie": 6717, "NSCU": 26150}
print(schools)

# what happens when a key does not exist
# print(schools["UNCC"])

# Example looping over the keys of a dictt
for key in schools:
    print(f"Key: {key} -> Value: {schools[key]}")