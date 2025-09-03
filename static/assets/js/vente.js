/*RECUPERATION DES PRODUITS DEPUIS API*/

    
     function insererChampsprod() {
         /*Recuperation de l'api des données*/
        idpro=document.getElementById('idprod').value;
        prod=fetch("http://127.0.0.1:8000/apidetailprod").then((response) => {
        return response.json();}).then((produit) => {
        for ( const prod of produit) {
             /*Expression de la condition necessaire pour afficher les données dans les champs*/
             if (prod.id == idpro) {
               document.getElementById("marque").value=prod.marque_id;
               document.getElementById("prixu").value=prod.prixu;
               document.getElementById("qtestock").value=prod.qte;
               document.getElementById("seuil").value=prod.seuil;
               document.getElementById("cat").value=prod.cat_id;
               document.getElementById("couleur").value=prod.couleur;
                }
                }
        });
    }



    /*RECUPERATION DES DETAILS DES POINTS DE VENTE*/
     function insererChampspv() {
         /*Recuperation de l'api des données*/
        idpv=document.getElementById('idpv').value;
        pointv=fetch("http://127.0.0.1:8000/apidetailpoitv").then((response) => {
        return response.json();}).then((pointvente) => {
        for ( const pointv of pointvente) {
             /*Expression de la condition necessaire pour afficher les données dans les champs*/
             if (pointv.id == idpv) {
               document.getElementById("region").value=pointv.Region_id;

                }
                }
        });
    }

    


///INSERTION DANS LE TABLEAU

    function insererCellules() {
        var num= document.getElementById("idprod").value;
        var designation=idprod.options[idprod.selectedIndex].text;
        var marque= document.getElementById("marque").value;
        var cat= document.getElementById("cat").value;
        var qte= parseInt ( document.getElementById("qte").value);
        var mht= parseInt ( document.getElementById("montant").value);
        var rem= parseInt ( document.getElementById("remise").value);
        var np= parseInt ( document.getElementById("netpayer").value);

      if (mht && np) {
        const table_details = document.getElementById('table_details').getElementsByTagName('tbody')[0];
        const ligne = table_details.insertRow();

        ligne.insertCell(0).textContent = num;
        ligne.insertCell(1).textContent = designation;
        ligne.insertCell(2).textContent = marque;
        ligne.insertCell(3).textContent = cat;
        ligne.insertCell(4).textContent = qte;
        ligne.insertCell(5).textContent = mht;
        ligne.insertCell(6).textContent = rem;
        ligne.insertCell(7).textContent = np;

        
      } else {
        alert("Veuillez remplir tous les champs.");
      }
    }



    /*CALCUL DES TOTAUX */

    function calcultoto(){
        /**  ANCIENNES DONNEES TOTALES DE LA  VENTE */

        let old_total=parseFloat (document.getElementById("old_total").value);
        
        /**  TOTAL LIGNE  VENTE */
        let qte= parseFloat ( document.getElementById("qte").value);
        let prixu= parseFloat ( document.getElementById("prixu").value);
        let mttc=parseFloat (qte)* parseFloat (prixu);
        let np=parseFloat(mttc)

        document.getElementById("netpayer").value=parseFloat(np);

        /** GRAND TOTAL VENTE */
        let totalvente=old_total+np;
        let totalnp=totalvente;

        document.getElementById("p_soustotal").value=parseFloat(totalvente);
        document.getElementById("p_netapayer").value=parseFloat(totalnp);




    }


    ///INSERTION DANS LE TABLEAU

    function insererCellulesventeparvendeur() {
      debut=document.getElementById('du').value
      fin=document.getElementById('au').value
      
      const table_details = document.getElementById('table_details').getElementsByTagName('tbody')[0];
        //Vider la table
          table_details.innerHTML='';

          
      //while (table_details.rows.length > 0) {
                //table_details.deleteRow(0);}


      lavente=fetch("http://127.0.0.1:8000/apiventeparvendeur").then((response) => {
      //lavente=fetch("http://127.0.0.1:8000/apiventeparvendeur").then((response) => {

        return response.json();}).then((lesventes) => {
        for ( const lavente of lesventes) {
             if (lavente.datevente>=debut & lavente.datevente<=fin ) {

            
            const ligne = table_details.insertRow();

            ligne.insertCell(0).textContent = lavente.datevente;
            ligne.insertCell(1).textContent = lavente.User__first_name;
            ligne.insertCell(2).textContent = lavente.Client__Region__libelle;
            ligne.insertCell(3).textContent = lavente.Client__nom;
            ligne.insertCell(4).textContent = lavente.nombre;
            ligne.insertCell(5).textContent = lavente.achateff;
            ligne.insertCell(6).textContent = lavente.somme;
              
      }
    }
  })}
