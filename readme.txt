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

# Minor
-------------------------------
***************************************************************************
funderburkjim repo
***************************************************************************

# get all repos for funderburkjim
python github_extract_repos.py funderburkjim data/funderburkjim_repos.txt

sh make_redo_issues.sh funderburkjim 2000-01-01 > redo_funderburkjim_issues.sh

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
***************************************************************************
------------------------------------
sh make_redo_issues.sh sanskrit-lexicon-scans 2024-01-01 > redo_sanskrit-lexicon-scans_issues.sh
sh redo_sanskrit-lexicon-scans_issues.sh
#  creates data/sanskrit-lexicon-scans/X_issues.txt   for all repos X owned by sanskrit-lexicon-scans
  
# create a file that has a count of the 2024 issues
wc -l data/sanskrit-lexicon-scans/*issues.txt > sanskrit-lexicon-scans_2024_issue_counts.txt

***************************************************************************

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
python issue_comments_
------------------------------



***************************************************************************
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
---
------------------------------------
------------------------------------
------------------------------------
------------------------------------
------------------------------------

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
https://docs.github.com/en/rest/issues/comments?apiVersion=2022-11-28
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
