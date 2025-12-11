
/*RECUPERATION DES BIENS DEPUIS API*/
function viderchamps(){
    document.getElementById('table_details').options.length=1;
}


function ventepriodique() {
    const debu=new Date(document.getElementById('du').value);
    const fin =new Date(document.getElementById('au').value);
    let a=fetch("http://127.0.0.1:8000/apivente/")
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
            ligne.insertCell(3).textContent = vent.Client_id;
            ligne.insertCell(4).textContent = vent.net_payer;
            ligne.insertCell(5).textContent = vent.commentaire;
        
    });
      }
    )}


//VENTE PAR VENDEUR
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
            ligne.insertCell(3).textContent = vent.Client_id;
            ligne.insertCell(4).textContent = vent.net_payer;
            ligne.insertCell(5).textContent = vent.commentaire;
            }
        
        });
        }
)}


//VENTES PAR POINT DE VENTE/client
function venteparpv(){
    idpointv=document.getElementById("idpv").value
    fetch("http://127.0.0.1:8000/apivente/")
    .then((response) => {return response.json();})
        .then((ventes) => {
        const table_details = document.getElementById('table_details').getElementsByTagName('tbody')[0];
        table_details.innerHTML='';
        ventes.forEach(vent => {
            if (vent.idclient == idpointv){
            const ligne = table_details.insertRow();
            ligne.insertCell(0).textContent = vent.id;
            ligne.insertCell(1).textContent = vent.datevente;
            ligne.insertCell(2).textContent = vent.user_name;
            ligne.insertCell(3).textContent = vent.Client_id;
            ligne.insertCell(4).textContent = vent.net_payer;
            ligne.insertCell(5).textContent = vent.commentaire;
            }
        
        });
        }
)}

//VENTES PAR MARQUES
function venteparmarque(){
    
    idm=document.getElementById("idmaque").value
    fetch("http://127.0.0.1:8000/apilignev/")
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
            ligne.insertCell(9).textContent = lvent.net_payer;

            }
        
        });
        }
)}


//VENTES PAR CATEGORIE

function venteparcat(){
    idc=document.getElementById("idcate").value
    fetch("http://127.0.0.1:8000/apilignev/")
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
            ligne.insertCell(9).textContent = lvent.net_vente;

            }
        
        });
        }
)}


//VENTES GENERALES PAR VENDEUR
function ventegeneraleparpvendeur() {
    let debut = new Date(document.getElementById('du').value);
    let fin = new Date(document.getElementById('au').value);
    
    fetch("http://127.0.0.1:8000/apilignev/")
        .then(response => response.json())
        .then(ventes => {
            const table_details = document.getElementById('table_details').getElementsByTagName('tbody')[0];
            table_details.innerHTML = '';

            // Filtrer les ventes dans la période et avec état "VENTE"
            const ventesFiltrees = ventes.filter(v => {
                const dateV = new Date(v.datevente);
                return dateV >= debut && dateV <= fin && v.etat === "VENTE";
            });

            // Calculer le total par commande
            const totalParCommande = ventesFiltrees.reduce((acc, v) => {
                acc[v.idcomm] = (acc[v.idcomm] || 0) + v.net_payer;
                return acc;
            }, {});

            // Afficher dans le tableau
            for (const idcomm in totalParCommande) {
                    const ligne = table_details.insertRow();
                    fetch("http://127.0.0.1:8000/apiuser").then(res => res.json()).then(users => {
                        users.forEach(us => {
                       
                        if (idcomm == us.id) {
                            ligne.insertCell(0).textContent = us.first_name;
                            ligne.insertCell(1).textContent = totalParCommande[idcomm].toFixed(2);
                        }
                }
            )
            }
        )
    }
}
)
        .catch(error => console.error("Erreur:", error));
}
