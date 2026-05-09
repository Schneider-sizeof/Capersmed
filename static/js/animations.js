document.addEventListener('DOMContentLoaded', () => {
    // Check if GSAP is loaded
    if (typeof gsap !== 'undefined' && typeof ScrollTrigger !== 'undefined') {
        gsap.registerPlugin(ScrollTrigger);

        // Hero Text Animation
        gsap.from(".hero-content h1", {
            duration: 1,
            y: 50,
            opacity: 0,
            ease: "power3.out",
            delay: 0.2
        });

        gsap.from(".hero-content p", {
            duration: 1,
            y: 30,
            opacity: 0,
            ease: "power3.out",
            delay: 0.4
        });

        gsap.from(".hero-content .btn", {
            duration: 1,
            y: 20,
            opacity: 0,
            ease: "power3.out",
            delay: 0.6,
            stagger: 0.2
        });

        // Parallax Effect for Hero
        gsap.to(".hero", {
            backgroundPosition: "50% 100%",
            ease: "none",
            scrollTrigger: {
                trigger: ".hero",
                start: "top top",
                end: "bottom top",
                scrub: true
            }
        });

        // Fade in elements on scroll
        const fadeElements = document.querySelectorAll('.fade-up');
        fadeElements.forEach(elem => {
            gsap.from(elem, {
                scrollTrigger: {
                    trigger: elem,
                    start: "top 85%",
                },
                y: 50,
                opacity: 0,
                duration: 0.8,
                ease: "power2.out"
            });
        });

        // Stagger product cards
        const productGrids = document.querySelectorAll('.product-grid');
        productGrids.forEach(grid => {
            gsap.from(grid.children, {
                scrollTrigger: {
                    trigger: grid,
                    start: "top 80%"
                },
                y: 40,
                opacity: 0,
                duration: 0.6,
                stagger: 0.15,
                ease: "power2.out"
            });
        });
    }
});
