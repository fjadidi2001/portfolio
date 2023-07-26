// static/scripts.js

// Function to check if an element is in the viewport
function isInViewport(element) {
  var rect = element.getBoundingClientRect();
  return (
    rect.top >= 0 &&
    rect.left >= 0 &&
    rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
    rect.right <= (window.innerWidth || document.documentElement.clientWidth)
  );
}

// Function to add animation class to visible project cards
function showVisibleProjectCards() {
  const projectCards = document.querySelectorAll('.project-card');
  projectCards.forEach((card) => {
    if (isInViewport(card)) {
      card.classList.add('fadeIn');
    }
  });
}

// Event listener for scroll events
window.addEventListener('scroll', showVisibleProjectCards);

// Run the function on page load
window.addEventListener('load', showVisibleProjectCards);
