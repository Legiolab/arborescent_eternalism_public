# Témoin fini : sélection, préparation rare et entropie

Ce modèle fini distinct remplace le noyau de réinitialisation précédent par une dynamique locale sur un réseau de six bits. Cette publication de calcul ne modifie pas le manuscrit et ne conserve pas les anciennes constantes 0,469 et 0,0822.

## 1. Modèle et projection

L'espace physique sur une coupe est X={0,1}^6. Une histoire comporte quatre états (x0,x1,x2,x3). À chaque transition, elle reste immobile ou retourne un seul bit. E est l'arbre des préfixes admissibles : sa racine vide se prolonge par l'un des 64 états initiaux, puis par les sept actions disponibles à chaque étape. Les feuilles sont les histoires complètes. Pi envoie une feuille sur la suite physique obtenue en exécutant ses actions ; r_Sigma extrait x0. Les actions sont reconstructibles depuis deux états consécutifs : Pi est ici bijective sur les feuilles. Cette construction explicite la correspondance, mais reste un codage jouet, sans espace-temps relativiste.

Le noyau P(x,x)=1/2, P(x,y)=1/12 si les états diffèrent d'un bit, et zéro sinon est symétrique, irréductible, apériodique. Il conserve le comptage uniforme mu(x)=1/64. Chaque déplacement modifie un seul site. Il ne conserve pas une énergie et n'est pas une dérivation cosmologique.

La loi initiale est p(x)=0,8/20=1/25 si K(x)=3, et 0,2/44=1/220 sinon. Elle est normalisée et privilégie le macroétat central. Les poids complets sont w(H)=p(x0) produit_t P(xt,xt+1). Toutes ces lois sont fixées avant la sélection.

## 2. Entropie physique du témoin

Les macroétats sont les classes de même nombre K de bits à un. Leur multiplicité est binom(6,K). L'entropie de Boltzmann sans constante additive est S_B(x)=log binom(6,K(x)), en unités k_B=1.

Le macroétat K=0 comporte un seul des 64 microétats : mu(K=0)=1/64, contre mu(K=3)=20/64. Il a une entropie 0, contre log20 au centre. Cette rareté est relative au comptage choisi ; ce petit témoin ne démontre pas une rareté exponentielle asymptotique.

## 3. Contribution tardive et sélection

La tâche consiste à atteindre z=(1,1,1,0,0,0) en ayant retourné chacun des trois premiers bits exactement une fois pendant les trois transitions. A(H)=1 lorsque la tâche est achevée, zéro sinon. Le score n'est attribué qu'à la fin et dépend de la mémoire des actions. Il n'est pas une fonction du seul état final : une histoire immobile en z n'est pas récompensée.

J_beta(H)=-log w(H)-beta A(H), avec beta>=0. Le critère porte sur les histoires complètes. Il n'ajoute ni exclusion d'histoires ni modification des poids.

Toute histoire récompensée commence nécessairement en 000000, puis retourne les trois premiers bits dans un ordre quelconque. Il y en a 3!=6. Leurs nombres d'excitations sont 0,1,2,3 et leurs entropies sont 0,log6,log15,log20 : croissance stricte sur l'horizon du témoin.

ATTENTION : cette propriété est une conséquence de la tâche choisie, qui encode implicitement la préparation et les déplacements favorisés. A ne contient pas explicitement S_B, mais la tâche favorise précisément ces histoires. Ce témoin établit une possibilité mathématique, pas une explication indépendante de cette préférence. Appeler A « agentivité » exige de motiver le système, ses actions, sa mémoire et son objectif. Le noyau décrit ici les possibilités de déplacements ; il n'est pas une politique de contrôle causal d'un agent.

## 4. Seuil exact et preuve globale

Sans récompense, w(H)<= (1/25)(1/2)^3. L'égalité est atteinte exactement par les vingt histoires constantes issues de K=3. Leur entropie est maximale et constante.

Chaque histoire récompensée a poids (1/220)(1/12)^3. Leur rapport de coût avec le meilleur concurrent non récompensé vaut

beta_c = log(220/25) + 3 log(12/2) = log(8,8) + 3 log6 = 7,550030129168326.

Pour beta<beta_c, les vingt histoires constantes centrales gagnent. Au seuil, elles sont à égalité avec les six histoires récompensées. Pour beta>beta_c, seules les six histoires récompensées gagnent : chacune commence rare et présente une croissance stricte de S_B. Ceci compare toutes les concurrentes : les non récompensées ne peuvent battre le maximum de référence ; toutes les récompensées ont le même poids.

Il n'y a pas de gagnant unique. Une règle de départage fixée indépendamment peut en sélectionner un, sans changer les conclusions communes aux six. Le témoin ne dérive pas cette règle.

## 5. Relaxation d'ensemble distincte

Pour comparaison, partir de rho0=delta_000000 et appliquer P donne une entropie de Shannon croissante : 0 ; 1,589027 ; 2,492801 ; 3,051154 ; 3,410866 ; 3,648991 ; 3,809347 aux temps 0 à 6, vers log64.

La croissance suit aussi analytiquement de la stricte concavité : chaque probabilité nouvelle est une moyenne positive de la probabilité du site et de celles de ses six voisins. L'égalité d'entropie exige que les probabilités soient égales sur chaque arête, donc uniformes puisque le graphe est connecté. Depuis delta, la distribution ne devient pas exactement uniforme à un temps fini : les modes propres non nuls présents initialement subsistent. Cette entropie d'ensemble est distincte de S_B le long des gagnantes.

L'ensemble delta est ici préparé par une règle explicite : répéter le même état initial sélectionné. Le calcul n'identifie pas cette distribution avec un ensemble produit automatiquement par la sélection globale, et les trajectoires de cet ensemble ne sont pas les six seules gagnantes.

## 6. Conclusions et limites

Conservable : une dynamique locale fixée avant J, un objectif tardif dépendant de la mémoire et une référence favorisant le macroétat central peuvent produire des gagnantes à préparation rare dont l'entropie de macroétat augmente. Le seuil de compensation est exact et vérifié par énumération complète de 21 952 histoires.

Non démontré : nécessité de A pour toute flèche thermodynamique ; croissance pour une dynamique ou une tâche quelconque ; justification physique de l'objectif et de la mesure ; extrapolation cosmologique ; croissance au-delà des trois étapes ; anciennes bornes numériques ; contrôle causal par un agent.

Le témoin montre que la structure demandée est cohérente. Sa force explicative dépend encore d'une raison indépendante pour laquelle la tâche favorisée serait celle d'un agent physique. Sans cela, il est possible de fabriquer la conclusion par le choix de l'objectif.


## Reproduction publique

```bash
python proofs/paper-c-modal-rarity/computational/local_delayed_objective_v1/check.py
```

Python 3, bibliothèque standard uniquement. Comparer la sortie avec results.json. Le script énumère toutes les histoires admissibles et vérifie les nombres de gagnantes de part et d'autre du seuil et au seuil. Les comparaisons numériques utilisent une tolérance de 1e-10 ; la preuve globale ci-dessus établit le seuil exact indépendamment de cette tolérance.

Provenance : construction distincte du 30 septembre 2026 ; elle ne remplace ni les constantes du modèle spatial ni le témoin delayed_agentive_selection_v1_6. Une contribution d'objectif tardive est le statut mathématique de A.
