const form = document.querySelector(".main-form");
const inputs = form.querySelectorAll(".form-inputs");
const submitButton = form.querySelector("button");

// Function to check form validity
function isFormValid() {
    let allFieldsValid = true;

    inputs.forEach(input => {
        if (input.value.trim().length < 3) {
            allFieldsValid = false;
        }
    });

    return allFieldsValid;
}

// Prevent form submission if fields are invalid
form.addEventListener("submit", (event) => {
    if (!isFormValid()) {
        event.preventDefault();  // Stop the form from submitting
        alert("ERROR: Please fill out all fields with at least 3 characters before submitting.");
    }
});