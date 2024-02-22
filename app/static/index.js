// index.js

// Function to display the current date and time
function displayDateTime() {
    // Get the current date and time
    var currentDate = new Date();
    
    // Format the date and time
    var formattedDateTime = currentDate.toLocaleString();
    
    // Display the formatted date and time on the webpage
    document.getElementById("datetime").innerText = formattedDateTime;
}

// Call the displayDateTime function when the page loads
window.onload = displayDateTime;
