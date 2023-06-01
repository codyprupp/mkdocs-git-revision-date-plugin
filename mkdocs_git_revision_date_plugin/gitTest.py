import git
import datetime

myRepo = git.Repo("C:/Users/Cody/Desktop/TUAS/wiki")

# print(myRepo.commit('bdea42410c5655e1e9505b3d87099897716987a0').)

# iterator for each blame 'chunk' of the file
blameIter = myRepo.blame_incremental(myRepo.head, "docs/embedded/electronics-diagram.md")

# print each timestamp of the git blame
def listBlame(blameIter):
    for blame in blameIter:
        rawEpochTime = blame.commit.authored_date
        timeSince = datetime.datetime.fromtimestamp(rawEpochTime).strftime('%Y-%m-%d %H:%M:%S')
        print(timeSince)

listBlame(blameIter)