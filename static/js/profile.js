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

let formData = new FormData();

fileUpload.addEventListener('change', function(event){
    
    let preview = document.getElementById('preview');
    let file = event.target.files[0];
    let size = file.size / 1024;
   
    if(size < 200) {
        size = Math.round(size*100)/100;
        
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
        
	    formData.append('file', file);
	    
    } else {
        $('.img-error').css('display', 'inline');
        setTimeout(function(){
            $('.img-error').css('display', 'none');
        },3000);
    }
    
});


$('#profile-edit-form').on('submit', function(event){
    event.preventDefault();
    let csrfmiddlewaretoken = $("[name=csrfmiddlewaretoken]").val();
    
    formData.append('csrfmiddlewaretoken', csrfmiddlewaretoken);
    let url ='/accounts/profile/';
    
    $.ajax({
        url : url,
        type : "POST", 
        data : formData,
        processData:false,
        contentType: false,
        success : function(json) {
            
            $('#comment-text').val('');
            
            $('#pre').remove();
            $("#img-avatar").attr("src",json.avatar_url);

        },
    });
    
});


