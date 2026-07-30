// ==========================================
// Marketing Campaign Response Prediction
// script.js
// ==========================================

// Wait until the page is fully loaded
document.addEventListener("DOMContentLoaded", function () {

    // Select the form
    const form = document.querySelector("form");

    if (!form) {
        return;
    }

    // Select submit button
    const submitBtn = form.querySelector("button");

    // Validate form before submitting
    form.addEventListener("submit", function (event) {

        let isValid = true;

        // Select all required input and select fields
        const fields = form.querySelectorAll("input[required], select[required]");

        fields.forEach(function(field) {

            // Remove previous error styles
            field.style.border = "1px solid #cccccc";

            // Check for empty value
            if (field.value.trim() === "") {

                field.style.border = "2px solid red";
                isValid = false;

            }

            // Check numeric values
            if (field.type === "number") {

                const value = Number(field.value);

                if (field.value !== "" && value < 0) {

                    field.style.border = "2px solid red";
                    isValid = false;

                }

            }

        });

        if (!isValid) {

            event.preventDefault();

            alert("Please fill in all required fields correctly.");

            return;

        }

        // Show loading animation
        submitBtn.innerHTML = "Predicting...";
        submitBtn.disabled = true;

    });

    // Remove error highlight while typing
    const allFields = form.querySelectorAll("input, select");

    allFields.forEach(function(field){

        field.addEventListener("input", function(){

            field.style.border = "1px solid #cccccc";

        });

        field.addEventListener("change", function(){

            field.style.border = "1px solid #cccccc";

        });

    });

});


// ==========================================
// Reset Form
// ==========================================

function resetForm(){

    const form = document.querySelector("form");

    if(form){

        form.reset();

    }

}


// ==========================================
// Show Current Year (Optional)
// ==========================================

const year = document.getElementById("year");

if(year){

    year.textContent = new Date().getFullYear();

}