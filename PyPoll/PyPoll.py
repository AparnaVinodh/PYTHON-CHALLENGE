import csv

votestotal = 0
candidate = ""
votes = {}
percentagesc ={}
votesforwinner = 0
winner = ""


filepath = 'C:/Users/aparn/Documents/DATA ANALYTICS BOOTCAMP/PYTHON HOMEWORK/Homework/Instructions/PyPoll/Resources/election_data.csv'
with open(filepath,'r', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)

    
    for row in csvreader:
        votestotal = votestotal + 1
        candidate = row[2]
        if candidate in votes:
            votes[candidate] = votes[candidate] + 1
        else:
            votes[candidate] = 1


for person, vote_count in votes.items():
    percentagesc[person] = '{0:.0%}'.format(vote_count / votestotal)
    if vote_count > votesforwinner:
        votesforwinner = vote_count
        winner = person

dashbreak = "-------------------------"


print("Election Results")
print(dashbreak)
print(f"Total Votes: {votestotal}")
print(dashbreak)
for person, vote_count in votes.items():
    print(f"{person}: {percentagesc[person]} ({vote_count})")
print(dashbreak)
print(f"Winner: {winner}")
print(dashbreak)

with open("PyPollNote.txt","w") as txtfile:
   txtfile.write("Election Results" + "\n")
   
   txtfile.write("--------------------------------" + "\n")
   txtfile.write(str(votestotal)  + "\n")
   txtfile.write("---------------------------------" + "\n")

   for person, vote_count in votes.items():
       txtfile.write(str(person) + ": " + str( "{:2.3f}".format(vote_count/votestotal))  + "% (" + str(vote_count) + ")\n")

   txtfile.write("--------------------------------" + "\n")
   txtfile.write(str(winner)  + "\n")
   txtfile.write("--------------------------------" + "\n")

   txtfile.close()
