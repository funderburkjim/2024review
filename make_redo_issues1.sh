owner=$1
start=$2
end=$3
reposfile="data/${owner}_repos.txt"
cat $reposfile | while read repo
do
    cmd="python github_repo_issues1.py ${owner} ${repo} ${start} ${end} data1/${owner}/${repo}_issues.txt"
    echo ""
    echo "echo ${owner} ${repo} ${start} ${end}"
    echo "$cmd"
    echo ""
done
