"""
github_repo_commits1
start_date, last_date

"""
import requests
from datetime import datetime
import sys,re,codecs
import os # for os.environ
from githubutil import get_commits_between_dates

def get_commit_date(commit):
    return commit['commit']['author']['date']

def make_outlines(commits):
    lines = []
    cols = ('date', 'sha' , 'title')
    lines.append('\t'.join(cols))
    for icommit,commit in enumerate(commits):
        updated_at = get_commit_date(commit)
        d = updated_at[0:10] # yyyy-mm-dd
        sha = commit['sha']
        message = commit['commit']['message']
        #m = message.replace('\n',' LB ')
        m = re.sub(r'[\n\r]',' LB ',message)
        vals = (d,sha,m)
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
    first_ymd = sys.argv[3] # 2023-01-01
    last_ymd = sys.argv[4]
    fileout = sys.argv[5] #
    start_date = "%sT00:00:00Z" % first_ymd # ISO 8601 format  NOT USED!
    end_date  = "%sT23:59:59Z" % last_ymd
    token = os.environ['GITHUB_ACCESS_TOKEN']
    commits = get_commits_between_dates(repo_owner, repo_name,
                               start_date, end_date, token)
    print('%s commits from %s to %s' % (len(commits),start_date,end_date))
    outlines = make_outlines(commits)
    write_lines(fileout,outlines)
    
