testing/2024review

01-15-2025
-------------------------------
Make new github access token.
See https://github.com/sanskrit-lexicon/csl-corrections/blob/master/readme_howto.txt
------------------------------

***************************************************************************
owners: funderburkjim sanskrit-lexicon sanskrit-lexicon-scans
***************************************************************************

# summary of all repos for the above list of owners

# get all repos for funderburkjim
python github_extract_repos.py funderburkjim data/funderburkjim_repos.txt

# get all repos for sanskrit-lexicon
python github_extract_repos.py sanskrit-lexicon data/sanskrit-lexicon_repos.txt

# get all repos for sanskrit-lexicon-scans
python github_extract_repos.py sanskrit-lexicon-scans data/sanskrit-lexicon-scans_repos.txt

wc -l data/*_repos.txt
  43 data/funderburkjim_repos.txt
  55 data/sanskrit-lexicon-scans_repos.txt
  69 data/sanskrit-lexicon_repos.txt
 167 total

-------------------------------
mkdir data/funderburkjim
mkdir data/sanskrit-lexicon
mkdir data/sanskrit-lexicon-scans


-------------------------------
***************************************************************************
funderburkjim repo
***************************************************************************


# get all repos for funderburkjim
python github_extract_repos.py funderburkjim data/funderburkjim_repos.txt

sh make_redo_issues.sh funderburkjim 2000-01-01 > redo_funderburkjim_issues.sh

--- sample url with commits
python github_repo_commits1.py funderburkjim elispsanskrit 2015-01-01,2016-07-31 temp.txt
# execute the script
sh redo_funderburkjim_issues.sh

# create a file that has a count of the issues
wc -l data/funderburkjim/*issues.txt > funderburkjim_issue_counts.txt


sh make_redo_commits.sh funderburkjim 2000-01-01 > redo_funderburkjim_commits.sh

sh redo_funderburkjim_commits.sh

# create a file that has a count of the commits
wc -l data/funderburkjim/*commits.txt > funderburkjim_commit_counts.txt

------------------------------------

***************************************************************************
sanskrit-lexicon repo
***************************************************************************

# get all repos for sanskrit-lexicon
python github_extract_repos.py sanskrit-lexicon data/sanskrit-lexicon_repos.txt

# run script that makes, for each repo owned by sanskrit-lexicon,
# a list of 2024 issues 
sh make_redo_issues.sh sanskrit-lexicon 2024-01-01 > redo_sanskrit-lexicon_issues.sh

#  creates data/sanskrit-lexicon/X_issues.txt   for all repos X owned by sanskrit-lexicon
sh redo_sanskrit-lexicon_issues.sh
  
# create a file that has a count of the 2024 issues
wc -l data/sanskrit-lexicon/*issues.txt > sanskrit-lexicon_2024_issue_counts.txt

# run script that makes, for each repo owned by sanskrit-lexicon,
# a list of 2024 commits 
sh make_redo_commits.sh sanskrit-lexicon 2024-01-01 > redo_sanskrit-lexicon_commits.sh

# execute that script
sh redo_sanskrit-lexicon_commits.sh


# create a file that has a count of the 2024 commit
wc -l data/sanskrit-lexicon/*commits.txt > sanskrit-lexicon_2024_commit_counts.txt


***************************************************************************
sanskrit-lexicon-scans
***************************************************************************
# get all repos for sanskrit-lexicon-scans
python github_extract_repos.py sanskrit-lexicon-scans data/sanskrit-lexicon-scans_repos.txt

------------------------------------
# run script that makes, for each repo owned by sanskrit-lexicon-scans,
# a list of issues 
sh make_redo_issues.sh sanskrit-lexicon-scans 2001-01-01 > redo_sanskrit-lexicon-scans_issues.sh

#  execute that script
#  creates data/sanskrit-lexicon-scans/X_issues.txt   for all repos X owned by sanskrit-lexicon-scans
sh redo_sanskrit-lexicon-scans_issues.sh
  
# create a file that has a count of the issues
wc -l data/sanskrit-lexicon-scans/*issues.txt > sanskrit-lexicon-scans_issue_counts.txt

# run script that makes, for each repo owned by sanskrit-lexicon-scans,
# a list of commits 
sh make_redo_commits.sh sanskrit-lexicon-scans 2001-01-01 > redo_sanskrit-lexicon-scans_commits.sh

# execute that script
sh redo_sanskrit-lexicon-scans_commits.sh

# create a file that has a count of the commit
wc -l data/sanskrit-lexicon-scans/*commits.txt > sanskrit-lexicon-scans_commit_counts.txt

***************************************************************************
sanskrit-lexicon full history
***************************************************************************
mkdir data1
mkdir data1/sanskrit-lexicon

# get all repos for sanskrit-lexicon
python github_extract_repos.py sanskrit-lexicon data1/sanskrit-lexicon_repos.txt

# run script that makes, for each repo owned by sanskrit-lexicon,
# a list of all commits 
sh make_redo_commits1.sh sanskrit-lexicon 2000-01-01 2050-12-31 > redo_sanskrit-lexicon_commits1.sh

# execute that script
sh redo_sanskrit-lexicon_commits1.sh
409 error for two repos:  MCI santamlegacy

# create a file that has a count of the commits
python count_lines.py data1 sanskrit-lexicon commits data1/sanskrit-lexicon_commit_counts.txt

# just the counts.  Not as useful as count_lines.py
# wc -l data1/sanskrit-lexicon/*commits.txt > data1/sanskrit-lexicon_commit_counts.txt


# run script that makes, for each repo owned by sanskrit-lexicon,
# a list of all issues 
sh make_redo_issues1.sh sanskrit-lexicon 2000-01-01 2050-12-31 > redo_sanskrit-lexicon_issues1.sh

# sample from redo_sanskrit-lexicon_issues1.sh:
python github_repo_issues1.py sanskrit-lexicon ACC 2000-01-01 2050-12-31 data1/sanskrit-lexicon/ACC_issues.txt

# create data1/sanskrit-lexicon/X_issues.txt for all repos X of sanskrit-lexicon
sh redo_sanskrit-lexicon_issues1.sh
  
# create a file that has a count of the issues
python count_lines.py data1 sanskrit-lexicon issues data1/sanskrit-lexicon_issue_counts.txt

# summary of activity in data1
cd data1
python repo_activity.py sanskrit-lexicon './' sanskrit-lexicon_activity.txt
# note:
 MCI and santamlegacy have no commits!
 csl-pywork 

***************************************************************************
sanskrit-lexicon-scans full history
***************************************************************************
mkdir data1
mkdir data1/sanskrit-lexicon-scans

# get all repos for sanskrit-lexicon-scans
python github_extract_repos.py sanskrit-lexicon-scans data1/sanskrit-lexicon-scans_repos.txt
# 55 repos

# run script that makes, for each repo owned by sanskrit-lexicon-scans,
# a list of all commits 
sh make_redo_commits1.sh sanskrit-lexicon-scans 2000-01-01 2050-12-31 > redo_sanskrit-lexicon-scans_commits1.sh

# sample repo
python github_repo_commits1.py sanskrit-lexicon-scans ACC 2000-01-01 2050-12-31 temp.txt


# execute that script
sh redo_sanskrit-lexicon-scans_commits1.sh


# create a file that has a count of the commit
python count_lines.py data1 sanskrit-lexicon-scans commits data1/sanskrit-lexicon-scans_commit_counts.txt

# run script that makes, for each repo owned by sanskrit-lexicon-scans,
# a list of all issues 
sh make_redo_issues1.sh sanskrit-lexicon-scans 2000-01-01 2050-12-31 > redo_sanskrit-lexicon-scans_issues1.sh

# sample from redo_sanskrit-lexicon-scans_issues1.sh:
python github_repo_issues1.py sanskrit-lexicon-scans ACC 2000-01-01 2050-12-31 temp.txt

# create data1/sanskrit-lexicon-scans/X_issues.txt for all repos X of sanskrit-lexicon-scans
sh redo_sanskrit-lexicon-scans_issues1.sh
  
# create a file that has a count of the 2024 issues
python count_lines.py data1 sanskrit-lexicon-scans issues data1/sanskrit-lexicon-scans_issue_counts.txt

# summary of activity in data1
cd data1
python repo_activity.py sanskrit-lexicon-scans './' sanskrit-lexicon-scans_activity.txt


***************************************************************************
commit this work and update associated issue

***************************************************************************
01-28-2015
mkdir data1a
mkdir data1a/andhrabharati

--- test 1
python github_repo_issues1a.py sohilpandya octocat Hello-World 2024-06-01 2050-12-31 temp_octocat.txt

--- test 2
python github_repo_issues1a.py Andhrabharati sanskrit-lexicon pwg 2024-01-01 2050-12-31 temp_test2.txt

python github_repo_issues1a.py Andhrabharati sanskrit-lexicon mws 2024-01-01 2050-12-31 temp_test3.txt

python github_repo_issues1a.py Andhrabharati sanskrit-lexicon mws 2024-01-01 2050-12-31 andhrabharati/mws_issues.txt


# make script for all repos
sh make_redo_issues1a.sh sanskrit-lexicon 2000-01-01 2050-12-31 Andhrabharati > redo_issues1a.sh

# run the script
sh redo_issues1a.sh  # takes several minutes

# aggregate
cat andhrabharati/*_issues.txt > andhrabharati_activity.txt


***************************************************************************
***************************************************************************
miscellany
***************************************************************************


sh make_redo_issues.sh sanskrit-lexicon-scans 2024-01-01 > redo_sanskrit-lexicon-scans_issues.sh
sh redo_sanskrit-lexicon-scans_issues.sh
#  creates data/sanskrit-lexicon-scans/X_issues.txt   for all repos X owned by sanskrit-lexicon-scans
  
# create a file that has a count of the 2024 issues
wc -l data/sanskrit-lexicon-scans/*issues.txt > sanskrit-lexicon-scans_2024_issue_counts.txt

python github_repo_commits.py sanskrit-lexicon AP90 2023-01-01,2024-01-01 temp1.txt

------------------------------
test_get_comments_from_issue.py is from copilot.
It gets ALL comments  (using pagination) from a sample owner, repo, issue number

 minor modification: token = os.environ['GITHUB_ACCESS_TOKEN']
 
The function get_issue_comments(owner, repo, issue_number, token)
does the heavy lifting, and can be imported by another program.

------------------------------
test_get_comments_from_issue_1.py
 similar to above, but gets "owner, repo, issue_number"
 from command-line

Sample usages:
python test_get_comments_from_issue_1.py funderburkjim elispsanskrit 51
34 comments in https://github.com/funderburkjim/elispsanskrit/issues/51

python test_get_comments_from_issue_1.py sanskrit-lexicon pwg 72
16 comments in https://github.com/sanskrit-lexicon/pwg/issues/72


------------------------------


Miscellany
------------------------------------
# test program for commits
python github_repo_commits.py funderburkjim ankiwork '2000-01-01' temp_funderburkjim_ankiwork_commits.txt

# make a script that generates commits file for all repos owned by funderburkjim
sh make_redo_commits.sh funderburkjim 2000-01-01 > redo_funderburkjim_commits.sh

# run that script
sh redo_funderburkjim_commits.sh

unexpected error(s)
python github_repo_commits.py funderburkjim ben 2000-01-01 data/funderburkjim/ben_commits.txt
Error fetching commits: 409
get_commits_main: no commits for ben


python github_repo_issues.py funderburkjim ankiwork '2000-01-01' data/funderburkjim_ankiwork_issues.txt

python github_repo_issues.py sanskrit-lexicon csl-orig '2010-01-01' data/slex_issues.txt

--------------------------------
# adapted from copilot
python github_repo_commits_test.py

python github_repo_commits_test1.py funderburkjim ankiwork data/funderburkjim_ankiwork_commits.txt

python github_repo_commits_test1.py sanskrit-lexicon pwg data/slex_pwg_commits.txt

python github_repo_commits_test1.py sanskrit-lexicon csl-orig data/slex_csl-orig_commits.txt


----- issue comments
https://api.github.com/repos/funderburkjim/elispsanskrit/issues
 array of objects c:
  c['number']  The issue number
  'state'  values : 'open', 'closed'
  'created_at'
  'updated_at'
  'closed_at'

parents
python github_extract_issues.py sanskrit-lexicon csl-orig data/slex_issues.txt

python github_extract_issues.py funderburkjim elispsanskrit data/jim_elispsanskrit_issues.txt


------------------
commits
https://api.github.com/repos/funderburkjim/ankiwork/commits/08b89170f5fae01fa94b7eafa116b2978ba85612
    "parents": [
        {
            "sha": "de17ca48aa0bcbad94c38459d94c900496e6e950",
            "url": "https://api.github.com/repos/funderburkjim/ankiwork/commits/de17ca48aa0bcbad94c38459d94c900496e6e950",
            "html_url": "https://github.com/funderburkjim/ankiwork/commit/de17ca48aa0bcbad94c38459d94c900496e6e950"
        }
    ],

Using "url"  
https://api.github.com/repos/funderburkjim/ankiwork/commits/de17ca48aa0bcbad94c38459d94c900496e6e950
    "parents": [],
So this is the first commit!

-------------------------------------------------------
//https:docs.github.com/en/rest/issues/comments?apiVersion=2022-11-28
github api query parameters
sort: created  (updated)
direction

Path parameters
Name, Type, Description

owner string Required
The account owner of the repository. The name is not case sensitive.

repo string Required
The name of the repository without the .git extension. The name is not case sensitive.

Query parameters
Name, Type, Description
sort string
The property to sort the results by.

Default: created

Can be one of: created, updated

di
direction string
Either asc or desc. Ignored without the sort parameter.

Can be one of: asc, desc

since string
Only show results that were last updated after the given time. This is a timestamp in ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ.

per_page integer
The number of results per page (max 100). For more information, see "Using pagination in the REST API."

Default: 30

page integer
The page number of the results to fetch. For more information, see "Using pagination in the REST API."

Default: 1
============================================================
https://docs.github.com/en/rest/commits/commits?apiVersion=2022-11-28
Parameters for "List commits"
Headers
Name, Type, Description
accept string
Setting to application/vnd.github+json is recommended.

Path parameters
Name, Type, Description
owner string Required
The account owner of the repository. The name is not case sensitive.

repo string Required
The name of the repository without the .git extension. The name is not case sensitive.

Query parameters
Name, Type, Description
sha string
SHA or branch to start listing commits from. Default: the repository’s default branch (usually main).

path string
Only commits containing this file path will be returned.

author string
GitHub username or email address to use to filter by commit author.

committer string
GitHub username or email address to use to filter by commit committer.

since string
Only show results that were last updated after the given time. This is a timestamp in ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ. Due to limitations of Git, timestamps must be between 1970-01-01 and 2099-12-31 (inclusive) or unexpected results may be returned.

until string
Only commits before this date will be returned. This is a timestamp in ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ. Due to limitations of Git, timestamps must be between 1970-01-01 and 2099-12-31 (inclusive) or unexpected results may be returned.

per_page integer
The number of results per page (max 100). For more information, see "Using pagination in the REST API."

Default: 30

page integer
The page number of the results to fetch. For more information, see "Using pagination in the REST API."

Default: 1

HTTP response status codes for "List commits"
Status code	Description
200	
OK

400	
Bad Request

404	
Resource not found

409	
Conflict

500
Internal Error

python copilot_test_commits.py


https://docs.github.com/en/rest?apiVersion=2022-11-28

========================================================
https://docs.github.com/en/rest/issues?apiVersion=2022-11-28

https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}/comments

https://api.github.com/repos/sanskrit-lexicon/mws/issues/1/comments

