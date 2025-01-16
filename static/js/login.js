document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("login-form");
    const message = document.getElementById("message");

    form.addEventListener("submit", async (event) => {
        event.preventDefault();
        const email = document.getElementById("email").value;
        const password = document.getElementById("password").value;

        try {
            const response = await fetch("/login", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ email, password }),
            });

            const result = await response.json();
            if (response.ok) {
                message.textContent = `Success: ${result.message}`;
                message.style.color = "green";
            } else {
                message.textContent = `Error: ${result.message}`;
                message.style.color = "red";
            }
        } catch (err) {
            message.textContent = "An error occurred.";
            message.style.color = "red";
        }
    });
});
