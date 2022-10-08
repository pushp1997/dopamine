from datetime import datetime

from settings import EVENTS, PROJECTS, BEGINNER_DEFINING_THRESHOLD, SUCCESS_DEFINING_THRESHOLD
from util import p2c, c2dat, a2c


def main():
    for event in EVENTS:
        # Get all authors from the projects that were created during each event
        authors_committed_during_event = set()
        event_start_datetime = datetime.strptime(event.start_date, "%d/%m/%Y %H:%M:%S")
        event_end_datetime = datetime.strptime(event.end_date, "%d/%m/%Y %H:%M:%S")
        for project in PROJECTS:
            commits = p2c(project)
            for commit in commits:
                commit_data = c2dat(commit)
                timestamp = commit_data.split(";")[1]
                author = commit_data.split(";")[3]
                commit_date = datetime.fromtimestamp(timestamp)
                if commit_data >= event_start_datetime and commit_data <= event_end_datetime:
                    authors_commited_during_event.add(author)
        
        # Get all the commits of the author prior to the commit during event
        # and identify the users who are beginners and were motivated to contribute
        # because of the event.
        total_newcommeres_influenced_by_the_event = 0
        successful_newcomers_converted_from_zero_to_hero = 0
        authors_commit_history = {}
        for author in authors_committed_during_event:
            authors_commit_history[author] = {
                "count_before_event": 0,
                "count_after_event": 0
            }
            all_commits_made_by_author = a2c(author)
            for commit in all_commits_made_by_author:
                commit_data = c2dat(commit)
                timestamp = commit_data.split(";")[1]
                author = commit_data.split(";")[3]
                commit_date = datetime.fromtimestamp(timestamp)
                if commit_data < event_start_datetime:
                    authors_commit_history[author]["count_before_event"] += 1
                if commit_data > event_start_datetime:
                    authors_commit_history[author]["count_after_event"] += 1
            
            if authors_commit_history[author]["count_before_event"] > BEGINNER_DEFINING_THRESHOLD:
                total_newcommeres_influenced_by_the_event += 1
                if authors_commit_history[author]["count_after_event"] > SUCCESS_DEFINING_THRESHOLD:
                    successful_newcomers_converted_from_zero_to_hero += 1
        
        # Calculate success percentage of the event
        success = successful_newcomers_converted_from_zero_to_hero / total_newcommeres_influenced_by_the_event * 100
        print(f"Success percentage of the event is {success}%")
                



if __name__ == '__main__':
    main()