$('#burger').click(function(){
    if($('nav').css('display') === 'none'){
        $('nav').css('display','grid');
    } else {
        $('nav').css('display','none');
    }
});

$( window ).resize(function() {
  if($(window).width() > 767) {
     //$('header').css('display', 'grid');
	   $('nav').css('display','grid');
  } else {
      $('nav').css('display','none');
  }
});


//Removes an item from the cart
$('.cart-remove').click(function(){
    
    $(this).closest('div').addClass('remove');
    
    let item_id = +$(this).attr('id');
    let data = {'item_id': item_id};
    data.csrfmiddlewaretoken = $("[name=csrfmiddlewaretoken]").val();
    let url = '/cart/adjust/';
    $.ajax({
            type : 'POST',
            url : url,
            dataType: 'json',
            data : data,
            success: function(data){
                $('.remove').remove();
                let quantity = +$('.badge').text()-1;
                if(quantity === 0) {
                    $('.badge').addClass('hide-label');
                } else {
                    $('.badge').removeClass('hide-label');
                }
                $('.badge').text(quantity);
                let total = +$('.cart-amt').text()-50;
                $('.cart-amt').text(total);
            }
          });
});

