
if (localStorage.getItem('cart') == undefined) {
    var cart = {}
    num = 0;
    document.getElementById('cartnum').innerHTML = "(0)";
}
else {
    cart = JSON.parse(localStorage.getItem('cart'))
    num = ((Object.keys(cart)).length)
    document.getElementById('cartnum').innerHTML = "(" + num + ")";
}
updatecart(cart);
$('body').on('click','.addcart',function () {
    id = this.id.toString();
    prodname=document.getElementById('brandname'+id).innerHTML+"'s "+document.getElementById('prodname'+id).innerHTML;
    console.log(prodname)
    qty=1;
    price=document.getElementById('price'+id).innerHTML;
    cart[id] = [qty,prodname,price];
    num = ((Object.keys(cart)).length);
    document.getElementById('cartnum').innerHTML = "(" + num + ")";
    localStorage.setItem('cart', JSON.stringify(cart));
    updatecart(cart);
});

function updatecart(cart) {
    for (var item in cart) {
        but1 = document.getElementById("new" + item);
        but2 = document.getElementById("newb" + item);
        if (but1 != null) {
            document.getElementById("new" + item).innerHTML = "<button id='minus" + item + "'class='btn btn-primary minus mx-2' style='display:inline-block;width: 20%;height: auto;text-align: center;'>-</button> <span id='val" + item + "'>" + cart[item][0] + "</span><button id='plus" + item + "'class='btn btn-primary plus mx-2'  style='display:inline-block;width: 20%;height: auto;text-align: center;'>+</button>";
            if (cart[item][0] == 0) {
                document.getElementById("new" + item).innerHTML = '<button id="' + item + '" class="fw-bold btn-primary btn mx-4 addcart" style="display: inline-block;background-color: rgb(61,138,232);color: black;height: max-content;">Add to Cart</button>';
                delete cart[item];
                num = num - 1;
            }
        }
        if (but2 != null) {
            document.getElementById("newb" + item).innerHTML = "<button id='minus" + item + "'class='btn btn-primary minus mx-2' style='display:inline-block;width: 10%;height: auto;text-align: center;'>-</button> <span id='val" + item + "'>" + cart[item][0] + "</span><button id='plus" + item + "'class='btn btn-primary plus mx-2'  style='display:inline-block;width: 10%;height: auto;text-align: center;'>+</button>";
            if (cart[item][0] == 0) {
                document.getElementById("newb" + item).innerHTML = '<button id="' + item + '" class="fw-bold btn-primary btn mx-4 addcart" style="display: inline-block;background-color: rgb(61,138,232);color: black;height: max-content;">Add to Cart</button>'
                delete cart[item];
                num = num - 1;
            }
        }
    }
    document.getElementById('cartnum').innerHTML = "(" + num + ")";
    localStorage.setItem('cart', JSON.stringify(cart));
}
$('.newb').on('click', 'button.minus', function () {
    str = this.id.slice(5,)
    cart[str][0] = cart[str][0] - 1
    cart[str][0] = Math.max(0, cart[str][0])
    localStorage.setItem('cart', JSON.stringify(cart));
    updatecart(cart);
})
$('.newb').on('click', 'button.plus', function () {
    str = this.id.slice(4,)
    cart[str][0] = cart[str][0] + 1
    localStorage.setItem('cart', JSON.stringify(cart));
    updatecart(cart);
})


// const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

// $.ajax({
//     headers: { "X-CSRFToken": csrftoken },
//     URL: 'cart',
//     type: 'post',
//     dataType: 'json',
//     data: {
//         cartJson: JSON.stringify(cart)
//     },
//     success: function () {
//         console.log('success')
//     }
// });



