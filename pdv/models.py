from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import datetime


# TYPE DE POINT DE VENTE

class type_pv (models.Model):
    libelle=models.CharField(default="", max_length=50)
    datecreation=models.DateTimeField(default=datetime.now, blank=True)
    def _str_(self):
        return self.libelle
    


    def _str_(self):
        return self.nom

# TYPE DE POINT DE VENTE

class zonecouv (models.Model):
    nom=models.CharField(default="", max_length=50)
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


#COMMERCIAL
class commercial (models.Model):
    nom=models.CharField(default="", max_length=100)
    zonecouv=models.ForeignKey(zonecouv, on_delete=models.CASCADE)
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

#POINT DE VENTE
class pointv(models.Model):
    type_pv=models.ForeignKey(type_pv, on_delete=models.CASCADE)
    nom=models.CharField(default="", max_length=200)
    proprietaire=models.CharField(default="", max_length=200)
    contact_pro=models.CharField(default="", max_length=200)
    gerant=models.CharField(default="", max_length=200, null=True)
    contact_gerant=models.CharField(default="", max_length=200, null=True)
    ville=models.CharField(default="", max_length=200)
    commune=models.CharField(default="", max_length=200)
    quartier=models.CharField(default="", max_length=200)
    gps=models.CharField(default="", max_length=200)
    commentaire=models.CharField(default="", max_length=200)
    datecreation=models.DateTimeField(default=datetime.now, blank=True)

#PRODUITS
class produit(models.Model):
    marque=models.ForeignKey(marque_prod, on_delete=models.CASCADE)
    cat=models.ForeignKey(cat_prod, on_delete=models.CASCADE)
    nom=models.CharField(default="", max_length=100)
    prixu=models.BigIntegerField(default=0,  null=True )
    qte=models.BigIntegerField(default=0,  null=True)
    seuil=models.BigIntegerField(default=0,  null=True)
    couleur=models.CharField(default="", max_length=50, null=True)
    description=models.CharField(default="", max_length=200 , null=True)
    datecreation=models.DateTimeField(default=datetime.now, blank=True)


    def _str_(self):
        return self.nom

#VENTE
class vente(models.Model):
    User=models.ForeignKey(User, on_delete=models.CASCADE)
    pointv=models.ForeignKey(pointv, on_delete=models.CASCADE)
    montant=models.BigIntegerField(default=0, )
    remise=models.BigIntegerField(default=0, )
    net_payer=models.BigIntegerField(default=0, )
    statut=models.CharField(default="", max_length=10)
    commentaire=models.CharField(default="", max_length=200)
    datevente=models.DateTimeField(default=datetime.now, blank=True)


#LIGNE DE VENTE
class ligne_vente(models.Model):
    vente_id=models.ForeignKey(vente, on_delete=models.CASCADE) 
    produit=models.ForeignKey(produit, on_delete=models.CASCADE)
    qte=models.BigIntegerField(default=0)
    prixu=models.BigIntegerField(default=0)
    prix_total=models.BigIntegerField(default=0)
    net_payer=models.BigIntegerField(default=0)
    remise=models.BigIntegerField(default=0)
    datevente=models.DateTimeField(default=datetime.now, blank=True)

    
