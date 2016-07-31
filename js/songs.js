var webPage = require('webpage');
var pageTb = webPage.create();
var system = require('system')

var tbUrl = system.args[1]
pageTb.open(tbUrl, function(status) {
        var result = pageTb.evaluate(function() {
           var d = document.getElementById("g_iframe").contentWindow.document;
           var covers = d.getElementsByTagName('table')[0].getElementsByClassName('txt');
           var array = new Array();
           for(var i=0;i<covers.length;i++){
               array.push(covers[i].getElementsByTagName("a")[0].getAttribute("href"));
           }
           return array
        });
        console.log(result.length);
        for(var i=0;i<result.length;i++){
            console.log(result[i]);
        }
        phantom.exit();
});
