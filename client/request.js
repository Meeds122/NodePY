function x_request(call){
    request_object = new XMLHttpRequest();
    api_url = "http://127.0.0.1:31337/" + call;
    request_object.open("GET", api_url)
    request_object.send();
    request_object.onreadystatechange=function(){
        if(this.readyState==4 && this.status==200){
            return request_object.response;
        }
    }
}

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