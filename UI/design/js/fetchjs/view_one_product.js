var token = sessionStorage.getItem('token');
var role = sessionStorage.getItem('role');

function productDetails(data){

    product = `
        <div class="details">
            <h4>${data.Product.product_name}</h4>
            <h4>${data.Product.unit_price}/= per unit</h4>
            <h4>${data.Product.quantity} units</h4>
            <h4>${data.Product.category}</h4>
            <h3 class="small-title">minimum quantity allowed</h3>
            <h4>1 unit per time</h4>
        </div>
    `;
    return product
}

function adminProductDetails(data){

    product = `
        <div class="details">
            <h4>${data.Product.product_name}</h4>
            <h4>${data.Product.unit_price}/= per unit</h4>
            <h4>${data.Product.quantity} units</h4>
            <h4>${data.Product.category}</h4>
            <h3 class="small-title">minimum quantity allowed</h3>
            <h4>1 unit per time</h4>
        </div>
        <a href="edit.html"><button class="button1">Edit</button></a>
        <a href="admin.html"><button class="button2" type="button" onclick="deleteItem(${data.Product.productid})">Delete</button></a>
    `;
    return product
}

function viewOneProduct(productid){

    fetch('http://127.0.0.1:5000/api/v2/products/'+productid, {
        method: 'GET',
        headers: {
            'Content-type': 'application/json',
            'Authorization': 'Bearer '+ token
        }
    })
    .then((response) => {
        status_code = response.status
        return response.json()
    })
    .then((data) => {
        var err = document.getElementById('errormsg')
        if (data.msg === 'Token has expired'){
            window.location.href = 'index.html'
        }
        else if(status_code === 404){
            err.innerHTML = data['message']
        }
        else if(status_code === 400){
            err.innerHTML = data['message']
        }
        else if(status_code === 200 && role === 'attendant'){
            //attendants: view products
            productDetails(data)
            document.getElementById('product').innerHTML = product;
        }
        else if(status_code === 200 && role === 'admin'){
            //admin: view products
            adminProductDetails(data);
            document.getElementById('product').innerHTML = product;
        }
    })
    .catch((error) => {
        console.log(error)
    })
}