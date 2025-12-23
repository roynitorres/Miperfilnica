document.querySelectorAll("[data-slider]").forEach(initSlider);

function initSlider(track) {
    const cards = track.children;
    let currentIndex = 0;

    const btnPrev = document.querySelector(".slider-btn.prev");
    const btnNext = document.querySelector(".slider-btn.next");
    const dotsContainer = document.querySelector("[data-dots]");

    function cardsPerView() {
        return window.innerWidth < 768 ? 1 : 4;
    }

    function maxIndex() {
        return cards.length - cardsPerView();
    }

    function moveTo(index) {
        currentIndex = Math.max(0, Math.min(index, maxIndex()));
        track.style.transform = `translateX(-${currentIndex * (100 / cardsPerView())}%)`;
        updateDots();
        updateButtons();
    }

    /* ---------- BOTONES ---------- */

    btnNext.addEventListener("click", () => {
        moveTo(currentIndex + 1);
    });

    btnPrev.addEventListener("click", () => {
        moveTo(currentIndex - 1);
    });

    /* ---------- DOTS ---------- */

    function totalSteps() {
        return maxIndex() + 1;
    }

    function createDots() {
        dotsContainer.innerHTML = "";
        for (let i = 0; i < totalSteps(); i++) {
            const dot = document.createElement("button");
            dot.addEventListener("click", () => moveTo(i));
            dotsContainer.appendChild(dot);
        }
    }

    function updateDots() {
        dotsContainer.querySelectorAll("button").forEach((dot, i) => {
            dot.classList.toggle("active", i === currentIndex);
        });
    }

    /* ---------- ESTADOS ---------- */

    function updateButtons() {
        btnPrev.disabled = currentIndex === 0;
        btnNext.disabled = currentIndex === maxIndex();
    }

    /* ---------- INIT ---------- */

    track.style.transition = "transform 0.8s ease-in-out";

    window.addEventListener("resize", () => {
        moveTo(0);
        createDots();
    });

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

