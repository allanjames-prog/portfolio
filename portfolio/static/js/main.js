// Typewriter Effect
function initTypewriter() {
  const typewriterTexts = [
    "Software Developer",
    "Physics Enthusiast",
    "Problem Solver",
    "Full Stack Engineer",
    "Tech Innovator"
  ];
  
  let currentTextIndex = 0;
  const typewriterElement = document.querySelector('.typewriter-text');
  
  function typeWriter(text, i, cb) {
    if (i < text.length) {
      typewriterElement.innerHTML = text.substring(0, i + 1);
      setTimeout(() => typeWriter(text, i + 1, cb), 100);
    } else {
      setTimeout(cb, 1500);
    }
  }
  
  function startTyping() {
    typeWriter(typewriterTexts[currentTextIndex], 0, () => {
      setTimeout(eraseText, 1500);
    });
  }
  
  function eraseText() {
    let text = typewriterElement.innerHTML;
    if (text.length > 0) {
      typewriterElement.innerHTML = text.substring(0, text.length - 1);
      setTimeout(eraseText, 50);
    } else {
      currentTextIndex = (currentTextIndex + 1) % typewriterTexts.length;
      startTyping();
    }
  }
  
  startTyping();
}

// Smooth scrolling for navigation links
function initSmoothScrolling() {
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      e.preventDefault();
      
      const targetId = this.getAttribute('href');
      if (targetId === '#') return;
      
      const targetElement = document.querySelector(targetId);
      if (targetElement) {
        window.scrollTo({
          top: targetElement.offsetTop - 80,
          behavior: 'smooth'
        });
      }
    });
  });
}

// Initialize tooltips
function initTooltips() {
  const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
  tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl);
  });
}

// Animate elements when they come into view
function initScrollAnimations() {
  const animateOnScroll = function() {
    const elements = document.querySelectorAll('.timeline-item, .service-card, .project-card, .skill-category');
    
    elements.forEach(element => {
      const elementPosition = element.getBoundingClientRect().top;
      const windowHeight = window.innerHeight;
      
      if (elementPosition < windowHeight - 100) {
        element.classList.add('animate__animated', 'animate__fadeInUp');
      }
    });
  };
  
  window.addEventListener('scroll', animateOnScroll);
  animateOnScroll(); // Run once on page load
}

// Initialize all functions when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
  initTypewriter();
  initSmoothScrolling();
  initTooltips();
  initScrollAnimations();
  
  // Initialize particles.js if available
  if (typeof particlesJS !== 'undefined') {
    particlesJS.load('particles-js', '{% static "js/particles-config.json" %}', function() {
      console.log('Particles.js loaded successfully');
    });
  }
  
  // Back to top button
  const backToTopButton = document.getElementById('btn-back-to-top');
  if (backToTopButton) {
    window.addEventListener('scroll', () => {
      if (window.pageYOffset > 300) {
        backToTopButton.classList.remove('d-none');
      } else {
        backToTopButton.classList.add('d-none');
      }
    });
    
    backToTopButton.addEventListener('click', () => {
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
    });
  }
});