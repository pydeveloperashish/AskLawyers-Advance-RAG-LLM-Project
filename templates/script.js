// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // Select the form element
    const form = document.getElementById('textForm');

    // Add an event listener for form submission
    form.addEventListener('submit', async function(event) {
        event.preventDefault(); // Prevent the default form submission

        // Get the user input value
        const userInput = document.getElementById('userInput').value;

        try {
            // Send a POST request to the backend endpoint '/submit'
            const response = await fetch('/submit', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json', // Set the content type to JSON
                },
                body: JSON.stringify({ userInput }), // Convert user input to JSON string
            });

            // Check if the response is successful
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }

            // Parse the JSON response from the backend
            const result = await response.json();

            // Display the response in the output div
            const outputDiv = document.getElementById('output');
            outputDiv.innerText = "LLM Response: " + result["LLM Response"];

        } catch (error) {
            console.error('Error:', error); // Log any errors to the console
        }
    });
});
