// ===============================
// Marketing Campaign Prediction
// script.js
// ===============================

document.addEventListener("DOMContentLoaded", function () {

    const form = document.querySelector("form");
    const submitButton = document.querySelector("button[type='submit']");
    const inputs = document.querySelectorAll("input, select");

    // ===========================
    // Form Validation
    // ===========================

    form.addEventListener("submit", function (event) {

        let valid = true;

        inputs.forEach(function (input) {

            if (input.value.trim() === "") {

                valid = false;
                input.style.border = "2px solid red";

            } else {

                input.style.border = "1px solid #ccc";

            }

        });

        if (!valid) {

            alert("Please fill in all the required fields.");
            event.preventDefault();
            return;

        }

        // ===========================
        // Loading Button
        // ===========================

        submitButton.disabled = true;
        submitButton.innerHTML = "Predicting...";

    });

    // ===========================
    // Highlight Focus
    // ===========================

    inputs.forEach(function (input) {

        input.addEventListener("focus", function () {

            this.style.border = "2px solid #2196F3";

        });

        input.addEventListener("blur", function () {

            this.style.border = "1px solid #ccc";

        });

    });

    // ===========================
    // Reset Form
    // ===========================

    const resetButton = document.querySelector("button[type='reset']");

    if (resetButton) {

        resetButton.addEventListener("click", function () {

            inputs.forEach(function (input) {

                input.style.border = "1px solid #ccc";

            });

        });

    }

});