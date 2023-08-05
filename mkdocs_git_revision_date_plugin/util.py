from git.cmd import Git
import git.repo
import datetime
import os

class Util:

    def __init__(self):
        self.g = Git()

    # def get_revision_date_for_file(self, path: str):
    #     return self.g.log(path, n=1, date='short', format='%ad')
    

    # NOTE: this implies that a file is "up to date" if the most recent git commit displays a somewhat recent date.
    #   This is not entirely accurate, unless whoever made that commit checked the entire file for discrepancies, which is not always the case.
    #   To fix this, either display a verbose output with every single line of blame, or figure out a way to display the blame for a specific
    #       while hovering over the corresponding text.
    def get_revision_date_for_file(self, path: str):

        # get the raw blame for the file
        repo = git.repo.Repo(os.getcwd())
        blameIter = repo.blame_incremental(repo.head, path)

        blameTimes = []

        # extract each blame's date in the form YYYY-MM-DD
        for blame in blameIter:
            rawEpochTime = blame.commit.authored_date # type: ignore (not sure why this gives an error; it works fine)
            timeSince = datetime.datetime.fromtimestamp(rawEpochTime).strftime('%Y-%m-%d') # add %H:%M:%S for specific time
            blameTimes.append(timeSince)

        mostRecentTime = '0000-00-00'

        # find most recent blame (to be displayed as last updated)
        for time in blameTimes:
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
            elif (year == mostRecentTimeYear and month == mostRecentTimeMonth and day > mostRecentTimeDay):
                mostRecentTime = time

        return mostRecentTime