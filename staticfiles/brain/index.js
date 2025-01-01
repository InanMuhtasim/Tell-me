// mobile drop-down

const burgerIcon = document.querySelector("#burger");
const navbarMenu = document.querySelector("#nav-links");

burgerIcon.addEventListener('click', ()=> {
    navbarMenu.classList.toggle('is-active');
});

const deleteButtons = document.querySelectorAll('.notification .delete');

deleteButtons.forEach(function(button) {
    button.addEventListener('click', function() {
      // Find the parent .notification element and remove it
      const notification = button.closest('.notification');
      notification.remove();
    });
  });
