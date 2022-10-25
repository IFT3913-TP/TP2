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
#time_in_year=`expr $time / 31536000`
time_in_year=`printf "%.4f" $((10**4 * $time/31536000))e-4`
time_between_commits=`expr $time / $n_commits`

#Si il y a en moyenne un commit par mois et que le projet a au moins 1 an d'existence alors le code est mature
code_mature="0"
if [ $time_between_commits -gt 84600 ] && [ $time -gt 31536000 ]
    then
    code_mature="1"
fi

python Mesure.py $JFREECHART_PATH $code_mature