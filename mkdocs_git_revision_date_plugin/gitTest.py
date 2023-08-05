import git
from git.cmd import Git
import git.repo
import datetime

myRepo = git.repo.Repo("C:/Users/Cody/tuas/wiki")

# print(myRepo.commit('bdea42410c5655e1e9505b3d87099897716987a0').)

# iterator for each blame 'chunk' of the file
path = "docs/airframe/packing_list.md"
blameIter = myRepo.blame_incremental(myRepo.head, path)
g = Git("C:/Users/Cody/tuas/wiki/")
currOutput = myRepo.blame(myRepo.head, "docs/embedded/electronics-diagram.md")

# print each timestamp of the git blame

blameTimes = []

for blame in blameIter:
    rawEpochTime = blame.commit.authored_date # type: ignore (not sure why this gives an error; it works fine)
    timeSince = datetime.datetime.fromtimestamp(rawEpochTime).strftime('%Y-%m-%d') # add %H:%M:%S for specific time
    blameTimes.append(timeSince)

print(blameTimes)

if not blameTimes:
    print('no blames; defaulting to git logs')

def getMostRecentTime(times):

    if not times:
        mostRecentTime = g.log(path, n=1, date='short', format='%ad')
    else:
        mostRecentTime = '0000-00-00'

    mostRecentTimeYear = int(mostRecentTime[0:4])
    mostRecentTimeMonth = int(mostRecentTime[5:7])
    mostRecentTimeDay = int(mostRecentTime[8:10])

    for time in times:
        year = int(time[0:4])
        month = int(time[5:7])
        day = int(time[8:10])
        # print(year)

        if year > mostRecentTimeYear:
            # print('yes')
            mostRecentTime = time
        elif (year == mostRecentTimeYear and month > mostRecentTimeMonth):
            mostRecentTime = time
        elif (year == mostRecentTimeYear and month == mostRecentTimeMonth and day > mostRecentTimeDay):
            mostRecentTime = time

        mostRecentTimeYear = int(mostRecentTime[0:4])
        mostRecentTimeMonth = int(mostRecentTime[5:7])
        mostRecentTimeDay = int(mostRecentTime[8:10])

    # print(mostRecentTimeYear)

    if (mostRecentTimeYear == 0):
        return 

    # have to do this case because windows can't use the %-d strftime code. %e is the windows equivalent,
    #   but instead of actually removing the 0 padding, it prepends the number with a space, leaving some awkward gaps when the number has 2 digits.
    #   tldr; gg windows sucks
    if (mostRecentTimeDay < 10):
        return datetime.date(mostRecentTimeYear,mostRecentTimeMonth,mostRecentTimeDay).strftime("%B%e, %Y")

    return datetime.date(mostRecentTimeYear,mostRecentTimeMonth,mostRecentTimeDay).strftime("%B %d, %Y")

print('most recent time:', getMostRecentTime(blameTimes))