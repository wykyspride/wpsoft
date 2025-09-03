from django.shortcuts import render,redirect
from .models import  vente,Client,marque_prod, cat_prod, produit, Vendeur,vente,ligne_vente, Region,Ville,Basedom,Catpresta
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from django.db.models import Q
from num2words import num2words
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.db.models import Count, Sum
import json
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import requests

# Page d'accueil
def home(request):
    return render (request, 'index.html')

def maquette(request):
    if request.user.is_authenticated:
        user=request.user
        context={'user':user}
    return render(request, "maquette.html", context)

# Connexion.
def conex(request):
    if request.method == "POST":
        email = request.POST.get('admail', None)
        password = request.POST.get('password', None)
        user = User.objects.filter(username=email).first()
        if user:
            auth_user = authenticate(username=user.username, password=password)
             #Si le mail et le mot de passe sont justes, il se connecte
            if auth_user:
                login(request, auth_user)

                #Notification de derniere connextion
                #notif=send_mail('Notification de connexion','Nous vous envoyons ce message parceque nous avons constaté une connexion sur votre espace client djafa à la date du:'+' '+str(datetime.today())+"\n"+"\n"+ 'Cordialement','kobenanwykys@gmail.com',[email],fail_silently=False)
                
                #Redirection vers la page superadmin selon qu'il soit designé comme superadmin
                if user.is_authenticated:
                    return redirect('espaceuser',iduser=user.id)
                
                #Redirection vers la page staff selon qu'il soit designé comme un memebre du staff
                #if user.is_authenticated and user.is_staff:
                    #return redirect('espacestaff')
                
                #Sinon Redirection vers la page d'accueil
                #else:
                    #return redirect('home')

            else:
                print("mot de passe incorrecte")
        else:
            print("L'utilisateur n'existe pas")
    return render(request, 'conex.html', {})



#DECONNEXION
def deconex(request):
    logout(request)
    return redirect('conex')



#REGIONS
def region(request):
    lesregions=Region.objects.all()
    context={'lesregions':lesregions}

    if request.method =="POST":
        libelle=request.POST.get('libelle')
        saveRegion=Region.objects.create(libelle=libelle)
        saveRegion.save()
    return render(request, 'region.html',  context)

#BASE DOM
def basedom(request):
    lesbasedom=Basedom.objects.all()
    lesregions=Region.objects.all()
    lesvilles=Ville.objects.all()
    context={'lesbasedom':lesbasedom, 'lesregions':lesregions , 'lesvilles':lesvilles}

    if request.method =="POST":
        libelle=request.POST.get('libelle')
        region_id=request.POST.get('region')
        ville_id=request.POST.get('ville')
        saveBasedom=Basedom.objects.create(libelle=libelle, Region_id=region_id, Ville_id=ville_id)
        saveBasedom.save()
    return render(request, 'basedom.html',  context)


#CATEGORIE DE PRESTATAIRE
def adcatpresta (request):
    lescatpresta=Catpresta.objects.all()
    context={'lescatpresta':lescatpresta}
    if request.method =="POST":
        libelle=request.POST.get('libelle')
        savecatpresta=Catpresta.objects.create(libelle=libelle)
        savecatpresta.save()
    return render(request, 'adcatpresta.html', context)


#Espace User
def espaceuser(request, iduser):
    if request.user.is_authenticated:
        lesclients=Client.objects.all()
        lesprod=produit.objects.all()
        lescatpres=Catpresta.objects.all()
        mesventes=vente.objects.filter(User_id=iduser)
        context={'lesclients':lesclients, 'mesventes' : mesventes, "lesprod":lesprod, 'lescatpres':lescatpres }

        if request.method =="POST":
            net_payer=request.POST.get('venterealise')
            commentaire=request.POST.get('commentaire')
            datevente=request.POST.get('datevente')
            etat=request.POST.get('etat')
            nbreJtravail=request.POST.get('nbreJtravail')
            objectifvisite=request.POST.get('objectifvisite')
            visiterealise=request.POST.get('visiterealise')
            visiteplanifie=request.POST.get('visiteplanifie')
            pdvreussit=request.POST.get('pdvreussit')
            nbremoyskupdv=request.POST.get('nbremoyskupdv')
            objectifvente=request.POST.get('objectifvente')
            venterealise=request.POST.get('venterealise')
            nbrebso=request.POST.get('nbrebso')
            Catpresta_id=request.POST.get('Catpresta_id')
            Client_id=request.POST.get('Client_id')
            User_id=iduser
            savevente=vente.objects.create(User_id=User_id,Client_id=Client_id,Catpresta_id=Catpresta_id,nbrebso=nbrebso,venterealise=venterealise,objectifvente=objectifvente,nbremoyskupdv=nbremoyskupdv,pdvreussit=pdvreussit, visiteplanifie=visiteplanifie, net_payer=net_payer, commentaire=commentaire,datevente=datevente, etat=etat,  nbreJtravail=nbreJtravail, objectifvisite=objectifvisite, visiterealise=visiterealise)
            savevente.save()
    else:
        print("Veuillez vous connecter")
        return redirect(conex)
    return render(request, "espaceuser.html", context)




#VILLE
def adtypepoint(request):
    return render(request, "adtypepoint.html")

#ESPACE VILLE
def adville(request):
    lesvilles=Ville.objects.all()
    lesregions=Region.objects.all()
    context={'lesvilles':lesvilles, 'lesregions':lesregions}
    if request.method == "POST":
        libelle=request.POST.get('libelle')
        idregion=request.POST.get('idregion')
        saveville=Ville.objects.create(libelle=libelle, Region_id=idregion)
        saveville.save()
    return render(request, 'ville.html', context)


#CLENTS
def adclient(request):
    lesclients=Client.objects.all()
    lesregions=Region.objects.all()
    lesville=Ville.objects.all()
    context={'lesville':lesville, 'lesregions':lesregions, 'lesclients':lesclients}

    if request.method =="POST":
        type_pv_id=request.POST.get('idtype')
        Region_id=request.POST.get('zonecouv')
        nom=request.POST.get("nom")
        proprietaire=request.POST.get("proprietaire")
        contact_pro=request.POST.get("contact_pro")
        gerant=request.POST.get("gerant")
        contact_gerant=request.POST.get("contact_gerant")
        ville_id=request.POST.get("ville")
        commune=request.POST.get("commune")
        quartier=request.POST.get("quartier")
        gps=request.POST.get("gps")
        commentaire=request.POST.get("commentaire")
        datecreation=request.POST.get("datecreation")
        savepv=Client.objects.create(type_pv_id=type_pv_id, Region_id=Region_id, nom=nom, proprietaire=proprietaire, contact_pro=contact_pro, gerant=gerant, contact_gerant=contact_gerant, ville_id=ville_id, commune=commune,  quartier=quartier, gps=gps,  commentaire=commentaire )
        savepv.save()
    return render(request, "pointdevente.html",context)


#Marque de prduit
def marqueprod(request):
    lesmarques=marque_prod.objects.all()
    context={'lesmarques':lesmarques}
    if request.method == "POST":
        libelle=request.POST.get('libelle')
        savemarque=marque_prod.objects.create(libelle=libelle)
        savemarque.save()
    return render(request, "marque.html", context)


#CATEGORIE DE MARQUE DE PRODUIT
def catprod(request):
    lesmarques=marque_prod.objects.all()
    lescats=cat_prod.objects.all()
    context={'lesmarques':lesmarques, 'lescats':lescats}

    if request.method == "POST":
        marque_prod_id=request.POST.get('idmarque')
        libelle=request.POST.get('libelle')
        savecat=cat_prod.objects.create(marque_prod_id=marque_prod_id, libelle=libelle)
        savecat.save()
    return render(request, "catprod.html", context)

#LES CLIENTS
def adclient(request):
    lesclients=Client.objects.all()
    lesregions=Region.objects.all()
    lesvilles=Ville.objects.all()
    context={'lesclients':lesclients, 'lesregions':lesregions, 'lesvilles':lesvilles }
    if request.method=='POST':
        nom=request.POST.get('nom')
        proprietaire=request.POST.get('proprietaire')
        contact_pro=request.POST.get('contactpro')
        gerant=request.POST.get('gerant')
        contact_gerant=request.POST.get('contactgerant')
        commentaire=request.POST.get('commentaire')
        Region_id=request.POST.get('region')
        Ville_id=request.POST.get('ville')
        saveclient=Client.objects.create(nom=nom, proprietaire=proprietaire, contact_pro=contact_pro, gerant=gerant,  contact_gerant=contact_gerant, commentaire=commentaire, Region_id=Region_id, Ville_id=Ville_id )
        saveclient.save()
    return render(request, "client.html", context)

#LES PRODUITS
def prod(request):
    lesprods=produit.objects.all()
    lesmarques=marque_prod.objects.all()
    context={'lesprods':lesprods, 'lesmarques':lesmarques}

    if request.method == "POST" :
        marque=request.POST.get("idmarque")
        cat=request.POST.get("idcat")
        nom=request.POST.get("nom")
        prixu=request.POST.get("prixu")
        qte=request.POST.get("qte")
        seuil=request.POST.get("seuil")
        couleur=request.POST.get("couleur")
        description=request.POST.get("description")
        saveprod=produit.objects.create(marque_id=marque, cat_prod_id=cat, nom=nom, prixu=prixu, qte=qte, seuil=seuil, description=description)
        saveprod.save()
    return render(request, 'produit.html', context)




#API DE RECUPERATION DES CATEGORIES PAR MARQUES
    #API
def apicatparmarque(request):
    data=cat_prod.objects.all()
    datalist=[]
    for i in data:
        datalist.append({'id':i.id, 'libelle':i.libelle,  'marque_prod_id':i.marque_prod_id})
    return JsonResponse(datalist, safe=False)


#API DE RECUPERATION DES PRODUITS 
    #API
def apidetailprod(request):
    data=produit.objects.all()
    datalist=[]
    for i in data:
        datalist.append({'id':i.id, 'prixu':i.prixu, 'qte':i.qte, 'seuil':i.seuil, "marque_id":i.marque.libelle})
    return JsonResponse(datalist, safe=False)


#API DE RECUPERATION DES POINT DE VENTE 
    #API
def apidetailpoitv(request):
    data=Client.objects.all()
    datalist=[]
    for i in data:
        datalist.append({'id':i.id, 'Region_id':i.Region.libelle})
    return JsonResponse(datalist, safe=False)

#API DE RECUPERATION DES VENTE 
    #API
def apivente(request):
    data=vente.objects.all()
    datalist=[]
    for i in data:
        datalist.append({'id':i.id, "user_id":i.User_id,"user_name":i.User.first_name, "datevente":i.datevente , "Catpresta_id":i.Catpresta_id,  "net_payer":i.net_payer,  "commentaire":i.commentaire,  "Client_id":i.Client.nom, "idclient":i.Client_id})
    return JsonResponse(datalist, safe=False)


#API VENTE PAR VENDEUR PAR ZONE
def apiventeparvendeur(request):
    #◙data=(vente.objects.values('User_id','pointv__nom', 'User__first_name','datevente', 'zonecouv__nom').annotate(nombre=Count('User_id'), somme=Sum('net_payer'), achateff=Count('id', filter=Q('etat='VENTE'))).order_by()))
    data = (vente.objects.values('User_id', 'Client__nom', 'User__first_name', 'datevente', 'Client__Region__libelle').annotate(nombre=Count('User_id'),somme=Sum('net_payer'), achateff=Count('id', filter=Q(etat='VENTE'))).order_by())
    print(data)
    datalist=[]
    for i in data:
        datalist.append({ "datevente":i['datevente'],"Client__nom":i['Client__nom'] ,"User_id":i['User_id'], "User__first_name":i['User__first_name'], "Client__Region__libelle":i['Client__Region__libelle'], "nombre":i['nombre'], "achateff":i['achateff'], "somme":i['somme']  })
    return JsonResponse(datalist, safe=False)

#API DE RECUPERATION DES LIGNES VENTE 
    #API
def apilignev(request):
    data=ligne_vente.objects.all()
    datalist=[]
    for i in data:
        datalist.append({'id':i.id, "vente_id":i.vente_id,  "marque_id":i.produit_id, "lacat":i.produit.cat_prod.libelle, "lamarc":i.produit.marque.libelle, "pointvente":i.vente.Client.nom,"qte":i.qte, "prixu":i.prixu , "datevente":i.datevente, "produit_id":i.produit.nom, "net_payer":i.net_vente, "comm":i.vente.User.first_name})
    return JsonResponse(datalist, safe=False)



#USER AND COMMERCIAL COMMERCIAL
def vendeurs(request):
    lesvendeur =Vendeur.objects.all()
    lesregions=Region.objects.all()
    lesvilles=Ville.objects.all()
    lesbasedom=Basedom.objects.all()

    context={'lesvendeur': lesvendeur, 'lesregions':lesregions, 'lesvilles':lesvilles, 'lesbasedom':lesbasedom}
    if request.method == "POST":
        
        #ENREGISTREMENT DANS USER
        username=request.POST.get('login')
        password=request.POST.get("mdp")
        email=request.POST.get('adressemail')

        #ENREGISTREMENT DU COMMERCIAL
        nom=request.POST.get('nom')
        contact=request.POST.get('contact')
        ville_id=request.POST.get('ville')
        Basedom_id=request.POST.get('basedom')
        Region_id=request.POST.get('region')
        photo=request.POST.get('photo')
        datenaiss=request.POST.get('datenaiss')
        lieunaiss=request.POST.get('lieunaiss')
        lieuresidence=request.POST.get('lieuresidence')
        profil=request.POST.get('profil')
        cni=request.POST.get('cni')

        # Email
        saveuser = User(username = username, email = email,first_name=nom,last_name=nom, password=password )
        saveuser.save()
        saveuser.password = password
        saveuser.set_password(saveuser.password)
        saveuser.save()

        #ENREGISTREMENT DANS COMMERCIAL
        
        user_id=saveuser.id
        savecom=Vendeur.objects.create(nom=nom, login=username,Ville_id=ville_id,Region_id=Region_id, Basedom_id=Basedom_id, contact=contact, profil=profil, cni=cni, user_id=user_id,   adressemail=email, photo=photo, datenaiss=datenaiss, lieunaiss=lieunaiss, lieuresidence=lieuresidence     )
        savecom.save()
    return render(request, "vendeurs.html", context)



#LIGNES DE VENTE
def lignevente(request, idvente):
    lavente=vente.objects.get(id=idvente)
    if lavente.etat=="VENTE":
        lesprod=produit.objects.all()
        leslignes=ligne_vente.objects.filter(vente_id=lavente.id)
        context={'lavente':lavente, 'lesprod':lesprod, 'leslignes':leslignes }

        #Enregistrement de la ligne de vente
        if request.method=="POST":
            vente_id=lavente.id
            produit_id=request.POST.get('idprod')
            qte=request.POST.get('qte')
            prixu=request.POST.get('prixu')
            net_vente=request.POST.get('netpayer')
            datevente=lavente.datevente
            saveligne=ligne_vente.objects.create(vente_id=vente_id, produit_id=produit_id, qte=qte, prixu=prixu,  datevente=datevente, net_vente=net_vente)
            saveligne.save()

        #Modification de la vente
            lavente.net_payer=lavente.net_payer
            lavente.save()
            if request.user.is_authenticated:
                user=request.user
                return redirect (espaceuser, user.id )
        return render (request, 'lignevente.html', context)
    else:
        user=request.user
        return redirect (espaceuser, user.id )



#ETAT VENTE
def etatvente(request,idvente):
    lavente=vente.objects.get(id=idvente)
    leslignes=ligne_vente.objects.filter(vente_id=idvente)
    lepointdevente=Client.objects.filter(id=lavente.Client_id)
    levendeur=Vendeur.objects.get(id=lavente.User_id)
    netenletre=num2words(lavente.net_payer,lang='fr')
    #context=get_invoice(pk)
    context={'leslignes':leslignes,'lepointdevente':lepointdevente,'lavente':lavente,'netenletre':netenletre, 'levendeur':levendeur}
    template_path = 'etatvente.html'
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="BILAN_VENTE.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    # create a pdf
    pisa_status = pisa.CreatePDF(html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response



#STATISTIQUES VENTES
def stativente(request):
    return render(request, 'stativente.html')


#VENTES PAR COMMERCIAL
def venteparcom(request):
    lescom=User.objects.all()
    context={'lescom':lescom}
    return render(request, "venteparcom.html", context)


#VENTES PAR POINT DE VENTE
def venteparpv(request):
    lespv=Client.objects.all()
    context={'lespv':lespv}
    return render(request, "venteparpointvente.html", context)


#VENTES PAR MARQUES
def venteparmarque(request):
    lesmarques=marque_prod.objects.all()
    context={'lesmarques':lesmarques}
    return render(request, "venteparmarque.html", context)


#VENTES PAR MARQUES
def venteparcat(request):
    lescats=cat_prod.objects.all()
    context={'lescats':lescats}
    return render(request, "venteparcat.html", context)




#ETABLISSEMENT DE GRAPHES
def grapheparcom(request):
    #Recuperation du nombre de vente par categorie
    venteparcom= (vente.objects.values('User_id', 'User__first_name').annotate(nombre=Count('User_id')).order_by())
    venteparpdv= (vente.objects.values('Client_id', 'Client__nom').annotate(mont=Sum('net_payer')).order_by())
    print(venteparpdv)
    context={'venteparcom':venteparcom, 'venteparpdv':venteparpdv}
    return render (request,'grapheparcom.html',context)



#Nbre de Points de vente visités par vendeur
def Nbrepvviste(request):
    nbrevisite=(vente.objects.values('User_id','Client__nom', 'User__first_name','datevente', 'Client__Region__libelle').annotate(nombre=Count('User_id'), somme=Sum('net_payer')).order_by())
    context={'nbrevisite':nbrevisite}
    return render(request, 'nbrevisite.html',context)