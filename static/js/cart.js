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

function setDisabled() {
    $('.disable').prop('checked','checked');
    $('.disable').attr('disabled','disabled');
    $('.cart-amt').text('50');
}
setDisabled();

//Updates the total of features to be purchased in cart
$('input[type="checkbox"]').change(function(){
    if($(this).prop('checked')) {
        let total = +$('.cart-amt').text()+50;
        $('.cart-amt').text(total);
    } else {
        let total = +$('.cart-amt').text()-50;
        $('.cart-amt').text(total);
    }
});

//Removes an item from the cart
$('.cart-remove').click(function(){
    
    if( $(this).closest('div').find('[type=checkbox]').prop('checked')) {
         let amt = +$('.cart-amt').text()-50;
         $('.cart-amt').text(amt);
         $(this).closest('div').addClass('remove');
    } else {
        $(this).closest('div').addClass('remove');
    }
    
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
                $('.badge').text(quantity);
            }
          });
});

