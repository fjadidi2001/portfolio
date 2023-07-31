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
// ... (existing code)

// Function to show an alert when the "Build Project" button is clicked
function buildProject() {
    fetch('/build')
        .then(response => response.text())
        .then(output => alert(output))
        .catch(error => alert('Failed to build the project.'));
}

buildBtn.addEventListener('click', buildProject);

// Function to show an alert when the "Animate Me!" button is clicked
function animateText() {
    const text = document.querySelector('h2');
    text.style.transition = 'all 1s ease-in-out';
    text.style.transform = 'rotateY(360deg) scale(1.2)';
}

animateBtn.addEventListener('click', animateText);

// Function to redirect to the education page
function goToEducationPage() {
    window.location.href = '/education';
}

// Add an event listener to the "Education" button to redirect to the education page
const educationBtn = document.getElementById('educationBtn');
educationBtn.addEventListener('click', goToEducationPage);
