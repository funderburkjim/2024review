"""
Copilot query: python program to get all github repos for a given owner
Copilot response
Certainly! Here's a Python program that fetches all GitHub repositories for a given owner using the GitHub API:
"""

import requests
from datetime import datetime
import sys,re,codecs
import os # for os.environ

def get_repo_commits(owner,repo,token):
    reponame = repo['name']
    url = f"https://api.github.com/users/{owner}/{reponame}/commits"
    #"https://api.github.com/repos/{0}/{1}/commits".format(githubUser, currentRepo)
    
    commits = []
    page = 1

    while True:
        response = requests.get(url, params={'page': page, 'per_page': 100})
        if response.status_code != 200:
            print(f"Failed to retrieve data: {response.status_code}")
            print('url=%s' % url)
            exit(1)

        data = response.json()
        if not data:
            break

        commits.extend(data)
        page += 1
    return commits
    
def get_github_repos(owner,token):
    url = f"https://api.github.com/users/{owner}/repos"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    params = {
        #"since": since_date,
        "state": "all"
    }
    repos = []
    page = 1

    while True:
        response = requests.get(url, params={'page': page, 'per_page': 100})
        if response.status_code != 200:
            print('get_github_repos error')
            print(f"Failed to retrieve data: {response.status_code}")
            break

        data = response.json()
        if not data:
            break

        repos.extend(data)
        page += 1

    return repos

def make_outlines(repos,lastcommitdates):
    lines = []
    for repo in repos:
        line = f"{repo['name']}"
        lines.append(line)
    return lines

def write_lines(fileout,lines):
 with codecs.open(fileout,"w","utf-8") as f:
   for line in lines:
    f.write(line+'\n')
 print('%s lines written to %s' % (len(lines),fileout))

if __name__ == "__main__":
    repo_owner = sys.argv[1] # "your-repo-owner"
    fileout = sys.argv[2] # 
    token = os.environ['GITHUB_ACCESS_TOKEN'] # Personal access token
     
    owner = repo_owner #GitHub username of the owner
    repos = get_github_repos(owner,token)
    if len(repos) == 0:
        print(f"No repositories found for owner: {owner}")
        exit(0)
    print(f"{len(repos)} Repositories owned by {owner}:")
    # get latest commit for each repo
 
    lastcommitdates = []
    for repo in repos:
        """
        allcommits = get_repo_commits(owner,repo)
        if len(allcommits) == 0:
           print('repo %s has no commits!' % repo)
           continue
        latest_commit = allcommits[0]
        lastcommitdate = latest_commit['date']
        lastcommitdates.append(lastcommitdate)
"""
    lines = make_outlines(repos,lastcommitdates)
    write_lines(fileout,lines)

"""
Explanation:
Imports: The requests library is used to make HTTP requests.
Function get_github_repos(owner):
Constructs the URL for the GitHub API.
Uses pagination to fetch all repositories (GitHub API returns a limited number of results per page).
Collects all repositories in a list.
Main Function:
Sets the GitHub username (owner).
Calls get_github_repos to fetch repositories.
Prints the names of the repositories.
Notes:
Replace "octocat" with the desired GitHub username.
Ensure you have the requests library installed (pip install requests).

This program is adaptable and can be modified to include additional details or handle more complex scenarios. If you need further customization, feel free to ask!
"""
