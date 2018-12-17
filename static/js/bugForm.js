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

$('.submit-btn').click(function(){
    event.preventDefault();
    let data = {};
    data.bug_title = $('#id_bug_title').val();
    data.initial_comment = $('#id_initial_comment').val();
    data.csrfmiddlewaretoken = $("[name=csrfmiddlewaretoken]").val();
    
    let url ='/bugs/issue/';
    
    $.ajax({
        url : url,
        type : "POST", 
        data : data,
        success : function(json) {
            window.location = '/bugs/'
        },
    });
    
});