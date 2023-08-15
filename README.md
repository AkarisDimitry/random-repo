# Random Commit GitHub Bot

The Random Commit GitHub Bot is a Python script that automates the process of creating a new private GitHub repository (if it doesn't already exist) and making commits at random dates from 1 year in the past to the present. 

## How it Works

1. The script authenticates with the GitHub API using a Personal Access Token (PAT).
2. It checks if the specified repository already exists for the authenticated user.
3. If the repository does not exist, the script creates a new private repository.
4. The script clones the repository to the local machine.
5. The script makes commits at random dates in the past year. The date for each commit is randomly generated within a time range from 1 year ago to the current date.
6. Finally, the script pushes the commits to the remote repository on GitHub.

## Installation

1. Install the `PyGithub` library, which provides a Python interface for the GitHub API:

   ```shell
   pip install PyGithub
   ```

2. Clone this repository or download the Python script.

3. Generate a Personal Access Token (PAT) on GitHub with the "repo" scope. Instructions on how to create a PAT can be found in the [GitHub documentation](https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token).

4. Replace the placeholder `YOUR_PERSONAL_ACCESS_TOKEN` in the Python script with your actual PAT.

5. Run the script:

   ```shell
   python random_commit_bot.py
   ```

## Complexity

The time complexity of the script is mainly determined by the number of commits it makes and the time it takes to push these commits to the remote repository. The time complexity is O(n) where n is the number of commits.

The space complexity is O(1) as the script uses a constant amount of space regardless of the number of commits.

## Dependencies

- Python 3.x
- `PyGithub` library
- `git` command line tool

## Notes

- The script uses the `subprocess` module to run git commands.
- The script manipulates the `GIT_AUTHOR_DATE` and `GIT_COMMITTER_DATE` environment variables to set the date for each commit.
- The date for each commit is randomly generated within a time range from 1 year ago to the current date.
- The script assumes that the repository does not have any uncommitted changes when it runs.
- Please be aware that making commits with previous dates will rewrite the commit history, which might not be desirable in all cases.
- The script is intended for educational purposes and should be used responsibly.

## License

This project is licensed under the MIT License.
