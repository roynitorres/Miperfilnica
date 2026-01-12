document.querySelectorAll("[data-slider]").forEach(initSlider);

function initSlider(track) {
    const cards = Array.from(track.children);
    const container = track.closest(".slider-container");

    const btnPrev = container.querySelector(".slider-btn.prev");
    const btnNext = container.querySelector(".slider-btn.next");
    /*const dotsContainer = container.querySelector("[data-dots]");*/
    const dotsContainer = container.nextElementSibling;

    let positions = [];
    let currentStep = 0;

    function cardsPerView() {
    if (window.innerWidth < 768) return 1;   // móvil
    if (window.innerWidth < 992) return 3;   // tablet (opcional, recomendado)
    return 5;                                // escritorio
}

    function buildPositions() {
        positions = [];
        const perView = cardsPerView();
        const total = cards.length;

        let i = 0;
        while (i + perView < total) {
            positions.push(i);
            i += perView;
        }

        // último paso especial (solapado)
        positions.push(total - perView);
    }

    function moveTo(step) {
        currentStep = Math.max(0, Math.min(step, positions.length - 1));

        const index = positions[currentStep];
        const cardWidth = cards[0].offsetWidth;
        const gap = parseFloat(getComputedStyle(track).gap) || 0;

        const offset = index * (cardWidth + gap);
        track.style.transform = `translateX(-${offset}px)`;

        updateDots();
        updateButtons();
    }

    /* ---------- BOTONES ---------- */

    btnNext.addEventListener("click", () => moveTo(currentStep + 1));
    btnPrev.addEventListener("click", () => moveTo(currentStep - 1));

    /* ---------- DOTS ---------- */

    function createDots() {
        dotsContainer.innerHTML = "";
        positions.forEach((_, i) => {
            const dot = document.createElement("button");
            dot.addEventListener("click", () => moveTo(i));
            dotsContainer.appendChild(dot);
        });
    }

    function updateDots() {
        dotsContainer.querySelectorAll("button").forEach((dot, i) => {
            dot.classList.toggle("active", i === currentStep);
        });
    }

    function updateButtons() {
        btnPrev.disabled = currentStep === 0;
        btnNext.disabled = currentStep === positions.length - 1;
    }

    /* ---------- INIT ---------- */

    track.style.transition = "transform 0.8s ease-in-out";

    window.addEventListener("resize", () => {
        buildPositions();
        createDots();
        moveTo(0);
    });

    buildPositions();
    createDots();
    moveTo(0);
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

/* ==============================
   Animacion de contadores - About Us
================================ */


document.addEventListener("DOMContentLoaded", () => {
    const counters = document.querySelectorAll(".about-card h3");
    let started = false;

    function animateCounters() {
        const section = document.querySelector(".about-cards");
        const sectionTop = section.getBoundingClientRect().top;
        const screenHeight = window.innerHeight;

        // Activar animación solo cuando la sección está visible
        if (sectionTop < screenHeight && !started) {
            counters.forEach(counter => {
                const targetText = counter.textContent.trim();
                let isPercentage = targetText.includes("%");
                let isPlus = targetText.includes("+");

                // Extraer solo el número
                const targetNumber = parseFloat(targetText.replace(/[^\d.]/g, ""));
                let current = 0;
                const increment = targetNumber / 100; // Ajusta velocidad de animación

                const updateCounter = setInterval(() => {
                    current += increment;
                    if (current >= targetNumber) {
                        counter.textContent = targetNumber + (isPercentage ? "%" : "") + (isPlus ? "+" : "");
                        clearInterval(updateCounter);
                    } else {
                        // Mostrar número redondeado, mantener decimales si los tiene
                        counter.textContent = (targetNumber % 1 !== 0 ? current.toFixed(1) : Math.floor(current)) 
                                              + (isPercentage ? "%" : "") + (isPlus ? "+" : "");
                    }
                }, 20); // velocidad de actualización en ms
            });

            started = true; // Evitar que se repita la animación
        }
    }

    // Escuchar scroll y cargar inicial
    window.addEventListener("scroll", animateCounters);
    animateCounters(); // Por si la sección ya está visible al cargar
});
