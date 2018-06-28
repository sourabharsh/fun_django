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
});