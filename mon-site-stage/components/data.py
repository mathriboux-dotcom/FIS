# --- Contenu des missions ---
FIS_RELAY_CALENDAR_CONTENT = """
### 📌 FIS Relay Calendar
Le rôle **FIS Relay Calendar** est utilisé pour gérer les fichiers de calendrier de l’application.
Ces fichiers indiquent à l’application certaines dates importantes qu’elle doit prendre en compte.
Même si ces fichiers semblent simples, ils sont essentiels au bon fonctionnement de certaines fonctionnalités.

Lorsque j’ai travaillé sur ce rôle, mon objectif n’était pas de modifier les calendriers eux-mêmes.
Mon travail consistait à **automatiser leur intégration** dans l’environnement Ansible afin de simplifier leur déploiement.

Pour cela, j’ai développé le script **`build_all_sub_fisrelay_calendar.sh`**.
Ce script analyse les configurations existantes puis récupère automatiquement les informations nécessaires à chaque serveur.
Les fichiers sont ensuite générés automatiquement et intégrés dans la structure du rôle.

Cette automatisation permet de :
- Gagner du temps ;
- Éviter les oublis ;
- Garantir que les mêmes règles sont appliquées partout.
"""

FIS_RELAY_ENRICHDATA_CONTENT = """
### 📌 FIS Relay EnrichData
Le rôle **FIS Relay EnrichData** est utilisé pour gérer les fichiers *enrichdata* de l’application.
Ces fichiers permettent d’ajouter des informations complémentaires utilisées par FIS Relay.

Au début du projet, ces fichiers existaient déjà sur les serveurs.
Mon objectif était de les **récupérer automatiquement** puis de les intégrer dans la structure Ansible.

Pour cela, j’ai travaillé sur :
- **`build_all_ini_enrichdata_fisrelay.sh`** : parcourt les environnements existants et récupère les fichiers nécessaires.
- **`build_all_sub_fisrelay_enrichdata.sh`** : génère les parties spécifiques à chaque serveur.

Grâce à cette organisation, les fichiers EnrichData peuvent être déployés automatiquement tout en conservant les particularités de chaque environnement.
"""

# ... (Ajoute les autres contenus de la même manière)

# --- Contenu de "Ce que j'ai appris" ---
EXPERIENCE_PERSPECTIVES_CONTENT = """
Avant ce stage, je connaissais surtout l’informatique à travers les cours et quelques projets personnels.
En arrivant chez **FIS Global**, j’ai découvert un environnement professionnel beaucoup plus vaste.
J’ai compris qu’une application ne se résume pas au code qui permet de la faire fonctionner.
Derrière chaque service se cachent des **serveurs, des configurations, des outils de déploiement, des contrôles de qualité** et des équipes qui travaillent ensemble.

Au fil des semaines, j’ai découvert le fonctionnement d’un secteur que je connaissais peu : celui des **technologies financières**.
J’ai compris que ce domaine ne se limite pas au développement informatique.
On y retrouve également des métiers liés à la **gestion de projet, à l’organisation des processus, à l’accompagnement des clients** ou encore à l’amélioration continue des outils utilisés par les équipes.

Cette expérience m’a permis d’élargir ma vision du monde professionnel et de mieux comprendre les nombreuses opportunités qu’offre ce secteur.
"""

TRANSFORMATION_DIGITALE_CONTENT = """
Au cours de mon stage, j’ai pu observer **concrètement** l’impact de la transformation digitale dans le secteur financier.
Les applications utilisées par les entreprises doivent aujourd’hui être déployées **plus rapidement**, tout en garantissant un haut niveau de **fiabilité et de sécurité**.

Pour répondre à ces exigences, de plus en plus d’opérations sont automatisées.
C’est notamment ce que j’ai observé chez FIS à travers l’utilisation d’outils comme **Jenkins, Ansible et les différents scripts de génération de configuration**.

Les tâches répétitives sont progressivement remplacées par des processus automatisés capables d’effectuer les mêmes opérations de manière **plus rapide et plus fiable**.

Cette évolution permet de :
- Réduire les erreurs humaines ;
- Gagner du temps ;
- Garantir une meilleure cohérence entre les différents environnements utilisés par l’entreprise.

Les missions sur lesquelles j’ai travaillé participent directement à cette démarche.
Les scripts développés permettent par exemple de générer automatiquement des fichiers de configuration qui étaient auparavant plus longs à produire et à maintenir.

J’ai également constaté que cette transformation modifie les **méthodes de travail**.
Les équipes passent moins de temps sur des tâches répétitives et peuvent se concentrer davantage sur :
- L’amélioration des processus ;
- L’analyse des problèmes ;
- L’optimisation des outils existants.

Cette expérience m’a permis de comprendre que la transformation digitale ne consiste pas simplement à utiliser de nouvelles technologies.
Elle représente avant tout une **évolution des méthodes de travail** visant à rendre les organisations plus efficaces, plus fiables et plus réactives face aux besoins de leurs clients.
"""

# ... (Ajoute le reste des contenus ici)

# --- Contenu du bilan ---
DIFFICULTES_CONTENT = """
Au début du stage, la principale difficulté a été de comprendre l’environnement dans lequel j’allais travailler.
Je découvrais de nombreux outils, de nouvelles méthodes de travail et un vocabulaire que je ne connaissais pas encore.

Lorsque j’entendais parler de **Jenkins, Ansible, rôles, playbooks** ou encore de fichiers de configuration, ces notions me semblaient très abstraites.
J’avais du mal à comprendre comment tous ces éléments fonctionnaient ensemble.

L’une des difficultés les plus importantes a donc été de comprendre **le lien entre les différents outils** utilisés dans le projet.
Il m’a fallu du temps pour comprendre comment :
1. Les scripts généraient les fichiers de configuration ;
2. Ces fichiers étaient intégrés dans Ansible ;
3. Jenkins utilisait ensuite l’ensemble pour réaliser les déploiements.

Au début, je voyais chaque élément séparément.
Je comprenais ce que faisait un script ou un fichier, mais je ne comprenais pas encore la **chaîne complète**.

Une autre difficulté était de comprendre l’organisation des fichiers de configuration.
Entre les **commons, les fichiers .sub, les rôles Ansible** et les différents environnements, il n’était pas toujours évident de savoir où se trouvait l’information recherchée.

J’ai progressivement appris à naviguer dans cette structure et à identifier plus rapidement les éléments utiles.

J’ai également dû apprendre à travailler dans un environnement **Linux**.
Certaines commandes et certaines méthodes de travail étaient totalement nouvelles pour moi.
Il fallait apprendre à se repérer dans les serveurs, comprendre leur organisation et retrouver les fichiers nécessaires pour effectuer les vérifications demandées.

La lecture des scripts existants a également représenté un défi.
Les projets étaient déjà en place avant mon arrivée et comportaient de nombreux scripts développés au fil du temps.
Avant de pouvoir les modifier ou les améliorer, je devais d’abord comprendre leur logique et la manière dont ils interagissaient entre eux.

Cette phase d’apprentissage demandait de la **patience, de la rigueur et beaucoup d’observation**.

Ce que j’ai le plus apprécié, c’est que les difficultés rencontrées au début ont progressivement laissé place à une meilleure compréhension du projet.
Chaque problème résolu me permettait de comprendre un peu mieux l’environnement sur lequel je travaillais.
Petit à petit, ce qui me semblait complexe est devenu plus clair.

Aujourd’hui, je réalise que ces difficultés ont été **essentielles dans mon apprentissage**.
Elles m’ont permis de développer :
- Ma capacité d’adaptation ;
- Ma persévérance ;
- Mon autonomie face à des situations nouvelles.
"""

# ... (Ajoute le reste des contenus du bilan)
