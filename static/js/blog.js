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

function changeDateView() {
    // to remove the time in date
    let regex = /\d{4}\,/;
    
    let dateView = $('.date').text();
    let num = dateView.search(regex);
    dateView = dateView.substr(0,num+4);
    $('.date').text(dateView);
}

changeDateView();