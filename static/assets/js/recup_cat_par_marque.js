
/*RECUPERATION DES BIENS DEPUIS API*/
function viderchamps(){
    document.getElementById('idcat').options.length=1;
}


function recupcats() {
    idmarc=document.getElementById('idmarque').value;
    const app = document.getElementById('idcat');

    fetch("https://wykys.pythonanywhere.com/apicatparmarque/")
        .then((response) => {return response.json();})
        .then((categories) => {
            app.innerHTML = '<option value="">-------------</option>';            
            /*pour tous les elements de notre api, on insere dans le combo si l'id du bien du composant est egal à l'id du bien selectionné*/
            categories.forEach(cat_prod => {
                if (cat_prod.marque_prod_id == idmarc) {
                    const option = document.createElement("option");
                    option.value = cat_prod.id;
                    option.textContent = cat_prod.libelle;
                    app.appendChild(option);
                }
           });
    })}