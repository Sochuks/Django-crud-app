$(document).ready(function() {
  $('#display_table').DataTable({
    "aLengthMenu": [[3, 5, 10, 25, -1], [3, 5, 10, 25, "All"]],
      "iDisplayLength": 3,
      responsive: true
     }
  );
} )


const btn = document.getElementById('menu-icon')
const nav = document.getElementById('menu')

btn.addEventListener("click", () => {
  btn.classList.toggle('open')
  nav.classList.toggle('flex')
  nav.classList.toggle('hidden')
});


