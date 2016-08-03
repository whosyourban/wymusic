var webPage = require('webpage');
var pageTb = webPage.create();
var system = require('system')

var tbUrl = system.args[1]
pageTb.open(tbUrl, function(status) {
    setTimeout(function (){
        var result = pageTb.evaluate(function() {
           var array = new Array();
           var d = document.getElementById("g_iframe").contentWindow.document;
           array.push(d.getElementsByClassName("tit")[0].innerText);
           array.push(d.getElementsByClassName("des")[1].innerText);
           array.push(d.getElementById('comment-box').getElementsByClassName("j-flag")[0].innerText);
           return array
        });
        var song = result[0].replace(/ /g,"").replace('"','').replace("'",'').replace('\n','');
        var author = result[1].replace('歌手：','').replace('"','').replace("'",'');
        var comments = result[2];
        var obj = new Object();
        obj.name = song
        obj.author = author
        obj.c = comments;
        var jsonString= JSON.stringify(obj);
        console.log(jsonString);
        phantom.exit();
    }, 1000);
});
