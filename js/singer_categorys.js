// 根据歌手类型获取歌手
// http://music.163.com/#/discover/artist/cat?id=1001
var webPage = require('webpage');
var pageTb = webPage.create();
var system = require('system')

var tbUrl = system.args[1]
pageTb.open(tbUrl, function(status) {
        var result = pageTb.evaluate(function() {
           var d = document.getElementById("g_iframe").contentWindow.document;
           var categorys = d.getElementById('initial-selector').getElementsByTagName('a');
           var array = new Array();
           for(var i=0;i<categorys.length;i++){
               array.push(categorys[i].getAttribute("href"));
           }
           return array
        });
        for(var i=0;i<result.length;i++){
            console.log(result[i]);
        }
        phantom.exit();
});
