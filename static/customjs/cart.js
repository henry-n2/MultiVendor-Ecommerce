

// function change_cart_quantity(cart_id,values) {
//     // console.log(typeof(cart_id))
//     // console.log(typeof(values))

//     var xhr = new XMLHttpRequest()

//     xhr.onload= function() {
//         var response = xhr.responseText
//          console.log(typeof(response['total_product_price']))
//          console.log(response['total_product_price'])
//          console.log(typeof(response['sub_total']))
//          response = JSON.parse(response)
//          var jsonResponse = response['carts_product']
//         //  console.log(jsonResponse)
//         let formatteTortalProductPrice = response['total_product_price'].toFixed(2);
//         let formattedSubTotal   = response['sub_total'].toFixed(2);
//          document.getElementById('product-quantity-'+cart_id).innerText = response['product_quantity']
//          document.getElementById('total_product_price-'+cart_id).innerText = '₹'+ formatteTortalProductPrice
//          document.getElementById('sub_total_price').innerText = '₹'+ formattedSubTotal 

//          // Get the table element to append product rows
//         var table = document.querySelector('table');



//         if ( jsonResponse.length > 0) {

//             if ( jsonResponse[0] === 'no-product'){
                
//                 // Get the table element to append product rows
//                 var table = document.querySelector('table');            

//                 // Clear the existing table
//                 while (table.firstChild) {
//                     table.removeChild(table.firstChild);
//                 }
//                 return;
                
//             }

//             // Get the table element to append product rows
//             var table = document.querySelector('table');            

//             // Clear the existing table
//             while (table.firstChild) {
//                 table.removeChild(table.firstChild);
//             }
//             // Loop through the JSON response and create a row for each product
//             jsonResponse.forEach(function(product, index) {
//                 var row = document.createElement('tr');
                
//                 var thumbnailCell = document.createElement('td');
//                 thumbnailCell.className = 'product-thumbnail';
//                 var thumbnailLink = document.createElement('a');
//                 thumbnailLink.href = 'shop-details.html';
//                 var thumbnailImage = document.createElement('img');
//                 thumbnailImage.src = product.image;
//                 thumbnailImage.alt = '';
//                 thumbnailLink.appendChild(thumbnailImage);
//                 thumbnailCell.appendChild(thumbnailLink);
                
//                 var nameCell = document.createElement('td');
//                 nameCell.className = 'product-name';
//                 var nameLink = document.createElement('a');
//                 nameLink.href = 'shop-details.html';
//                 nameLink.textContent = product.title;
//                 nameCell.appendChild(nameLink);
                
//                 var priceCell = document.createElement('td');
//                 priceCell.className = 'product-price';
//                 var priceSpan = document.createElement('span');
//                 priceSpan.className = 'amount';
//                 priceSpan.textContent = '$' + product.regular_price;
//                 priceCell.appendChild(priceSpan);
//                 var quantityCell = document.createElement('td');
//                 quantityCell.className = 'product-quantity';
            
//                 var quantityDiv = document.createElement('div');
//                 quantityDiv.className = 'd-inline-flex';
            
//                 var minusButton = document.createElement('div');
//                 minusButton.className = 'btn btn-outline-info minus';
//                 minusButton.textContent = '-';
//                 minusButton.onclick = function() {
//                 change_cart_quantity(product.id, 2);
//                 };
            
//                 var quantityP = document.createElement('p');
//                 quantityP.className = 'mx-2 cart-quantity';
//                 quantityP.id = 'product-quantity-' + product.id;
//                 quantityP.textContent = product.quantity;
            
//                 var plusButton = document.createElement('div');
//                 plusButton.className = 'btn btn-outline-info plus-' + product.id;
//                 plusButton.textContent = '+';
//                 plusButton.onclick = function() {
//                 change_cart_quantity(product.id, 1);
//                 };

//                 var subtotalCell = document.createElement('td');
//                 subtotalCell.className = 'product-subtotal';
//                 var subtotalSpan = document.createElement('span');
//                 subtotalSpan.className = 'amount';
//                 subtotalSpan.textContent = '$'+product.total_product_price;
//                 subtotalCell.appendChild(subtotalSpan);
            
//                 var removeCell = document.createElement('td');
//                 removeCell.className = 'product-remove';
//                 var removeLink = document.createElement('a');
//                 removeLink.href = '#';
//                 removeLink.onclick = function() {
//                   change_cart_quantity(product.id, 0);
//                 }
//                 var removeIcon = document.createElement('i');
//                 removeIcon.className = 'fa fa-times';
//                 removeLink.appendChild(removeIcon);
//                 removeCell.appendChild(removeLink);
            
                
//                 // Add the cells to the row
//                 row.appendChild(thumbnailCell);
//                 row.appendChild(nameCell);
//                 row.appendChild(priceCell);

//                 quantityDiv.appendChild(minusButton);
//                 quantityDiv.appendChild(quantityP);
//                 quantityDiv.appendChild(plusButton);
            
//                 quantityCell.appendChild(quantityDiv);
//                 row.appendChild(quantityCell);
//                 row.appendChild(subtotalCell);
//                 row.appendChild(removeCell);

//                 // Append the row to the table
//                 table.appendChild(row);
//             });

//         }


//     }

//     xhr.open(
//         'POST',
//         '/increse-cart/'
//     )

//     var data ={
//         "id":cart_id,
//         'values': values
//     }

//     xhr.send(JSON.stringify(data))

// }


// function change_cart_quantity(cart_id, values) {
//     var xhr = new XMLHttpRequest();

//     xhr.onload = function () {
//         var response = JSON.parse(xhr.responseText); // ✅ Parse JSON first

//         let formattedTotalProductPrice = response['total_product_price'].toFixed(2);
//         let formattedSubTotal = response['sub_total'].toFixed(2);

//         // ✅ Update the quantity and prices
//         document.getElementById('product-quantity-' + cart_id).innerText = response['product_quantity'];
//         document.getElementById('total_product_price-' + cart_id).innerText = '₹' + formattedTotalProductPrice;
//         document.getElementById('sub_total_price').innerText = '₹' + formattedSubTotal;

//         var jsonResponse = response['carts_product'];
//         var table = document.querySelector('table');

//         if (jsonResponse.length > 0) {
//             if (jsonResponse[0] === 'no-product') {
//                 while (table.firstChild) {
//                     table.removeChild(table.firstChild);
//                 }
//                 return;
//             }

//             // Refresh the table
//             while (table.firstChild) {
//                 table.removeChild(table.firstChild);
//             }

//             jsonResponse.forEach(function (product) {
//                 var row = document.createElement('tr');

//                 var thumbnailCell = document.createElement('td');
//                 thumbnailCell.className = 'product-thumbnail';
//                 var thumbnailLink = document.createElement('a');
//                 thumbnailLink.href = 'shop-details.html';
//                 var thumbnailImage = document.createElement('img');
//                 thumbnailImage.src = product.image;
//                 thumbnailImage.alt = '';
//                 thumbnailLink.appendChild(thumbnailImage);
//                 thumbnailCell.appendChild(thumbnailLink);

//                 var nameCell = document.createElement('td');
//                 nameCell.className = 'product-name';
//                 var nameLink = document.createElement('a');
//                 nameLink.href = 'shop-details.html';
//                 nameLink.textContent = product.title;
//                 nameCell.appendChild(nameLink);

//                 var priceCell = document.createElement('td');
//                 priceCell.className = 'product-price';
//                 var priceSpan = document.createElement('span');
//                 priceSpan.className = 'amount';
//                 priceSpan.textContent = '₹' + product.regular_price;
//                 priceCell.appendChild(priceSpan);

//                 var quantityCell = document.createElement('td');
//                 quantityCell.className = 'product-quantity';
//                 var quantityDiv = document.createElement('div');
//                 quantityDiv.className = 'd-inline-flex';

//                 var minusButton = document.createElement('div');
//                 minusButton.className = 'btn btn-outline-info minus';
//                 minusButton.textContent = '-';
//                 minusButton.onclick = function () {
//                     change_cart_quantity(product.id, 2);
//                 };

//                 var quantityP = document.createElement('p');
//                 quantityP.className = 'mx-2 cart-quantity';
//                 quantityP.id = 'product-quantity-' + product.id;
//                 quantityP.textContent = product.quantity;

//                 var plusButton = document.createElement('div');
//                 plusButton.className = 'btn btn-outline-info plus-' + product.id;
//                 plusButton.textContent = '+';
//                 plusButton.onclick = function () {
//                     change_cart_quantity(product.id, 1);
//                 };

//                 var subtotalCell = document.createElement('td');
//                 subtotalCell.className = 'product-subtotal';
//                 var subtotalSpan = document.createElement('span');
//                 subtotalSpan.className = 'amount';
//                 subtotalSpan.textContent = '₹' + product.total_product_price;
//                 subtotalCell.appendChild(subtotalSpan);

//                 var removeCell = document.createElement('td');
//                 removeCell.className = 'product-remove';
//                 var removeLink = document.createElement('a');
//                 removeLink.href = '#';
//                 removeLink.onclick = function () {
//                     change_cart_quantity(product.id, 0);
//                 };
//                 var removeIcon = document.createElement('i');
//                 removeIcon.className = 'fa fa-times';
//                 removeLink.appendChild(removeIcon);
//                 removeCell.appendChild(removeLink);

//                 quantityDiv.appendChild(minusButton);
//                 quantityDiv.appendChild(quantityP);
//                 quantityDiv.appendChild(plusButton);
//                 quantityCell.appendChild(quantityDiv);

//                 row.appendChild(thumbnailCell);
//                 row.appendChild(nameCell);
//                 row.appendChild(priceCell);
//                 row.appendChild(quantityCell);
//                 row.appendChild(subtotalCell);
//                 row.appendChild(removeCell);

//                 table.appendChild(row);
//             });
//         }
//     };

//     xhr.open('POST', '/increse-cart/');

//     xhr.setRequestHeader('Content-Type', 'application/json'); // ✅ Important
//     xhr.setRequestHeader('X-CSRFToken', getCSRFToken()); // ✅ Add your CSRF token logic

//     var data = {
//         id: cart_id,
//         values: values
//     };

//     xhr.send(JSON.stringify(data));
// }

// // Optional utility for getting CSRF token from cookie
// function getCSRFToken() {
//     var name = 'csrftoken';
//     var cookieValue = null;
//     if (document.cookie && document.cookie !== '') {
//         var cookies = document.cookie.split(';');
//         for (var i = 0; i < cookies.length; i++) {
//             var cookie = cookies[i].trim();
//             if (cookie.substring(0, name.length + 1) === (name + '=')) {
//                 cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                 break;
//             }
//         }
//     }
//     return cookieValue;
// }
function change_cart_quantity(cart_id, values) {
    var xhr = new XMLHttpRequest();

    xhr.onload = function () {
        var response = JSON.parse(xhr.responseText);

        var jsonResponse = response['carts_product'];

        // Select table body
        var table = document.querySelector('table');
        var tableBody = table.querySelector('tbody') || table;

        // Clear table body
        tableBody.innerHTML = '';

        // Empty cart condition
        if (!jsonResponse || jsonResponse.length === 0 || jsonResponse[0] === 'no-product') {
            var emptyRow = document.createElement('tr');
            var emptyTd = document.createElement('td');
            emptyTd.colSpan = 6;
            emptyTd.className = 'text-center';
            emptyTd.innerText = 'Your cart is empty.';
            emptyRow.appendChild(emptyTd);
            tableBody.appendChild(emptyRow);

            // Also reset subtotal
            document.getElementById('sub_total_price').innerText = '₹0.00';
            return;
        }

        // Rebuild cart rows
        jsonResponse.forEach(function (product) {
            var row = document.createElement('tr');

            row.innerHTML = `
                <td class="product-thumbnail">
                    <a href="shop-details.html"><img src="${product.image}" alt=""></a>
                </td>
                <td class="product-name">
                    <a href="shop-details.html">${product.title}</a>
                </td>
                <td class="product-price">
                    <span class="amount">₹${parseFloat(product.regular_price).toFixed(2)}</span>
                </td>
                <td class="product-quantity">
                    <div class="d-inline-flex">
                        <div class="btn btn-outline-info minus" onclick="change_cart_quantity(${product.id}, 2)">-</div>
                        <p class="mx-2 cart-quantity" id="product-quantity-${product.id}">${product.quantity}</p>
                        <div class="btn btn-outline-info plus" onclick="change_cart_quantity(${product.id}, 1)">+</div>
                    </div>
                </td>
                <td class="product-subtotal">
                    <span class="amount" id="total_product_price-${product.id}">₹${parseFloat(product.total_product_price).toFixed(2)}</span>
                </td>
                <td class="product-remove">
                    <a href="#" onclick="change_cart_quantity(${product.id}, 0); return false;"><i class="fa fa-times"></i></a>
                </td>
            `;

            tableBody.appendChild(row);
        });

        // ✅ Update subtotal price at the end
        let formattedSubTotal = response['sub_total'].toFixed(2);
        document.getElementById('sub_total_price').innerText = '₹' + formattedSubTotal;
    };

    xhr.open('POST', '/increse-cart/');
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.setRequestHeader('X-CSRFToken', getCSRFToken());

    var data = {
        id: cart_id,
        values: values
    };

    xhr.send(JSON.stringify(data));
}

// CSRF utility
function getCSRFToken() {
    var name = 'csrftoken';
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
