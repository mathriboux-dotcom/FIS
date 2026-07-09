// Navigation fluide
document.querySelectorAll('a[href^=""]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        // Ne pas interférer avec les liens vers d'autres pages
        if (this.getAttribute('href').startsWith('http') || this.getAttribute('href').includes('.html')) {
            return;
        }
        e.preventDefault();
        const targetId = this.getAttribute('href');
        const targetElement = document.querySelector(targetId);
        targetElement.scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Gestion des onglets pour les missions
function showMission(missionId) {
    document.querySelectorAll('.mission-content').forEach(content => {
        content.classList.remove('active');
    });
    document.querySelectorAll('.mission-tab').forEach(tab => {
        tab.classList.remove('active');
    });
    document.getElementById(missionId).classList.add('active');
    event.target.classList.add('active');
}
