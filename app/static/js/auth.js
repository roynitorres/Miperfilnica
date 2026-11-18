/**
 * MIPERFILNICA - Validaciones Interactivas del Módulo de Autenticación
 * Vanilla JavaScript (Sin dependencias externas)
 */

document.addEventListener("DOMContentLoaded", () => {
  const loginForm = document.getElementById("loginForm");
  const usernameInput = document.getElementById("username");
  const passwordInput = document.getElementById("password");
  const submitBtn = document.getElementById("submitBtn");
  const authCard = document.querySelector(".auth-card");
  const togglePwdBtn = document.getElementById("togglePwdBtn");
  const capsWarning = document.getElementById("capsWarning");

  const usernameError = document.getElementById("usernameError");
  const passwordError = document.getElementById("passwordError");

  if (!loginForm) return;

  // 1. REVELAR / OCULTAR CONTRASEÑA
  if (togglePwdBtn && passwordInput) {
    togglePwdBtn.addEventListener("click", () => {
      const isPassword = passwordInput.getAttribute("type") === "password";
      passwordInput.setAttribute("type", isPassword ? "text" : "password");

      const icon = togglePwdBtn.querySelector("i");
      if (icon) {
        icon.className = isPassword ? "bi bi-eye-slash" : "bi bi-eye";
      }

      togglePwdBtn.setAttribute(
        "aria-label",
        isPassword ? "Ocultar contraseña" : "Ver contraseña"
      );
      passwordInput.focus();
    });
  }

  // 2. DETECTOR DE BLOQ MAYÚS (CAPS LOCK)
  if (passwordInput && capsWarning) {
    const checkCapsLock = (e) => {
      if (e.getModifierState && e.getModifierState("CapsLock")) {
        capsWarning.classList.add("active");
      } else {
        capsWarning.classList.remove("active");
      }
    };

    passwordInput.addEventListener("keydown", checkCapsLock);
    passwordInput.addEventListener("keyup", checkCapsLock);
    passwordInput.addEventListener("blur", () => {
      capsWarning.classList.remove("active");
    });
  }

  // 3. FUNCIONES DE VALIDACIÓN DE CAMPOS
  const validateUsername = () => {
    const val = usernameInput.value.trim();
    if (!val) {
      showError(usernameInput, usernameError, "El nombre de usuario es obligatorio.");
      return false;
    }
    if (val.length < 3) {
      showError(usernameInput, usernameError, "El usuario debe tener al menos 3 caracteres.");
      return false;
    }
    clearError(usernameInput, usernameError);
    return true;
  };

  const validatePassword = () => {
    const val = passwordInput.value;
    if (!val) {
      showError(passwordInput, passwordError, "Por favor ingresa tu contraseña.");
      return false;
    }
    if (val.length < 4) {
      showError(passwordInput, passwordError, "La contraseña debe tener al menos 4 caracteres.");
      return false;
    }
    clearError(passwordInput, passwordError);
    return true;
  };

  const showError = (input, errorElem, message) => {
    input.classList.add("is-invalid");
    input.classList.remove("is-valid");
    if (errorElem) {
      errorElem.innerHTML = `<i class="bi bi-exclamation-circle-fill"></i> ${message}`;
      errorElem.classList.add("active");
    }
  };

  const clearError = (input, errorElem) => {
    input.classList.remove("is-invalid");
    input.classList.add("is-valid");
    if (errorElem) {
      errorElem.classList.remove("active");
      errorElem.innerHTML = "";
    }
  };

  // 4. EVENTOS EN TIEMPO REAL (INPUT & BLUR)
  if (usernameInput) {
    usernameInput.addEventListener("blur", () => {
      usernameInput.value = usernameInput.value.trim();
      validateUsername();
    });
    usernameInput.addEventListener("input", () => {
      if (usernameInput.classList.contains("is-invalid")) {
        validateUsername();
      }
    });
  }

  if (passwordInput) {
    passwordInput.addEventListener("blur", validatePassword);
    passwordInput.addEventListener("input", () => {
      if (passwordInput.classList.contains("is-invalid")) {
        validatePassword();
      }
    });
  }

  // 5. VALIDACIÓN AL ENVIAR FORMULARIO (SUBMIT)
  loginForm.addEventListener("submit", (e) => {
    const isUserValid = validateUsername();
    const isPassValid = validatePassword();

    if (!isUserValid || !isPassValid) {
      e.preventDefault();

      // Animación de temblor en la tarjeta
      if (authCard) {
        authCard.classList.remove("shake");
        void authCard.offsetWidth; // Forzar reflow para reiniciar animación
        authCard.classList.add("shake");
      }

      // Foco en el primer campo con error
      if (!isUserValid && usernameInput) {
        usernameInput.focus();
      } else if (!isPassValid && passwordInput) {
        passwordInput.focus();
      }
      return false;
    }

    // Estado visual de carga durante el submit válido
    if (submitBtn) {
      submitBtn.classList.add("loading");
      submitBtn.disabled = true;
      const btnText = submitBtn.querySelector(".auth-btn-text");
      if (btnText) {
        btnText.textContent = "Verificando acceso...";
      }
    }
  });
});
