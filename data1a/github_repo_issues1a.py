"""
github_repo_issues1a.py
"""
import requests
from datetime import datetime
import sys,re,codecs
import os # for os.environ
#from githubutil import get_issue_comments
sys.path.append('../')
from githubutil import get_commits_between_dates
from githubutil import get_issues_between_dates
from githubutil import get_issue_comments

def unused_get_issues_range(repo_owner, repo_name ):
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

def unused_get_one_issue(repo_owner, repo_name, token, issue_number ):
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

def unused_get_latest_issue_number(repo_owner, repo_name, since_date, token):
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
    
        
def unused_get_issues_main(repo_owner, repo_name, since_date, token):
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

def count_user(user_name,issue_user,comments):
    nall = len(comments)
    n = 0
    if user_name == issue_user:
        n = n + 1
    for comment in comments:
        user = comment['user']['login']
        if user_name == user:
            n = n + 1
    return (nall,n)

def make_outlines(issues,owner,repo,user_name):
    lines = []
    #cols = ('date','issue',   'state','comm','title')
    cols = ('repo','date', 'issue',  'state',user_name,'title')
    lines.append('\t'.join(cols))
    for issue in issues:
        created_at = issue['created_at']
        issue_date = created_at[0:10] # yyyy-mm-dd
        number = issue['number'] # int
        title = issue['title']
        state = issue['state'] # open,closed
        issue_user = issue['user']['login']
        comments = get_issue_comments(owner,repo,number,token)
        ncomment,nuser_comment = count_user(user_name,issue_user,comments)
        if nuser_comment == 0:
            continue
        #ncomment = len(comments)
        nc = str(ncomment)
        ncu = str(nuser_comment)
        #vals = (str(number),d,state,nc,title)
        vals = (repo,issue_date,str(number),state,ncu,title)
        line = '\t'.join(vals)
        lines.append(line)
    return lines

def write_lines(fileout,lines):
 with codecs.open(fileout,"w","utf-8") as f:
   for line in lines:
    f.write(line+'\n')
 print('%s lines written to %s' % (len(lines),fileout))
 
if __name__ == "__main__":
    user_name  = sys.argv[1]      # github user name (for issue comments)
    repo_owner = sys.argv[2] # "your-repo-owner"
    repo_name = sys.argv[3]  # "your-repo-name"
    first_ymd = sys.argv[4] # 2023-01-01
    last_ymd = sys.argv[5]
    fileout = sys.argv[6] #
    start_date = "%sT00:00:00Z" % first_ymd # ISO 8601 format  NOT USED!
    end_date  = "%sT23:59:59Z" % last_ymd
    token = os.environ['GITHUB_ACCESS_TOKEN']
    issues = get_issues_between_dates(repo_owner, repo_name,
                               start_date, end_date, token)
    print('#issues=',len(issues))
    
    print('All %s issues from %s to %s' % (len(issues),start_date,end_date))
    outlines = make_outlines(issues,repo_owner,repo_name,user_name)
    write_lines(fileout,outlines)
    
