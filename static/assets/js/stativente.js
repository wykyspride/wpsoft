
/*RECUPERATION DES BIENS DEPUIS API*/
function viderchamps(){
    document.getElementById('table_details').options.length=1;
}


function ventepriodique() {
    const debu=new Date(document.getElementById('du').value);
    const fin =new Date(document.getElementById('au').value);
      fetch("http://127.0.0.1:8000/apivente/")
        .then((response) => {return response.json();})
        .then((ventes) => {

        const table_details = document.getElementById('table_details').getElementsByTagName('tbody')[0];
        table_details.innerHTML='';

        // Filtrer les ventes entre deux dates
        const ventesFiltrees = ventes.filter(vente => {
        const dateVente = new Date(vente.datevente);
    return dateVente >= debu && dateVente <= fin;
    });

        ventesFiltrees.forEach(vent => {
            const ligne = table_details.insertRow();
            ligne.insertCell(0).textContent = vent.id;
            ligne.insertCell(1).textContent = vent.datevente;
            ligne.insertCell(2).textContent = vent.user_name;
            ligne.insertCell(3).textContent = vent.pointv_id;
            ligne.insertCell(4).textContent = vent.montant;
            ligne.insertCell(5).textContent = vent.remise;
            ligne.insertCell(6).textContent = vent.net_payer;
            ligne.insertCell(7).textContent = vent.commentaire;
        
    });
      }
    )}



function venteparcom(){
    idcom=document.getElementById("idcom").value
    fetch("http://127.0.0.1:8000/apivente/")
    .then((response) => {return response.json();})
        .then((ventes) => {
        const table_details = document.getElementById('table_details').getElementsByTagName('tbody')[0];
        table_details.innerHTML='';
        ventes.forEach(vent => {
            if (vent.user_id == idcom){
            const ligne = table_details.insertRow();
            ligne.insertCell(0).textContent = vent.id;
            ligne.insertCell(1).textContent = vent.datevente;
            ligne.insertCell(2).textContent = vent.user_name;
            ligne.insertCell(3).textContent = vent.pointv_id;
            ligne.insertCell(4).textContent = vent.montant;
            ligne.insertCell(5).textContent = vent.remise;
            ligne.insertCell(6).textContent = vent.net_payer;
            ligne.insertCell(7).textContent = vent.commentaire;
            }
        
        });
        }
)}