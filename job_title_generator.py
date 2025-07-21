import random

adjectives = ["Certified", "Global", "Dynamic", "Invisible", "Strategic", "Epic", "Virtual"]
roles = ["Meme", "Unicorn", "AI", "Banana", "Quantum", "Pizza", "Emoji"]
suffixes = ["Engineer", "Strategist", "Consultant", "Guru", "Overlord", "Architect", "Wizard"]

def generate_fake_job_title():
    adjective = random.choice(adjectives)
    role = random.choice(roles)
    suffix = random.choice(suffixes)
    job_title = f"{adjective} {role} {suffix}"
    print("Your fake job title is:", job_title)

while True:
    generate_fake_job_title()
    again = input("Would you like another job title? (yes/no): ").strip().lower()
    if again != "yes":
        print("Thanks for playing!")
        break