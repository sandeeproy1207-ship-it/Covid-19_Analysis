import datetime

def commit_callback(commit):
    now = datetime.datetime.now(datetime.timezone.utc)
    new_date = now.strftime("%Y-%m-%d %H:%M:%S %z")
    commit.committer_date = new_date.encode()
    commit.author_date = new_date.encode()
