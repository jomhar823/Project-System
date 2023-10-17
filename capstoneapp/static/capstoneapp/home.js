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

// JavaScript to handle changing the image on dropdown item click
function changeImage(imageName) {
  const imageButton = document.querySelector(".image-button");

  // Update the image source based on the selected item
  if (imageName === "login") {
    imageButton.src = "path_to_login_image.png";
  } else if (imageName === "header") {
    imageButton.src = "path_to_header_image.png";
  } else if (imageName === "content") {
    imageButton.src = "path_to_content_image.png";
  } else if (imageName === "footer") {
    imageButton.src = "path_to_footer_image.png";
  }
}

// JavaScript to toggle the dropdown menu
function toggleDropdown() {
  const dropdown = document.getElementById("imageDropdown");
  dropdown.classList.toggle("show");
}

  
// Close the dropdown if the user clicks outside of it
window.onclick = function (event) {
  if (!event.target.matches(".dropbtn")) {
    const dropdowns = document.getElementsByClassName("dropdown-content");
    for (let i = 0; i < dropdowns.length; i++) {
      const openDropdown = dropdowns[i];
      if (openDropdown.classList.contains("show")) {
        openDropdown.classList.remove("show");
      }
    }
  }
};
