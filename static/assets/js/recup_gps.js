
    /**RECUPERATION DES COORDONNEES GPS */
    
    function getLocation() {
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function(position) {
        var lat = position.coords.longitude;
        var lon = position.coords.latitude;
        var gps=lat+ ";"+lon;
         document.getElementById("gps").value = gps;
        });
      } else {
        alert("La géolocalisation n'est pas supportée.");
      }
    }