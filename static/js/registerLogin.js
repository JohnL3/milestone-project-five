
(function(){
    let msg = $('.errorlist li').text();

    if(msg && msg.includes('incorrect..')) {
        $('.form-box-register').css('display', 'none');
        $('.form-box-login').css('display', 'block');
        $('.login-tab').css('background', '#151414');
        $('.login-tab').css('color', 'white');
        $('.signup-tab').css('background', '#282929');
        $('.signup-tab').css('color', 'white');
        
    } else {
       $('.form-box-register').css('display', 'block'); 
    }

})();
/*
let msg = $('.errorlist li').text();

if(msg && msg.includes('incorrect..')) {
    $('.form-box-register').css('display', 'none');
    $('.form-box-login').css('display', 'block');
    $('.login-tab').css('background', 'lightsalmon');
    $('.login-tab').css('color', 'white');
    $('.signup-tab').css('background', '#ffbea4');
    $('.signup-tab').css('color', 'darkslategray');
    
} else {
   $('.form-box-register').css('display', 'block'); 
}*/

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

$('.login-tab').click(function(){
    $(this).css('background', '#151414');
    $(this).css('color', 'white');
    $('.signup-tab').css('background', '#282929');
    $('.signup-tab').css('color', 'white');
    $('.form-box-register').css('display', 'none');
    $('.form-box-login').css('display', 'block');
});

$('.signup-tab').click(function(){
    $(this).css('background', '#151414');
    $(this).css('color', 'white');
    $('.login-tab').css('background', '#282929');
    $('.login-tab').css('color', 'white');
    $('.form-box-register').css('display', 'block');
    $('.form-box-login').css('display', 'none');
});