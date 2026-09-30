# Source à énergie conservée : prolongement du calcul

## Question
Une contrainte physique indépendante d'un objectif entropique peut-elle exclure la source nulle sélectionnée dans operational_record_capacity_v1 ?

## Modèle
Source de n bits, Hamiltonien H_S = Delta * somme S_j. On fixe une couche d'énergie k*Delta avec 1 <= k < n. Copie et reset préservent exactement S. La couche positive est une condition aux limites supplémentaire : la conservation seule ne justifie ni sa valeur ni sa positivité. Sa distribution uniforme est également déclarée.

On reprend les masques CNOT, toutes les préparations mémoire, la certification de capacité sur TOUS les messages, le noyau thermique et le coût de contrôleur kappa=0.2 du test précédent. Aucun terme d'entropie n'est récompensé. epsilon=5 ; alpha=0.5, 0.7, 0.9 ; n=2,3,4 ; chaque k intérieur.

## Résultat analytique
Soit L1=max(K(1,0),K(1,1)). Le seuil de récompense de capacité est

beta_c = n*kappa + k*log(K(0,0)/L1).

Le meilleur appareil incapable est l'identité, avec mémoire vierge, reset nul et source quelconque dans la couche. Le meilleur appareil capable copie la source puis choisit pour chaque bit la sortie de reset la plus probable. La source a k bits à 1. En dessous du seuil : binom(n,k) gagnantes incapables. Au seuil : deux fois ce nombre. Au-dessus : binom(n,k) gagnantes capables. Une couche d'énergie élimine le message nul mais ne détermine pas une source unique.

18 cas et 54 comparaisons exhaustives vérifient le seuil, les ensembles complets de gagnantes et la normalisation de la référence.

## Deux distinctions nouvelles
1. A alpha=0.5, la sortie la plus probable d'un bit copié à 1 reste 1 : les gagnantes capables n'échangent aucune chaleur pendant le reset. L'ensemble conditionnel produit néanmoins une entropie totale moyenne positive. Une moyenne positive ne garantit pas une dissipation strictement positive du reset sur la gagnante.
2. A alpha=0.7 ou 0.9, les gagnantes capables remettent la mémoire à zéro. Dans la macro-partition par nombre de bits à 1, la mémoire suit 0 -> log binom(n,k) -> 0. Sa croissance n'est pas monotone. Le bain reçoit 5*k unités d'entropie. Cette partition mémoire ne décrit pas le macroétat de l'univers.

Exemple n=4,k=3,alpha=0.9 : beta_c=1.11810225038 ; 4 gagnantes capables au-dessus ; trace mémoire 0 -> log4 -> 0 ; entropie du bain sur ces gagnantes 15. Dans l'ensemble conditionnel : Delta H(S,M)=1.05115836626 ; Delta S_bain=13.3795286834 ; Sigma=14.4306870496.

## Contrôles et portée
Le calcul causal conditionnel P(s,y)=P(s)*produit K(s_j,y_j) donne exactement la même loi. La sélection MAP ne génère pas cette distribution d'ensemble ; les valeurs moyennes se rapportent explicitement à la distribution conditionnelle déclarée.

Une seconde CNOT contrôlée par la source défait la copie, conserve l'information totale et rend la mémoire vierge sans chaleur dans le modèle logique idéal. Ainsi même une source nécessairement non nulle, une mémoire initialement vierge et une copie exacte n'imposent pas un reset dissipatif. Le bain et le calendrier restent externes ; le contrôleur autonome et le bain microscopique ne sont pas dérivés. Le coût de contrôleur est un score, pas un travail physique.

Conclusion : on peut exclure l'histoire nulle par une restriction admissible indépendante de l'entropie. Cela déplace toutefois la charge explicative vers une condition d'énergie positive. Ce test ne distingue pas AE d'un modèle causal préparé de la même façon et ne démontre pas une flèche cosmologique.

Reproduction : python3 check.py ; bibliothèque standard ; résultats dans results.json.
