from github import Github
import random
from datetime import datetime, timedelta
import os
import subprocess

def commit_with_date(repo_path, commit_message, author_date, committer_date):
    os.chdir(repo_path)
    os.environ['GIT_AUTHOR_DATE'] = author_date
    os.environ['GIT_COMMITTER_DATE'] = committer_date
    subprocess.run(['git', 'add', '.'])
    subprocess.run(['git', 'commit', '-m', commit_message])
    os.environ['GIT_AUTHOR_DATE'] = ''
    os.environ['GIT_COMMITTER_DATE'] = ''

def random_date(start, end):
    return start + timedelta(seconds=random.randint(0, int((end - start).total_seconds())))

if __name__ == '__main__':
    # Authenticate with the GitHub API
    token = "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"
    g = Github(token)

    # Check if the repository already exists
    repo_name = "random-repo"
    user = g.get_user()
    repo = None
    try:
        repo = user.get_repo(repo_name)
    except:
        pass

    # Create the repository if it doesn't exist
    if repo is None:
        repo = user.create_repo(repo_name, private=True)

    clone_url = repo.ssh_url

    # Clone the repository locally
    local_repo_path = os.path.join(os.getcwd(), repo_name)
    subprocess.run(['git', 'clone', clone_url, local_repo_path])

    # Make commits at random dates in the past year
    start_date = datetime.now() - timedelta(days=365)
    end_date = datetime.now()
    for i in range(100):  # Change this to the number of commits you want to make
        commit_date = random_date(start_date, end_date)
        commit_message = f"Random commit {i}"
        commit_with_date(local_repo_path, commit_message, commit_date.isoformat(), commit_date.isoformat())

    # Push the commits to the remote repository
    os.chdir(local_repo_path)
    subprocess.run(['git', 'push'])
