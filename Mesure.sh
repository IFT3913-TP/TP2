#!/bin/sh
JFREECHART_PATH="/home/loic/Téléchargements/jfreechart/"
CURRENT_DIR=`pwd`
cd $JFREECHART_PATH

first_commit=`git log --reverse --date="format:%s" --format="format:%ad" | head -n 1`
last_commit=`git log --date="format:%s" --format="format:%ad" | head -n 1`
# n_commits est le nombre total de commits
n_commits=`git log --oneline | wc -l`
cd $CURRENT_DIR

# la valeur time est l'écart de temps en sec. entre le premier et le dernier commit
time=`expr $last_commit - $first_commit`
echo $time

echo $n_commits
python Mesure.py $JFREECHART_PATH