import requests
import os
def get_issues(owner, repo, token):
    url = f"https://api.github.com/repos/{owner}/{repo}/issues"
    headers = {'Authorization': f'token {token}'}
    issues = []
    page = 1
    while True:
        response = requests.get(url, headers=headers, params={'page': page, 'per_page': 100})
        if response.status_code != 200:
            print(f"Failed to retrieve data: {response.status_code}")
            break
        data = response.json()
        if not data:
            break
        issues.extend(data)
        page += 1
    return issues

def main():
    owner = "octocat"  # Replace with the GitHub username of the repository owner
    repo = "Hello-World"  # Replace with the repository name
    #token = "your_github_token"  # Replace with your GitHub token
    token = os.environ['GITHUB_ACCESS_TOKEN']
    issues = get_issues(owner, repo, token)
    if issues:
        print(f"Issues for {owner}/{repo}:")
        for issue in issues:
            print(f"- {issue['title']}")
    else:
        print(f"No issues found for {owner}/{repo}")

if __name__ == "__main__":
    main()
