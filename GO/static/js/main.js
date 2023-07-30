// Get the button element
const animateBtn = document.getElementById('animateBtn');

// Function to animate the text
function animateText() {
    const text = document.querySelector('h2');
    text.style.transition = 'all 1s ease-in-out';
    text.style.transform = 'rotateY(360deg) scale(1.2)';
}

// Add a click event listener to the button
animateBtn.addEventListener('click', animateText);
const buildBtn = document.getElementById('buildBtn');

function buildProject() {
    fetch('/build')
        .then(response => response.text())
        .then(output => alert(output))
        .catch(error => alert('Failed to build the project.'));
}

buildBtn.addEventListener('click', buildProject);
