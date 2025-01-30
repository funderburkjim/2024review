import requests
import os
def get_comments(owner, repo, issue_number, token):
    url = f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}/comments"
    headers = {'Authorization': f'token {token}'}
    comments = []
    page = 1
    while True:
        response = requests.get(url, headers=headers, params={'page': page, 'per_page': 100})
        if response.status_code != 200:
            print(f"Failed to retrieve data: {response.status_code}")
            break
        data = response.json()
        if not data:
            break
        comments.extend(data)
        page += 1
    return comments

def main():
    owner = "octocat"  # Replace with the GitHub username of the repository owner
    repo = "Hello-World"  # Replace with the repository name
    issue_number = 1  # Replace with the issue number
    #token = "your_github_token"  # Replace with your GitHub token
    token = os.environ['GITHUB_ACCESS_TOKEN']

    comments = get_comments(owner, repo, issue_number, token)
    if comments:
        print(f"Comments for issue #{issue_number} in {owner}/{repo}:")
        for comment in comments:
            user = comment['user']['login']
            comment = comment['body'] #  a string
            comment1 = comment[0:40]  # shorten
            print(f"- {user} {comment1}")
    else:
        print(f"No comments found for issue #{issue_number} in {owner}/{repo}")

if __name__ == "__main__":
    main()
