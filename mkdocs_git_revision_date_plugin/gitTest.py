import git
import git.repo
import datetime

myRepo = git.repo.Repo("C:/Users/Cody/tuas/wiki")

# print(myRepo.commit('bdea42410c5655e1e9505b3d87099897716987a0').)

# iterator for each blame 'chunk' of the file
blameIter = myRepo.blame_incremental(myRepo.head, "docs/software/software_home.md")
currOutput = myRepo.blame(myRepo.head, "docs/embedded/electronics-diagram.md")

# print each timestamp of the git blame

blameTimes = []

for blame in blameIter:
    rawEpochTime = blame.commit.authored_date # type: ignore (not sure why this gives an error; it works fine)
    print(rawEpochTime)
    timeSince = datetime.datetime.fromtimestamp(rawEpochTime).strftime('%Y-%m-%d') # add %H:%M:%S for specific time
    blameTimes.append(timeSince)

print(blameTimes)

def getMostRecentTime(times):

    mostRecentTime = '0000-00-00'

    for time in times:
        year = int(time[0:4])
        month = int(time[5:7])
        day = int(time[8:10])

        mostRecentTimeYear = int(mostRecentTime[0:4])
        mostRecentTimeMonth = int(mostRecentTime[5:7])
        mostRecentTimeDay = int(mostRecentTime[8:10])

        if year > mostRecentTimeYear:
            mostRecentTime = time
        elif (year == mostRecentTimeYear and month > mostRecentTimeMonth):
            mostRecentTime = time
        elif (year == mostRecentTimeYear and month == mostRecentTimeMonth and mostRecentTimeDay > mostRecentTimeDay):
            mostRecentTime = time

    return mostRecentTime

print('most recent time:', getMostRecentTime(blameTimes))