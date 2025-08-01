from django.shortcuts import render,redirect
from .models import type_pv, pointv,marque_prod, cat_prod, produit, commercial,vente,ligne_vente, zonecouv
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



#ZONE DE COUVERTURES
def zonecouve(request):
    leszones=zonecouv.objects.all()
    context={'leszones':leszones}

    if request.method =="POST":
        nom=request.POST.get('nom')
        savezone=zonecouv.objects.create(nom=nom)
        savezone.save()
    return render(request, 'zonecouv.html',  context)


#Espace User
def espaceuser(request, iduser):
    if request.user.is_authenticated:
        lespv=pointv.objects.all()
        lesprod=produit.objects.all()
        mesventes=vente.objects.filter(User_id=iduser)
        context={'lespv':lespv, 'mesventes' : mesventes, "lesprod":lesprod }

        if request.method =="POST":
            User_id=iduser
            pointv_id=request.POST.get('idpv')
            montant=0
            remise=0
            net_payer=0
            statut="EN COURS"
            commentaire=request.POST.get('commentaire')
            datevente=request.POST.get('datev')
            etat=request.POST.get('etat')
            zonecouv=request.POST.get('zonecouv')
            savevente=vente.objects.create( User_id=iduser, zonecouv_id=zonecouv, pointv_id=pointv_id, montant=montant, etat=etat,  net_payer=net_payer, statut=statut , commentaire=commentaire, datevente=datevente )
            savevente.save()
    else:
        print("Veuillez vous connecter")
        return redirect(conex)
    return render(request, "espaceuser.html", context)




#TYPE POINT DE VENTE
def adtypepoint(request):
    return render(request, "adtypepoint.html")

#ESPACE TYPE POINT DE VENTE
def typepointvente(request):
    lestypepv=type_pv.objects.all()
    context={'lestypepv':lestypepv}
    if request.method == "POST":
        libelle=request.POST.get('libelle')
        savetypepoint=type_pv.objects.create(libelle=libelle)
        savetypepoint.save()
    return render(request, 'typepointvente.html', context)


#POINT DE VENTE
def pointdevente(request):
    typepoints=type_pv.objects.all()
    leszonescouv=zonecouv.objects.all()
    lespv=pointv.objects.all()
    context={'typepoints':typepoints, 'lespv':lespv, 'leszonescouv':leszonescouv}

    if request.method =="POST":
        type_pv_id=request.POST.get('idtype')
        zonecouv_id=request.POST.get('zonecouv')
        nom=request.POST.get("nom")
        proprietaire=request.POST.get("proprietaire")
        contact_pro=request.POST.get("contact_pro")
        gerant=request.POST.get("gerant")
        contact_gerant=request.POST.get("contact_gerant")
        ville=request.POST.get("ville")
        commune=request.POST.get("commune")
        quartier=request.POST.get("quartier")
        gps=request.POST.get("gps")
        commentaire=request.POST.get("commentaire")
        datecreation=request.POST.get("datecreation")
        savepv=pointv.objects.create(type_pv_id=type_pv_id, zonecouv_id=zonecouv_id, nom=nom, proprietaire=proprietaire, contact_pro=contact_pro, gerant=gerant, contact_gerant=contact_gerant, ville=ville, commune=commune,  quartier=quartier, gps=gps,  commentaire=commentaire )
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
        saveprod=produit.objects.create(marque_id=marque, cat_id=cat, nom=nom, prixu=prixu, qte=qte, seuil=seuil, couleur=couleur, description=description)
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
        datalist.append({'id':i.id, 'prixu':i.prixu, 'qte':i.qte, 'seuil':i.seuil, "marque_id":i.marque.libelle, "cat_id":i.cat.libelle, "couleur":i.couleur})
    return JsonResponse(datalist, safe=False)


#API DE RECUPERATION DES POINT DE VENTE 
    #API
def apidetailpoitv(request):
    data=pointv.objects.all()
    datalist=[]
    for i in data:
        datalist.append({'id':i.id, "nom":i.nom, "proprietaire":i.proprietaire, "contact_pro":i.contact_pro, "gerant":i.gerant, "contact_gerant":i.contact_gerant, "ville":i.ville, "commune":i.commune, "quartier":i.quartier, "gps":i.gps})
    return JsonResponse(datalist, safe=False)

#API DE RECUPERATION DES VENTE 
    #API
def apivente(request):
    data=vente.objects.all()
    datalist=[]
    for i in data:
        datalist.append({'id':i.id, "user_id":i.User_id,"user_name":i.User.first_name, "datevente":i.datevente , "idpointv":i.pointv_id, "pointv_id":i.pointv.nom, "montant":i.montant, "remise":i.remise, "net_payer":i.net_payer, "commentaire":i.commentaire})
    return JsonResponse(datalist, safe=False)


#API VENTE PAR VENDEUR PAR ZONE
def apiventeparvendeur(request):
    #◙data=(vente.objects.values('User_id','pointv__nom', 'User__first_name','datevente', 'zonecouv__nom').annotate(nombre=Count('User_id'), somme=Sum('net_payer'), achateff=Count('id', filter=Q('etat='VENTE'))).order_by()))
    data = (vente.objects.values('User_id', 'pointv__nom', 'User__first_name', 'datevente', 'zonecouv__nom').annotate(nombre=Count('User_id'),somme=Sum('net_payer'), achateff=Count('id', filter=Q(etat='VENTE'))).order_by())
    print(data)
    datalist=[]
    for i in data:
        datalist.append({ "datevente":i['datevente'],"pointv__nom":i['pointv__nom'] ,"User_id":i['User_id'], "User__first_name":i['User__first_name'], "zonecouv__nom":i['zonecouv__nom'], "nombre":i['nombre'], "achateff":i['achateff'], "somme":i['somme']  })
    return JsonResponse(datalist, safe=False)

#API DE RECUPERATION DES LIGNES VENTE 
    #API
def apilignev(request):
    data=ligne_vente.objects.all()
    datalist=[]
    for i in data:
        datalist.append({'id':i.id, "vente_id":i.vente_id_id, "cat_id":i.produit.cat_id, "marque_id":i.produit_id, "lacat":i.produit.cat.libelle, "lamarc":i.produit.marque.libelle, "pointvente":i.vente_id.pointv.nom,"qte":i.qte, "prixu":i.prixu , "prix_total":i.prix_total, "remise":i.remise, "datevente":i.datevente, "produit_id":i.produit.nom, "net_payer":i.net_payer, "comm":i.vente_id.User.first_name})
    return JsonResponse(datalist, safe=False)



#USER AND COMMERCIAL COMMERCIAL
def commerciaux(request):
    lescommercio =commercial.objects.all()
    leszones=zonecouv.objects.all()
    context={'lescommercio': lescommercio, 'leszones':leszones}
    if request.method == "POST":
        
        #ENREGISTREMENT DANS USER
        username=request.POST.get('login')
        password=request.POST.get("mdp")
        email=request.POST.get('adressemail')

        #ENREGISTREMENT DU COMMERCIAL
        nom=request.POST.get('nom')
        contact=request.POST.get('contact')
        photo=request.POST.get('photo')
        datenaiss=request.POST.get('datenaiss')
        zonecouv_id=request.POST.get('zonecouv')
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
        savecom=commercial.objects.create(nom=nom, login=username,  contact=contact, profil=profil, cni=cni, user_id=user_id,   adressemail=email, photo=photo, datenaiss=datenaiss, zonecouv_id=zonecouv_id, lieunaiss=lieunaiss, lieuresidence=lieuresidence     )
        savecom.save()
    return render(request, "commercial.html", context)



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
            remise=request.POST.get('remise')
            prix_total=request.POST.get('montant')
            net_payer=request.POST.get('netpayer')
            datevente=lavente.datevente
            saveligne=ligne_vente.objects.create(vente_id_id=vente_id, produit_id=produit_id, qte=qte, prixu=prixu, prix_total=prix_total, datevente=datevente, remise=remise, net_payer=net_payer)
            saveligne.save()

        #Modification de la vente
            lavente.montant=request.POST.get('p_soustotal')
            lavente.remise=request.POST.get('p_remise')
            lavente.net_payer=request.POST.get('p_netapayer')
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
    lepointdevente=pointv.objects.filter(id=lavente.pointv_id)
    netenletre=num2words(lavente.net_payer,lang='fr')
    #context=get_invoice(pk)
    context={'leslignes':leslignes,'lepointdevente':lepointdevente,'lavente':lavente,'netenletre':netenletre}
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
    lespv=pointv.objects.all()
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
    venteparpdv= (vente.objects.values('pointv_id', 'pointv__nom').annotate(mont=Sum('net_payer')).order_by())
    print(venteparpdv)
    context={'venteparcom':venteparcom, 'venteparpdv':venteparpdv}
    return render (request,'grapheparcom.html',context)



#Nbre de Points de vente visités par vendeur
def Nbrepvviste(request):
    nbrevisite=(vente.objects.values('User_id','pointv__nom', 'User__first_name','datevente', 'zonecouv__nom').annotate(nombre=Count('User_id'), somme=Sum('net_payer')).order_by())
    context={'nbrevisite':nbrevisite}
    return render(request, 'nbrevisite.html',context)





