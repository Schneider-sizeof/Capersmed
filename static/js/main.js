document.addEventListener('DOMContentLoaded', () => {
    // Mobile menu toggle
    const menuBtn = document.querySelector('.mobile-menu-btn');
    const navLinks = document.querySelector('.nav-links');

    if(menuBtn && navLinks) {
        menuBtn.addEventListener('click', () => {
            navLinks.classList.toggle('active');
        });
    }

    // Change header background on scroll
    const header = document.querySelector('header');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            header.style.background = 'rgba(255, 255, 255, 0.98)';
            header.style.boxShadow = '0 2px 10px rgba(0,0,0,0.1)';
        } else {
            header.style.background = 'rgba(255, 255, 255, 0.95)';
            header.style.boxShadow = 'none';
        }
    });

    // WhatsApp Focus Logic
    const scrollIndicator = document.querySelector('.js-scroll-to-wa');
    const whatsappBtn = document.getElementById('whatsapp-btn');
    const aboutSection = document.getElementById('about-section');
    let waEffectShown = false;
    let waTimeout = null;

    const showWaEffect = (duration = 10000) => {
        if (waEffectShown || !whatsappBtn) return;
        waEffectShown = true;
        
        whatsappBtn.classList.add('highlight');
        
        waTimeout = setTimeout(() => {
            whatsappBtn.classList.remove('highlight');
        }, duration);
    };

    const stopWaEffect = () => {
        if (whatsappBtn) {
            whatsappBtn.classList.remove('highlight');
            if (waTimeout) clearTimeout(waTimeout);
        }
    };

    if (scrollIndicator) {
        scrollIndicator.addEventListener('click', () => {
            showWaEffect(8000);
        });
    }

    // Trigger on manual scroll
    window.addEventListener('scroll', () => {
        // Start effect when user scrolls a bit
        if (window.scrollY > 100 && !waEffectShown) {
            showWaEffect(8000);
        }
    }, { passive: true });
});
