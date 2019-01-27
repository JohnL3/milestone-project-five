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


function changeDateView() {
    // to remove the time in date
    let regex = /\d{4}\,/;
    
    let dateView = $('.date');
    $('.date').each(function(){
        let num = $(this).text().search(regex);
        let date = $(this).text().substr(0, num+4);
        $(this).text(date);
    });
}

changeDateView();



