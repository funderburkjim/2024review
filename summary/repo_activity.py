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
 def __init__(self,owner,datadir,reponame):
  self.reponame = reponame
  self.owner = owner
  self.datadir = datadir
  self.commits = self.init_commits(datadir,owner,reponame)
  self.issues = self.init_issues(datadir,owner,reponame)
 def init_commits(self,datadir,owner,reponame):
  filein = '%s/%s/%s_commits.txt' % (datadir,owner,reponame)
  lines = read_lines(filein)
  commits = lines[1:]  # skip tsv-colnames
  return commits
 def init_issues(self,datadir,owner,reponame):
  filein = '%s/%s/%s_issues.txt' % (datadir,owner,reponame)
  lines = read_lines(filein)
  issues = lines[1:]  # skip tsv-colnames
  return issues

def make_lines_sort(tuples,owner):
 if owner == 'sanskrit-lexicon':
  # sort by ncommits + nissues, descending order
  tuples1 = sorted(tuples, key = lambda tuple: tuple[1]+tuple[2],reverse=True)
 else:
  # sort by reponame (tuples[0])  KLUDGE
  tuples1 = sorted(tuples, key = lambda tuple: tuple[0].lower())
 return tuples1
     
def make_lines(repos,owner):
 tuples = []
 for repo in repos:
  name = repo.reponame
  ncommits = len(repo.commits)
  nissues  = len(repo.issues)
  tuple = (name,ncommits,nissues)
  tuples.append(tuple)
 tuples1 = make_lines_sort(tuples,owner)
 # generate lines to be written
 lines = []
 titles = ('ncommit','nissues','repo')
 line = '\t'.join(titles)
 lines.append(line)
 for t in tuples1:
  a = [ str(t[1]), str(t[2]),t[0]]
  line = '\t'.join(a)
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

