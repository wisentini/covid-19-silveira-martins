document.addEventListener('DOMContentLoaded', () => {
  const menu = document.getElementById('menu');
  const navbarLinks = document.querySelector('.navbar-menu');

  menu.addEventListener('click', () => {
    navbarLinks.classList.toggle('active');
    
    if (menu.src.match('menu.svg')) {
      menu.src = 'img/x.svg';
    } else {
      menu.src = 'img/menu.svg';
    }
  });
});