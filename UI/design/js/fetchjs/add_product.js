var token = sessionStorage.getItem('token')
document.getElementById('adding').addEventListener('submit', addProduct);

function addProduct(e){

    e.preventDefault();
    let product_name = document.getElementById('product_name').value;
    let unit_price = document.getElementById('unit_price').value;
    let quantity = document.getElementById('quantity').value;
    let category = document.getElementById('categories').value;

    fetch('http://127.0.0.1:5000/api/v2/products', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-type': 'application/json',
            'Authorization': 'Bearer '+ token
        },
        body:JSON.stringify({product_name:product_name, unit_price:unit_price, quantity:quantity, category:category})
    })
    .then((response) => {
        status_code = response.status
        return response.json()
    })
    .then((data) => {
        var error = document.getElementById('error-message')
        var success = document.getElementById('success-message')
        if (data.msg == 'Token has expired'){
            window.location.href = 'index.html'
        }
        else if(status_code == 401){
            error.innerHTML = data['message']
        }
        else if(status_code == 400){
            console.log(data.message)
            error.innerHTML = data['message']
        }
        else if(status_code == 201){
            window.location.reload();
            success.innerHTML = data['message']
        }
    })
    .catch((error) => {
        console.log(error)
    })
}
