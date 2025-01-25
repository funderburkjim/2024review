"""

"""

# from datetime import datetime
import sys,re,codecs

def read_lines(filein,printflag=False):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 if printflag:
  print(len(lines),"from",filein)
 return lines

def write_lines(fileout,lines):
 with codecs.open(fileout,"w","utf-8") as f:
   for line in lines:
    f.write(line+'\n')
 print('%s lines written to %s' % (len(lines),fileout))

def get_repos(owner,datadir):
 filein = '%s/%s_repos.txt' %(datadir,owner)
 print(filein)
 lines = read_lines(filein)  # the list of repos
 return lines

class Repo:
 """
commits columns=['date', 'sha', 'title']
issues columns=['date', 'issue', 'state', 'title']

"""
 def __init__(self,owner,datadir,reponame):
  self.reponame = reponame
  self.owner = owner
  self.datadir = datadir
  self.commits = self.init_summary(datadir,owner,reponame,'commits')
  self.issues =  self.init_summary(datadir,owner,reponame,'issues')
 def init_summary(self,datadir,owner,reponame,typename):
  filein = '%s/%s/%s_commits.txt' % (datadir,owner,reponame)
  #typename = 'commits'
  lines = read_lines(filein)
  lines1 = lines[1:]  # skip tsv-colnames
  columns = lines[0].split('\t')
  #print('%s columns=%s' %(typename,columns))
  #exit(1)
  array = []
  for iline,line in enumerate(lines1):
   vals = line.split('\t')
   if len(vals) < len(columns):
    print('%s %s ERROR' % (reponame,typename))
    print('%s columns: %s' %(len(columns),columns))
    print('%s values : %s' %(len(vals),vals))
    for i,val in enumerate(vals):
     print('line %s = %s' % (iline + 2,line))
     column = columns[i]
     print('columns[%s]=%s, val[%s] = %s' % (i,column,i,val))
    exit(1)
   d = {}
   for i,column in enumerate(columns):
    val = vals[i]
    d[column] = val
   #if len(columns) < len(vals):
   # # probably tabs in the title of commit
   # pass
   array.append(d)
  return array

 def unused_init_issues(self,datadir,owner,reponame):
  filein = '%s/%s/%s_issues.txt' % (datadir,owner,reponame)
  typename = 'issues'
  lines = read_lines(filein)
  lines1 = lines[1:]  # skip tsv-colnames
  columns = lines[0].split('\t')
  #print('%s columns=%s' %(typename,columns))
  #exit(1)
  d = {}
  for iline,line in enumerate(lines1):
   vals = line.split('\t')
   if len(vals) < len(columns):
    print('%s %s ERROR' % (reponame,typename))
    print('%s columns: %s' %(len(columns),columns))
    print('%s values : %s' %(len(vals),vals))
    for i,val in enumerate(vals):
     print('line %s = %s' % (iline + 2,line))
     column = columns[i]
     print('columns[%s]=%s, val[%s] = %s' % (i,column,i,val))
    exit(1)
   for i,column in enumerate(columns):
    val = vals[i]
    d[column] = val
   if len(columns) < len(vals):
    # probably tabs in the title of commit
    pass
  return d

def unused_make_lines_sort(tuples,owner):
 if owner == 'sanskrit-lexicon':
  # sort by ncommits + nissues, descending order
  tuples1 = sorted(tuples, key = lambda tuple: tuple[1]+tuple[2],reverse=True)
 else:
  # sort by reponame (tuples[0])  KLUDGE
  tuples1 = sorted(tuples, key = lambda tuple: tuple[0].lower())
 return tuples1

def get_commit_dates(commits,reponame):
 # first and last date of commits
 # commits is an array of dicts
 firstdate = '?'
 lastdate = '?'
 if len(commits) != 0:
  lastdate = commits[0]['date']
  firstdate  = commits[-1]['date']
 return firstdate,lastdate

def make_lines(repos,owner):
 tuples = []
 for repo in repos:
  name = repo.reponame
  ncommits = len(repo.commits)
  nissues  = len(repo.issues)
  first_c,last_c = get_commit_dates(repo.commits,repo.reponame)
  d = {}
  d['repo'] = name
  d['ncommit'] = str(ncommits)
  d['nissue'] = str(nissues)
  d['first-c'] = first_c
  d['last-c'] = last_c
  tuples.append(d)
 # tuples1 = make_lines_sort(tuples,owner)
 # don't sort.
 tuples1 = tuples  
 # generate lines to be written
 lines = []
 # titles determines order of tab-delimited values
 titles = ('ncommit','nissue','first-c','last-c','repo')
 line = '\t'.join(titles)
 lines.append(line)
 for d in tuples1:
  vals = [d[x] for x in titles]
  line = '\t'.join(vals)
  lines.append(line)
 return lines

def init_repos(owner,datadir,reponames):
 repos = []
 for reponame in reponames:
  repo = Repo(owner,datadir,reponame)
  repos.append(repo)
 return repos
if __name__ == "__main__":
 owner = sys.argv[1]  # github repo owner, e.g. sanskrit-lexicon
 datadir = sys.argv[2] # relative path to the data directory
 fileout = sys.argv[3]  # output file for this summary

 # read repos from this owner
 reponames = get_repos(owner,datadir)
 repos = init_repos(owner,datadir,reponames)
 outlines = make_lines(repos,owner)
 write_lines(fileout,outlines)

