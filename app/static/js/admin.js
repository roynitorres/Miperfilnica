/**
 * MIPERFILNICA - JavaScript Interactivo del Panel Administrativo
 * Vanilla JS Puro (Sin Bootstrap, Sin jQuery)
 */

document.addEventListener("DOMContentLoaded", () => {
  // 1. FILTRADO Y BÚSQUEDA EN TIEMPO REAL
  const searchInput = document.getElementById("adminSearchInput");
  const tabButtons = document.querySelectorAll(".admin-tab-btn");
  const tableRows = document.querySelectorAll(".admin-product-row");
  const emptyState = document.getElementById("adminEmptyState");
  const visibleCountElem = document.getElementById("visibleCount");
  const tableCard = document.getElementById("adminTableCard");

  const initialActiveTab = document.querySelector(".admin-tab-btn.active");
  let activeCategory = initialActiveTab ? (initialActiveTab.dataset.category || "platform") : "platform";
  let searchQuery = "";

  const applyFilters = () => {
    let visibleCount = 0;

    tableRows.forEach((row) => {
      const title = (row.dataset.title || "").toLowerCase();
      const category = row.dataset.category || "";
      const code = (row.dataset.code || "").toLowerCase();

      const matchesCategory =
        activeCategory === "all" || category === activeCategory;
      const matchesSearch =
        !searchQuery ||
        title.includes(searchQuery) ||
        code.includes(searchQuery);

      if (matchesCategory && matchesSearch) {
        row.style.display = "";
        visibleCount++;
      } else {
        row.style.display = "none";
      }
    });

    // Actualizar contador
    if (visibleCountElem) {
      visibleCountElem.textContent = visibleCount;
    }

    // Mostrar estado vacío si no hay coincidencias
    if (emptyState) {
      if (visibleCount === 0 && tableRows.length > 0) {
        emptyState.style.display = "flex";
      } else {
        emptyState.style.display = "none";
      }
    }
  };

  // Evento de búsqueda por texto
  if (searchInput) {
    searchInput.addEventListener("input", (e) => {
      searchQuery = e.target.value.trim().toLowerCase();
      applyFilters();
    });
  }

  // Evento de pestañas de categoría
  tabButtons.forEach((btn) => {
    btn.addEventListener("click", () => {
      tabButtons.forEach((b) => b.classList.remove("active"));
      btn.classList.add("active");
      activeCategory = btn.dataset.category || "platform";
      applyFilters();
    });
  });

  // Aplicar filtro inicial según pestaña activa
  applyFilters();

  // 2. PREVISUALIZACIÓN DE IMÁGENES EN TIEMPO REAL (FORMULARIO: IMAGEN 1 E IMAGEN 2)
  const setupImagePreview = (inputId, previewImgId, containerId) => {
    const fileInput = document.getElementById(inputId);
    const previewImg = document.getElementById(previewImgId);
    const previewContainer = document.getElementById(containerId);

    if (fileInput && previewImg) {
      fileInput.addEventListener("change", (e) => {
        const file = e.target.files[0];
        if (file) {
          if (!file.type.startsWith("image/")) {
            alert("Por favor selecciona un archivo de imagen válido (.png, .jpg, .svg, .webp)");
            fileInput.value = "";
            return;
          }

          const reader = new FileReader();
          reader.onload = (event) => {
            previewImg.src = event.target.result;
            if (previewContainer) {
              previewContainer.style.display = "flex";
            }
          };
          reader.readAsDataURL(file);
        }
      });
    }
  };

  setupImagePreview("imageFileInput", "imageLivePreview", "imagePreviewContainer");
  setupImagePreview("imageFileInput2", "imageLivePreview2", "imagePreviewContainer2");

  // 2.1 CONMUTADOR DINÁMICO DE CAMPOS SEGÚN CATEGORÍA (COMBOS DÚO = 2 IMÁGENES)
  const categorySelect = document.getElementById("categorySelect");
  const image2FieldGroup = document.getElementById("image2FieldGroup");
  const image1Label = document.getElementById("image1Label");

  if (categorySelect && image2FieldGroup) {
    const handleCategoryChange = () => {
      const isDuo = categorySelect.value === "combosDuo";
      image2FieldGroup.style.display = isDuo ? "block" : "none";
      if (image1Label) {
        image1Label.innerHTML = isDuo
          ? '<i class="bi bi-image"></i> Imagen 1 (Primera Plataforma del Combo Dúo) *'
          : 'Imagen / Portada Oficial *';
      }
    };

    categorySelect.addEventListener("change", handleCategoryChange);
  }

  // 3. CIERRE DE ALERTAS
  const closeAlertBtns = document.querySelectorAll(".admin-alert-close");
  closeAlertBtns.forEach((btn) => {
    btn.addEventListener("click", () => {
      const alert = btn.closest(".admin-alert");
      if (alert) {
        alert.style.opacity = "0";
        alert.style.transform = "translateY(-8px)";
        setTimeout(() => alert.remove(), 250);
      }
    });
  });

  // 4. MENÚ DESPLEGABLE DE USUARIO EN TOPBAR
  const userDropdown = document.getElementById("adminUserDropdown");
  const userBtn = document.getElementById("adminUserBtn");

  if (userDropdown && userBtn) {
    userBtn.addEventListener("click", (e) => {
      e.stopPropagation();
      const isActive = userDropdown.classList.toggle("active");
      userBtn.setAttribute("aria-expanded", isActive ? "true" : "false");
    });

    // Cerrar al hacer clic fuera
    document.addEventListener("click", (e) => {
      if (!userDropdown.contains(e.target)) {
        userDropdown.classList.remove("active");
        userBtn.setAttribute("aria-expanded", "false");
      }
    });

    // Cerrar con tecla Escape
    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape" && userDropdown.classList.contains("active")) {
        userDropdown.classList.remove("active");
        userBtn.setAttribute("aria-expanded", "false");
        userBtn.focus();
      }
    });
  }
});
