from flask import Flask, request, redirect, flash, make_response
import nlogHTML as n
import datetime
import hashlib as hash
import os
import ast

keywordum = """I'm a blonde barbie girl in a fantasy world"""
databaseName = "whateveryouwant"
extension = hash.sha256(keywordum.encode('utf-8')).hexdigest()[8:12]
magicWords = "cav de genne"


def hangiMenu():
    if kimdirBeBu():
        m = n.basganMenuHTML
    else:
        m = n.menuHTML

    return n.header.replace("vvvtitvvv", "") + m



def kimdirBeBu():
    birey = ''
    sifre = ''

    if request.cookies:
        birey = request.cookies.get("kim")
        sifre = request.cookies.get("sifre")

    if os.path.isfile(databaseName + "." + extension):
        kontrol = open(databaseName + "." + extension, 'r')
        oku = kontrol.readlines()
        kontrol.close()

        for teyitLine in oku:
            if d(teyitLine)["kim"] == birey:
                if d(teyitLine)["sifre"] == sifre:
                    print (d(teyitLine)["sifre"])
                    return True    
        return False
    else:
        return False

def kriptolize(kim, sifre):
    birlesim = kim + sifre + keywordum
    return str(hash.sha256(str(birlesim).encode('utf-8')).hexdigest())

def yaziBase():
    q = open("Posts/myLittleDatabase.nysrs", "r")
    qq = q.readlines()
    q.close()
    return qq


def d(gelen):
    return ast.literal_eval(gelen)

def mLDB():
    y = open("Posts/myLittleDatabase.nysrs", "r")
    yy = y.readlines()
    y.close()

    return yy   

def sf(kelime):
    kelime = kelime.replace("İ", "i")
    kelime = str(kelime).lower()
    kelime= kelime.replace("/", "").replace("\"", "").replace("!", "").replace("\\","").replace(" ", "_").replace("?", "")
    kelime = kelime.replace("ç","c").replace("ğ","g").replace("ı","i").replace("ö","o").replace("ş","s").replace("ü","u")
    return kelime


def icerigi(neyin):
    r = open(neyin, 'r')
    rr = r.read()
    r.close()
    return rr

def yoksaYap(klasor):
    if os.path.isdir(klasor):
        pass
    else:
        os.mkdir(klasor)

def yoksaYapDosya(klasor, dosya):
    if os.path.isfile(klasor + "/" + dosya):
        pass
    else:
        os.system("touch " + klasor + "/" + dosya)

def yaziyiKaydet(kategoriler, baslik, imaj, icerik, durum):
    yy = ""
    edit = False

    esasBaslik = baslik
    baslik = sf(baslik)
    postum = {}
    postum["baslik"] = esasBaslik
    postum["zaman"] = str(datetime.datetime.now())
    postum["icerik"] = icerik
    postum["kategoriler"] = kategoriler
    postum["imaj"] = imaj
    postum["link"] = sf(baslik)
    postum["durum"] = durum
    

    zumba = open("Posts/myLittleDatabase.nysrs", "r").readlines()

    if durum == "YAZI":
        for oncekiler in zumba:
            if d(oncekiler)["link"] == postum["link"]:
                if "durum" in d(oncekiler):
                    if d(oncekiler)["durum"] == "TASLAK":
                        zumba.remove(oncekiler)

    for zz, i in enumerate(zumba):
        if d(i)["link"] == sf(baslik):
            edit = True
            zumba[zz] = postum
    
    open("Posts/myLittleDatabase.nysrs", "w").close()

    if edit == False:
        zumba.insert(0, str(postum))

    for est in reversed(zumba):
        est = str(est).replace("\r\n", "").replace("\n", "") + "\n"
        yy = str(est) + yy




        ekle = open("Posts/myLittleDatabase.nysrs", "w")
        ekle.write(yy)
        ekle.close()



    
def remove(link):
    yy = ""
    zumba = open("Posts/myLittleDatabase.nysrs", "r").readlines()

    for zz, i in enumerate(zumba):
        if d(i)["link"] == sf(link):
            zumba[zz] = ""
    
    open("Posts/myLittleDatabase.nysrs", "w").close()

    for est in reversed(zumba):
        est = str(est).replace("\r\n", "").replace("\n", "") + "\n"
        if len(est) > 5:
            yy = str(est) + yy
            ekle = open("Posts/myLittleDatabase.nysrs", "w")
            ekle.write(yy)
            ekle.close()
    
    


app = Flask(__name__)


@app.route("/yaz")
def man():
    if kimdirBeBu():
        return n.header.replace("vvvtitvvv", "") + n.basganMenuHTML + n.yazHTML
    else:
        return "Seni tanımıyorum adamım..."

@app.route("/yazEkle", methods=['POST'])
def yazEkle():
    if request.method == 'POST':
        yazi = request.form.get("yaziText").replace("\r\n", "<br>").replace("\n", "<br>")
        baslik = request.form.get("yaziBaslik")
        ima = request.form.get("kapakGorseli")
        kategoriler = request.form.get("kategoriler").split(",")
        durum = "YAZI"
        
        yoksaYap("Posts")
        yoksaYapDosya("Posts", "myLittleDatabase.nysrs")

        

        yaziyiKaydet(kategoriler, baslik, ima, yazi, durum)

    
    

    return redirect("Posts/" + sf(baslik)) 


@app.route("/Posts/<post>")
def yaziOku(post):
    y = open("Posts/myLittleDatabase.nysrs", "r")
    yy = y.readlines()
    y.close()   

    for s in yy:
        if ast.literal_eval(s)["link"] == post:
            aa = n.header.replace("vvvimajvvv", d(s)["imaj"]).replace("vvvtitvvv", d(s)["baslik"])
            if kimdirBeBu():
                bb = n.xbasganMenuHTML.replace("vvvlinkvvv", d(s)["link"])
            else:
                bb = n.menuHTML
            cc = n.postTitle.replace("vvvtitlevvv", d(s)["baslik"])
            dd = n.ustGorsel.replace("vvvimajvvv", d(s)["imaj"])
            ee = n.yaziContainer.replace("vvvyazivvv", d(s)["icerik"])
            return  aa + bb + cc + dd + ee

    return "En güzel yazı henüz yazılmamış olandır..."



@app.route("/edit/<yazi>")
def edit(yazi):
    if kimdirBeBu():
        for f in yaziBase():
            if d(f)["link"] == yazi:
                kate = ""
                editle = ""
                baslik = d(f)["baslik"]
                imaj = d(f)["imaj"]
                kategoriler = d(f)["kategoriler"]
                icerik = d(f)["icerik"].replace("<br>", "\n")

                for kt in kategoriler:
                    if len(kate) > 1:
                        kate = kate + "," + kt
                    else:
                        kate = kt
                                        
                editle = n.editHTML.replace("vvvkategorilervvv", kate)
                editle = editle.replace("vvvkapakgorselivvv", imaj)
                editle = editle.replace("vvvbaslikvvv", baslik)
                editle = editle.replace("vvvyazivvv", icerik)

                return n.header.replace("vvvtitvvv", baslik) + n.basganMenuHTML  + editle


@app.route("/remove/<link>")
def removeIt(link):
    if request.headers.get("Referer").startswith("https://" + request.headers.get("Host")):
        if kimdirBeBu():
            remove(link)
        return redirect("/")
    
    else:
        return "gözleri aşka gülen taze söğüt dalısın"


@app.route("/")
def yazilarList():
    y = open("Posts/myLittleDatabase.nysrs", "r")
    yy = y.readlines()
    y.close()

    m = n.kapakFoto.replace("vvvimajvvv", "static/nlogbanner.svg")

    if kimdirBeBu():
        m = n.basganMenuHTML
    else:
        m = n.menuHTML

    yL = n.header.replace("vvvtitvvv", "") + m



    for i in yy:
        if "durum" in d(i):
            if d(i)["durum"] == "YAZI":
                zub = n.yaziListContainer.replace("imaj", d(i)["imaj"])
                zub = zub.replace("vvvbaslikvvv", d(i)["baslik"])
                zub= zub.replace("vvvicerikvvv", str(d(i)["icerik"][0:100]).replace("<", " ") + "...<strong>[devamını oku]</strong>")
                zub = zub.replace("vvvlinkvvv", d(i)["link"])
                yL = yL + zub
        else:
            zub = n.yaziListContainer.replace("imaj", d(i)["imaj"])
            zub = zub.replace("vvvbaslikvvv", d(i)["baslik"])
            zub= zub.replace("vvvicerikvvv", str(d(i)["icerik"][0:100]).replace("<", " ") + "...<strong>[devamını oku]</strong>")
            zub = zub.replace("vvvlinkvvv", d(i)["link"])
            yL = yL + zub
    return yL



@app.route("/upload", methods=['POST'])
def upload():
    if request.method == 'POST':
        if kimdirBeBu():
            yoksaYap("static")
            yoksaYap("static/media")
            ff = request.files["leFile"]
            ff.save("static/media/" + sf(str(ff.filename)))
            return "/static/media/" + sf(str(ff.filename)) + n.kapakFotoYapButon
        else:
            return("yetkisiz deneme")



@app.route("/boss")
def boss():

    return n.header.replace("vvvtitvvv", "") + n.basganPanel


@app.route("/club", methods= ['POST'])
def club():
    if request.method == 'POST':
        giren = request.form.get("bossText")
        girilen = request.form.get("passText")
        dBase = databaseName + "." + extension
        yoksaYapDosya(".", dBase)
        
        dbAc = open(dBase, 'r')
        dbOkunan = dbAc.readlines()
        dbAc.close()

        if len(dbOkunan) > 0:
            for dbLine in dbOkunan:
                if d(dbLine)["kim"] == giren:
                    if d(dbLine)["sifre"] == kriptolize(giren,girilen):

                        resp = make_response(redirect("/Panel"))
                        resp.set_cookie("kim", giren)
                        resp.set_cookie("sifre", kriptolize(giren, girilen))
                        return resp



            return "Kimsin sen?"
        else:
            if magicWords in giren:
                giren = giren.replace(magicWords, "")
                ferit = {}
                ferit["kim"] = giren
                ferit["sifre"] = kriptolize(giren,girilen)
                feritiYaz = open(dBase, "a")
                feritiYaz.write(str(ferit) + "\n")
                feritiYaz.close()
                return "Goyduk çocuğu"
            return "Olmadı senin iş..."


@app.route("/signout")
def signout():
    resp = make_response(redirect("/"))
    resp.set_cookie("kim","", expires=0)
    resp.set_cookie("sifre","", expires=0)
    return resp    


@app.route("/Panel")
def panel():
    if kimdirBeBu():
        panelHTMLsi = n.panelHTML
        panelHTMLsi = panelHTMLsi.replace("vvvstyletextvvv", icerigi("static/nlog.css"))
        panelHTMLsi = panelHTMLsi.replace("vvvscripttextvvv", icerigi("static/nlog.js"))
        panelHTMLsi = panelHTMLsi.replace("vvvheadertextvvv", icerigi("static/header.html"))
        panelHTMLsi = panelHTMLsi.replace("vvvmobilestyletextvvv", icerigi("static/nlogmobile.css"))
        
        return n.header.replace("vvvtitvvv", "") + n.basganMenuHTML + panelHTMLsi
    else:
        return "<center>.</center>"



@app.route("/cicile", methods = ['POST'])
def cicile():
    if request.method == 'POST':
        if kimdirBeBu():
            yeri = ''
            datasi = request.form.get("icerik")
            neyi = request.form.get("neyinIcerigi")

            if neyi == "headerText":
                yeri = "static/header.html"
            if neyi == "styleText":
                yeri = "static/nlog.css"
            if neyi == "mobileStyleText":
                yeri = "static/nlogmobile.css"
            if neyi == "scriptText":
                yeri = "static/nlog.js"

            
            
            
            
            zq = open(yeri, "w")
            zq.write(datasi)
            zq.close()
            return "kayıtladık"
        else:
            return "whoareyou"
        
    return "okkk"


@app.route("/duzenle/<path:yol>")
def duzenleBakem(yol):
    return n.duzenleHTML.replace("vvvduzentextvvv", icerigi(yol))
    

@app.route("/Kategoriler")
def kategorileriListele():
    alinanKategoriler = []
    donecek = n.kapakFoto.replace("vvvimajvvv", "static/nlogbanner.svg")

    for satir in mLDB():
        for katkat in d(satir)["kategoriler"]:
            if "durum" in d(satir):
                if d(satir)["durum"]=="YAZI":
                    if not katkat.strip() in alinanKategoriler:
                        alinanKategoriler.append(katkat.strip())
            else:
                
                if not katkat.strip() in alinanKategoriler:
                    alinanKategoriler.append(katkat.strip())


    alinanKategoriler = sorted(alinanKategoriler)

    for z in alinanKategoriler:
        donecek = donecek + n.buton.replace("vvvlinkvvv", "/Kategoriler/" + sf(str(z).strip())).replace("vvvkatkatvvv", z)
        
    
    return hangiMenu() +  """<br><div class="titleStyle">Kategoriler:</div><br>""" + donecek


@app.route("/Kategoriler/<kat>")
def kategoridekileriListele(kat):
    alinanKategoriler = []
    donecek = n.kapakFoto.replace("vvvimajvvv", "static/nlogbanner.svg")


    for satir in mLDB():
        for katkat in d(satir)["kategoriler"]:
            if kat.strip() == sf(katkat.strip()):
                alinanKategoriler.append(satir)

    for i in sorted(alinanKategoriler):
        zub = n.yaziListContainer.replace("imaj", d(i)["imaj"])
        zub = zub.replace("vvvbaslikvvv", d(i)["baslik"])
        zub= zub.replace("vvvicerikvvv", str(d(i)["icerik"][0:int(len(d(i)["icerik"]) * 0.05)]).replace("<", " ") + "...<strong>[devamını oku]</strong>")
        zub = zub.replace("vvvlinkvvv", d(i)["link"])
        donecek = donecek + zub
    return hangiMenu() + donecek
    
@app.route("/About")
def aboutum():
    return hangiMenu() + """<div class="titleStyle">Bir ara burayı da yapacam :)))))</div>"""
    
@app.route("/Contact")
def contactim():
    return hangiMenu() + """<div class="titleStyle">Bir ara burayı da yapacam :)))))</div>"""
    


@app.route("/taslakat", methods=['POST'])
def taslakat():
    if kimdirBeBu():
        if request.method == 'POST':
            
            yazi = request.form.get("yaziText").replace("\r\n", "<br>").replace("\n", "<br>")
            baslik = request.form.get("yaziBaslik")
            ima = request.form.get("kapakGorseli")
            kategoriler = request.form.get("kategoriler")
            durum = "TASLAK"
            
            
 
            yoksaYap("Posts")
            yoksaYapDosya("Posts", "myLittleDatabase.nysrs")

            if kategoriler == baslik == ima == yazi == "":
                return "Çizmedin ki kesesin."
                        

            if kategoriler == "":
                kategoriler = "."
            if baslik == "":
                return "Bir başlık isderik"
            if ima == "":
                ima = ".jpg"
            if yazi == "":
                yazi = "Lorem Ipsum"
                
            kategoriler = kategoriler.split(",")

               
            yaziyiKaydet(kategoriler, baslik, ima, yazi, durum)
            return ("Yazı taslak olarak kaydedildi...")
            
            
@app.route("/Taslaks")
def taslaks():
    
    
    
    y = open("Posts/myLittleDatabase.nysrs", "r")
    yy = y.readlines()
    y.close()

    m = ''

    if kimdirBeBu():
        m = n.basganMenuHTML
    else:
        return "<center>.</center>"
        m = n.menuHTML

    yL = n.header.replace("vvvtitvvv", "") + m



    for i in yy:
        if "durum" in d(i):
            if d(i)["durum"] == "TASLAK":
                zub = n.yaziListContainer.replace("imaj", d(i)["imaj"])
                zub = zub.replace("vvvbaslikvvv", d(i)["baslik"])
                zub= zub.replace("vvvicerikvvv", str(d(i)["icerik"][0:int(len(d(i)["icerik"]) * 0.05)]).replace("<", " ") + "...<strong>[devamını oku]</strong>")
                zub = zub.replace("vvvlinkvvv", d(i)["link"])
                yL = yL + zub
    return yL
