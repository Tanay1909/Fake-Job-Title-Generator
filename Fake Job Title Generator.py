import random

adjectives = [
    "Certified", "Dynamic", "Global", "Chief", "Principal", "Future", "Virtual", "Corporate", "Strategic", "Senior"
]

roles = [
    "Meme", "Unicorn", "Synergy", "Innovation", "Paradigm", "Optimization", "Vision", "Metrics", "Infrastructure", "Solutions"
]

suffixes = [
    "Engineer", "Manager", "Strategist", "Coordinator", "Consultant", "Architect", "Director", "Analyst", "Officer", "Designer"
]

def generate_fake_job_title():
    return f"{random.choice(adjectives)} {random.choice(roles)} {random.choice(suffixes)}"

if __name__ == "__main__":
    print("Fake Job Title Generator")
    while True:
        print(generate_fake_job_title())
        again = input("Generate another? (y/n): ").strip().lower()
        if again != 'y':
            break