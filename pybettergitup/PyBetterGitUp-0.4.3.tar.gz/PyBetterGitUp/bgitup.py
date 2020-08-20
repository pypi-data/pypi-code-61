from PyGitUp.gitup import GitUp
import git
import os


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def warn(msg):
    print(f"{bcolors.WARNING}{msg}{bcolors.ENDC}")


def update(msg):
    print(f"{bcolors.OKGREEN}{msg}{bcolors.ENDC}")


def yes_or_no(question):
    reply = str(input(question+' (y/n): ')).lower().strip()
    if reply[0] == 'y':
        return True
    if reply[0] == 'n':
        return False
    else:
        return yes_or_no("Uhhhh... please enter ")


class BGitUp():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    remoteDoesNotExist = "remote branch doesn't exist"
    missingRemoteBranches = []

    def __init__(self):
        self.gitUp = GitUp()

    def run(self):
        self.gitUp.run()

        # getting length of list of states
        states = self.gitUp.states

        # Look for any branches that are no longer connect to a remote origin
        # Iterating the index
        for i in range(len(states)):
            if states[i] == self.remoteDoesNotExist:
                branch = self.gitUp.branches[i]
                self.missingRemoteBranches.append(branch)

        missbranchesLength = len(self.missingRemoteBranches)
        if missbranchesLength > 0:
            branchPlural = "" if missbranchesLength == 1 else "es"
            thisPlural = "this" if missbranchesLength == 1 else "these"
            warn("\nBranch" + branchPlural +
                 " found that no longer exist on the emote")
            for i in range(missbranchesLength):
                warn(f"\t{self.missingRemoteBranches[i].name}")

            if yes_or_no(f"Would you like to remove {thisPlural} branch{branchPlural}?"):
                # loop over each branch and delete it locally
                repo = git.Repo(self.dir_path, search_parent_directories=True)
                for i in range(len(self.missingRemoteBranches)):
                    update(f"\t deleting {self.missingRemoteBranches[i].name}")
                    git.Head.delete(
                        repo, self.missingRemoteBranches[i].name, force=True)


def run():
    BGitUp().run()


if __name__ == "__main__":
    run()
