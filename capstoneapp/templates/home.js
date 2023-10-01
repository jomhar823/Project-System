// JavaScript function to toggle the sidebar
function toggleSidebar() {
  var sidebar = document.getElementById("mySidebar");
  var content = document.getElementById("main-content");
  if (sidebar.classList.contains("open")) {
    sidebar.classList.remove("open");
    content.classList.remove("open");
  } else {
    sidebar.classList.add("open");
    content.classList.add("open");
  }
}
