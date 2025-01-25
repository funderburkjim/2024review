"""
prompt to copilot (edge)
python program to get all commits pf a repo between two dates, using pagination

Certainly! Here's a Python program that uses the GitHub API to fetch all commits from a repository between two dates, handling pagination. You'll need to have a GitHub personal access token for authentication.
"""
import requests
from datetime import datetime

# Replace these with your own values
# GITHUB_TOKEN = 'your_github_token'
import os
GITHUB_TOKEN = os.environ['GITHUB_ACCESS_TOKEN']

REPO_OWNER = 'funderburkjim'  #'repo_owner'
REPO_NAME = 'elispsanskrit'   # 'repo_name'
START_DATE = '2015-01-01T00:00:00Z'
END_DATE = '2015-12-31T23:59:59Z'

def get_commits_between_dates(owner, repo, start_date, end_date, token):
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    headers = {'Authorization': f'token {token}'}
    params = {
        'since': start_date,
        'until': end_date,
        'per_page': 100
    }
    commits = []
    while url:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        commits.extend(response.json())
        # Check for pagination
        if 'next' in response.links:
            url = response.links['next']['url']
        else:
            url = None
    return commits

if __name__ == '__main__':
    commits = get_commits_between_dates(REPO_OWNER, REPO_NAME, START_DATE, END_DATE, GITHUB_TOKEN)
    for commit in commits:
        commit_date = commit['commit']['author']['date']
        commit_message = commit['commit']['message']
        print(f"Date: {commit_date}, Message: {commit_message}")
"""
Explanation:
Authentication: Uses a GitHub personal access token for authentication.
API Request: Sends a GET request to the GitHub API to fetch commits.
Pagination: Handles pagination by checking the next link in the response headers.
Date Filtering: Filters commits between the specified start and end dates.
Output: Prints the date and message of each commit.

Make sure to replace 'your_github_token', 'repo_owner', and 'repo_name' with your actual GitHub token, repository owner, and repository name, respectively. Adjust the START_DATE and END_DATE as needed.

Feel free to reach out if you need further assistance or modifications!
"""
