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

/*
$('.submit-btn').click(function(event){
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
            window.location = '/bugs/';
        },
    });
    
});
*/
$('#bug-form').submit(function(e){
    e.preventDefault();
    let post_url = $(this).attr("action"); //get form action url
	let request_method = $(this).attr("method"); //get form GET/POST method
	let form_data = $(this).serialize();
	console.log(form_data);
	
	$.ajax({
		url : post_url,
		type: request_method,
		data : form_data
	}).done(function(response){ 
		if(response.status_code === 1) {
		    window.location = '/bugs/';
		} else {
		    alert('Issue with the way you filled in form.');
		}
	});
})