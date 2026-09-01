
document.addEventListener("DOMContentLoaded", () => {

    const forms = document.querySelectorAll("form");

    forms.forEach(form => {
        form.addEventListener("submit", () => {
            const button = form.querySelector("button[type='submit']");

            if (button) {
                button.disabled = true;
                button.style.opacity = "0.7";
                button.textContent = "Please wait...";
            }
        });
    });

    const passwordInputs = document.querySelectorAll(
        "input[type='password']"
    );

    passwordInputs.forEach(input => {
        const wrapper = document.createElement("div");

        wrapper.style.position = "relative";

        input.parentNode.insertBefore(wrapper, input);
        wrapper.appendChild(input);

        const toggle = document.createElement("button");

        toggle.type = "button";
        toggle.textContent = "Show";
        toggle.style.position = "absolute";
        toggle.style.right = "10px";
        toggle.style.top = "9px";
        toggle.style.padding = "7px 10px";
        toggle.style.fontSize = "12px";
        toggle.style.background = "transparent";
        toggle.style.color = "#6366f1";
        toggle.style.boxShadow = "none";

        wrapper.appendChild(toggle);

        toggle.addEventListener("click", () => {
            if (input.type === "password") {
                input.type = "text";
                toggle.textContent = "Hide";
            } else {
                input.type = "password";
                toggle.textContent = "Show";
            }
        });
    });

    const textarea = document.querySelector("textarea[name='question']");

    if (textarea) {
        textarea.addEventListener("keydown", event => {
            if (event.key === "Enter" && !event.shiftKey) {
                event.preventDefault();

                const form = textarea.closest("form");

                if (form) {
                    form.requestSubmit();
                }
            }
        });
    }

    const flashMessages = document.querySelectorAll(".flash");

    flashMessages.forEach(message => {
        setTimeout(() => {
            message.style.opacity = "0";
            message.style.transform = "translateY(-10px)";

            setTimeout(() => {
                message.remove();
            }, 300);
        }, 4000);
    });

});

