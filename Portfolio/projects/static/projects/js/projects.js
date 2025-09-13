// Animations et interactions avancées
document.addEventListener('DOMContentLoaded', function() {
    // Animation d'apparition des cartes
    const projectCards = document.querySelectorAll('.project-card');
    const detailsSections = document.querySelectorAll('.details-section');
    
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);
    
    // Configuration des animations initiales
    projectCards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(40px)';
        card.style.transition = 'opacity 0.8s ease, transform 0.8s ease';
        card.style.transitionDelay = `${index * 0.1}s`;
        observer.observe(card);
    });
    
    detailsSections.forEach((section, index) => {
        section.style.opacity = '0';
        section.style.transform = 'translateX(-30px)';
        section.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        section.style.transitionDelay = `${index * 0.05 + 0.3}s`;
        observer.observe(section);
    });
    
    // Effet de parallaxe sur le header
    const projectHeaders = document.querySelectorAll('.project-header');
    projectHeaders.forEach(header => {
        header.addEventListener('mousemove', (e) => {
            const x = (e.clientX / window.innerWidth - 0.5) * 20;
            const y = (e.clientY / window.innerHeight - 0.5) * 20;
            header.style.transform = `translate(${x}px, ${y}px)`;
        });
        
        header.addEventListener('mouseleave', () => {
            header.style.transform = 'translate(0, 0)';
        });
    });
    
    // Tooltips pour les métriques
    const metricItems = document.querySelectorAll('.metric-item');
    metricItems.forEach(item => {
        item.addEventListener('mouseenter', () => {
            const value = item.querySelector('.metric-value');
            value.style.transform = 'scale(1.1)';
        });
        
        item.addEventListener('mouseleave', () => {
            const value = item.querySelector('.metric-value');
            value.style.transform = 'scale(1)';
        });
    });
    
    // Animation au scroll
    let lastScrollY = window.scrollY;
    window.addEventListener('scroll', () => {
        const currentScrollY = window.scrollY;
        const scrollDirection = currentScrollY > lastScrollY ? 'down' : 'up';
        
        document.querySelectorAll('.project-card').forEach(card => {
            const rect = card.getBoundingClientRect();
            if (rect.top < window.innerHeight * 0.8) {
                card.style.transform = `translateY(${scrollDirection === 'down' ? -10 : 0}px)`;
            }
        });
        
        lastScrollY = currentScrollY;
    });
    
    // Effet de focus sur les champs de données
    const dataHighlights = document.querySelectorAll('.data-highlight');
    dataHighlights.forEach(highlight => {
        highlight.addEventListener('mouseenter', () => {
            highlight.style.background = 'var(--primary-gradient)';
            highlight.style.backgroundClip = 'text';
            highlight.style.webkitBackgroundClip = 'text';
            highlight.style.webkitTextFillColor = 'transparent';
        });
        
        highlight.addEventListener('mouseleave', () => {
            highlight.style.background = 'none';
            highlight.style.backgroundClip = 'border-box';
            highlight.style.webkitBackgroundClip = 'border-box';
            highlight.style.webkitTextFillColor = 'var(--text-primary)';
            highlight.style.color = 'var(--text-primary)';
        });
    });
});