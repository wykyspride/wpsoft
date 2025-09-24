from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import datetime
    
# REGION
class Region (models.Model):
    libelle=models.CharField(default="", max_length=50)
    datecreation=models.DateTimeField(default=datetime.now, blank=True)
    def _str_(self):
        return self.libelle


# VILLE
class Ville (models.Model):
    Region=models.ForeignKey(Region, on_delete=models.CASCADE)
    libelle=models.CharField(default="", max_length=50)
    datecreation=models.DateTimeField(default=datetime.now, blank=True)
    def _str_(self):
        return self.libelle

# BASE DOM
class Basedom (models.Model):
    libelle=models.CharField(default="", max_length=50)
    Region=models.ForeignKey(Region, on_delete=models.CASCADE)
    Ville=models.ForeignKey(Ville, on_delete=models.CASCADE)
    datecreation=models.DateTimeField(default=datetime.now, blank=True)
    def _str_(self):
        return self.libelle

#VENDEUR
class Vendeur (models.Model):
    nom=models.CharField(default="", max_length=100)
    Basedom=models.ForeignKey(Basedom, on_delete=models.CASCADE)
    Region=models.ForeignKey(Region, on_delete=models.CASCADE)
    Ville=models.ForeignKey(Ville, on_delete=models.CASCADE)
    contact=models.CharField(default="", max_length=20)
    adressemail=models.CharField(default="", max_length=50)
    datecreation=models.DateTimeField(default=datetime.now, blank=True)
    profil=models.CharField(default="", max_length=50)
    datenaiss = models.DateTimeField(default="", max_length=50, blank=True)
    lieunaiss=models.CharField(default="", max_length=50)
    lieuresidence=models.CharField(default="", max_length=50)
    cni=models.CharField(default="", max_length=50)
    login=models.CharField(default="", max_length=50)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def _str_(self):
        return self.nom


#POINT DE VENTE/CLIENT
class Client(models.Model):
    Ville=models.ForeignKey(Ville, on_delete=models.CASCADE)
    Region=models.ForeignKey(Region, on_delete=models.CASCADE)
    nom=models.CharField(default="", max_length=200)
    proprietaire=models.CharField(default="", max_length=200)
    contact_pro=models.CharField(default="", max_length=200)
    gerant=models.CharField(default="", max_length=200, null=True)
    contact_gerant=models.CharField(default="", max_length=200, null=True)
    commentaire=models.CharField(default="", max_length=200)
    gps=models.CharField(default="", max_length=200)
    gpsx=models.CharField(default="", max_length=200)
    gpsy=models.CharField(default="", max_length=200)
    datecreation=models.DateTimeField(default=datetime.now, blank=True)

# CATEGORIE PRESTATAIRE
class Catpresta (models.Model):
    libelle=models.CharField(default="", max_length=50)
    datecreation=models.DateTimeField(default=datetime.now, blank=True)
    def _str_(self):
        return self.libelle

#MARQUE PRODUIT
class marque_prod(models.Model):
    libelle=models.CharField(default="", max_length=75)
    datecreation=models.DateTimeField(default=datetime.now, blank=True)

    def _str_(self):
        return self.libelle


#CATEGORIE PRODUIT
class cat_prod(models.Model):
    libelle=models.CharField(default="", max_length=75)
    marque_prod=models.ForeignKey(marque_prod, on_delete=models.CASCADE)
    datecreation=models.DateTimeField(default=datetime.now, blank=True)

    def _str_(self):
        return self.libelle

#PRODUITS
class produit(models.Model):
    marque=models.ForeignKey(marque_prod, on_delete=models.CASCADE)
    cat_prod=models.ForeignKey(cat_prod, on_delete=models.CASCADE)
    nom=models.CharField(default="", max_length=100)
    prixu=models.BigIntegerField(default=0,  null=True )
    qte=models.BigIntegerField(default=0,  null=True)
    seuil=models.BigIntegerField(default=0,  null=True)
    description=models.CharField(default="", max_length=200 , null=True)
    datecreation=models.DateTimeField(default=datetime.now, blank=True)

    def _str_(self):
        return self.nom
    

#JOURNEE
class Journe(models.Model):
    User=models.ForeignKey(User, on_delete=models.CASCADE)
    commentaire=models.CharField(default="", max_length=200, null=True)
    datejoune=models.DateTimeField(default=datetime.now, blank=True)
    etat=models.CharField(default="", max_length=20, blank=False )
    objectifjourne=models.IntegerField(default=0, null=True)
    ventejourne=models.IntegerField(default=0, null=True)
    visiterealise=models.IntegerField(default=0, null=True)
    visiteplanifie=models.IntegerField(default=0, null=True)



#VISITES VENTE
class vente(models.Model):
    User=models.ForeignKey(User, on_delete=models.CASCADE)
    Journe=models.ForeignKey(Journe, on_delete=models.CASCADE, default=0)
    Catpresta=models.ForeignKey(Catpresta, on_delete=models.CASCADE)
    Client=models.ForeignKey(Client, on_delete=models.CASCADE)
    net_payer=models.BigIntegerField(default=0, )
    commentaire=models.CharField(default="", max_length=200)
    datevente=models.DateTimeField(default=datetime.now, blank=True)
    etat=models.CharField(default="", max_length=20, blank=False )
    objectifvisite=models.IntegerField(default=0, null=True)
    visiterealise=models.IntegerField(default=0, null=True)
    visiteplanifie=models.IntegerField(default=0, null=True)
    pdvreussit=models.IntegerField(default=0, null=True)
    nbremoyskupdv=models.DecimalField(default=0, null=True,max_digits=10,decimal_places=2)
    objectifvente=models.IntegerField(default=0, null=True)
    venterealise=models.IntegerField(default=0, null=True)
    nbrebso=models.IntegerField(default=0, null=True)
    gps=models.CharField(default="", max_length=200)
    gpsx=models.CharField(default="", max_length=200)
    gpsy=models.CharField(default="", max_length=200)

#LIGNE DE VENTE
class ligne_vente(models.Model):
    vente=models.ForeignKey(vente, on_delete=models.CASCADE) 
    produit=models.ForeignKey(produit, on_delete=models.CASCADE)
    qte=models.BigIntegerField(default=0)
    prixu=models.BigIntegerField(default=0)
    net_vente=models.BigIntegerField(default=0)
    datevente=models.DateTimeField(default=datetime.now, blank=True)