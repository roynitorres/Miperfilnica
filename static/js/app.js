document.querySelectorAll("[data-slider]").forEach(initSlider);

function initSlider(track) {
    let currentStep = 0;
    const totalCards = track.children.length;
    const delay = 5000;

    function getCardsPerView() {
        return window.innerWidth < 768 ? 1 : 4; // móvil = 1, desktop = 4
    }

    function move() {
        const cardsPerView = getCardsPerView();
        const totalSteps = Math.ceil(totalCards / cardsPerView) - 1;

        currentStep++;

        if (currentStep > totalSteps) {
            track.style.transition = "none";
            track.style.transform = "translateX(0)";
            currentStep = 0;

            requestAnimationFrame(() => {
                requestAnimationFrame(() => {
                    track.style.transition = "transform 0.9s ease-in-out";
                    track.style.transform = `translateX(-${currentStep * 100}%)`;
                });
            });
        } else {
            track.style.transition = "transform 0.9s ease-in-out";
            track.style.transform = `translateX(-${currentStep * 100}%)`;
        }
    }

    let interval = setInterval(move, delay);

    track.addEventListener("mouseenter", () => clearInterval(interval));
    track.addEventListener("mouseleave", () => {
        interval = setInterval(move, delay);
    });

    // Actualizar on resize para mantener responsive
    window.addEventListener("resize", () => {
        track.style.transition = "none";
        track.style.transform = `translateX(-${currentStep * 100}%)`;
    });
}





/*Animacion para ver los baner al hacer escroll*/
document.addEventListener("DOMContentLoaded", () => {
    const banners = document.querySelectorAll(".step-banner");

    const observer = new IntersectionObserver(
        entries => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add("show");
                    observer.unobserve(entry.target);
                }
            });
        },
        {
            threshold: 0.3
        }
    );

    banners.forEach((banner, index) => {
        banner.style.setProperty("--delay", `${index * 0.15}s`);
        observer.observe(banner);
    });
});

/*Animacion del footer*/
document.addEventListener("DOMContentLoaded", () => {
    const footer = document.querySelector(".footer-animate");

    if (!footer) return;

    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add("show");
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.2 });

    observer.observe(footer);
});

