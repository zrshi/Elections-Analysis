counties = ["Arapahoe", "Denver", "Jefferson"]
if counties[1] == "Denver":
    print(counties[1])
    
    
#What is the score?
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
else:
    if score >= 80:
        print('Your grade is a B.')
    else:
        if score >= 70:
            print('Your grade is a C.')
        else:
            if score >= 60:
                print('Your grade is a D.')
            else:
                print('Your grade is an F.')

counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

x = 0 
while x <=5:
    print(x)
    x = x + 1

counties_dict = {"Arapahoe":422829, "Denver": 463353, "Jefferson": 432438}


for county, voters in counties_dict.items():
    print(county, "county has", voters, "registered voters")


voting_data = [{"county": "Arapahoe", "registered_voters": 422829},
                {"county": "Denver", "registered_voters": 463353},
                {"county": "Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

for county_dict in voting_data:
    print(county_dict['registered_voters'])

print(county_dict.values())


my_votes = int(input("How many votes did you get in the election?"))
total_votes = int(input("What is the total votes in the eleciotn?"))
percentage_votes - (my_votes / total_votes) * 100
print("I received" + str(percentage_votes) + "% of the total votes")
print(f"I received {my_votes / total_votes * 100} % of the total votes")
