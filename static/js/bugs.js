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

// get bug status from label on html.page
let tx = $('#status').text();

//set the option showing in select to the value of the status got from the label at top of html.page
$( "#status-select").val(tx[0]);


$('#comment-form').on('submit', function(event){
    event.preventDefault();
    let post_url = $(this).attr("action"); //get form action url
	let request_method = $(this).attr("method"); //get form GET/POST method
	let form_data = $(this).serialize();

    create_comment(post_url, request_method, form_data);
});


function create_comment(url, method, data) {
   
    $.ajax({
        url : url,
        type : method, 
        data : data,
        success : function(json) {
            $('#comment-text').val('');
            
            if (!json.message){
                $('#status').text(json.bug_status);
                // create a new comment box and append to dom
                createNewComment(json);
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
                
                $('#upvote-count').text(json.count);
            }
        },
    });
    
});

function createNewComment(json) {
    
    //destructure json
    ({avatar, bug_id, bug_status, comment_text,created_date, user_id, username}={...json});
    
    let url = 'https://s3-eu-west-1.amazonaws.com/features-bugs/media/'+avatar;
    
    created_date = thisDate(created_date);
    
    // create comment section
    let surround = `<div class='surround'>
        <div class='avatar'>
            <img src='${url}' alt='avatar'>
        </div>
        <div class='comment-head'>
            <span class='user-name'>${username}</span>
            <span class='user'>Commented: </span>
            <span class='date'>${created_date}</span>
        </div>
        <div class='comment-area'>
            <p>${comment_text}</p>
        </div>
    </div>`;
    
    $('#all-comments').append(surround);
}

function thisDate(date) {
    let m = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
  
    let md = new Date(date);
    
    //format return as Month Day, year
    return `${m[md.getMonth()]} ${date.substring(8,10)}, ${md.getFullYear()}`;
}
