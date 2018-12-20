let fileUpload = document.getElementById('id_image');
let myData = '';
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


$('.tab-c').click(function(){
    $(this).addClass('profile-tab-active');
    $('.edit-profile').css('display', 'block');
    
    $('.tab-a').removeClass('profile-tab-active');
    
    $('.tab-b').removeClass('profile-tab-active');
    
});

$('.tab-a').click(function(){
    $(this).addClass('profile-tab-active');
    
    
    $('.tab-b').removeClass('profile-tab-active');
    
    $('.tab-c').removeClass('profile-tab-active');
    $('.edit-profile').css('display', 'none');
});

$('.tab-b').click(function(){
    $(this).addClass('profile-tab-active');
    
    
    $('.tab-a').removeClass('profile-tab-active');
    
    $('.tab-c').removeClass('profile-tab-active');
    $('.edit-profile').css('display', 'none');
});

let formData = new FormData();
fileUpload.addEventListener('change', function(event){
    let preview = document.getElementById('preview');
    let file = event.target.files[0];
    let size = file.size / 1024;
    let name = file.name;
    console.log('NAME', name, 'Size',size);
    if(size < 500) {
        size = Math.round(size*100)/100;
        
        let IMAGE = '';
        let prev = document.getElementById('pre');
        
        if(prev === null) {
              IMAGE = document.createElement('IMG');
              IMAGE.id = 'pre';
              IMAGE.src = URL.createObjectURL(file);
              console.log('[FILE] ',file.name);
              preview.prepend(IMAGE);
              URL.revokeObjectURL(file);
            } else {
              prev.style.transform = 'none';
              prev.src = URL.createObjectURL(file);
              document.getElementById("pre").style.maxWidth = '50px';
            }
        //let formData = new FormData();
	    formData.append('file', file);
	    myData = formData;
	    
    } else {
        alert('Image file size is too large.')
    }
    
});


$('#profile-edit-form').on('submit', function(event){
    event.preventDefault();
    let csrfmiddlewaretoken = $("[name=csrfmiddlewaretoken]").val();
    let arr = [csrfmiddlewaretoken];
    //formData.csrfmiddlewaretoken = $("[name=csrfmiddlewaretoken]").val();
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
            console.log(json);
            
            if (!json.message){
                console.log('sorted');
            // create a new comment box and append to dom
            
            } else {
                console.log('Back');
            }
        },
    });
    
});


