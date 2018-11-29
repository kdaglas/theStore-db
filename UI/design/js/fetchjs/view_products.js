window.addEventListener('load', viewProducts);
// document.getElementById('logout').addEventListener('click', logout);
var token = sessionStorage.getItem('token');
var role = sessionStorage.getItem('role');

//attendants function to view all products
function allProducts(data){

    let products = '';
    data.All_products.forEach((product) => {
        products += `
            <tr>
                <td>${product.product_name}</td>
                <td>${product.unit_price}/=</td>
                <td>${product.quantity} Units</td>
                <td>${product.category}</td>
                <td><a href="#modalbox"><button class="button1" id="${product.productid}" onclick="viewOneProduct(${product.productid})" type="submit">View</button></a></td>
                <td><button class="button" onclick="sugar()">Add</button></td>
            </tr>
        `;
    });
    return products
}

//admin function to view all products
function allTheProducts(data){
    
    let all_products = '';
    data.All_products.forEach((product) => {
        all_products += `
            <tr>
                <td>${product.product_name}</td>
                <td>${product.unit_price}/=</td>
                <td>${product.quantity} Units</td>
                <td>${product.category}</td>
                <td><a href="#modalbox"><button class="button1" id="${product.productid}" onclick="viewOneProduct(${product.productid})" type="submit">View</button></a></td>
            </tr>
        `;
    });
    return all_products
}

function viewProducts(){
    
    fetch('http://127.0.0.1:5000/api/v2/products', {
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
        else if(status_code === 200 && role === 'attendant'){
            //attendants: view products
            let all_products = allProducts(data);
            document.getElementById('products').innerHTML = all_products;
        }
        else if(status_code === 200 && role === 'admin'){
            //admin: view products
            let all_the_products = allTheProducts(data);
            document.getElementById('all_products').innerHTML = all_the_products;
        }
    })
    .catch((error) => {
        console.log(error)
    })
}
