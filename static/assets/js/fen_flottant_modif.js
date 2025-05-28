  function fen_flotante () {
    const modal = document.getElementById("myModal");
    const span = document.querySelector(".close");

    // Ouvrir automatiquement
    modal.style.display = "block";


    span.onclick = () => {
      modal.style.display = "none";
    };

    window.onclick = (event) => {
      if (event.target === modal) {
        modal.style.display = "none";
      }
    };
  }

  document.addEventListener("DOMContentLoaded", fen_flotante);
