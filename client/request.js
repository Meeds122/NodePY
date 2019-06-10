function request(call, cb){
    var myurl = "http://127.0.0.1:31337/" + call;
    var xmlhttp;
    if (window.XMLHttpRequest){
        xmlhttp=new XMLHttpRequest();}
    else{
        xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");}
 
     xmlhttp.onreadystatechange=function(){
         if (xmlhttp.readyState==4 && xmlhttp.status==200){
             if( typeof cb === 'function' )
                 cb(xmlhttp.responseText);
         }
     }
 
    xmlhttp.open("GET",myurl,true);
    xmlhttp.send();
 }