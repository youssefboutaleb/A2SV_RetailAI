
const navLinks = document.querySelectorAll('nav a');

navLinks.forEach(link => {
    link.addEventListener('click', (e) => {
        e.preventDefault();
        const targetId = link.getAttribute('href').substring(1);
        const targetElement = document.getElementById(targetId);
        targetElement.scrollIntoView({ behavior: 'smooth' });
    });
});


// Add an event listener to trigger the animation when the element enters the viewport
window.addEventListener("scroll", function() {
    const elements = document.querySelectorAll(".fade-in");
    elements.forEach(function(element) {
        const elementTop = element.getBoundingClientRect().top;
        const windowHeight = window.innerHeight;
        
        if (elementTop < windowHeight) {
            element.classList.add("appear");
        }
    });
});

