
/*RECUPERATION DES BIENS DEPUIS API*/
function viderchamps(){
    document.getElementById('table_details').options.length=1;
}


function ventepriodique() {
    const debu=new Date(document.getElementById('du').value);
    const fin =new Date(document.getElementById('au').value);
    let a=fetch("https://wykys.pythonanywhere.com/apivente/")
        a.then((response) => {return response.json();})
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
    fetch("https://wykys.pythonanywhere.com/apivente/")
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



function venteparpv(){
    idpointv=document.getElementById("idpv").value
    fetch("https://wykys.pythonanywhere.com/apivente/")
    .then((response) => {return response.json();})
        .then((ventes) => {
        const table_details = document.getElementById('table_details').getElementsByTagName('tbody')[0];
        table_details.innerHTML='';
        ventes.forEach(vent => {
            if (vent.idpointv == idpointv){
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


function venteparmarque(){
    idm=document.getElementById("idmaque").value
    fetch("https://wykys.pythonanywhere.com/apilignev/")
    .then((response) => {return response.json();})
        .then((lventes) => {
        const table_details = document.getElementById('table_details').getElementsByTagName('tbody')[0];
        table_details.innerHTML='';
        lventes.forEach(lvent => {
            if (lvent.marque_id == idm){
            const ligne = table_details.insertRow();
            ligne.insertCell(0).textContent = lvent.id;
            ligne.insertCell(1).textContent = lvent.vente_id;
            ligne.insertCell(2).textContent = lvent.datevente;
            ligne.insertCell(3).textContent = lvent.comm;
            ligne.insertCell(4).textContent = lvent.pointvente;
            ligne.insertCell(5).textContent = lvent.lamarc;
            ligne.insertCell(6).textContent = lvent.lacat;
            ligne.insertCell(7).textContent = lvent.prixu;
            ligne.insertCell(8).textContent = lvent.qte;
            ligne.insertCell(9).textContent = lvent.prix_total;
            ligne.insertCell(10).textContent = lvent.remise;
            ligne.insertCell(11).textContent = lvent.net_payer;

            }
        
        });
        }
)}



function venteparcat(){
    idc=document.getElementById("idcate").value
    fetch("https://wykys.pythonanywhere.com/apilignev/")
    .then((response) => {return response.json();})
        .then((lventes) => {
        const table_details = document.getElementById('table_details').getElementsByTagName('tbody')[0];
        table_details.innerHTML='';
        lventes.forEach(lvent => {
            if (lvent.cat_id == idc){
            const ligne = table_details.insertRow();
            ligne.insertCell(0).textContent = lvent.id;
            ligne.insertCell(1).textContent = lvent.vente_id;
            ligne.insertCell(2).textContent = lvent.datevente;
            ligne.insertCell(3).textContent = lvent.comm;
            ligne.insertCell(4).textContent = lvent.pointvente;
            ligne.insertCell(5).textContent = lvent.lamarc;
            ligne.insertCell(6).textContent = lvent.lacat;
            ligne.insertCell(7).textContent = lvent.prixu;
            ligne.insertCell(8).textContent = lvent.qte;
            ligne.insertCell(9).textContent = lvent.prix_total;
            ligne.insertCell(10).textContent = lvent.remise;
            ligne.insertCell(11).textContent = lvent.net_payer;

            }
        
        });
        }
)}