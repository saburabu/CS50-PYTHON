skills_1 = str(input("Person 1 Skills: ")).split()
p1_skills = set(skills_1)

skills_2 = str(input("Person 2 Skills: ")).split()
p2_skills = set(skills_2)

p1_skills.add("Git")
p2_skills.remove("SQL")

if "C++" in p1_skills:
    p1_skills.discard("C++")

x = p1_skills & p2_skills
y = p1_skills | p2_skills
z = p1_skills - p2_skills
print(x, y, z)