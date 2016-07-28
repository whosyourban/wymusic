var webPage = require('webpage');
var pageTb = webPage.create();
var system = require('system')

var tbUrl = system.args[1]
pageTb.open(tbUrl, function(status) {
        var result = pageTb.evaluate(function() {
           var array = new Array();
           var d = document.getElementById("g_iframe").contentWindow.document;
           array.push(d.getElementsByClassName("tit")[0].innerText);
           array.push(d.getElementsByClassName("des")[1].innerText);
           array.push(d.getElementById('comment-box').getElementsByClassName("j-flag")[0].innerText);
           return array
        });
        var song = result[0].replace(/ /g,"");
        var author = result[1].replace('歌手：','');
        var comments = result[2];
        console.log('{"name":"'+song+'","author":"'+author+'","c":"'+comments+'"}'); 
        phantom.exit();
});
