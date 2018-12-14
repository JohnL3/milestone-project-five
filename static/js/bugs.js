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
let tx = $('#status').text();
$( "#status-select").val(tx[0]);

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
    data.bug_status = $( ".set-bug-status option:selected" ).val();
    
    let url ='/bugs/'+bug_id+"/";
    
    $.ajax({
        url : url,
        type : "POST", 
        data : data,
        success : function(json) {
            $('#comment-text').val('');
            console.log(json);
            
            if (!json.message){
            $('#status').text(json.bug_status);
            // create a new comment box and append to dom
            createNewComment(json);
            } else {
                alert('comment is closed');
            }
        },
    });
    
}


$('.upvote-btn').click(function(){
    let data = {};
    data.bugid = +$('.bug-id').prop('id');
    data.csrfmiddlewaretoken = $("[name=csrfmiddlewaretoken]").val();
    
    let url ='/bugs/upvote/';
    
    $.ajax({
        url : url,
        type : "POST", 
        data : data,
        success : function(json) {
            
            if (!json.message){
                console.log(json);
                $('#upvote-count').text(json.count);
            } else {
                console.log(json.message);
            }
        },
    });
    
});

function createNewComment(json) {
    
    //destructure json
    ({bug_id, bug_status, comment_text,created_date, user_id, user_type, username}={...json});
    
    // get avatar image depending on user type
    let img = (user_type === 'A')? 'admin.jpg': (user_type === 'S')? 'staff.jpg': 'user.jpg';
    
    // create comment section
    let surround = `<div class='surround'>
        <div class='avatar'>
            <img src='/media/images/${img}' alt='avatar'>
        </div>
        <div class='comment-head'>
            <span class='user-name'>${username}</span>
            <span class='user'>Commented: </span>
            <span class='user'>${created_date}</span>
        </div>
        <div class='comment-area'>
            <p>${comment_text}</p>
        </div>
    </div>`;
    
    $('#all-comments').append(surround);
}

