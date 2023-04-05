// """ Libor Havránek App Copyright (C)  5.4 2023 """


$('.registration-email-input').on('input', function() {
  var email = $(this).val();
  // Get the CSRF token from the form
  var csrf_token = $('input[name=csrf_token]').val();
  var emailRegEx = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;

  if (email.length < 10) {
    $(this).removeClass('is-valid is-invalid');
    $('.customer_email_check').hide();
    return;
  }

  if (!emailRegEx.test(email)) {
    $(this).removeClass('is-valid').addClass('is-invalid');
    $('.customer_email_check').text("Prosím zadejte platný formát emailové adresy.").show();
    return false;
  }

  $.ajax({
    url: '/auth/check-email',
    method: 'POST',
    headers: { 'X-CSRFToken': csrf_token },
    data: { 'email': email },
    success: function(data) {
      if (data === 'invalid') {
        $(this).removeClass('is-valid').addClass('is-invalid');
        $('.customer_email_check').text("Prosím zadejte platný formát emailové adresy.").show();
      } else if (data === 'taken') {
        $(this).removeClass('is-valid').addClass('is-invalid');
        $('.customer_email_check').text("Tento email je již zaregistrovaný v naší databázi.").show();
      } else {
        $(this).removeClass('is-invalid').addClass('is-valid');
        $('.customer_email_check').hide();

      }
    }.bind(this)
  });
});




$('.registration-username-input').on('input', function() {
    var username =  $(this).val();
    // Get the CSRF token from the form
    var csrf_token = $('input[name=csrf_token]').val();
    $('.customer_username_check').hide(); // hide the message element before making the AJAX request
        $('.registration-username-input').removeClass('is-valid is-invalid');

    if (!username) { // check if the username field is empty
        return; // exit the function if the username field is empty
    }

    if (username.length < 5) { // check if the username is longer than 5 characters
        $('.customer_username_check').text("Uživatelské jméno musí obsahovat alespoň 5 znaků.").show();
        $(this).removeClass('is-valid').addClass('is-invalid');
        return; // exit the function if the username is too short
    }

    $.ajax({
        url: '/auth/check-username',
        method: 'POST',
        headers: { 'X-CSRFToken': csrf_token },
        data: {'username': username},
        success: function(data) {
            if (data == 'taken' ) {
                $('.customer_username_check').text("Tento uživatel je již zaregistrovaný v naší databázi.").show();
                $('.registration-username-input').removeClass('is-valid').addClass('is-invalid');
            }else {
                $('.registration-username-input').removeClass('is-invalid').addClass('is-valid');
            }
        }
    });
});