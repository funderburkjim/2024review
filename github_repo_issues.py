"""
github_repo_issues.py
"""
import requests
from datetime import datetime
import sys,re,codecs
import os # for os.environ
from githubutil import get_issue_comments

def get_issues_range(repo_owner, repo_name ):
    issues = []
    headers = {
     "Authorization": f"token {token}",
     'Accept': 'application/vnd.github.v3+json'
    }
    
    for issue_number in range(start_issue, end_issue + 1):
        url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/issues/{issue_number}"
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            issues.append(response.json())
        else:
            print(f"Issue #{issue_number} not found or inaccessible.")
    
    return issues

def get_one_issue(repo_owner, repo_name, token, issue_number ):
    headers = {
     "Authorization": f"token {token}",
     'Accept': 'application/vnd.github.v3+json'
    }
    
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/issues/{issue_number}"
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        issue = response.json()
    else:
        print(f"Issue #{issue_number} not found or inaccessible.")
        issue = None
    return issue

def get_latest_issue_number(repo_owner, repo_name, since_date, token):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/issues"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    params = {
        "sort": "updated",  # default is "created"
        "state": "all",  # both open and closed issues
    }
    
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code != 200:
        print (f"Error fetching issues: {response.status_code}")
        return 0 #
    issues = response.json()
    if len(issues) == 0:
        return 0
    issue = issues[0] # latest issue
    updated_at = issue['updated_at']
    if updated_at < since_date:
        return 0
    issuenum = issue['number'] # an int
    return issuenum
    
        
def get_issues_main(repo_owner, repo_name, since_date, token):
    lastissuenum = get_latest_issue_number(repo_owner, repo_name,since_date,token)
    issues = []
    if lastissuenum == 0:
        return issues
    issuenum = lastissuenum
    while issuenum > 0:
     issue = get_one_issue(repo_owner, repo_name,  token, issuenum)
     if issue == None:
         break
     updated_at = issue['updated_at']
     if updated_at < since_date:
         break  # this issue is too old
     issues.append(issue)
     issuenum = issuenum - 1
    return issues

def make_outlines(issues,owner,repo):
    lines = []
    cols = ('issue', 'date', 'state','#comm','title')
    lines.append('\t'.join(cols))
    for issue in issues:
        updated_at = issue['updated_at']
        d = updated_at[0:10] # yyyy-mm-dd
        number = issue['number']
        title = issue['title']
        state = issue['state']
        comments = get_issue_comments(owner,repo,number,token)
        ncomment = len(comments)
        nc = str(ncomment)
        vals = (str(number),d,state,nc,title)
        line = '\t'.join(vals)
        lines.append(line)
    return lines

def write_lines(fileout,lines):
 with codecs.open(fileout,"w","utf-8") as f:
   for line in lines:
    f.write(line+'\n')
 print('%s lines written to %s' % (len(lines),fileout))
 
if __name__ == "__main__":
    repo_owner = sys.argv[1] # "your-repo-owner"
    repo_name = sys.argv[2]  # "your-repo-name"
    indate = sys.argv[3] # yyyy-mm-dd
    fileout = sys.argv[4] #
    since_date = "%sT00:00:00Z" % indate # ISO 8601 format  NOT USED!
    token = os.environ['GITHUB_ACCESS_TOKEN']
    issues = get_issues_main(repo_owner, repo_name, since_date, token)
    print('%s issues returned before filtering' % len(issues))
    outlines = make_outlines(issues,repo_owner,repo_name)
    write_lines(fileout,outlines)
    
    
"""

Explanation:
Imports: The requests library is used to make HTTP requests.
Function get_issues:
Parameters: repo_owner, repo_name, since_date, and token.
URL: Constructs the API endpoint URL.
Headers: Includes the authorization token and specifies the API version.
Params: Specifies the date to filter issues and includes all states (open, closed).
Response Handling: Checks for successful response and processes the JSON data.
Issue Filtering: Excludes pull requests by checking for the absence of the pull_request key.
Main Block: Sets the repository details, date, and token, then calls the get_issues function.
Note:
Replace "your-repo-owner", "your-repo-name", and "your-github-token" with actual values.
Ensure your GitHub token has the necessary permissions to access the repository's issues.

Feel free to adapt this script to suit your specific needs!
"""
