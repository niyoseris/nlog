function uploadImage() {
    var file = document.getElementById("imageUploadButton").files[0];
    var formdata = new FormData();
    formdata.append("leFile", file);
    var ajax = new XMLHttpRequest();
    ajax.addEventListener("load", completeHandler, false);
    ajax.addEventListener("error", errorHandler, false);
    ajax.open("POST", "/upload");
    ajax.send(formdata);
  }


  function taslakat(){
    var yaziBaslik = document.getElementById("yaziBaslik").value;
    var kapakGorseli = document.getElementById("kapakGorseli").value;
    var yaziText = document.getElementById("yaziText").value;
    var kategorilerText = document.getElementById("kategorilerText").value;

    var gonderilecekData = new FormData();
    gonderilecekData.append("yaziBaslik", yaziBaslik);
    gonderilecekData.append("kapakGorseli", kapakGorseli);
    gonderilecekData.append("yaziText", yaziText);
    gonderilecekData.append("kategoriler", kategorilerText);

    var ajax = new XMLHttpRequest();
    ajax.addEventListener("load", taslakDurum, false);
    ajax.addEventListener("error", taslakDurum, false);
    ajax.open("POST", "/taslakat");
    ajax.send(gonderilecekData);
  }
  



 function completeHandler(event) {
    alert("Upload completed");
    document.getElementById("uploadedFile").innerHTML = event.target.responseText;
    
}

  function errorHandler(event) {
    alert("Failure.");
}

function taslakDurum(event) {
    document.getElementById("uploadedFile").innerHTML = event.target.responseText;
}

function editDurum(event) {
    alert(event.target.responseText);
}


function regregor(ne){
    var regro = document.getElementById(ne);
    regro.value = regro.value.replaceAll("&lt;", "<").replaceAll("&gt;", ">");
}

function gregor(ne){
    var zubuzu = document.getElementById(ne).value;

    var f = new FormData();
    f.append("icerik", zubuzu);
    f.append("neyinIcerigi", ne);
    var ajax = new XMLHttpRequest();
    ajax.addEventListener("load", editDurum, false);
    ajax.open("POST", "/cicile");
    ajax.send(f);
}



function silemMi(gurban){
    var r = confirm("Hiçbir güç onu geri getiremeyecek");
    if (r === true) {
        window.location.href = "/remove/" + gurban;
    }
}



  function menuAcKapa(){
      if (document.getElementById("menuContainer").style.display != "block"){
          document.getElementById("menuContainer").style.display = "block";
      
        } else {
      
            document.getElementById("menuContainer").style.display = "none";
      
        }
}

  function panelAcKapa(neyi){
      if (document.getElementById(neyi).style.display != "block"){
          document.getElementById(neyi).style.display = "block";
      
        } else {
      
            document.getElementById(neyi).style.display = "none";
      
        }
}



function kapakFotosuYap(){
    var ne = document.getElementById("uploadedFile").innerHTML;

    document.getElementById("kapakGorseli").value = ne.split("<")[0]
}


function makeBold(){
    var yaziText = document.getElementById("yaziText");
    var start = yaziText.selectionStart;
    var finish = yaziText.selectionEnd;
    var sel = yaziText.value.substring(start, finish);
    var selLenght = finish - start;

    if (sel != ""){
        var eskisi = yaziText.value;
        var oncesi = eskisi.substring(0,finish);
        yaziText.value = eskisi.replace(oncesi, oncesi.substring(0,start) + "<strong>" + sel + "</strong>")
    }

}

function makeItalic(){
    var yaziText = document.getElementById("yaziText");
    var start = yaziText.selectionStart;
    var finish = yaziText.selectionEnd;
    var sel = yaziText.value.substring(start, finish);
    if (sel != ""){
        var eskisi = yaziText.value;
        var oncesi = eskisi.substring(0,finish);
        yaziText.value = eskisi.replace(oncesi, oncesi.substring(0,start) + "<i>" + sel + "</i>")
    }
}

function makeUnderline(){
    var yaziText = document.getElementById("yaziText");
    var start = yaziText.selectionStart;
    var finish = yaziText.selectionEnd;
    var sel = yaziText.value.substring(start, finish);
    if (sel != ""){
        var eskisi = yaziText.value;
        var oncesi = eskisi.substring(0,finish);
        yaziText.value = eskisi.replace(oncesi, oncesi.substring(0,start) + "<u>" + sel + "</u>")
    }
}

function makeh1(){
    var yaziText = document.getElementById("yaziText");
    var start = yaziText.selectionStart;
    var finish = yaziText.selectionEnd;
    var sel = yaziText.value.substring(start, finish);
    if (sel != ""){
        var eskisi = yaziText.value;
        var oncesi = eskisi.substring(0,finish);
        yaziText.value = eskisi.replace(oncesi, oncesi.substring(0,start) + "<h1>" + sel + "</h1>")
    }
}

function makeh2(){
    var yaziText = document.getElementById("yaziText");
    var start = yaziText.selectionStart;
    var finish = yaziText.selectionEnd;
    var sel = yaziText.value.substring(start, finish);
    if (sel != ""){
        var eskisi = yaziText.value;
        var oncesi = eskisi.substring(0,finish);
        yaziText.value = eskisi.replace(oncesi, oncesi.substring(0,start) + "<h2>" + sel + "</h2>")
    }
}

function makeh3(){
    var yaziText = document.getElementById("yaziText");
    var start = yaziText.selectionStart;
    var finish = yaziText.selectionEnd;
    var sel = yaziText.value.substring(start, finish);
    if (sel != ""){
        var eskisi = yaziText.value;
        var oncesi = eskisi.substring(0,finish);
        yaziText.value = eskisi.replace(oncesi, oncesi.substring(0,start) + "<h3>" + sel + "</h3>")
    }
}

function makeCenter(){
    var yaziText = document.getElementById("yaziText");
    var start = yaziText.selectionStart;
    var finish = yaziText.selectionEnd;
    var sel = yaziText.value.substring(start, finish);
    if (sel != ""){
        var eskisi = yaziText.value;
        var oncesi = eskisi.substring(0,finish);
        yaziText.value = eskisi.replace(oncesi, oncesi.substring(0,start) + "<center>" + sel + "</center>")
    }
}

function addImage(){
    var yaziText = document.getElementById("yaziText");
    var start = yaziText.selectionStart;
    var finish = yaziText.selectionEnd;
    var sel = yaziText.value.substring(start, finish);
    if (sel != ""){
        var eskisi = yaziText.value;
        var oncesi = eskisi.substring(0,finish);
        yaziText.value = eskisi.replace(oncesi, oncesi.substring(0,start) + "<img style=\"height:20%;\" src=\"" + sel + "\">")
    }
}


function addLink(){
    var yaziText = document.getElementById("yaziText");
    var start = yaziText.selectionStart;
    var finish = yaziText.selectionEnd;
    var sel = yaziText.value.substring(start, finish);
    var link = prompt("Gidilecek link?","")
    if (sel != ""){
        var eskisi = yaziText.value;
        var oncesi = eskisi.substring(0,finish);
        yaziText.value = eskisi.replace(oncesi, oncesi.substring(0,start) + "<a href=\"" + link + "\">" + sel + "</a>")
    }
}




