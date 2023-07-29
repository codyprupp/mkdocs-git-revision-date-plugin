from git.cmd import Git

class Util:

    def __init__(self):
        self.g = Git()

    # def get_revision_date_for_file(self, path: str):
    #     return self.g.log(path, n=1, date='short', format='%ad')
    
    def get_revision_date_for_file(self, path: str):
        return self.g.blame(path)