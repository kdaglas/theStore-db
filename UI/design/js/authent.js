/* --- function to verify attendant or owner --- */
function Check(){
    var username = document.querySelector("#username").value;
    var password = document.querySelector("#password").value;
    if(username==='user' && password ==="user"){
        window.location.href ="homepage.html";
    }else if(username==='admin' && password ==="admin"){
        window.location.href ="admin.html";
    }else{
        alert('invalid information')
    }
}