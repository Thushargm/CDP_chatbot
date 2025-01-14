document.addEventListener("DOMContentLoaded", () => {
    const messageInput = document.getElementById("user-message");
    const messagesDiv = document.getElementById("messages");
    const submitButton = document.getElementById("send-btn");

    async function sendMessage() {
        const userMessage = messageInput.value.trim();

        if (!userMessage) return;

        // Append user's message with a fade-in effect
        const userMessageDiv = document.createElement("div");
        userMessageDiv.className = "user-msg";
        userMessageDiv.innerHTML = `<span>You: ${userMessage}</span>`;
        messagesDiv.appendChild(userMessageDiv);
        messageInput.value = '';
        messagesDiv.scrollTop = messagesDiv.scrollHeight; // Smooth scroll to the bottom

        // Add a typing indicator
        const typingDiv = document.createElement("div");
        typingDiv.className = "bot-msg typing";
        typingDiv.innerHTML = `<span>Bot: Typing...</span>`;
        messagesDiv.appendChild(typingDiv);

        try {
            // Make an API call to GPT-Turbo backend
            const response = await fetch('/get_response/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value // Ensure CSRF token for security
                },
                body: JSON.stringify({
                    prompt: userMessage, // Message sent to GPT-Turbo
                    model: "gpt-3.5-turbo", // Specify the model (if required by your API)
                    max_tokens: 100, // Adjust as per your use case
                    temperature: 0.7 // Adjust creativity of the response
                })
            });

            const data = await response.json();

            // Remove typing indicator
            messagesDiv.removeChild(typingDiv);

            // Append GPT-Turbo's response
            const botMessageDiv = document.createElement("div");
            botMessageDiv.className = "bot-msg";
            botMessageDiv.innerHTML = `<span>Bot: ${data.response || "Sorry, I didn't understand that."}</span>`;
            messagesDiv.appendChild(botMessageDiv);

        } catch (error) {
            // Remove typing indicator
            messagesDiv.removeChild(typingDiv);

            // Append an error message
            const errorDiv = document.createElement("div");
            errorDiv.className = "bot-msg error";
            errorDiv.innerHTML = `<span>Error: ${error.message}</span>`;
            messagesDiv.appendChild(errorDiv);
        }

        // Scroll smoothly to the latest message
        messagesDiv.scrollTop = messagesDiv.scrollHeight;
    }

    // Event listener for the send button
    submitButton.addEventListener("click", sendMessage);

    // Allow Enter key to send the message
    messageInput.addEventListener("keypress", (e) => {
        if (e.key === "Enter") sendMessage();
    });
});
