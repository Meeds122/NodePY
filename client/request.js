function request(call){
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