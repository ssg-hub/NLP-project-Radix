import json

with open("assets/cleaned_related_skills.json", "r") as f:
    data = f.read()
    print(data)


# f = open("assets/cleaned_related_skills.json")
# skillset = json.loads(f)

# print(type(skillset))