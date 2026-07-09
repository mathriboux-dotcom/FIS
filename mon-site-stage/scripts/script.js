// Attendre que le DOM soit chargé
document.addEventListener('DOMContentLoaded', function() {
    // Initialiser Highlight.js pour la coloration syntaxique
    if (typeof hljs !== 'undefined') {
        hljs.highlightAll();
    }

    // Gérer le menu mobile
    const navbarToggle = document.querySelector('.navbar-toggle');
    const navbarMenu = document.querySelector('.navbar-menu');

    if (navbarToggle && navbarMenu) {
        navbarToggle.addEventListener('click', function() {
            navbarMenu.classList.toggle('active');
            navbarToggle.classList.toggle('active');
        });
    }

    // Fermer le menu mobile si on clique en dehors
    document.addEventListener('click', function(e) {
        if (navbarToggle && navbarMenu && !navbarToggle.contains(e.target) && !navbarMenu.contains(e.target)) {
            navbarMenu.classList.remove('active');
            navbarToggle.classList.remove('active');
        }
    });

    // Gérer la navigation fluide
    document.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href').substring(1);
            const targetSection = document.getElementById(targetId);

            // Fermer le menu mobile
            if (navbarMenu && navbarToggle) {
                navbarMenu.classList.remove('active');
                navbarToggle.classList.remove('active');
            }

            // Scroll vers la section
            if (targetSection) {
                targetSection.scrollIntoView({
                    behavior: 'smooth'
                });

                // Mettre à jour l'URL sans recharger la page
                history.pushState(null, null, `#${targetId}`);
            }
        });
    });

    // Gérer l'arborescence des missions
    const treeItems = document.querySelectorAll('.tree-item');
    const missionContents = document.querySelectorAll('.mission-content');

    treeItems.forEach(item => {
        item.addEventListener('click', function() {
            const targetId = this.getAttribute('data-target');

            // Masquer tous les contenus
            missionContents.forEach(content => {
                content.classList.remove('active');
            });

            // Afficher le contenu cible
            const targetContent = document.getElementById(targetId);
            if (targetContent) {
                targetContent.classList.add('active');

                // Scroll vers le contenu si on est sur mobile
                if (window.innerWidth <= 768) {
                    targetContent.scrollIntoView({
                        behavior: 'smooth',
                        block: 'nearest'
                    });
                }
            }

            // Gérer les sous-menus
            if (targetId === 'ansible') {
                const ansibleSubitems = document.getElementById('ansible-subitems');
                if (ansibleSubitems) {
                    ansibleSubitems.style.display = ansibleSubitems.style.display === 'none' ? 'block' : 'none';
                }
            }
            if (targetId === 'roles') {
                const rolesSubitems = document.getElementById('roles-subitems');
                if (rolesSubitems) {
                    rolesSubitems.style.display = rolesSubitems.style.display === 'none' ? 'block' : 'none';
                }
            }
            if (targetId === 'scripts') {
                const scriptsSubitems = document.getElementById('scripts-subitems');
                if (scriptsSubitems) {
                    scriptsSubitems.style.display = scriptsSubitems.style.display === 'none' ? 'block' : 'none';
                }
            }
        });
    });

    // Gérer le scroll pour la navbar
    window.addEventListener('scroll', function() {
        const navbar = document.querySelector('.navbar');
        if (navbar) {
            if (window.scrollY > 50) {
                navbar.style.boxShadow = '0 2px 10px rgba(0, 0, 0, 0.15)';
            } else {
                navbar.style.boxShadow = '0 4px 6px rgba(0, 0, 0, 0.1)';
            }
        }
    });

    // Gérer le clic sur les liens de téléchargement
    document.querySelectorAll('.btn-secondary').forEach(button => {
        button.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            if (href && href.startsWith('assets/docs/')) {
                console.log(`Téléchargement de ${href}...`);
            }
        });
    });
});
