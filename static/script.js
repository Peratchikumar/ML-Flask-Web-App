// =========================================
// Marketing Campaign Response Prediction
// script.js
// =========================================

document.addEventListener("DOMContentLoaded", () => {

    // ===============================
    // Auto Focus
    // ===============================

    const firstInput = document.querySelector("input");

    if (firstInput) {
        firstInput.focus();
    }

    // ===============================
    // Form Validation
    // ===============================

    const form = document.querySelector("form");

    if (!form) return;

    form.addEventListener("submit", function (event) {

        const income = parseFloat(document.getElementById("Income").value);
        const kidhome = parseInt(document.getElementById("Kidhome").value);
        const teenhome = parseInt(document.getElementById("Teenhome").value);
        const recency = parseFloat(document.getElementById("Recency").value);
        const wine = parseFloat(document.getElementById("MntWines").value);

        if (income < 0) {
            alert("Income cannot be negative.");
            event.preventDefault();
            return;
        }

        if (kidhome < 0 || kidhome > 5) {
            alert("Kidhome must be between 0 and 5.");
            event.preventDefault();
            return;
        }

        if (teenhome < 0 || teenhome > 5) {
            alert("Teenhome must be between 0 and 5.");
            event.preventDefault();
            return;
        }

        if (recency < 0) {
            alert("Recency cannot be negative.");
            event.preventDefault();
            return;
        }

        if (wine < 0) {
            alert("Wine spending cannot be negative.");
            event.preventDefault();
            return;
        }

        // ===============================
        // Loading Button
        // ===============================

        const submitBtn = document.querySelector("button[type='submit']");

        if (submitBtn) {
            submitBtn.innerHTML = "⏳ Predicting...";
            submitBtn.disabled = true;
        }

    });

    // ===============================
    // Input Animation
    // ===============================

    const inputs = document.querySelectorAll("input");

    inputs.forEach(input => {

        input.addEventListener("focus", () => {
            input.style.transform = "scale(1.02)";
        });

        input.addEventListener("blur", () => {
            input.style.transform = "scale(1)";
        });

    });

});