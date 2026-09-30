# Test indépendant : enregistrement fiable et préparation — 30 septembre 2026

## Question et résultat

Une tâche d'enregistrement définie sans référence à l'entropie peut-elle sélectionner une préparation rare et une flèche entropique ?

**Résultat : préparation locale oui, flèche thermodynamique générale non.** Pour une copie réversible qui préserve la source, le critère d'enregistrement sélectionne une mémoire vierge parmi toutes les préparations libres. Cependant l'entropie de Shannon jointe reste constante ; la croissance de Boltzmann dépend de la macro-partition et n'est pas monotone sur toutes les gagnantes. Cela constitue une restriction du mécanisme envisagé, pas une réfutation d'AE.

Ce test est distinct du témoin local à six bits qui prescrivait une classe de trajectoires. Ici l'objectif ne mentionne ni macroétat initial, ni nombre de déplacements, ni entropie.

## Modèle complet

Deux registres S (source) et M (mémoire), chacun de n bits. Tous les 2^(2n) couples initiaux (s,m) sont admissibles, de même poids w=2^(-2n). La dynamique est fixée avant l'objectif : au pas j, appliquer la porte CNOT locale entre S_j et M_j : M_j <- M_j XOR S_j. La source ne change jamais. Après n portes, M_fin = m XOR s. On peut prolonger par identité pour conserver le record, mais cette rétention sans bruit n'établit aucune robustesse physique.

Chaque porte est bijective et involutive. Le calendrier des portes et son sens sont donnés par le modèle, non dérivés. Il s'agit d'un modèle logique de registres réversibles, pas d'un Hamiltonien, d'un appareil avec bruit, d'un bain thermique ou d'une cosmologie. Il n'y a ni degrés de liberté effacés ni environnement thermodynamique représenté. L'entropie totale d'un dispositif réel n'est donc pas calculée.

L'arbre E est l'ensemble des préfixes de ces trajectoires ; Pi renvoie leur suite de couples (S,M), et r_Sigma le couple initial. A(H)=1 exactement si M_fin=S_initial. Le score tardif mesure la fidélité du record ; la préservation de la source est assurée par la dynamique. Ce score ne démontre pas l'existence d'un agent ou d'un contrôleur autonome.

J_beta(H) = -log w(H) - beta A(H), beta >= 0.

## Preuve de la sélection

Le coût de référence est constant, 2n log2. Pour beta=0, toutes les préparations gagnent. Pour tout beta>0, les minimisatrices sont exactement les histoires fidèles.

Or m XOR s = s si et seulement si m=0. Il existe donc 2^n gagnantes, une par source, toutes issues d'une mémoire vierge. Leur ensemble initial a mesure 2^(-n) sous le comptage uniforme joint. Cette rareté porte sur la préparation de la mémoire dans ce protocole ; elle ne démontre pas que tout enregistrement exige une mémoire vierge.

Aucune sélection préalable des préparations n'a été faite. La tâche est fidèle pour tous les messages, et non seulement pour une source choisie. Le seuil beta=0 vient de la référence uniforme ; il ne s'étend pas à une loi de référence arbitraire.

## Entropies distinctes

Pour examiner les gagnantes, on prend explicitement l'ensemble uniforme sur leurs 2^n sources. Cette distribution est un diagnostic déclaré, pas une loi d'ensemble automatiquement produite par un argmin.

Avant la copie : H(S)=n log2, H(M)=0, H(S,M)=n log2.

Après la copie : H(S)=H(M)=n log2, H(S,M)=n log2, I(S;M)=n log2.

Au pas t, H(M)=I(S;M)=t log2 et H(S,M)=n log2. La hausse de la somme des entropies marginales est exactement compensée par la corrélation. Elle ne constitue pas une production d'entropie jointe. Le maximum logique joint est 2n log2 : l'ensemble sélectionné reste en dessous avant et après la copie.

Deux macro-partitions sont fixées et testées séparément, en unités k_B=1 :

1. **Comptages par registre** : (K_S,K_M), multiplicité binom(n,K_S) binom(n,K_M). Au départ, S_B=log binom(n,k) ; à la fin, S_B=2 log binom(n,k). Pour n>=2, le macroétat initial a au plus la moitié de l'entropie maximale de cette partition. La hausse finale est stricte sauf pour les deux messages homogènes. Elle n'est pas monotone le long des messages comportant plus de n/2 bits à un.
2. **Comptage total** : K_S+K_M, multiplicité binom(2n,K_S+K_M). S_B passe de log binom(2n,k) à log binom(2n,2k). Des copies fidèles font décroître cette entropie.

Ces partitions ne sont pas des dérivations d'une entropie thermodynamique. La première distingue les rôles fonctionnels des deux registres ; la seconde les regroupe. La dynamique CNOT ne conserve pas le nombre de bits à un. Aucune énergie physique n'est spécifiée.

## Résultats exhaustifs

| n | Histoires examinées | Gagnantes beta>0 | S_B final supérieur, registres séparés | Trajectoires S_B non décroissantes | S_B total : hausse / égalité / baisse |
|---|---:|---:|---:|---:|---:|
| 2 | 16 | 4 | 2 | 3 | 2 / 1 / 1 |
| 4 | 256 | 16 | 14 | 11 | 10 / 1 / 5 |
| 6 | 4 096 | 64 | 62 | 42 | 41 / 16 / 7 |
| 8 | 65 536 | 256 | 254 | 163 | 218 / 1 / 37 |

La colonne de non-décroissance vaut pour les deux partitions dans ce protocole. Une hausse entre les extrémités n'est pas une hausse monotone. Une constante est comptée comme non décroissante, mais jamais comme croissance stricte.

Contre-exemple n=6 : pour la source 111111 et la mémoire initiale 000000, la copie est parfaitement fidèle. L'entropie de comptage total passe de log binom(12,6)=log924 à log binom(12,12)=0. Avec la partition par registres, l'entropie commence et finit à zéro et augmente puis diminue pendant la copie. Cette gagnante interdit toute affirmation de croissance sur toutes les histoires.

## Contrôles indispensables

- **Ablation de l'objectif** : 2^(2n) gagnantes, aucune préparation de mémoire favorisée.
- **Identité** : un record final fidèle sélectionne les 2^n états déjà corrélés m=s, sans aucune évolution entropique. Une corrélation finale ne prouve pas l'acquisition d'information.
- **SWAP** : échanger les deux registres produit M_fin=S_initial pour toutes les préparations. Il n'exige aucune mémoire vierge mais remplace la source. Préserver la source est donc une hypothèse substantive.
- **Inversion** : inverser l'ordre des portes restitue exactement toute préparation. Le test ne dérive pas une direction temporelle à partir de lois seules.
- **Comparaison causale** : préparer causalement M=0 puis exécuter ces mêmes portes produit exactement les mêmes histoires et observations. La sélection globale organise les conditions compatibles, mais ce témoin ne distingue pas empiriquement AE de ce protocole causal. AE n'a pas encore expliqué pourquoi ce critère serait la loi d'actualisation physique.

## Ce que Paper C peut conserver

Un objectif fonctionnel de copie, indépendant de l'entropie, peut sélectionner une préparation initiale rare dans une dynamique donnée. Il sélectionne aussi un faible macroétat initial sous la partition par registres, et une hausse finale sur presque toutes les sources sous le diagnostic uniforme déclaré. Ce résultat dépasse le témoin dont l'objectif prescrivait les déplacements.

Ce qu'il ne permet pas : dériver une flèche monotone sur toutes les gagnantes ; identifier Shannon et chaleur ; expliquer une basse entropie cosmologique ; dériver le calendrier ou son orientation ; démontrer l'agentivité ; établir une supériorité spécifique d'AE.

Prochaine question physique : les contraintes indépendantes de bruit, de rétention, de préservation de la source et de ressources, appliquées au dispositif et à son environnement, imposent-elles un budget hors équilibre ? Ajouter simplement une pénalité entropique recréerait la circularité que ce test cherche à éviter.

## Reproduction

```bash
python proofs/paper-c-modal-rarity/computational/reliable_record_v1/check.py
```

Python 3, bibliothèque standard uniquement. results.json contient les traces, comptages et exemples. Le script vérifie l'ensemble des préparations pour n=2,4,6,8, la bijectivité, l'inversion, les minimisatrices, les identités de Shannon et les contrôles. Les valeurs de logarithmes utilisent une tolérance de 1e-12 ; la caractérisation des gagnantes est établie algébriquement ci-dessus.

Référence de contexte : C. H. Bennett (1973), *Logical Reversibility of Computation*, IBM Journal of Research and Development 17(6), 525–532, DOI 10.1147/rd.176.0525. Texte : https://www.cs.princeton.edu/courses/archive/fall04/cos576/papers/bennett73.html . Bennett établit la possibilité de copies réversibles avec un support vierge ; les comptages ci-dessus sont ceux de notre modèle, pas des résultats attribués à son article.
