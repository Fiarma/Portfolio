// Fonction pour initialiser la navbar
function initNavbar() {
    const toggle = document.getElementById('navbarToggle');
    const links = document.getElementById('navbarLinks');
    
    // Vérifie que les éléments existent pour éviter les erreurs
    if (!toggle || !links) {
        console.error("Les éléments de la navbar (toggle ou links) sont introuvables.");
        return;
    }
    
    // Gère le clic sur le bouton "hamburger" pour ouvrir/fermer le menu
    toggle.addEventListener('click', function() {
        links.classList.toggle('mobile-active');
        toggle.classList.toggle('mobile-active');
        
        // Gère le défilement du corps de la page
        if (links.classList.contains('mobile-active')) {
            document.body.style.overflow = 'hidden';
        } else {
            document.body.style.overflow = '';
        }
    });

    // Écoute les clics à l'intérieur du menu
    links.addEventListener('click', function(event) {
        // Vérifie si l'élément cliqué est un lien <a>
        if (event.target.tagName === 'A') {
            // Ferme le menu lorsque l'utilisateur clique sur un lien
            links.classList.remove('mobile-active');
            toggle.classList.remove('mobile-active');
            document.body.style.overflow = '';
        }
    });

    // Gère le redimensionnement de la fenêtre pour fermer le menu si on passe en mode bureau
    window.addEventListener('resize', function() {
        if (window.innerWidth > 768) {
            links.classList.remove('mobile-active');
            toggle.classList.remove('mobile-active');
            document.body.style.overflow = '';
        }
    });
}

// Assure que le script s'exécute une fois le DOM complètement chargé
document.addEventListener('DOMContentLoaded', initNavbar);