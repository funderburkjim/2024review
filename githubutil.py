"""
github_utilities.py
"""
import requests
import os  
def get_issue_comments(owner, repo, issue_number, token):
    # uses pagination to get ALL comments for the issue
    url = f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}/comments"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    comments = []
    page = 1

    while True:
        response = requests.get(url, headers=headers, params={"page": page, "per_page": 100})
        response.raise_for_status()
        page_comments = response.json()
        if not page_comments:
            break
        comments.extend(page_comments)
        page += 1
    return comments

def get_commits_between_dates(owner, repo, start_date, end_date, token):
    # see copilot_test_commits.py for example
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
        try:
         response.raise_for_status()
         # no problem
        except requests.exceptions.HTTPError as err:
         print()
         print('******** BEGIN WARNING commits %s %s********' %(owner,repo))
         print('%s %s %s %s' %(owner,repo,start_date,end_date))
         print(f"HTTP error occurred: {err}")
         print('url: %s' % url)
         print('******** END WARNING ********')
         print()
         return commits
        commits.extend(response.json())
        # Check for pagination
        if 'next' in response.links:
            url = response.links['next']['url']
        else:
            url = None
    return commits

def get_issues_between_dates(owner, repo, start_date, end_date, token):
    url = f'https://api.github.com/repos/{owner}/{repo}/issues'
    headers = {'Authorization': f'token {token}'}
    params = {
        'since': start_date,
        'until': end_date,
        "state": "all",  # both open and closed issues
        'per_page': 100}
    issues = []
    while url:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        issues.extend(response.json())
        # Check for pagination
        if 'next' in response.links:
            url = response.links['next']['url']
        else:
            url = None
    return issues

# Example usage (from copilot)
if __name__ == "__main__":
    owner = "octocat"
    repo = "Hello-World"
    issue_number = 1
    token = "your_github_token_here"  # Replace with your GitHub token
    token = os.environ['GITHUB_ACCESS_TOKEN'] # MODIFIED
    comments = get_issue_comments(owner, repo, issue_number, token)
    print('# comments = %s' % len(comments))
    #for comment in comments:
    #    print(f"{comment['user']['login']}: {comment['body']}\n")
