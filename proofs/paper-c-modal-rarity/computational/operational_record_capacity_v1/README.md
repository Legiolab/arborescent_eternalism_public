# Capacité d'enregistrement, ressources initiales et sélection globale

30 septembre 2026 — prolongement des tests reliable_record_v1 et record_reset_thermodynamics_v1.

## Question et réponse

Comment distinguer un appareil capable d'enregistrer une source variable d'une histoire où il « copie » seulement un message nul ?

On certifie **la même préparation et le même dispositif pour chaque entrée possible**, indépendamment de l'entropie et des messages effectivement réalisés. Cette exigence implique une borne générale sur les ressources initiales dans un modèle classique fini réversible. Elle élimine les appareils incapables, mais n'oblige pas à réaliser des messages variés : la minimisation d'une seule histoire peut encore choisir le message nul dans un appareil réellement capable.

Le résultat positif est donc **capacité fonctionnelle -> déficit de ressources initiales sous hypothèses déclarées**, non une dérivation de la flèche cosmologique ni une discrimination d'AE.

## 1. Capacité et histoire sont deux niveaux distincts

Une histoire contient une entrée réalisée s, une préparation r et une trajectoire. La capacité exige que le même appareil et la même préparation réussissent aussi sur les autres entrées admissibles.

Dans la famille testée, S et M ont n bits. Une porte CNOT est présente au site j si le bit a_j d'un masque a vaut 1 ; sinon la porte est l'identité. Toutes les préparations m et tous les masques a sont autorisés.

La fonction réalisée est M_out=m XOR (a AND s), et S_out=s. L'exigence de capacité exacte est

M_out(s)=s pour chaque s dans {0,1}^n, avec a et m fixes.

L'entrée s=0 impose m=0 ; les entrées comportant un seul bit à 1 imposent chaque a_j=1. L'unique appareil capable de cette famille est donc CNOT sur tous les sites, avec mémoire vierge. Aucun macroétat entropique ne figure dans la définition de réussite.

| n | Couples appareil/préparation examinés | Entrées contrefactuelles vérifiées | Appareils/préparations capables |
|---|---:|---:|---:|
| 1 | 4 | 8 | 1 |
| 2 | 16 | 64 | 1 |
| 4 | 256 | 4 096 | 1 |
| 6 | 4 096 | 262 144 | 1 |

Le mot « contrefactuel » ne signifie pas que toutes les entrées sont actualisées. Il exprime une propriété de la fonction de l'appareil. Cette propriété peut être décrite dans AE ou dans un modèle causal muni d'une description de l'appareil ; elle n'établit pas une nécessité exclusive de l'ontologie modale d'AE.

## 2. Proposition : borne de ressource pour un enregistrement réversible

**Hypothèses.** Messages classiques s parmi d valeurs. Mémoire M de d états, auxiliaire E de e états. La ressource R=(M,E) a donc D=d*e états. Pour chaque source fixée s, le protocole préserve S et agit sur R par une bijection U_s. Tout degré de liberté recevant de l'information effacée de M doit être inclus dans R ; un contrôle ou réservoir caché invaliderait cette fermeture. La préparation est fixée indépendamment de s. Le record doit satisfaire M_out=s.

**Résultat exact.** Pour chaque appareil fixé, au plus e états initiaux de R permettent une copie exacte pour tous les messages. Leur fraction sous le comptage uniforme est au plus 1/d. Toute distribution préparée sur ces états satisfait

H(R_initial) <= log e,

soit un déficit par rapport au maximum de comptage :

log(d*e)-H(R_initial) >= log d.

**Preuve.** Fixer une entrée s. Le sous-ensemble de sorties avec M=s contient exactement e états, un pour chaque E. La bijection U_s a donc exactement e préimages de ce sous-ensemble. Les préparations capables pour tous les messages appartiennent à l'intersection de ces préimages ; cette intersection contient au plus e états. Son entropie de Shannon maximale est log e. Le protocole peut déplacer la ressource vers E mais ne peut augmenter cette cardinalité.

Cette preuve concerne une tâche opérationnelle indépendante du score entropique, pas une récompense ajustée à un macroétat désiré. La condition sur toutes les entrées est cependant une hypothèse supplémentaire par rapport à une simple récompense de fidélité sur une histoire.

**Limite physique.** H(R) est une entropie de préparation d'ensemble, pas l'entropie de Boltzmann d'un microétat individuel. La fraction de comptage du secteur admissible ne prouve pas que ce secteur correspond à une macrocellule thermodynamique indépendamment définie. Le maximum log D correspond à la référence uniforme finie ; pour un Hamiltonien non dégénéré et une référence Gibbs, le lien au hors équilibre demande une analyse de divergence relative ou de libre énergie. La proposition n'est pas un résultat quantique.

## 3. Enregistrement imparfait

Pour chaque entrée, autoriser une probabilité d'erreur de message entier au plus delta, avec 0<=delta<=1-1/d. L'état initial aléatoire de R doit rester indépendant de s.

Alors

H(R_initial) <= log e + h(delta) + delta*log(d-1),

et

log D-H(R_initial) >= log d-h(delta)-delta*log(d-1),

où h(delta)=-delta log delta-(1-delta)log(1-delta).

**Preuve.** Fixer s, et noter eta<=delta l'erreur effective. La bijection conserve H(R). Les sorties correctes appartiennent à e états, les sorties incorrectes à (d-1)*e états. Décomposer selon correct/incorrect donne

H(R_out) <= h(eta)+(1-eta)log e+eta log((d-1)*e).

La fonction h(eta)+eta log(d-1) croît pour eta<=1-1/d, d'où la borne avec delta. Il n'est pas nécessaire de supposer une croissance d'entropie ni de la récompenser.

**Borne atteinte dans notre famille.** Utiliser les CNOT, préparer m=0 avec probabilité 1-delta, et distribuer le reste uniformément sur les d-1 autres mémoires ; E est uniforme et inactif. La fidélité vaut 1-delta pour chaque message et l'entropie initiale atteint la borne. Le script vérifie 32 cas (n=1,2,4,6 ; delta=0,0,01,0,05,0,1 ; e=1,4).

Pour n=6, d=64, e=1 et delta=0,01 :

| Quantité | Valeur, en nats |
|---|---:|
| Maximum log64 | 4,158883083 |
| Entropie initiale maximale compatible avec la capacité | 0,097432882 |
| Déficit minimal | 4,061450202 |

La fidélité de 99 % porte sur **le message entier de six bits pour chaque entrée**, non sur chaque bit pris isolément. Cette distribution est une préparation statistique spécifiée ; elle ne découle pas de la règle d'argmin sur une histoire unique.

## 4. Les auxiliaires ne suppriment pas la ressource

Le script examine exhaustivement les 576 appareils classiques réversibles qui préservent une source d'un bit, avec M et E d'un bit : chaque source choisit l'une des 24 permutations de R. Le nombre de préparations universellement capables est 0 pour 96 appareils, 1 pour 384 appareils et 2 pour 96 appareils ; jamais plus que e=2.

Un contrôle explicite permet de commencer avec une mémoire M uniforme, donc d'entropie maximale, et E vierge : échanger M et E, puis copier S vers M. La source est préservée, M_out=S et E_out=M_initial. La préparation nécessaire est alors dans l'auxiliaire. La mémoire vierge n'est donc pas une nécessité universelle ; la restriction concerne la ressource complète R.

H(R_initial)=log2 contre un maximum log4, soit un déficit log2. Le bilan source+mémoire+auxiliaire est réversible et ne produit aucune chaleur dans ce contrôle logique idéal. La borne de ressource initiale n'est donc pas une preuve de dissipation.

## 5. Est-ce que la capacité répare l'argmin d'une histoire ?

On reprend le noyau thermique du test précédent, sans le reconstruire : epsilon=5, alpha=0,9. Après copie, le reset a probabilité K(c_j,y_j), c=m XOR (a AND s).

Une histoire est (a,m,s,y). La référence normalisée est

w(H)=2^(-3n)*produit_j K(c_j,y_j).

On récompense désormais **la capacité universelle de l'appareil**, et non sa seule réussite sur l'entrée réalisée :

J(H)=-log w(H)+kappa*nombre_de_CNOT-beta*Cap(a,m).

kappa=0,2 est un coût de score explicite de complexité du contrôleur, **pas un travail thermodynamique dérivé**. Cap=1 seulement pour a=111... et m=0. Cette capacité est évaluée par la table de vérité complète avant la comparaison des histoires.

Pour epsilon>0 et alpha<1, K(0,0) est strictement maximal. Le meilleur appareil incapable est le masque identité a=0 avec m=0, source quelconque et y=0. Le meilleur appareil capable réalise s=0 et y=0. Les coûts de référence sont identiques pour ces meilleurs concurrents et le coût de contrôleur est n*kappa. Ainsi, pour beta>n*kappa, l'unique gagnante est

a=111..., m=0, s=0, y=0.

L'appareil est effectivement capable de copier **tous** les messages ; l'histoire sélectionnée ne contient pourtant qu'un message nul et des registres constants. L'exigence de capacité exclut les appareils incapables, mais ne force pas une utilisation informative dans l'histoire réelle.

Le script énumère 16, 256 et 4 096 histoires complètes pour n=1,2,3, en dessous, au seuil et au-dessus de beta=n*kappa. Au-dessus, cette gagnante est unique ; en dessous, les 2^n histoires avec appareil-identité, préparation m=0 et sources variables sont gagnantes ; au seuil, les 2^n+1 candidats sont ex aequo. Il vérifie aussi la normalisation de la référence sur toutes les histoires. La preuve par maximum de K établit le résultat pour tout n. Le changement de récompense n'élimine donc pas le cas trivial réalisé ; prétendre le contraire serait confondre compétence et activité.

## 6. Opération avec une source réellement variable

Fixer indépendamment une loi de messages P(S=1)=p avec p=0,1 ; 0,5 ; 0,9, puis utiliser l'appareil capable. Cette hypothèse d'entrée non dégénérée définit un problème conditionnel ; elle ne doit pas être présentée comme une conséquence d'AE.

Avec mémoire vierge et CNOT, la loi juste après copie est rho(s,m)=P(s) si m=s. Après reset : rho_fin(s,y)=P(s)*K(s,y). Le script compare cette loi avec une propagation causale indépendante et vérifie exactement les mêmes probabilités et les mêmes bilans.

Sigma_joint=Delta H(S,M)-Q = D(rho_initial || P_S*q)-D(rho_fin || P_S*q)>=0.

| p | Production moyenne par bit, epsilon=5, alpha=0,9 |
|---|---:|
| 0,1 | 0,486812654 |
| 0,5 | 2,407341336 |
| 0,9 | 4,327870018 |

La positivité concerne cet ensemble et ce reset. Elle n'est ni une croissance de Boltzmann sur toute histoire ni une production d'entropie imposée par la capacité seule. Le bain idéal, le calendrier et la source de travail restent des hypothèses du modèle précédent ; le contrôleur autonome et un bain microscopique fini ne sont pas ajoutés.

## 7. Conclusion utilisable pour Paper C

**Résultat nouveau conservable :** dans un système classique fini réversible qui préserve la source, une capacité d'enregistrement définie indépendamment de l'entropie impose un déficit initial de ressources, même en tenant compte d'un auxiliaire et d'une erreur tolérée. L'exigence fonctionnelle peut donc contraindre la préparation sans nommer une basse entropie dans l'objectif.

**Limite décisive :** la capacité ne garantit ni une source effectivement variable dans la gagnante ni une flèche thermodynamique. La récompense de capacité testée ici conserve le message nul comme gagnant unique. Une loi d'entrée fixée indépendamment permet un problème d'opération informative, mais les résultats restent reproduits causalement.

Pour AE, il reste à justifier le passage d'une propriété d'appareil sur les alternatives à une loi d'actualisation de l'histoire réelle, et à expliquer l'activité informative ou les contraintes de messages sans les ajuster au résultat voulu. Le secteur rare et la borne d'entropie d'ensemble ne doivent pas être vendus comme une démonstration de basse entropie cosmologique.

## Reproduction

```bash
python proofs/paper-c-modal-rarity/computational/operational_record_capacity_v1/check.py
```

Python 3, bibliothèque standard uniquement. Dépend du check.py publié dans record_reset_thermodynamics_v1 pour son noyau thermique et l'entropie binaire. results.json contient les énumérations, les bornes atteintes, le contrôle auxiliaire, les gagnantes et les bilans. Tolérance numérique : 1e-10. Les preuves algébriques ci-dessus ne dépendent pas des petites tailles énumérées.
