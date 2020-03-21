$(document).ready(function(){
     
    $('form').on('submit', function(event){

        $.ajax({
            data : {
                username : $('#username').val(),
                password : $('#password').val()
            },
            type : 'POST',
            url : '/login'
        })
        .done(function(data) {

            if (data.error) {
                $('#errorAlert').text(data.error).show();
                $('#sucessAlert').hide();
            }
            else{
                $('#sucessAlert').text(data.username).show();
                $('#errorAlert').hide();
            }
        });

        event.preventDefault();
    });

});