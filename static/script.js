// Function to update the displayed max length value
function updateMaxLength(value) {
    document.getElementById('maxLengthValue').textContent = value;
}

function paraphraseText() {
    // Get references to the text areas and buttons
    const inputText = document.getElementById('inputText');
    const outputText = document.getElementById('outputText');
    const maxLength = document.getElementById('maxLengthInput').value; // Get max length value

    // Clear any previous error messages
    outputText.value = '';

    // Show loading indicator
    document.getElementById('loadingIndicator').style.display = 'block';

    // Create a new AbortController
    const controller = new AbortController();

    fetch('http://localhost:8080/paraphrase', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        signal: controller.signal, // Pass the signal to the fetch request
        body: JSON.stringify({ text: inputText.value, max_length: maxLength }), // Include max_length in the request body
    })
    .then(response => response.json())
    .then(data => {
        outputText.value = data.paraphrased_text;
    })
    .catch(error => {
        console.error('Error:', error);
    })
    .finally(() => {
        // Hide loading indicator when request completes
        hideLoadingIndicator();
    });

    // Function to hide the loading indicator
    function hideLoadingIndicator() {
        document.getElementById('loadingIndicator').style.display = 'none';
    }

    // Function to stop the paraphrasing process
    function stopParaphrasing() {
        // Abort the ongoing fetch request
        controller.abort();
        // Hide loading indicator
        hideLoadingIndicator();
        console.log("Paraphrasing process stopped.");
    }

    // Add event listener to the stop button
    document.getElementById('stopBtn').addEventListener('click', stopParaphrasing);
}


// Function to initialize event listeners for buttons
function initializeEventListeners() {
    // Get references to the text areas and buttons
    const inputText = document.getElementById('inputText');
    const outputText = document.getElementById('outputText');
    const paraphraseBtn = document.getElementById('paraphraseBtn');
    const clearBtn = document.getElementById('clearBtn');

    // Add event listener to the clear button
    clearBtn.addEventListener('click', () => {
        // Clear input text
        inputText.value = '';
        // Clear output text
        outputText.value = '';
        // Reset file input value
        const fileInput = document.getElementById('fileInput');
        if (fileInput) {
            fileInput.value = '';
        }
    });

    // Add event listener to the paraphrase button
    paraphraseBtn.addEventListener('click', paraphraseText);

    // Add event listener to update max length value when slider changes
    document.getElementById('maxLengthInput').addEventListener('input', function() {
        updateMaxLength(this.value);
    });

    // Initial update of max length value
    updateMaxLength(document.getElementById('maxLengthInput').value);
}

// Function to toggle the sidebar
function toggleSidebar() {
    const sidebar = document.getElementById('sidebar');
    if (sidebar.style.left === '0px') {
        sidebar.style.left = '-250px'; // Hide sidebar
    } else {
        sidebar.style.left = '0px'; // Show sidebar
    }
}

// Add event listener to the menu button to toggle sidebar visibility
document.getElementById('menuBtn').addEventListener('click', toggleSidebar);

// Add event listener to close the sidebar when clicking anywhere outside of it
document.addEventListener('click', function(event) {
    const sidebar = document.getElementById('sidebar');
    const menuBtn = document.getElementById('menuBtn');
    // Check if the clicked element is not the sidebar or the menu button
    if (!sidebar.contains(event.target) && event.target !== menuBtn) {
        sidebar.style.left = '-250px'; // Hide sidebar
    }
});

// Initialize event listeners for buttons
initializeEventListeners();
