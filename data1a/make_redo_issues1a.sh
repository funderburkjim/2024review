owner=$1
start=$2
end=$3
user=$4
reposfile="${owner}_repos.txt"
cat $reposfile | while read repo
do
    cmd="python github_repo_issues1a.py ${user} ${owner} ${repo} ${start} ${end} ${user}/${repo}_issues.txt"
    echo ""
    echo "# echo  ${user} ${owner} ${repo} ${start} ${end}"
    echo "$cmd"
    echo ""
done
