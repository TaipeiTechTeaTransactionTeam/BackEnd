git add .
git reset HEAD manage.py
if [ $# -ne 0 ];then
    echo $1
    git commit -m "$1"  
else
    echo "input a name for commit"
    read commitN
    git commit -m "$commitN"
fi


