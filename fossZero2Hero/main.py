from datetime import datetime
import csv

from settings import PROJECTS
from util import p2c, c2dat


def main():
    # Get all commits from the projects that were created during hacktoberfest
    commits_created_
    for all project in PROJECTS:
        commits = p2c(project)
        for commit in commits:
            commit_data = c2dat(commit)
            timestamp = commit_data.split(";")[1]
            commit_date = datetime.fromtimestamp(timestamp)



if __name__ == '__main__':
    main()