$(document).ready(function() {
    /* Set rates + misc */
    var shippingRate = 5000;
    var fadeTime = 300;

    inputs = document.getElementsByClassName('product-quantity');
    for (var i = 0; i < inputs.length; i+=1) {
        updateQuantity(inputs[i].getElementsByTagName('input'));
    }
    recalculateCart();


    /* Assign actions */
    $('.product-quantity input').change( function() {
        updateQuantity(this);
    });

    $('.product-removal button').click( function() {
        removeItem(this);
    });


    /* Recalculate cart */
    function recalculateCart()
    {
        var subtotal = 0;
        var item_count = 0;

        /* Sum up row totals */
        $('.product').each(function () {
        subtotal += parseInt($(this).children('.product-line-price').text());
        item_count += 1;
        });

        /* Calculate totals */
        var shipping = (subtotal > 0 ? shippingRate : 0);
        var total = subtotal + shipping;

        /* Update totals display */
        $('.totals-value').fadeOut(fadeTime, function() {
        $('#cart-subtotal').html(subtotal);
        $('#cart-shipping').html(shipping);
        $('#cart-total').html(total);
        $('#page--title').html('<i class="fas fa-shopping-cart"></i>&nbsp;Сагс <small>(' + item_count + ")</small>");
        if(total == 0){
            $('.order-btn').fadeOut(fadeTime);
        }else{
            $('.order-btn').fadeIn(fadeTime);
        }
        $('.totals-value').fadeIn(fadeTime);
        });
    }


    /* Update quantity */
    function updateQuantity(quantityInput)
    {
        /* Calculate line price */
        var productRow = $(quantityInput).parent().parent();
        var price = parseFloat(productRow.children('.product-price').text());
        var quantity = $(quantityInput).val();
        var linePrice = price * quantity;

        /* Update line price display and recalc cart totals */
        productRow.children('.product-line-price').each(function () {
            $(this).fadeOut(fadeTime, function() {
            $(this).text(linePrice);
            recalculateCart();
            $(this).fadeIn(fadeTime);
            });
        });
    }


    /* Remove item from cart */
    function removeItem(removeButton)
    {
        /* Remove row from DOM and recalc cart total */
        var productRow = $(removeButton).parent().parent();
        productRow.slideUp(fadeTime, function() {
            productRow.remove();
            recalculateCart();
        });
    }

    });