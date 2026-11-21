/* ==========================================================================
   MIPERFILNICA - JAVASCRIPT GLOBAL Y CALCULADORA (CLEAN CODE & VANILLA JS)
   ========================================================================== */

document.addEventListener("DOMContentLoaded", () => {
  initMobileMenu();
  initMobileAccordion();
  initNavDropdown();
  initPlatformsSlider();
  initComboCalculator();
});

/* 1. MENÚ MÓVIL INDEPENDIENTE DE BOOTSTRAP */
function initMobileMenu() {
  const toggleBtn = document.getElementById("mobileMenuBtn");
  const drawer = document.getElementById("mobileNavDrawer");

  if (!toggleBtn || !drawer) return;

  toggleBtn.addEventListener("click", () => {
    const isOpen = drawer.classList.toggle("open");
    toggleBtn.setAttribute("aria-expanded", isOpen);
    toggleBtn.innerHTML = isOpen 
      ? '<i class="bi bi-x-lg"></i>' 
      : '<i class="bi bi-list"></i>';
  });

  // Cerrar al hacer clic en un enlace
  drawer.querySelectorAll("a").forEach(link => {
    link.addEventListener("click", () => {
      drawer.classList.remove("open");
      toggleBtn.innerHTML = '<i class="bi bi-list"></i>';
    });
  });
}

/* 1.1 ACORDEÓN DESPLEGABLE EN MENÚ MÓVIL (CONTRAÍDO POR DEFECTO) */
function initMobileAccordion() {
  const toggleBtn = document.getElementById("mobileServicesToggle");
  const accordion = document.getElementById("mobileServicesAccordion");

  if (!toggleBtn || !accordion) return;

  toggleBtn.addEventListener("click", (e) => {
    e.stopPropagation();
    const isOpen = accordion.classList.toggle("open");
    toggleBtn.setAttribute("aria-expanded", isOpen);
  });
}

/* 2. MENÚ DESPLEGABLE: NUESTRO SERVICIOS */
function initNavDropdown() {
  const dropdown = document.querySelector(".nav-dropdown");
  const toggleBtn = document.getElementById("servicesDropdownBtn");

  if (!dropdown || !toggleBtn) return;

  toggleBtn.addEventListener("click", (e) => {
    e.stopPropagation();
    const isOpen = dropdown.classList.toggle("open");
    toggleBtn.setAttribute("aria-expanded", isOpen);
  });

  document.addEventListener("click", (e) => {
    if (!dropdown.contains(e.target)) {
      dropdown.classList.remove("open");
      toggleBtn.setAttribute("aria-expanded", "false");
    }
  });

  dropdown.querySelectorAll(".nav-dropdown-item").forEach(item => {
    item.addEventListener("click", () => {
      dropdown.classList.remove("open");
      toggleBtn.setAttribute("aria-expanded", "false");
    });
  });
}



/* 2.1 MOTOR DE SLIDERS HORIZONTALES (INDIVIDUALES Y COMBOS DÚO) */
function setupCardSlider({
  viewportId,
  trackId,
  prevBtnId,
  nextBtnId,
  dotsId,
  cardSelector = ".platform-card",
}) {
  const viewport = document.getElementById(viewportId);
  const track = document.getElementById(trackId);
  const btnPrev = document.getElementById(prevBtnId);
  const btnNext = document.getElementById(nextBtnId);
  const dotsContainer = document.getElementById(dotsId);

  if (!viewport || !track) return;

  const getCards = () => Array.from(track.querySelectorAll(cardSelector));

  const getMetrics = () => {
    const availableWidth = viewport.clientWidth;
    let cardsPerView = 4;
    let gap = 20;

    if (availableWidth < 600) {
      cardsPerView = 1;
      gap = 12;
    } else if (availableWidth < 992) {
      cardsPerView = 2;
      gap = 16;
    } else {
      cardsPerView = 4;
      gap = 20;
    }

    const totalGaps = (cardsPerView - 1) * gap;
    const cardWidth = Math.max(180, Math.floor((availableWidth - totalGaps) / cardsPerView));

    return { availableWidth, cardsPerView, gap, cardWidth };
  };

  const applyCardSizing = () => {
    const cards = getCards();
    if (cards.length === 0) return;

    const { cardWidth, gap, cardsPerView } = getMetrics();

    track.style.gap = `${gap}px`;
    track.style.setProperty("--platform-gap", `${gap}px`);
    track.style.setProperty("--platform-card-width", `${cardWidth}px`);

    cards.forEach((card) => {
      card.style.width = `${cardWidth}px`;
      card.style.flex = `0 0 ${cardWidth}px`;
      card.style.minWidth = `${cardWidth}px`;
      card.style.maxWidth = `${cardWidth}px`;
    });

    renderDots();
    updateControls();
  };

  const renderDots = () => {
    if (!dotsContainer) return;
    const cards = getCards();
    if (cards.length === 0) return;

    const { cardsPerView, cardWidth, gap } = getMetrics();
    const totalPages = Math.ceil(cards.length / cardsPerView);

    if (totalPages <= 1) {
      dotsContainer.style.display = "none";
      return;
    }
    dotsContainer.style.display = "flex";
    dotsContainer.innerHTML = "";

    const scrollStep = (cardWidth + gap) * cardsPerView;
    const currentScroll = viewport.scrollLeft;
    const currentPage = Math.min(
      totalPages - 1,
      Math.max(0, Math.round(currentScroll / scrollStep))
    );

    for (let i = 0; i < totalPages; i++) {
      const dot = document.createElement("button");
      dot.type = "button";
      dot.className = `platform-dot ${i === currentPage ? "is-active" : ""}`;
      dot.setAttribute("aria-label", `Página ${i + 1} de ${totalPages}`);
      dot.addEventListener("click", () => {
        const targetLeft = i * scrollStep;
        viewport.scrollTo({ left: targetLeft, behavior: "smooth" });
      });
      dotsContainer.appendChild(dot);
    }
  };

  const updateControls = () => {
    const { cardsPerView, cardWidth, gap } = getMetrics();
    const scrollLeft = viewport.scrollLeft;
    const maxScroll = Math.max(0, viewport.scrollWidth - viewport.clientWidth);
    const scrollStep = (cardWidth + gap) * cardsPerView;

    if (btnPrev) {
      const isStart = scrollLeft <= 8;
      btnPrev.disabled = isStart;
      btnPrev.classList.toggle("is-disabled", isStart);
      btnPrev.setAttribute("aria-disabled", isStart ? "true" : "false");
    }

    if (btnNext) {
      const isEnd = maxScroll === 0 || scrollLeft >= maxScroll - 8;
      btnNext.disabled = isEnd;
      btnNext.classList.toggle("is-disabled", isEnd);
      btnNext.setAttribute("aria-disabled", isEnd ? "true" : "false");
    }

    if (dotsContainer) {
      const dots = dotsContainer.querySelectorAll(".platform-dot");
      const activeIdx = Math.min(
        dots.length - 1,
        Math.max(0, Math.round(scrollLeft / scrollStep))
      );
      dots.forEach((dot, idx) => {
        dot.classList.toggle("is-active", idx === activeIdx);
      });
    }
  };

  if (btnPrev) {
    btnPrev.addEventListener("click", () => {
      const { cardWidth, gap, cardsPerView } = getMetrics();
      const scrollStep = (cardWidth + gap) * cardsPerView;
      viewport.scrollBy({ left: -scrollStep, behavior: "smooth" });
    });
  }

  if (btnNext) {
    btnNext.addEventListener("click", () => {
      const { cardWidth, gap, cardsPerView } = getMetrics();
      const scrollStep = (cardWidth + gap) * cardsPerView;
      viewport.scrollBy({ left: scrollStep, behavior: "smooth" });
    });
  }

  let scrollTimer;
  viewport.addEventListener(
    "scroll",
    () => {
      clearTimeout(scrollTimer);
      scrollTimer = setTimeout(updateControls, 25);
    },
    { passive: true }
  );

  window.addEventListener(
    "resize",
    () => {
      applyCardSizing();
    },
    { passive: true }
  );

  applyCardSizing();
  setTimeout(applyCardSizing, 100);
  setTimeout(applyCardSizing, 300);
}

function initPlatformsSlider() {
  // 1. Slider de Perfiles Individuales
  setupCardSlider({
    viewportId: "platformsViewport",
    trackId: "platformsTrack",
    prevBtnId: "platformsPrevBtn",
    nextBtnId: "platformsNextBtn",
    dotsId: "platformsDotsWrapper",
    cardSelector: ".platform-card",
  });

  // 2. Slider de Combos Dúo
  setupCardSlider({
    viewportId: "combosDuoViewport",
    trackId: "combosDuoTrack",
    prevBtnId: "combosDuoPrevBtn",
    nextBtnId: "combosDuoNextBtn",
    dotsId: "combosDuoDotsWrapper",
    cardSelector: ".combo-duo-card",
  });
}
function initComboCalculator() {
  const pills = document.querySelectorAll(".calc-pill-item");
  const countBadge = document.getElementById("selectedCountBadge");
  const badgeType = document.getElementById("comboBadgeType");
  const listContainer = document.getElementById("selectedPlatformsList");
  const subtotalEl = document.getElementById("calcSubtotal");
  const discountEl = document.getElementById("calcDiscount");
  const totalEl = document.getElementById("calcTotal");
  const orderBtn = document.getElementById("btnOrderCustomCombo");
  const orderBtnText = document.getElementById("btnOrderText");

  if (!pills.length) return;

  let selectedItems = [];

  // Toggle de Selección al hacer Clic
  pills.forEach(pill => {
    pill.addEventListener("click", () => {
      const id = pill.dataset.id;
      const name = pill.dataset.name;
      const price = parseFloat(pill.dataset.price) || 0;
      const iconCheck = pill.querySelector(".pill-check-box i");

      const existingIndex = selectedItems.findIndex(item => item.id === id);

      if (existingIndex === -1) {
        // Seleccionar
        selectedItems.push({ id, name, price });
        pill.classList.add("selected");
        if (iconCheck) iconCheck.style.display = "block";
      } else {
        // Deseleccionar
        selectedItems.splice(existingIndex, 1);
        pill.classList.remove("selected");
        if (iconCheck) iconCheck.style.display = "none";
      }

      updateCalculatorDisplay();
    });
  });

  // Pre-seleccionar las 2 primeras por defecto si están disponibles para feedback visual inmediato
  if (pills.length >= 2) {
    pills[0].click();
    pills[1].click();
  }

  function updateCalculatorDisplay() {
    const count = selectedItems.length;

    if (countBadge) {
      countBadge.textContent = `${count} seleccionada${count === 1 ? '' : 's'}`;
    }

    if (count === 0) {
      if (listContainer) {
        listContainer.innerHTML = '<p style="color:#94a3b8; font-size:0.75rem; font-style:italic;">Aún no has marcado plataformas. Haz clic en las opciones para armar tu combo.</p>';
      }
      if (badgeType) badgeType.textContent = "Selecciona cuentas";
      if (subtotalEl) subtotalEl.textContent = "C$ 0.00";
      if (discountEl) discountEl.textContent = "- C$ 0.00";
      if (totalEl) totalEl.innerHTML = 'C$ 0.00 <span style="font-size:0.85rem; font-weight:normal; color:#7dd3fc;">/mes</span>';
      if (orderBtn) {
        orderBtn.href = "https://wa.me/50576145799?text=Hola,%20deseo%20armar%20un%20combo%20personalizado";
      }
      if (orderBtnText) {
        orderBtnText.textContent = "Selecciona tus plataformas";
      }
      return;
    }

    // Render lista de chips seleccionados
    if (listContainer) {
      listContainer.innerHTML = selectedItems.map(item => `
        <div class="summary-item-chip">
          <span style="display:flex; align-items:center; gap:0.4rem;">
            <i class="bi bi-check-circle-fill" style="color:#34d399;"></i> ${escapeHtml(item.name)}
          </span>
          <span style="font-family:var(--font-mono); color:#cbd5e1;">C$ ${item.price.toFixed(2)}</span>
        </div>
      `).join('');
    }

    // Cálculo numérico
    const subtotal = selectedItems.reduce((acc, curr) => acc + curr.price, 0);

    // Descuentos progresivos
    let discountRate = 0;
    let label = "Cuenta Individual";

    if (count === 2) {
      discountRate = 0.15; // 15% Dúo
      label = "Combo Dúo (15% OFF)";
    } else if (count === 3) {
      discountRate = 0.25; // 25% Trío
      label = "Mega Trío (25% OFF)";
    } else if (count >= 4) {
      discountRate = 0.35; // 35% Pack Familiar
      label = `Super Pack x${count} (35% OFF)`;
    }

    if (badgeType) badgeType.textContent = label;

    const discountAmount = subtotal * discountRate;
    const finalTotal = subtotal - discountAmount;

    if (subtotalEl) subtotalEl.textContent = `C$ ${subtotal.toFixed(2)}`;
    if (discountEl) discountEl.textContent = `- C$ ${discountAmount.toFixed(2)} (${discountRate * 100}%)`;
    if (totalEl) {
      totalEl.innerHTML = `C$ ${finalTotal.toFixed(2)} <span style="font-size:0.85rem; font-weight:normal; color:#7dd3fc;">/mes</span>`;
    }

    // Generar enlace dinámico de WhatsApp
    const platformNames = selectedItems.map(i => i.name).join(", ");
    const waText = `Hola, armé mi Combo Personalizado en la web:\n- Plataformas: ${platformNames}\n- Total mensual en C$: C$ ${finalTotal.toFixed(2)}\n¿Me ayudan a activarlo?`;
    const waUrl = `https://wa.me/50576145799?text=${encodeURIComponent(waText)}`;

    if (orderBtn) orderBtn.href = waUrl;
    if (orderBtnText) {
      orderBtnText.textContent = `Pedir Combo por C$ ${finalTotal.toFixed(2)} en WhatsApp`;
    }
  }

  function escapeHtml(text) {
    const div = document.createElement("div");
    div.textContent = text;
    return div.innerHTML;
  }
}
