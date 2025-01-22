filename=$1
cat $filename | while read p
do
cmd="python github_repo_issues.py funderburkjim $p '2000-01-01' data/funderburkjim_${p}_issues.txt"
    echo "$cmd"
done
