var slideIndex = 1;
showSlide(slideIndex);

// Next/previous controls
function changeSlide(n) {
  showSlide(slideIndex += n);
}

// Show current slide
function showSlide(n) {
  var slides = document.getElementsByClassName("slide");
  
  // Wrap around if end of slides reached
  if (n > slides.length) {
    slideIndex = 1;
  } else if (n < 1) {
    slideIndex = slides.length;
  }
  
  // Set all slides to inactive
  for (var i = 0; i < slides.length; i++) {
    slides[i].classList.remove("active");
    slides[i].classList.remove("fade");
  }
  
  // Set active slide and apply fade animation
  slides[slideIndex-1].classList.add("active");
  slides[slideIndex-1].classList.add("fade");
}
window.onscroll = function() {
    if (window.pageYOffset > 0) {
      document.querySelector(".navbar").classList.add("sticky");
    } else {
      document.querySelector(".navbar").classList.remove("sticky");
    }
  };
  
