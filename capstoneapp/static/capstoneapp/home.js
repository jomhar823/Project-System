document.addEventListener("DOMContentLoaded", function () {
  let slideIndex = 0;
  showSlides();

  function showSlides() {
    const slides = document.querySelectorAll(".slide");

    // Hide all slides
    slides.forEach((slide) => {
      slide.style.display = "none";
    });

    // Increment slideIndex and reset if it exceeds the number of slides
    slideIndex++;
    if (slideIndex > slides.length) {
      slideIndex = 1;
    }

    // Display the current slide
    slides[slideIndex - 1].style.display = "block";

    // Change slide every 2 seconds (2000 milliseconds)
    setTimeout(showSlides, 2000);
  }
});
