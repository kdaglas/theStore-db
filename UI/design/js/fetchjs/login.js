document.getElementById('logging-in').addEventListener('submit', login);

function login(e){

    e.preventDefault();
    let username = document.getElementById('username').value;
    let password = document.getElementById('password').value;

    fetch('http://127.0.0.1:5000/api/v2/auth/login', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-type': 'application/json'
        },
        body:JSON.stringify({attendant_name:username, password:password})
    })
    .then((response) => {
        status_code = response.status
        return response.json()
    })
    .then((data) => {
        var err = document.getElementById('errormsg')
        var token = data['token']
        var role = data['role']
        if(status_code == 401){
            err.innerHTML = data['message']
        }
        else if(status_code == 200 && data["role"] == "admin"){
            sessionStorage.setItem('token', token)
            sessionStorage.setItem('role', role)
            window.location.href = 'admin.html'
        }
        else if(status_code == 200 && data["role"] == "attendant"){
            sessionStorage.setItem('token', token)
            sessionStorage.setItem('role', role)
            window.location.href = 'homepage.html'
        }
        else{
            err.innerHTML = data['message']
        }
    })
    .catch((error) => {
        console.log(error)
    })
}
