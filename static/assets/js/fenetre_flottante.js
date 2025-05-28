 
  
              const modal = document.getElementById("myModal");
              const btn = document.getElementById("openModal");
              const span = document.querySelector(".close");
              
              // Ouvre la fenêtre
              btn.onclick = () => {
                modal.style.display = "block";
              };
              
              // Ferme quand on clique sur le X
              span.onclick = () => {
                modal.style.display = "none";
              };
              
              // Ferme quand on clique en dehors du contenu
              window.onclick = (event) => {
                if (event.target === modal) {
                  modal.style.display = "none";
                }
              };
