owner=$1
start=$2
reposfile="data/${owner}_repos.txt"
cat $reposfile | while read repo
do
    cmd="python github_repo_commits.py ${owner} ${repo} ${start} data/${owner}/${repo}_commits.txt"
    echo "echo $cmd"
    echo "$cmd"
    echo ""
done
