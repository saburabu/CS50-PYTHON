users = [
    {
        "name": "John",
        "skills": ["Python", "AI"],
        "location": {
            "city": "Lagos",
            "country": "Nigeria"
        }
    },
    {
        "name": "Mary",
        "skills": ["JavaScript", "React"],
        "location": {
            "city": "Abuja",
            "country": "Nigeria"
        }
    }
]

for user in users:
    print(f"Name: {user['name']}\nCity: {user['location']['city']}\nSkills: {user['skills'][0]}")

for user_s in users:
    if "AI" in user_s["skills"]:
        print(f"Name: {user_s['name']}\nSkill: {user_s['skills']}")