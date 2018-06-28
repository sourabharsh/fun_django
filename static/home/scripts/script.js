$(document).ready(function() {
    $('[data-toggle="popover"]').popover({
        'html' : true,
        'content' : '<a href="/logout/">log out</a>'
    });
    
    // to switch to sign-in form
    $('#signin_link').click(function(){
        $('#signup_form').css("display", "none");
        $('#signin_form').css("visibility", "visible");
    });

    // push tweets in the ol 
    $('#load_more_tweets').click(function(){
        $('ol#tweets').append('<ul>whatssss</ul>');
        url = "get_tweets?start=0&limit=10";
        $.get(url, function(data,status) {
            print(data);
            $('ol#tweets').append(data);
        })
    });
});