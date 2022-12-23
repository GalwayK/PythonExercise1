athlete_ranking = ['John', "Sen", "Lisa"]
athlete_index = input("Enter the athlete name: ")
if athlete_ranking.__contains__(athlete_index):
    print("The athlete's rank is", athlete_ranking.index(athlete_index) + 1)
else:
    print("Error, invalid athlete.")
