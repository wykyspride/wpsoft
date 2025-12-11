function kpiterritoire() {
    let debut = document.getElementById('du').value;
    let fin = document.getElementById('au').value;

    let totaltplan = 0;
    let totalreal = 0;
    let pourcentage = 0;

    const table_details = document.getElementById('table_details').getElementsByTagName('tbody')[0];
    table_details.innerHTML = ''; // vider le tableau

    fetch("http://127.0.0.1:8000/apikpiterritoire/")
        .then(response => response.json())
        .then(lesventes => {

            // Parcours des ventes
            lesventes.forEach(v => {
                if (v.datevente >= debut && v.datevente <= fin) {
                    totaltplan += parseFloat(v.visiteplanifie);
                    totalreal += parseFloat(v.visiterealise);
                }
            });

            if (totaltplan > 0) {
                pourcentage = (totalreal * 100) / totaltplan;
            }

            // Calcul visites réussies venterealise
            let totalreussi = lesventes.filter(v => v.datevente >= debut && v.datevente <= fin && v.etat === "VENTE").length;
            let totalreussi_real = lesventes.filter(v => v.datevente >= debut && v.datevente <= fin && v.etat === "VENTE").length;
            let pourcentagereussi_real = (totalreussi > 0) ? (totalreussi_real * 100) / totalreussi : 0;
            // Fonction utilitaire pour ajouter une ligne
            function ajouterLigne(libelle, val1, val2, val3) {
                const ligne = table_details.insertRow();
                ligne.insertCell(0).textContent = libelle;
                ligne.insertCell(1).textContent = val1;
                ligne.insertCell(2).textContent = val2;
                ligne.insertCell(3).textContent = val3 + " %";

            }

            // Insertion des lignes
            ajouterLigne("Visites Planifiées (Respect Routing)", totaltplan, totalreal, pourcentage.toFixed(2));
            ajouterLigne("Visites Effectuées", totaltplan, totalreal, pourcentage.toFixed(2));
            ajouterLigne("Visites Réussies", totalreussi, totalreussi_real, pourcentagereussi_real.toFixed(2));
            ajouterLigne("Moyenne Commande", totaltplan, totalreal, pourcentage.toFixed(2));
            ajouterLigne("Sell Out FDV", totaltplan, totalreal, pourcentage.toFixed(2));
            ajouterLigne("Sell Out Grossiste", totaltplan, totalreal, pourcentage.toFixed(2));
            ajouterLigne("Sell In FSM", totaltplan, totalreal, pourcentage.toFixed(2));
            ajouterLigne("Sell Out VS Sell In", totaltplan, totalreal, pourcentage.toFixed(2));
            ajouterLigne("Nombre de BSO", totaltplan, totalreal, pourcentage.toFixed(2));
            ajouterLigne("Nombre SKU's vendus par visite", totaltplan, totalreal, pourcentage.toFixed(2));
        });
}
