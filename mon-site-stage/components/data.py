STAGE_INFO = {
    "entreprise": "FIS Financial Systems France",
    "dates": "18/05/2026 – 10/07/2026",
    "tuteur": "Franck-Olivier Robidas",
    "duree": "8 semaines",
    "projet_personnel_dates": "13/07/2026 – 24/07/2026",
    "projet_personnel_titre": "Stage intensif d’anglais",
}

# Description des missions (pour l'arborescence)
MISSIONS = {
    "playbooks": {
        "title": "📁 Playbooks Ansible",
        "description": "Scénarios de déploiement pour Ansible. Ils définissent les actions à exécuter (installation, configuration, vérification).",
        "processus": [
            "Vérification de l'environnement",
            "Sauvegarde de l'ancienne version",
            "Installation de la nouvelle version",
            "Déploiement des configurations",
            "Redémarrage du service"
        ],
        "scripts": ["deploy_fisrelay.yml"],
        "resultat": "Déploiements automatisés, fiables et reproductibles."
    },
    "inventories": {
        "title": "📁 Inventories",
        "description": "Fichiers qui décrivent les serveurs cibles pour Ansible. Ils associent les configurations aux machines.",
        "processus": [
            "Définition des groupes de serveurs (ex: production, staging)",
            "Association des variables spécifiques",
            "Lien avec les playbooks"
        ],
        "scripts": ["inventory_prod.ini", "inventory_staging.ini"],
        "resultat": "Déploiements ciblés et adaptés à chaque environnement."
    },
    "fisrelay": {
        "title": "📁 FIS Relay",
        "description": "Rôle principal pour gérer les configurations de l’application FIS Relay.",
        "processus": [
            "Analyse des configurations existantes",
            "Création des fichiers **commons** (valeurs partagées)",
            "Génération des fichiers **.sub** (valeurs spécifiques)",
            "Intégration dans Ansible"
        ],
        "scripts": [
            "build_all_common_ini_prod.sh",
            "build_all_sub_fisrelay.sh",
            "restore_ini_fisrelay.sh"
        ],
        "resultat": "Réduction des erreurs de configuration et gain de temps."
    },
    # Ajoute les autres missions ici (fisrelay_calendar, jenkins, etc.)
}
