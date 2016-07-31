// 根据歌手类型获取歌手
// http://music.163.com/#/discover/artist/cat?id=1001
var webPage = require('webpage');
var pageTb = webPage.create();
var system = require('system')

var tbUrl = system.args[1]
pageTb.open(tbUrl, function(status) {
        var result = pageTb.evaluate(function() {
           var d = document.getElementById("g_iframe").contentWindow.document;
           var categorys = d.getElementById('m-artist-box').getElementsByTagName('a');
           var array = new Array();
           for(var i=0;i<categorys.length;i++){
               var href =categorys[i].getAttribute("href");
               var title =categorys[i].getAttribute("title");
               if(href.indexOf("/artist?id=")==0){
                   array.push(title+'|||'+href);
               }
           }
           return array
        });
        for(var i=0;i<result.length;i++){
            console.log(result[i]);
        }
        phantom.exit();
});
