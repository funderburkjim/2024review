"""
github_repo_commits
"""
import requests
from datetime import datetime
import sys,re,codecs
import os # for os.environ

def get_one_commit(repo_owner, repo_name, token, commit_sha ):
    headers = {
     "Authorization": f"token {token}",
     'Accept': 'application/vnd.github.v3+json'
    }
    
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/commits/{commit_sha}"
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        commit = response.json()
    else:
        print(f"Commit #{commit_sha} not found or inaccessible.")
        commit = None
    return commit

def get_latest_commit(repo_owner, repo_name, since_date, token):
    # returns last commit dated no earlier than since_date
    # returns 0 if no such
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/commits"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    params = {
        "sort": "updated",  # default is "created"
        # "state": "all",  # 
    }
    
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code != 200:
        print (f"Error fetching commits: {response.status_code}")
        return 0 #
    commits = response.json()
    if len(commits) == 0:
        return 0
    commit = commits[0] # latest commit
    return commit
    
def get_commit_date(commit):
    return commit['commit']['author']['date']

def get_commits_main(repo_owner, repo_name, since_date, token):
    commits = []
    commit = get_latest_commit(repo_owner, repo_name,since_date,token)
    if commit == 0:
        print('get_commits_main: no commits for %s' % repo_name)
        return commits
    updated_at = get_commit_date(commit)
    if updated_at < since_date:
        print('get_commits_main: no commits for %s since %s (%s)' %
              (repo_name,since_date, updated_at))
        return commits
        
    sha = commit['sha'] # 
    #print('sha = %s for repo %s' % (sha,repo_name))
    #print('debug ending early')
    #exit(1)
    #commits = [commit]
    while sha != 0:
     commit = get_one_commit(repo_owner, repo_name,  token, sha)
     if commit == None:
         break
     updated_at = get_commit_date(commit)
     if updated_at < since_date:
         break  # this commit is too old. no
     commits.append(commit)
     # get parent sha
     parents = commit['parents']  # assumed to be a list, possibly empty
     if parents == []:
        break  # no more commits
     parent = parents[0]
     parentsha = parent['sha']
     sha = parentsha  # continue while loop
    return commits

def make_outlines(commits):
    lines = []
    cols = ('date', 'sha' , 'title')
    lines.append('\t'.join(cols))
    for icommit,commit in enumerate(commits):
        updated_at = get_commit_date(commit)
        d = updated_at[0:10] # yyyy-mm-dd
        sha = commit['sha']
        message = commit['commit']['message']
        m = message.replace('\n',' LB ')
        vals = (d,sha,m)
        line = '\t'.join(vals)
        #nid = icommit+1
        #line = '%03d: %s %s\t%s' %(nid,d,m,sha)
        #line = f"Commit #{commit['number']}: {d} {commit['title']}"
        lines.append(line)
    return lines

def make_outlines_version1(commits):
    lines = []
    for icommit,commit in enumerate(commits):
        updated_at = get_commit_date(commit)
        d = updated_at[0:10] # yyyy-mm-dd
        sha = commit['sha']
        message = commit['commit']['message']
        m = message.replace('\n',' LB ')
        nid = icommit+1
        line = '%03d: %s %s\t%s' %(nid,d,m,sha)
        #line = f"Commit #{commit['number']}: {d} {commit['title']}"
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
    indate = sys.argv[3] # 2023-01-01
    fileout = sys.argv[4] #
    # indate = '2001-01-01'  # Gets all Github work for cdsl
    #indate = '2024-01-01'  # 
    since_date = "%sT00:00:00Z" % indate # ISO 8601 format  NOT USED!
    token = os.environ['GITHUB_ACCESS_TOKEN']
    commits = get_commits_main(repo_owner, repo_name, since_date, token)
    print('%s commits returned before filtering' % len(commits))
    outlines = make_outlines(commits)
    write_lines(fileout,outlines)
    
