/**
 * Performance optimization script for CoreFlow EPC
 * Handles lazy loading, image optimization, and user experience improvements
 */

// Performance monitoring
if (window.performance && window.performance.mark) {
    window.performance.mark('script-start');
}

document.addEventListener('DOMContentLoaded', function() {
    
    // Intersection Observer for lazy loading improvements
    if ('IntersectionObserver' in window) {
        const imageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    if (img.dataset.src) {
                        img.src = img.dataset.src;
                        img.classList.remove('lazy-placeholder');
                        observer.unobserve(img);
                    }
                }
            });
        }, {
            rootMargin: '50px 0px',
            threshold: 0.01
        });

        // Observe all images with data-src
        document.querySelectorAll('img[data-src]').forEach(img => {
            imageObserver.observe(img);
        });
    }

    // Preload critical images on hover
    const cardLinks = document.querySelectorAll('.casestudy-link');
    cardLinks.forEach(link => {
        link.addEventListener('mouseenter', function() {
            const img = this.querySelector('img[loading="lazy"]');
            if (img && !img.complete) {
                img.loading = 'eager';
            }
        }, { passive: true });
    });

    // Optimize form submissions
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function() {
            const submitBtn = this.querySelector('button[type="submit"]');
            if (submitBtn) {
                submitBtn.disabled = true;
                submitBtn.textContent = 'Processing...';
            }
        });
    });

    // Optimize animations for better performance
    const cards = document.querySelectorAll('.card');
    cards.forEach(card => {
        card.style.willChange = 'transform';
        
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-2px) translateZ(0)';
        }, { passive: true });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) translateZ(0)';
        }, { passive: true });
    });

    // Performance mark
    if (window.performance && window.performance.mark) {
        window.performance.mark('script-end');
        window.performance.measure('script-execution', 'script-start', 'script-end');
    }
});

// Service Worker registration for caching (if available)
if ('serviceWorker' in navigator && location.protocol === 'https:') {
    window.addEventListener('load', function() {
        navigator.serviceWorker.register('/sw.js')
            .then(function(registration) {
                console.log('SW registered: ', registration);
            })
            .catch(function(registrationError) {
                console.log('SW registration failed: ', registrationError);
            });
    });
}

// Critical resource hints
const criticalResources = [
    '/static/css/style.css',
    '/static/images/logo.png'
];

criticalResources.forEach(resource => {
    const link = document.createElement('link');
    link.rel = 'prefetch';
    link.href = resource;
    document.head.appendChild(link);
});
