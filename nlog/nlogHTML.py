def icerigi(neyin):
    r = open(neyin, 'r')
    rr = r.read()
    r.close()
    return rr



header = icerigi("static/header.html")


buton = """<a href="vvvlinkvvv"><input type="button" class="menuButon" value="vvvkatkatvvv"></a>"""


yazHTML = """
<form action="yazEkle" method="POST">

<div class="contain">
Başlık:<br>
<input type="text" class="xText" id="yaziBaslik" name="yaziBaslik" required>
<br>Görsel:<br>
<input type="text" class="xText" id="kapakGorseli" name="kapakGorseli" required>

</div>

<div class="textButonContainer">
<input type="button" onclick="makeBold()" class="textButon" value="Bold">
<input type="button" onclick="makeItalic()" class="textButon" value="Italic">
<input type="button" onclick="makeUnderline()" class="textButon" value="Underline">

<input type="button" onclick="makeh1()" class="textButon" value="h1">
<input type="button" onclick="makeh2()" class="textButon" value="h2">
<input type="button" onclick="makeh3()" class="textButon" value="h3">

<input type="button" onclick="makeCenter()" class="textButon" value="Center">
<input type="button" onclick="addImage()" class="textButon" value="Image">
<input type="button" onclick="addLink()" class="textButon" value="Link">

<input type="file" class="textButon" value="Browse" id="imageUploadButton" name="imageUploadButton">
<input type="button" onclick="uploadImage()" class="textButon" value="Upload">
<br>
<div id="uploadedFile" class="textButon"></div>

</td>
</tr>

</table>
</div>
<br>
<textarea name="yaziText" id="yaziText" class="yazi" required></textarea>

<div class="contain">
Katerogiler (Virgülle ayırınız)<br>
<input type="text" class="xText" id="kategorilerText" name="kategoriler" required>
</div>


<input type="submit" class="buton" value="Gönder">
<input type="button" class="buton" onclick="taslakat()" value="Taslak Olarak Kaydet">


</form>

"""



editHTML = """
<form action="/yazEkle" method="POST">

<div class="contain">
Başlık:<br>
<input type="text" class="xText" id="yaziBaslik" name="yaziBaslik" value="vvvbaslikvvv" required>
<br>Görsel:<br>
<input type="text" class="xText" id="kapakGorseli" name="kapakGorseli" value="vvvkapakgorselivvv" required>

</div>

<div class="textButonContainer">
<input type="button" onclick="makeBold()" class="textButon" value="Bold">
<input type="button" onclick="makeItalic()" class="textButon" value="Italic">
<input type="button" onclick="makeUnderline()" class="textButon" value="Underline">

<input type="button" onclick="makeh1()" class="textButon" value="h1">
<input type="button" onclick="makeh2()" class="textButon" value="h2">
<input type="button" onclick="makeh3()" class="textButon" value="h3">

<input type="button" onclick="makeCenter()" class="textButon" value="Center">
<input type="button" onclick="addImage()" class="textButon" value="Image">
<input type="button" onclick="addLink()" class="textButon" value="Link">

<input type="file" class="textButon" value="Browse" id="imageUploadButton" name="imageUploadButton">
<input type="button" onclick="uploadImage()" class="textButon" value="Upload">
<br>
<div id="uploadedFile" class="textButon"></div>

</td>
</tr>

</table>
</div>
<br>
<textarea name="yaziText" id="yaziText" class="yazi" required>vvvyazivvv</textarea>

<div class="contain">
Katerogiler (Virgülle ayırınız)<br>
<input type="text" class="xText" id="kategorilerText" name="kategoriler" value="vvvkategorilervvv" required>
</div>

<input type="submit" class="buton" value="Gönder">
<input type="button" class="buton" onclick="taslakat()" value="Taslak Olarak Kaydet">



</form>

"""






kapakFoto = """
<meta property="og:image" content="vvvimajvvv"/>
"""

kapakFotoYapButon = """
<input type="button" onclick="kapakFotosuYap()" class="textButon" value="Kapak Fotoğrafı Yap">"""



ustGorsel = """<center><img class="ustFoto" src="vvvimajvvv"></center>"""

postTitle = """
<title>vvvtitlevvv</title>
<center>
<div class="titleStyle">vvvtitlevvv</div>
</center>
<br>
"""


yaziListContainer = """
<div>
<a href="/Posts/vvvlinkvvv">
<table class="yazilarTable">
<th colspan=2><div class="yazilarTableBaslik">vvvbaslikvvv</div></th>
<br>
<tr class="yazilarTableRow">
  <td class="yazilarTableCol"><img class="yazilarTableImaj" src="imaj"></td>
  <td class="yazilarTableCol"><div class="yazilarTableIcerik">vvvicerikvvv</div></td>
 </tr>
</table>
</a>
</div>
"""

yaziContainer = """
<div class="disYaziContainer">
<br>
<div class="yaziContainer">vvvyazivvv</div>
<br>
</div>
"""

basganPanel = """
    <center>
    <form method="POST" action="/club">
    <table>
    <tr><td>Who:</td><td><input type="text" name="bossText" autocomplete="off" class="xText"></td></tr>
    <tr><td>Passaporte:</td><td><input type="password" name="passText" class="xText"></td></tr>
    <tr><td><input type="submit" class="textButon" value="Benim">
    </table>
    </form>
    </center>
    """

panelHTML = """
<br>

<input type="button" class="menuButon" onclick="panelAcKapa('panelHeader')" value="Header">
<input type="button" class="menuButon" onclick="panelAcKapa('panelStyle')" value="Style">
<input type="button" class="menuButon" onclick="panelAcKapa('panelMobileStyle')" value="Mobile Style">
<input type="button" class="menuButon" onclick="panelAcKapa('panelScript')" value="Script">



<div id="panelHeader" style="display:none;">
    <div class="titleStyle">Header Düzenle</div>
    <div>
    <br>
        <input type="hidden" name="cici" value="header">
        <textarea id="headerText" class="yazi" name="headerText">vvvheadertextvvv</textarea>
        <br>
        <input type="button" class="buton" onclick="gregor('headerText')" value="Header Düzenle">  
    </div>
</div>



<div id="panelStyle" style="display:none;">
    <div class="titleStyle">Style Düzenle</div>
    <div>
    <br>
    <input type="hidden" name="cici" value="style">
        <textarea id="styleText" class="yazi" name="styleText">vvvstyletextvvv</textarea>
        <br>
        <input type="button" class="buton" onclick="gregor('styleText')" value="Style Düzenle">  
</div>
</div>



<div id="panelMobileStyle" style="display:none;">
    <div class="titleStyle">Mobile Style Düzenle</div>
    <div>
    <br>
    <input type="hidden" name="cici" value="mobilestyle">
        <textarea id="mobileStyleText" class="yazi" name="mobileStyleText">vvvmobilestyletextvvv</textarea>
        <br>
        <input type="button" class="buton" onclick="gregor('mobileStyleText')" value="Mobile Style Düzenle">  
    </div>
</div>



<div id="panelScript" style="display:none;">
    <div class="titleStyle">Script Düzenle</div>
    <div>
    <br>
        <textarea id="scriptText" class="yazi" name="scriptText">vvvscripttextvvv</textarea>
        <br>
        <input type="button" class="buton" onclick="gregor('scriptText')" value="Script Düzenle">  
</div>
</div>






"""


menuHTML = """
<div class="menuClickContainer">
<input type="button" class="menuClick" onclick="menuAcKapa()" value="MENU">
</div>
<div class="menuContainer" id="menuContainer">
<a href="/"><input type="button" class="menuButon" value="Anasayfa"></a>
<a href="/Kategoriler"><input type="button" class="menuButon" value="Kategoriler"></a>
<a href="/About"><input type="button" class="menuButon" value="Hakkında"></a>
<a href="/Contact"><input type="button" class="menuButon" value="İletişim"></a>
<a href="/boss"><input type="button" class="menuButon" value="Giriş"></a>
</div>
"""

basganMenuHTML = """
<div class="menuClickContainer">
<input type="button" class="menuClick" onclick="menuAcKapa()" value="MENU">
</div>
<div class="menuContainer" id="menuContainer">
<a href="/"><input type="button" class="menuButon" value="Anasayfa"></a>
<a href="/Kategoriler"><input type="button" class="menuButon" value="Kategoriler"></a>
<a href="/yaz"><input type="button" class="menuButon" value="Yaz"></a>
<a href="/Panel"><input type="button" class="menuButon" value="Panel"></a>
<a href="/Taslaks"><input type="button" class="menuButon" value="Taslaklar"></a>
<a href="/About"><input type="button" class="menuButon" value="About"></a>
<a href="/Contact"><input type="button" class="menuButon" value="İletişim"></a>
<a href="/signout"><input type="button" class="menuButon" value="Çıkış"></a>
</div>
"""

xbasganMenuHTML = """
<div class="menuClickContainer">
<input type="button" class="menuClick" onclick="menuAcKapa()" value="MENU">
</div>
<div class="menuContainer" id="menuContainer">
<a href="/"><input type="button" class="menuButon" value="Anasayfa"></a>
<a href="/Kategoriler"><input type="button" class="menuButon" value="Kategoriler"></a>
<a href="/edit/vvvlinkvvv"><input type="button" class="menuButon" value="~Edit~"></a>
<a><input type="button" onclick="silemMi('vvvlinkvvv')" class="menuButon" value="~~Remove~~"></a>
<a href="/Panel"><input type="button" class="menuButon" value="Panel"></a>
<a href="/Taslaks"><input type="button" class="menuButon" value="Taslaklar"></a>
<a href="/About"><input type="button" class="menuButon" value="About"></a>
<a href="/Contact"><input type="button" class="menuButon" value="İletişim"></a>
<a href="/signout"><input type="button" class="menuButon" value="Çıkış"></a>
</div>
"""