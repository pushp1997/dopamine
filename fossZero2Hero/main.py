from datetime import datetime

from settings import EVENTS, PROJECTS, BEGINNER_DEFINING_THRESHOLD, SUCCESS_DEFINING_THRESHOLD
from utils import p2c, c2data, a2c, convert_to_int


def get_commits_from_project()->list:
    """
    This functions fetches the all commits for events specified
    in the settings file
    """
    commits = p2c(PROJECTS)
    commits = commits[:4]
    return commits


def get_commit_data(commits: list)->set:
    commit_data = set()
    for commit in commits:
        data = c2data(commit)
        if data:
            commit_data.add(data)
    return commit_data


def filter_authors(
        commit_datas: set,
        event_start_datetime: datetime,
        event_end_datetime: datetime
    )->set:
    authors_commited_during_event = set()

    for commit_data in commit_datas:
        commit_data = commit_data.split(";")
        author = commit_data[3]
        author_commit_time_stamp = convert_to_int(commit_data[1])
        if author_commit_time_stamp:
            commit_date = datetime.fromtimestamp(author_commit_time_stamp)
            if commit_date >= event_start_datetime and commit_date <= event_end_datetime:
                authors_commited_during_event.add(author)

    return authors_commited_during_event


def get_authors_commit_insights(
        authors_committed_during_event: set,
        event_start_datetime: datetime,
        event_end_datetime: datetime

    ) -> dict:
    authors_commit_history = {}
    for author in authors_committed_during_event:
            authors_commit_history[author] = {
                "count_before_event": 0,
                "count_during_event": 0,
                "count_after_event": 0
            }
            all_commits_made_by_author = a2c(author)
            print(type(all_commits_made_by_author))
            for commit in all_commits_made_by_author:
                commit_data = c2data(commit)
                commit_data = commit_data.split(";")
                try:
                    if commit_data:
                        print(commit_data)
                        timestamp = commit_data[1]
                        author = commit_data[3]
                        commit_date = datetime.fromtimestamp(timestamp)
                        if commit_date < event_start_datetime:
                            authors_commit_history[author]["count_before_event"] += 1
                        elif commit_date > event_start_datetime:
                            authors_commit_history[author]["count_after_event"] += 1
                        else:
                            authors_commit_history[author]["count_during_event"] += 1
                    else:
                        print("no data")
                except:
                    pass
    print(authors_commit_history)
    return authors_commit_history



def main():
    for event in EVENTS:

        event_start = event.get("start_date")
        if not event_start:
            print("Oops!! You forgot to specify a start date for event. :(")
            exit()
        event_end = event.get("end_date")
        if not event_end:
            print("Oops!! You forgot to specify a end date for event. :(")
            exit()
        event_start_datetime = datetime.strptime(event_start, "%d/%m/%Y %H:%M:%S")
        event_end_datetime = datetime.strptime(event_end, "%d/%m/%Y %H:%M:%S")

        # Get all authors from the projects that were created during each event
        authors_committed_during_event = set()
        commits = get_commits_from_project()
        commit_data = get_commit_data(commits)
        authors = filter_authors(commit_data, event_start_datetime, event_end_datetime)
        get_authors_commit_insights(authors, event_start_datetime, event_end_datetime)


        # # Get all the commits of the author prior to the commit during event
        # # and identify the users who are beginners and were motivated to contribute
        # # because of the event.
        # total_newcommeres_influenced_by_the_event = 0
        # successful_newcomers_converted_from_zero_to_hero = 0
        # authors_commit_history = {}
        # for author in authors_committed_during_event:
        #     authors_commit_history[author] = {
        #         "count_before_event": 0,
        #         "count_after_event": 0
        #     }
        #     all_commits_made_by_author = a2c(author)
        #     for commit in all_commits_made_by_author:
        #         commit_data = c2dat(commit)
        #         timestamp = commit_data.split(";")[1]
        #         author = commit_data.split(";")[3]
        #         commit_date = datetime.fromtimestamp(timestamp)
        #         if commit_data < event_start_datetime:
        #             authors_commit_history[author]["count_before_event"] += 1
        #         if commit_data > event_start_datetime:
        #             authors_commit_history[author]["count_after_event"] += 1

        #     if authors_commit_history[author]["count_before_event"] > BEGINNER_DEFINING_THRESHOLD:
        #         total_newcommeres_influenced_by_the_event += 1
        #         if authors_commit_history[author]["count_after_event"] > SUCCESS_DEFINING_THRESHOLD:
        #             successful_newcomers_converted_from_zero_to_hero += 1

        # # Calculate success percentage of the event
        # success = successful_newcomers_converted_from_zero_to_hero / total_newcommeres_influenced_by_the_event * 100
        # print(f"Success percentage of the event is {success}%")




if __name__ == '__main__':
    main()