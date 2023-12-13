'''
dictionaryManipulation
'''
personal_profile = {"name": "John",
                  "surname": "Karatu",
                  "age": 15,
                  "game": "mindcraft"
                }

print(personal_profile["name"])
print(personal_profile["age"])

keys = personal_profile.keys()
values = personal_profile.values()

print(keys)
print(values)

print("surname" in personal_profile)