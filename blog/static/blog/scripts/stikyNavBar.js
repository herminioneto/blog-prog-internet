window.onscroll = function () {
  stickyNavBar();
};

const navbar = document.getElementById("nav-main-page");
const offsetTop = navbar.offsetTop;

function stickyNavBar() {
  if (window.scrollY >= offsetTop) {
    navbar.classList.add("sticky");
  } else {
    navbar.classList.remove("sticky");
  }
}
