# Statut de A et rôle explicatif de Paper C

30 septembre 2026. Audit conceptuel après les tests d'enregistrement. Aucun nouveau modèle ni nouvelle loi d'actualisation n'est introduit ici.

## 1. Conclusion de l'audit

Le foundational v3.4 définit A comme une information agentive représentée et C_A comme un coût de compatibilité conditionné par un objectif. J est un candidat d'évaluation globale ; l'argmin est une implémentation provisoire de l'actualisation. Il ne dérive ni une loi universelle favorisant les agents ni une flèche thermodynamique causée nécessairement par A.

Paper C doit conserver ce statut. Son apport est de tester quand des contraintes sur les histoires et des exigences fonctionnelles imposent une préparation particulière, puis de distinguer ce résultat de la croissance d'entropie. Le lien physique entre un coût de compatibilité agentive et la loi d'actualisation reste une hypothèse à justifier.

Sources auditées : *AE_Foundational_Preprint_v3_4(1).docx*, 28 septembre 2026, §§1.2, 2.4, 6.1–6.4 ; *Paper_C_Modal_Rarity_Physical_Preparation_and_Entropy_revised.docx*, révision du 30 septembre 2026, §§2.3, 9.1–9.7, 10. Les cinq tests du 30 septembre sont distingués ci-dessous. Le foundational n'est pas modifié par cet audit.

## 2. Les objets ne doivent pas être confondus

| Objet | Type et fonction | Statut |
|---|---|---|
| A dans l'architecture AE | Information représentée : objectif, délibération, mémoire, actions, quand un agent est effectivement modélisé | Donnée du modèle à motiver physiquement |
| C_A(H) | Compatibilité d'une histoire complète avec cette information | Contribution candidate à J, pas loi dérivée |
| A(H), q(H) ou Cap(D) dans les témoins | Score scalaire de réussite d'une tâche ou de capacité d'un appareil | Définition opérationnelle propre au témoin |
| J | Evaluation globale après E, Pi et w | Candidat fonctionnel ; sa forme n'est pas unique |
| Règle d'actualisation | Désignation de H* ; provisoirement H* appartient à Argmin J | Hypothèse ontique distincte du score |

La candidate foundational est J=-log w+B+C_A. Dans un témoin binaire, C_A=beta*(1-q) et la récompense -beta*q donnent le même classement, car elles diffèrent d'une constante beta. Cette équivalence algébrique ne transforme pas q en agent, ni beta en constante physique dérivée.

Trois questions restent séparées : pourquoi la tâche est une fonction physique légitime ; pourquoi un dispositif possède cette capacité ; pourquoi cette compatibilité entre dans une loi d'actualisation de l'univers. Les deux premières ne prouvent pas la troisième.

## 3. Ce que signifie une information non fixée sur une coupe

L'ambition A non réductible à une fonction du seul X_Sigma ne doit pas être assimilée à une preuve de liberté métaphysique. Il faut définir la coupe, les degrés de liberté inclus, la complétude de son état et les lois d'évolution. Un état local incomplet peut omettre une source ou un contrôleur ; un modèle causal stochastique peut avoir plusieurs continuations. Aucun de ces faits ne prouve une irréductibilité ontologique de A.

Dans un modèle réellement déterministe à état initial complet, une réécriture globale du même modèle ne crée pas deux continuations physiques à partir du même état. Une comparaison de buts à E, Pi, w fixes établit une sensibilité du candidat J à l'objectif ; un contrôle exogène aléatoire peut reproduire des distributions agrégées. L'audit conserve donc l'efficacité fonctionnelle conditionnelle et laisse ouverte l'irréductibilité métaphysique.

## 4. Ce que les calculs permettent effectivement de dire

| Construction | Résultat conservable | Limite décisive |
|---|---|---|
| Spatial preparation/reset | Borne sur le véritable état initial ; densité asymptotique <=0,469 ; déficit de comptage ~0,0822 nat/site | Histoires gagnantes constantes ; référence déjà favorable au zéro |
| Local delayed objective | Six gagnantes avec préparation rare et croissance de Boltzmann sur trois transitions | La tâche favorise précisément la classe voulue |
| Reliable record | La copie fidèle préservant la source contraint la préparation sans score entropique | Entropie jointe constante ; croissance de macroétat dépend de la partition |
| Record/reset thermodynamics | Chaleur, travail et corrélations donnent un bilan de production moyenne cohérent | Même résultat causal ; argmin complet avec source libre choisit le message nul |
| Operational record capacity | Une capacité indépendante de l'entropie implique un déficit initial de ressource complète, auxiliaires compris, sous hypothèses finies réversibles | La capacité ne garantit pas une activité informative réalisée ; elle ne dérive pas la flèche |

La dernière borne est le résultat le moins dépendant d'une trajectoire choisie pour son entropie. Pour une mémoire de d états et un auxiliaire de e états, tout protocole réversible préservant la source, capable de copier tous les messages avec la même préparation, admet au plus e préparations de ressource, soit une fraction de comptage <=1/d. L'entropie initiale d'ensemble satisfait H(R)<=log e. Avec une erreur de message entier <=delta pour chaque entrée, H(R)<=log e+h(delta)+delta log(d-1). Pour six bits et delta=0,01, le déficit au maximum de comptage est >=4,06145 nats.

Il s'agit d'une entropie d'ensemble de préparation et d'un comptage uniforme fini. Le résultat ne donne pas automatiquement une macrocellule de Boltzmann, un budget de libre énergie sous une référence Gibbs, ni une préparation cosmologique.

## 5. Comparaison explicative équitable

Il faut comparer les possibilités physiques, puis indiquer séparément les données de préparation et la sémantique d'actualisation. « Causal » et « global » ne sont pas deux classes nécessairement disjointes : une dynamique causale peut être écrite comme une loi sur les histoires complètes.

| Comparateur | Données indépendantes | Question testée |
|---|---|---|
| Causal sans préparation spéciale | Dynamique et loi initiale annoncées avant l'évaluation ; aucune sélection sur la réussite | Quelle probabilité d'opération réussie sans la ressource requise ? |
| Causal avec préparation spéciale | Même dynamique, préparation nécessaire ajoutée et coût de mise en place déclaré | Reproduit-il l'opération et son bilan ? |
| Global sans ontologie AE spécifique | Même espace d'histoires et même critère complet | La conclusion utilise-t-elle seulement une contrainte globale ? |
| AE | E, Pi, w, compatibilité agentive justifiée et règle d'actualisation déclarées | La même architecture contraint-elle la préparation sans nouveau réglage pour chaque cible ? |

Le deuxième comparateur doit inclure le coût de préparation lorsqu'on prétend comparer des bilans complets. Réciproquement AE ne peut compter la préparation comme gratuite simplement parce qu'elle appartient à la gagnante. Les copies idéales et resets publiés ne modélisent pas un contrôleur autonome ni un bain microscopique fini ; ils ne constituent pas encore une comparaison thermodynamique de tous les dispositifs.

Les tests d'enregistrement reproduisent l'opération causale une fois sa préparation fixée. Cela montre une équivalence conditionnelle des résultats, pas une égalité automatique des explications de la préparation. Mais AE ne gagne un avantage explicatif qu'en justifiant indépendamment le critère qui la sélectionne. Le comparateur global avec les mêmes ingrédients peut reproduire les mêmes minimisatrices : le vocabulaire modal seul ne procure pas de signature empirique.

## 6. Décision de cadrage pour Paper C

La question principale reste : **une résolution globale d'histoires peut-elle expliquer une préparation de basse entropie, plutôt que la poser séparément, et quelles conditions supplémentaires permettent une croissance entropique orientée ?**

A garde sa place dans le programme : une information agentive peut contribuer à la compatibilité de l'histoire, après définition des possibilités, projection et poids. Le paper ne postule pas ici une préférence cosmologique pour les agents. Les tâches de mémoire permettent de tester une partie physique indépendante : une capacité fonctionnelle peut contraindre une ressource initiale sans nommer son entropie.

Trois niveaux sont à écrire explicitement :

1. **Résultat démontré** : sous les hypothèses de la proposition de capacité, une fonction d'enregistrement implique un déficit initial de ressource.
2. **Mécanisme conditionnel** : dans un modèle déclaré, un coût global peut faire sélectionner une préparation rare ; une dynamique ou une tâche distincte peut donner une croissance entropique.
3. **Hypothèse AE restant à fonder** : cette compatibilité est une composante de la loi d'actualisation physique et impose, sans ajustement supplémentaire, les structures thermodynamiques d'une histoire effective.

La conclusion correcte n'est ni « A explique déjà la flèche » ni « la reproduction causale annule tout l'intérêt d'AE ». Elle est : **le lien fonction–préparation est établi dans une classe physique limitée ; le gain explicatif de l'actualisation globale et son apport spécifique à AE restent des tests ouverts.**

## Reproduction et intégration

Les preuves et sorties des cinq constructions sont dans computational/spatial_preparation_reset_v1, local_delayed_objective_v1, reliable_record_v1, record_reset_thermodynamics_v1 et operational_record_capacity_v1. Le dernier run_all.py a passé ses douze contrôles. Cet audit ajoute des distinctions et une comparaison, pas de nouvelle simulation.

La révision de Paper C doit expliciter ces niveaux en §2.4, intégrer le résultat de capacité et ses contrôles en §§9.8–9.9, puis poser la comparaison explicative en §10.4. Les preuves de préparation existantes et le témoin local restent conservés avec leur portée propre.
