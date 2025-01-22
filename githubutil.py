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
