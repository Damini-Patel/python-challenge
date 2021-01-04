# import Modules
import os
import csv

# set path for file
csvpath = os.path.join("..", "PyPoll", "Resources\\election_data.csv")

# open the CSV
with open(csvpath, "r") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # skip header
    csv_header = next(csvfile)

    # set varibales
    vote_count = 0
    votes_dic = {}
    
    # read through each line
    for row in csv_reader:
        candidate = row[2]

        # find total number of votes cast
        vote_count += 1

        # list candidates who received votes
        # find number of votes each candidate won
        if candidate in votes_dic:
            x = votes_dic[candidate]
            x += 1
            votes_dic[candidate] = x
        else:
            votes_dic[candidate] = 1

# print statements to terminal
# print to text file
with open("PyPoll_Results.txt", "w") as f:
    
    print("Election Results")
    f.write("Election Results\n")
    print("--------------------------------------------")
    f.write("--------------------------------------------\n")
    print("Total Votes: " + str(vote_count))
    f.write("Total Votes: " + str(vote_count) + '\n')
    print("--------------------------------------------")
    f.write("--------------------------------------------\n")

    # find percentage of votes each candidate received
    win_value = 0
    for c in votes_dic:
        percentage_votes = round(votes_dic[c] / vote_count * 100)
        percent_str = str(percentage_votes) + '%'
        x = votes_dic[c]
        print(c + ": " + percent_str + " (" + str(votes_dic[c]) + ")")
        f.write(c + ": " + percent_str + " (" + str(votes_dic[c]) + ")\n")

    # find winner of the election based on votes 
        if votes_dic[c] > win_value:
            win_value = votes_dic[c]
            winner = c
    print("--------------------------------------------")
    f.write("--------------------------------------------\n")
    print("Winner: " + winner)    
    f.write("Winner: " + winner + '\n')    
    print("--------------------------------------------")
    f.write("--------------------------------------------\n")






