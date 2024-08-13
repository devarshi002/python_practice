#function with keyword Arguments

def describe_pet(pet_name, animal_type="dog"):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

#call the function with keyword arguments
describe_pet(pet_name="tommy")
describe_pet(animal_type='cat', pet_name="tommy")