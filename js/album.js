var webPage = require('webpage');
var pageTb = webPage.create();
var system = require('system')

var tbUrl = system.args[1]
pageTb.open(tbUrl, function(status) {
        var result = pageTb.evaluate(function() {
           var array = new Array();
           try{
               var d = document.getElementById("g_iframe").contentWindow.document;
               var album = d.getElementById('m-song-module').getElementsByTagName('li');
               for(var i=0;i<album.length;i++){
                  var href = album[i].getElementsByTagName('a')[0].getAttribute("href");
                  var name = album[i].getElementsByTagName('p')[0].getAttribute("title");
                  var date = album[i].getElementsByTagName('p')[1].innerText;
                  var obj = new Object();
                  obj.name = name.replace("'",' ').replace('"','')
                  obj.id = href.replace('/album?id=','');
                  obj.date = date;
                  var jsonString= JSON.stringify(obj);
                  array.push(jsonString);
               }
           }catch(e){

           }
           return array
        });
        for(var i=0;i<result.length;i++){
            console.log(result[i]);
        }
        phantom.exit();
});
