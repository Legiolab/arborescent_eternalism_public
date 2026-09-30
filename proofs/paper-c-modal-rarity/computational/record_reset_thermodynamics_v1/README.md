# Enregistrement, réinitialisation et bain thermique — 30 septembre 2026

## Question et verdict

Prolonger reliable_record_v1 en comptant chaleur, travail, corrélations et entropie du bain, puis comparer la description globale avec une préparation causale équivalente.

**Verdict :** un protocole de remise à zéro indépendant de la source produit de l'entropie totale moyenne. Cette production est intégralement reproduite causalement et repose sur le bain et le pilotage déjà spécifiés. De plus, une minimisation globale naïve du coût de trajectoire choisit un message nul et une histoire de registres constante lorsque la thermalisation est incomplète. Le test ne fournit donc pas une dérivation de la flèche par AE.

## Hypothèses explicites

Unités k_B=T=1, logarithmes naturels. La source S est un bit dégénéré en énergie et préservé. La mémoire M possède deux niveaux E_M=epsilon*M pendant le reset, et deux niveaux dégénérés avant et après. La copie S->M est une CNOT idéale réversible, hors contact du bain, avec énergie constante. On ne dérive pas le coût réel de sa commande.

Le bain est un réservoir idéal à température constante. Un travailleur externe pilote le niveau d'énergie de la mémoire : montée instantanée de 0 à epsilon, contact thermique, descente instantanée à 0. Ce protocole n'est pas un dispositif autonome : le calendrier, la source de travail et le maintien du bain sont donnés. L'entropie microscopique d'un bain fini et le coût d'un contrôleur ne sont pas modélisés. Le bilan inclus est source + mémoire + échange entropique avec un bain idéal.

Le reset n'utilise pas la source comme information latérale. C'est une hypothèse substantielle ; le contrôle d'« uncopy » ci-dessous montre ce qui change si la source est accessible.

Pour q1=1/(1+exp(epsilon)), q0=1-q1 et 0<alpha<=1,

K(x,y)=(1-alpha)*1[x=y]+alpha*q_y.

Ce noyau normalisé satisfait q0*K(0,1)=q1*K(1,0) et log[K(0,1)/K(1,0)]=-epsilon. Il correspond à une relaxation de durée finie avec alpha=1-exp(-gamma*t), et alpha=1 est sa limite de thermalisation complète. Il est donc compatible avec le bilan de chaleur adopté, sans être une dynamique microscopique du bain.

Référence du cadre : U. Seifert (2012), *Stochastic thermodynamics, fluctuation theorems, and molecular machines*, Rep. Prog. Phys. 75, 126001, DOI 10.1088/0034-4885/75/12/126001 ; https://arxiv.org/abs/1205.4176 . Les calculs ci-dessous sont ceux de notre protocole, pas une nouvelle loi de thermodynamique.

## 1. Bilan de l'ensemble opérationnel

On fixe explicitement une source équitable, une mémoire vierge, puis une copie parfaite. Cette source variable est le diagnostic opérationnel du premier test. Ce choix d'ensemble ne découle pas d'une minimisation unique d'histoire.

Après copie : rho(S,M)=1/2 si M=S, zéro sinon ; H(S,M)=log2, H(M)=log2, I(S;M)=log2. La copie seule conserve l'entropie jointe et n'échange pas de chaleur dans le modèle idéal.

Après reset : rho_fin(s,y)=K(s,y)/2. Le taux d'erreur de préparation de la mémoire est

p=P(M_fin=1)=(1-alpha)/2+alpha*q1.

Les bilans par bit sont :

- Chaleur reçue par la mémoire : Q=epsilon*(p-1/2).
- Travail reçu pendant les deux changements de niveau : W=epsilon*(1/2-p).
- Energie finale moins initiale : 0=W+Q.
- Entropie du bain : Delta S_bain=-Q, la température étant 1.
- Delta H_joint=H(rho_fin)-log2=H(M_fin|S)>=0.
- Production totale moyenne : Sigma_joint=Delta H_joint-Q>=0.

Le bilan limité à la mémoire est Sigma_M=h(p)-log2-Q. Les deux bilans sont reliés par

Sigma_joint = Sigma_M + I_initial-I_final.

Le terme de corrélation est indispensable. Une diminution de l'entropie de la mémoire n'est pas une diminution de l'entropie totale. La positivité suit de Sigma_joint=D(rho_initial || pi)-D(rho_fin || pi), où pi(s,y)=q_y/2 est stationnaire : la divergence relative décroît sous le noyau. Le script vérifie aussi cette identité, la balance détaillée et le bilan de première loi pour 20 couples (epsilon,alpha).

### Exemple epsilon=5, alpha=1

| Quantité, par bit | Valeur |
|---|---:|
| Erreur finale de mémoire p | 0,006692851 |
| Delta H_joint | 0,040179603 |
| Delta H_memory | -0,652967577 |
| Entropie gagnée par le bain | 2,466535745 |
| Travail fourni W | 2,466535745 |
| Sigma_joint | 2,506715348 |
| Sigma_memory+bain | 1,813568168 |

Pour six paires indépendantes, multiplier les bilans entropiques, le travail et la chaleur par six. L'erreur de 0,00669 est par bit ; la probabilité que les six mémoires soient vierges est (1-p)^6, non 1-p.

Le reset est imparfait à epsilon fini. Le Hamiltonien retrouve sa valeur initiale, mais la distribution de mémoire ne retrouve pas exactement l'état vierge : ce n'est pas un cycle fermé exact. Le protocole abrupt n'est pas optimal ; ses valeurs ne constituent pas un minimum universel de dissipation.

L'égalité avec le protocole causal est vérifiée en propageant indépendamment la distribution initiale dans la CNOT et K. Même préparation, même calendrier et même noyau donnent la même loi finale et les mêmes bilans. Ce témoin ne discrimine donc pas AE.

## 2. Contrôle crucial : sélection d'histoires complètes

Il faut éviter de confondre le diagnostic d'ensemble ci-dessus avec un résultat d'argmin. On énumère donc aussi toutes les histoires (s,m,y), où s et m sont les préparations libres, la copie donne c=m XOR s, puis le reset donne y.

Référence normalisée :

w(H)=2^(-2n)*produit_j K(c_j,y_j).

La tâche récompense seulement la copie fidèle, évaluée avant le reset : A(H)=1 si c=s. Elle ne mentionne ni entropie ni énergie, et n'exige pas de conserver le record après son effacement.

J_beta(H)=-log w(H)-beta*A(H).

Pour epsilon>0 et 0<alpha<1, K(0,0) est strictement plus grand que les trois autres éléments. La trajectoire (s,m,y)=(0,0,0) pour tous les bits atteint à la fois le poids de référence maximal et la récompense maximale. Elle est donc l'unique gagnante pour tout beta>0. Tous les états de registres sont constants, sans chaleur ni travail sur cette trajectoire ; le pilotage est toujours externe et son coût propre n'est pas calculé.

La source gagnante est un message constant. La fidélité sur ce message ne suffit pas à établir la capacité d'acquérir une information variable. L'entropie moyenne positive de l'ensemble à source équitable ne peut pas être attribuée à cette unique histoire gagnante. Il ne faut pas non plus réappliquer à une distribution de gagnantes le noyau causal K comme si cette sélection avait préservé sa loi.

| n | Histoires complètes examinées, epsilon=5, alpha=0,9, beta=1 | Gagnantes |
|---|---:|---:|
| 1 | 8 | 1 |
| 2 | 64 | 1 |
| 4 | 4 096 | 1 |
| 6 | 262 144 | 1 |

Contrôle alpha=1 : K ne dépend plus de son entrée. Les 2^n sources deviennent ex aequo, avec m=0 et y=0. La dégénérescence du premier test n'est donc conservée que dans cette limite particulière. Contrôle beta=0 et alpha<1 : les gagnantes ont m=s, copient vers c=0 et terminent en y=0 ; la copie n'est pas fidèle sauf pour s=0.

Ce résultat réfute l'affirmation « ce J sélectionne une flèche et un enregistrement informatif » dans ce modèle. Il ne réfute pas toutes les lois de sélection envisageables pour AE. Une source ou une loi d'entrée fixée indépendamment, un critère opérationnel portant sur plusieurs entrées, ou une autre fonctionnelle peuvent changer le problème ; il faudra justifier ce changement au lieu d'ajuster J après avoir vu les résultats.

## 3. Contrôles thermodynamiques

- **Copie seule** : transformation bijective sur source + mémoire, entropie jointe constante, chaleur nulle dans le modèle idéal. Le besoin d'un record ne suffit pas à imposer une dissipation.
- **Uncopy avec source accessible** : appliquer une seconde CNOT à (s,s) donne (s,0). La mémoire redevient vierge sans bain ni changement d'énergie dans ce modèle idéal. Effacer une copie en utilisant sa source diffère du reset indépendant de la source. Ce contrôle détruit le record ; il ne conserve pas ailleurs une information qui n'existait pas déjà.
- **Equilibre sans pilotage** : partir de la loi q et appliquer K à epsilon fixe donne une production moyenne nulle. L'entropie stochastique totale est nulle pour chaque transition grâce à la balance détaillée.
- **Trajectoires et moyennes** : pour le reset d'une mémoire équitable sans corrélation avec une source, certaines trajectoires ont une production stochastique négative, tandis que la moyenne reste non négative. Une loi sur la moyenne ne prouve pas une hausse sur toute histoire. Pour l'ensemble parfaitement corrélé de notre copie, le script calcule séparément les valeurs de chaque transition ; il ne lui attribue pas ces fluctuations négatives par analogie.

## 4. Conséquence pour Paper C

Conservable : une tâche fonctionnelle de copie peut sélectionner une préparation particulière, et un protocole de remise à zéro thermique donne un bilan total cohérent lorsque les corrélations sont comptées.

Non établi : la sélection AE comme origine de la direction thermodynamique. Dans ce test, la source de travail, le calendrier et l'hypothèse de bain sont déjà donnés ; le modèle causal produit le même bilan. Le nouveau contrôle montre même que le MAP global complet sélectionne une histoire triviale si le message est laissé libre.

La prochaine question justifiée est donc précise : **quelle contrainte indépendante exprime une capacité de mémoire pour une source variable, et comment la loi d'actualisation d'AE traite-t-elle cette contrainte sans confondre histoire gagnante et ensemble ?** Il faut résoudre ce point avant d'attribuer à A une sélection robuste d'histoires thermodynamiques. Une nouvelle récompense conçue pour exclure le cas nul serait une hypothèse supplémentaire, pas une preuve obtenue par ce test.

## Reproduction

```bash
python proofs/paper-c-modal-rarity/computational/record_reset_thermodynamics_v1/check.py
```

Python 3, bibliothèque standard uniquement. results.json contient les 20 bilans, les distributions, les productions stochastiques, les contrôles et les résultats des énumérations complètes. Les comparaisons de logarithmes utilisent une tolérance de 1e-10. Les preuves algébriques ci-dessus établissent indépendamment la caractérisation des gagnantes et les identités thermodynamiques.
