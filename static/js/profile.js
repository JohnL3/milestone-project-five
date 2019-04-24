let fileUpload = document.getElementById('id_image');

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


$('.tab-c').click(function(){
    $(this).addClass('profile-tab-active');
    $('.edit-profile').css('display', 'block');
    
    $('.tab-a').removeClass('profile-tab-active');
    
    $('.tab-b').removeClass('profile-tab-active');
    $('.user-issues').css('display', 'none');
    $('.user-features').css('display', 'none');
});

$('.tab-a').click(function(){
    $(this).addClass('profile-tab-active');
    $('.user-features').css('display', 'block');
    
    $('.tab-b').removeClass('profile-tab-active');
    $('.user-issues').css('display', 'none');
    $('.tab-c').removeClass('profile-tab-active');
    $('.edit-profile').css('display', 'none');
     $('#pre').remove();
});

$('.tab-b').click(function(){
    $(this).addClass('profile-tab-active');
    $('.user-issues').css('display', 'block');
    
    $('.tab-a').removeClass('profile-tab-active');
    
    $('.tab-c').removeClass('profile-tab-active');
    $('.edit-profile').css('display', 'none');
    $('.user-features').css('display', 'none');
     $('#pre').remove();
});


// Show preview of Image
fileUpload.addEventListener('change', function(event){
    
    let preview = document.getElementById('preview');
    let file = event.target.files[0];
    
    let IMAGE = '';
    let prev = document.getElementById('pre');
    
    if(prev === null) {
          IMAGE = document.createElement('IMG');
          IMAGE.id = 'pre';
          IMAGE.src = URL.createObjectURL(file);
          
          preview.prepend(IMAGE);
          URL.revokeObjectURL(file);
        } else {
          prev.style.transform = 'none';
          prev.src = URL.createObjectURL(file);
          document.getElementById("pre").style.maxWidth = '50px';
        }
	  
});


$('#profile-edit-form').on('submit', function(event){
    event.preventDefault();
    
    let url = $(this).attr("action"); //get form action url
	let method = $(this).attr("method"); //get form GET/POST method
    let data = new FormData(this);
    
    $.ajax({
        url : url,
        type : method, 
        data : data,
        processData:false,
        contentType: false,
        success : function(json) {
            
            if (json.error) {
                 $('.img-error').css('display', 'inline');
                    setTimeout(function(){
                        $('.img-error').css('display', 'none');
                    },3000);
            } else {
                $('#comment-text').val('');
                let src = 'https://s3-eu-west-1.amazonaws.com/features-bugs/media/'+json.avatar;
                $('#pre').remove();
                $("#img-avatar").attr("src",src);
            }

        },
    });
    
});


