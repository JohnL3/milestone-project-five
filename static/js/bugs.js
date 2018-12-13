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


$('#comment-form').on('submit', function(event){
    event.preventDefault();
    console.log("form submitted!");
    create_comment();
});

function create_comment() {
    
    let data = {};
 
    let bug_id = +$('.bug-id').prop('id');
    data.comment = $('#comment-text').val();
    data.csrfmiddlewaretoken = $("[name=csrfmiddlewaretoken]").val();
    data.created_date = $('#date-comment').val();
    
    
    //console.log('DATE', data.created_date);
    
    let url ='/bugs/'+bug_id+"/";
    
    $.ajax({
        url : url,
        type : "POST", 
        data : data,
        success : function(json) {
            $('#comment-text').val(''); 
            console.log(json);
            console.log("successfully done yeeeeeee");
            createNewComment(json);
        },
    }); 
}

function createNewComment(json) {
    let surround = `<div class='surround'>
        <div class='avatar'>
            <img src='/media/images/admin.jpg' alt='avatar'>
        </div>
        <div class='comment-head'>
            <span class='user-name'>${json.username}</span>
            <span class='user'>Commented: </span>
            <span class='user'>${json.created_date}</span>
        </div>
        <div class='comment-area'>
            <p>${json.comment_text}</p>
        </div>
    </div>`;
    
    $('#all-comments').append(surround);
}