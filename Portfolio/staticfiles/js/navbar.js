
    document.addEventListener('DOMContentLoaded', function() {
    const navbarToggle = document.querySelector('.navbar-toggle');
    const navbarLinks = document.querySelector('.navbar-links');

    navbarToggle.addEventListener('click', function() {
        navbarLinks.classList.toggle('active');
        this.classList.toggle('active');
    });
});
