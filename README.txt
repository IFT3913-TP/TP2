lien du git : https://github.com/IFT3913-TP/TP2/

Prérequis:
 - Python >= 3.8
 - Java >= 8
 - sh shell
 - Distribution Linux permettant de satisfaire les prérequis précedents

Pour lancer la procédure de réponse aux question automatisé, il faut d'abord cloner le dépôt git de jfreechart puis il faut modifier la variable JFREECHART_PATH du script Mesure.sh pour qu'elle pointe vers le dossier dans lequel est cloné le dépôt.
Ensuite il suffit simplement d'exécter le script shell comme suit : 
./Mesure.sh
Il peut être nécessaire d'autiriser l'exécution du script avec la commande suivante : chmod +x Mesure.sh

La configuration de pmd peut être modifiée en éditant les fichiers xml sous config/pmd/rules 
Les sous programmes utilisés par la procédure sont localisés sous tools/

Le dossier output/temp comporte la sortie sous forme de fichier .csv du programme pmd, ces fichiers sont automatiquement lus et traités par le script python


