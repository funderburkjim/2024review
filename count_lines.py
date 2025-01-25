"""
count_lines.py 

"""
import requests
from datetime import datetime
import sys,re,codecs
import os # for os.environ

def write_lines(fileout,lines):
 with codecs.open(fileout,"w","utf-8") as f:
   for line in lines:
    f.write(line+'\n')
 print('%s lines written to %s' % (len(lines),fileout))

def read_lines(filein):
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def get_result(repo,parm,lines):
 lines1 = lines[1:] # assume first line is a title line
 result = {}
 result['repo'] = repo
 result['parm'] = parm
 n = len(lines1)
 result['count'] = str(n)
 if n == 0:
  first = '?'
  last = '?'
 else:
  firstline = lines1[-1]  # assume lines in reverse order by date
  parts = firstline.split('\t')
  first = parts[0]  # date 
  lastline = lines1[0]  # assume lines in reverse order by date
  parts = lastline.split('\t')
  last = parts[0]  # date 
 result['first'] = first
 result['last'] = last
 return result

def get_results(datadir,owner,repofile,parm):
 # datadir = 'data1'
 # owner = 'sanskrit-lexicon'
 reponames = read_lines(repofile)
 # parm = 'commits'
 results = []
 for repo in reponames:
  filein = '%s/%s/%s_%s.txt' %(datadir,owner,repo,parm)
  try:
   lines = read_lines(filein)
  except:
   print('Problem reading',filein)
   exit(1)
  n = len(lines)
  result = get_result(repo,parm,lines)
  results.append(result)
 return results

def write_results(fileout,results):
    lines = []
    titlevals = ['repo','parm','count','first','last'] 
    line = '\t' . join(titlevals)
    lines.append(line)
    for result in results:
        repo = result['repo']
        parm = result['parm']
        count = result['count']
        first = result['first']
        last = result['last']
        vals = (repo,parm,count,first,last)
        line = '\t' . join(vals)
        lines.append(line)
    write_lines(fileout,lines)
    
if __name__ == "__main__":
    datadir = sys.argv[1]
    owner = sys.argv[2]
    repofile = '%s/%s_repos.txt' %(datadir,owner) # hard-coded!
    parm = sys.argv[3]  # commits, issues
    fileout = sys.argv[4] #
    results = get_results(datadir,owner,repofile,parm)
    write_results(fileout,results)
