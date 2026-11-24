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
  setupImagePreview("imageFileInput3", "imageLivePreview3", "imagePreviewContainer3");

  // 2.1 CONMUTADOR DINÁMICO Y CALCULADORA INTELIGENTE DE COMBOS DÚO Y TRÍO
  const categorySelect = document.getElementById("categorySelect");
  const duoBuilderBox = document.getElementById("duoBuilderBox");
  const comboBuilderTitle = document.getElementById("comboBuilderTitle");
  const image2FieldGroup = document.getElementById("image2FieldGroup");
  const image3FieldGroup = document.getElementById("image3FieldGroup");
  const image1Label = document.getElementById("image1Label");
  const platform1Select = document.getElementById("platform1Select");
  const platform2Select = document.getElementById("platform2Select");
  const platform3FieldGroup = document.getElementById("platform3FieldGroup");
  const platform3Select = document.getElementById("platform3Select");
  const duoSumDisplay = document.getElementById("duoSumDisplay");
  const originalPriceInput = document.getElementById("originalPriceInput");
  const discountInput = document.getElementById("discountInput");
  const badgePreviewText = document.getElementById("badgePreviewText");
  const productPriceInput = document.getElementById("productPriceInput");
  const productTitleInput = document.getElementById("productTitleInput");
  const inheritedImage1 = document.getElementById("inheritedImage1");
  const inheritedImage2 = document.getElementById("inheritedImage2");
  const inheritedImage3 = document.getElementById("inheritedImage3");
  const previewImg1 = document.getElementById("imageLivePreview");
  const previewContainer1 = document.getElementById("imagePreviewContainer");
  const previewImg2 = document.getElementById("imageLivePreview2");
  const previewContainer2 = document.getElementById("imagePreviewContainer2");
  const previewImg3 = document.getElementById("imageLivePreview3");
  const previewContainer3 = document.getElementById("imagePreviewContainer3");

  if (categorySelect) {
    const handleCategoryChange = () => {
      const isDuo = categorySelect.value === "combosDuo";
      const isTrio = categorySelect.value === "combotres";
      const isCombo = isDuo || isTrio;

      if (duoBuilderBox) duoBuilderBox.style.display = isCombo ? "block" : "none";
      if (platform3FieldGroup) platform3FieldGroup.style.display = isTrio ? "block" : "none";
      if (image2FieldGroup) image2FieldGroup.style.display = isCombo ? "block" : "none";
      if (image3FieldGroup) image3FieldGroup.style.display = isTrio ? "block" : "none";

      if (comboBuilderTitle) {
        comboBuilderTitle.textContent = isTrio
          ? "Configurador Automático de Mega Combo Trío (x3)"
          : "Configurador Automático de Combo Dúo (x2)";
      }

      if (image1Label) {
        image1Label.innerHTML = isCombo
          ? '<i class="bi bi-image"></i> Imagen 1 (Primera Plataforma) *'
          : 'Imagen / Portada Oficial *';
      }
    };

    categorySelect.addEventListener("change", handleCategoryChange);
  }

  const updateDuoCalculation = (source = "platforms") => {
    if (!platform1Select || !platform2Select) return;

    const isTrio = categorySelect && categorySelect.value === "combotres";

    const opt1 = platform1Select.options[platform1Select.selectedIndex];
    const opt2 = platform2Select.options[platform2Select.selectedIndex];
    const opt3 = platform3Select ? platform3Select.options[platform3Select.selectedIndex] : null;

    const price1 = opt1 ? parseFloat(opt1.dataset.price) || 0 : 0;
    const price2 = opt2 ? parseFloat(opt2.dataset.price) || 0 : 0;
    const price3 = isTrio && opt3 ? parseFloat(opt3.dataset.price) || 0 : 0;
    const sum = price1 + price2 + price3;

    if (duoSumDisplay) duoSumDisplay.textContent = `C$ ${sum.toFixed(2)}`;
    if (originalPriceInput) originalPriceInput.value = sum.toFixed(2);

    let discount = discountInput ? parseFloat(discountInput.value) || 0 : 0;

    // Actualizar título sugerido si el usuario no ha escrito uno personalizado o si está creando
    if (source === "platforms" && productTitleInput) {
      const title1 = opt1 && opt1.dataset.title ? opt1.dataset.title.trim() : "";
      const title2 = opt2 && opt2.dataset.title ? opt2.dataset.title.trim() : "";
      const title3 = isTrio && opt3 && opt3.dataset.title ? opt3.dataset.title.trim() : "";

      if (isTrio) {
        if (title1 && title2 && title3) {
          productTitleInput.value = `${title1} + ${title2} + ${title3}`;
        }
      } else {
        if (title1 && title2) {
          productTitleInput.value = `${title1} + ${title2}`;
        }
      }
    }

    // Heredar imágenes si la plataforma tiene una y no se ha subido una personalizada
    if (source === "platforms") {
      const img1 = opt1 ? opt1.dataset.image : "";
      const img2 = opt2 ? opt2.dataset.image : "";
      const img3 = isTrio && opt3 ? opt3.dataset.image : "";

      if (img1 && inheritedImage1) {
        inheritedImage1.value = img1;
        if (previewImg1) {
          previewImg1.src = `/static/${img1}`;
          if (previewContainer1) previewContainer1.style.display = "flex";
        }
      }
      if (img2 && inheritedImage2) {
        inheritedImage2.value = img2;
        if (previewImg2) {
          previewImg2.src = `/static/${img2}`;
          if (previewContainer2) previewContainer2.style.display = "flex";
        }
      }
      if (img3 && inheritedImage3) {
        inheritedImage3.value = img3;
        if (previewImg3) {
          previewImg3.src = `/static/${img3}`;
          if (previewContainer3) previewContainer3.style.display = "flex";
        }
      }
    }

    if (source === "price" && productPriceInput) {
      const finalP = parseFloat(productPriceInput.value) || 0;
      if (sum > 0) {
        discount = Math.max(0, sum - finalP);
        if (discountInput) discountInput.value = discount.toFixed(0);
      }
    } else {
      // Calcular precio final a partir de la suma y el descuento
      const finalPrice = Math.max(0, sum - discount);
      if (productPriceInput && sum > 0) {
        productPriceInput.value = finalPrice.toFixed(2);
      }
    }

    if (badgePreviewText) {
      badgePreviewText.textContent = `AHORRA C$ ${discount.toFixed(0)}`;
    }
  };

  if (platform1Select) {
    platform1Select.addEventListener("change", () => updateDuoCalculation("platforms"));
  }
  if (platform2Select) {
    platform2Select.addEventListener("change", () => updateDuoCalculation("platforms"));
  }
  if (platform3Select) {
    platform3Select.addEventListener("change", () => updateDuoCalculation("platforms"));
  }
  if (discountInput) {
    discountInput.addEventListener("input", () => updateDuoCalculation("discount"));
  }
  if (productPriceInput) {
    productPriceInput.addEventListener("input", () => {
      if (categorySelect && (categorySelect.value === "combosDuo" || categorySelect.value === "combotres")) {
        updateDuoCalculation("price");
      }
    });
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
