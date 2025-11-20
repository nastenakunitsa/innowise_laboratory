def generate_profile(age):

    
    if 0 <= age <= 12:
        return "Child"
    elif 13 <= age <= 19:
        return "Teenager"
    else:
        return "Adult"


user_name = input("Enter your full name: ").strip()
birth_year_str = input("Enter your year of birth: ").strip()
birth_year = int(birth_year_str)
current_age = 2025 - birth_year

hobbies = []
while True:
    hobby= input("Enter your favorite hobby or type 'stop' to finish:")
    if hobby.strip().lower() == 'stop':
        break
    hobbies.append(hobby)
life_stage = generate_profile(current_age)

user_profile = {
        'Name': user_name,
        'Age': current_age,
        'Life Stage': life_stage,
        'Hobbies': hobbies
}

print("Profile Summary:")
for key, value in user_profile.items():
    if key == "Hobbies":
        if not value:
            print("You didn't mention any hobbies.")
        else:
            print(f"Favorite Hobbies ({len(value)}):")
            for hobby in value:  
                print(f"- {hobby}")  
    else:
        print(f"{key}: {value}")