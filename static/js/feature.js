$('#burger').click(function(){
    if($('nav').css('display') === 'none'){
        $('nav').css('display','grid');
    } else {
        $('nav').css('display','none');
    }
});

$( window ).resize(function() {
  if($(window).width() > 767) {
	   $('nav').css('display','grid');
  } else {
      $('nav').css('display','none');
  }
});

// Add an item to the cart 
$('#add-to-cart').on('submit', function(event){
     event.preventDefault();
     if($('this').is('[disabled=disabled]') === false) {
         
         let url = $(this).attr("action");
         let method = $(this).attr("method");
         let data = $(this).serialize();
       
         $.ajax({
            url : url,
            type : method, 
            data : data,
            success : function(data) {
                let badge = $('.badge').text();
                if(!badge) {
                   addLabel();
                }
                let quantity = +$('.badge').text()+1;
                $('.badge').text(quantity);
                $('.feature-success-msg').text('Added to cart');
                $('.feature-submit-btn').prop('disabled','disabled');
                setTimeout(function(){
                    $('.feature-success-msg').text('');
                },2000);
            },
        });
     }
});




function addLabel() {
    let cartLabel = `<label class='badge'></label>`;
    $('#attach').append(cartLabel);
}

