<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mes missions - Mon Stage chez FIS</title>
    <link rel="stylesheet" href="styles/main.css">
    <script src="scripts/main.js" defer></script>
</head>
<body>
    <!-- Menu latéral (identique) -->
    <aside class="sidebar">
        <!-- Menu identique aux autres pages -->
    </aside>

    <!-- Contenu spécifique à la page "Mes missions" -->
    <main class="main-content">
        <section class="section missions-section">
            <h2>Mes missions</h2>
            <div class="missions-nav">
                <button class="mission-tab active" onclick="showMission('playbooks')">Playbooks Ansible</button>
                <button class="mission-tab" onclick="showMission('inventories')">Inventories</button>
                <!-- Autres onglets -->
            </div>
            <div id="playbooks" class="mission-content active">
                <div class="mission-card">
                    <h3>📁 Playbooks Ansible</h3>
                    <p>Les playbooks pilotent les différentes étapes du déploiement...</p>
                </div>
            </div>
            <!-- Autres contenus de missions -->
        </section>
    </main>
</body>
</html>
