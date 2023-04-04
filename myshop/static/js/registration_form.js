// TODO reduce this code by elements what i havent in register.html

$('.costumer_email_check').hide();
$('#email').on('input', function() {
    var email = $(this).val();
    // Get the CSRF token from the form
    var csrf_token = $('input[name=csrf_token]').val();
    var emailRegEx = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
    if(!emailRegEx.test(email) && email.length > 10) {
        $('.costumer_email_check').text("Prosím zadejte platný formát emailové adresy.").show();
        $('.check-tag').css('visibility', 'hidden');  // hide the "check-tag" element
        return false;
    } else {
        $('.costumer_email_check').hide();
        $.ajax({
            url: '/auth/check-email',
            method: 'POST',
            headers: { 'X-CSRFToken': csrf_token },
            data: {'email': email},
            success: function(data) {
                if (data == 'taken') {
                    $('.costumer_email_check').text("Tento email je již zaregistrovaný v naší databázi.").show();
                    $('.check-tag').css('visibility', 'hidden');  // hide the "check-tag" element
                    $('.email-used').text("Tento email je již používán.");
                    $('#costumer_email_check_id').show();
                } else {
                    $('.costumer_email_check').hide();
                    $('.check-tag').css('visibility', 'visible');  // show the "check-tag" element
                    $('.email-used').text("");
                    $('#costumer_email_check_id').hide();
                }
            }
        });
    }
});