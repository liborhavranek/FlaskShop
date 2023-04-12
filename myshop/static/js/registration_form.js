// """ Libor Havránek App Copyright (C)  5.4 2023 """

// Helper methods
// This method allowed enter in field only numbers

$('.registration-phone-input, .registration-faktura-zipcode-input, .registration-dodej-zipcode-input, .registration-dodej-phone-input').on('keydown', function(event) {
// Allow only digits and the backspace key
if ((event.keyCode < 48 || event.keyCode > 57) && event.keyCode != 8 && (event.keyCode < 96 || event.keyCode > 105)) {
    event.preventDefault();
}
});

// ----------------------------- email control registration form start---------------------------------------

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

// ----------------------------- email control registration form end---------------------------------------


// ----------------------------- username control registration form start---------------------------------------


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

// ----------------------------- username control registration form end---------------------------------------

// ----------------------------- phonenumber control registration form start---------------------------------------


$('.registration-phone-input').on('input', function() {
  var phone_number = $(this).val();
  $('.registration-phone-input').removeClass('is-valid is-invalid');
  $('.registration-phone-code-input').removeClass('is-valid is-invalid');

  if (phone_number.length === 0) {
    // Do nothing if the phone number has 0 characters
  } else if (phone_number.length === 9) {
    $('.registration-phone-input').removeClass('is-invalid').addClass('is-valid');
    $('.registration-phone-code-input').addClass('is-valid');
  } else {
    $('.registration-phone-input').removeClass('is-valid').addClass('is-invalid');
    $('.registration-phone-code-input').removeClass('is-valid')
  }
});

// ----------------------------- phonenumber control registration form end---------------------------------------

// ----------------------------password control registration start -----------------------------------------


var password_one = '';

$('.registration-password-input').on('input', function(){
$('.registration-password-input').removeClass('is-valid is-invalid');
    password_one = $(this).val();
    if (password_one.length < 8 && password_one.length > 0){
        $('.customer_password_check').text("Heslo musí být dlouhé alespoň 8 znaků.").show();
        $('.registration-password-input').addClass('is-invalid').removeClass('is-valid');
    } else {
        $('.customer_password_check').hide();
        $('.registration-password-input').addClass('is-valid').removeClass('is-invalid');
    }
});

$('.registration-confirm-password-input').on('input', function(){
$('.registration-confirm-password-input').removeClass('is-valid is-invalid');
    var password_two = $(this).val();
    if (password_one === password_two){
        $('.customer_confirm_password_check').hide();
        $('.registration-confirm-password-input').addClass('is-valid').removeClass('is-invalid');
    } else {
        $('.customer_confirm_password_check').text("Hesla se musí shodovat.").show();
        $('.registration-confirm-password-input').addClass('is-invalid').removeClass('is-valid');
    }
});


// ----------------------------password control registration end -----------------------------------------


//------------------------------faktura first name start------------------------------------------


$(".registration-faktura-firstname-input").on('input', function() {
  var faktura_first_name = $(this).val();
  if (faktura_first_name.length > 1) {
    $('.registration-faktura-firstname-input').addClass('is-valid');
  } else {
    $('.registration-faktura-firstname-input').removeClass('is-valid');
  }
});

// ---------------------------- faktura first name end --------------------------------------------------


//------------------------------faktura last name start------------------------------------------


$(".registration-faktura-lastname-input").on('input', function() {
  var faktura_last_name = $(this).val();
  if (faktura_last_name.length > 1) {
    $('.registration-faktura-lastname-input').addClass('is-valid');
  } else {
    $('.registration-faktura-lastname-input').removeClass('is-valid');
  }
});

// ---------------------------- faktura last name end --------------------------------------------------

// ---------------------------- faktura city start --------------------------------------------------

$(".registration-faktura-city-input").on('input', function() {
  var faktura_city_name = $(this).val();
  if (faktura_city_name.length > 1) {
    $('.registration-faktura-city-input').addClass('is-valid');
  } else {
    $('.registration-faktura-city-input').removeClass('is-valid');
  }
});

// ---------------------------- faktura city end --------------------------------------------------

// ---------------------------- faktura street start --------------------------------------------------

$(".registration-faktura-street-input").on('input', function() {
  var faktura_street_name = $(this).val();
  if (faktura_street_name.length > 1) {
    $('.registration-faktura-street-input').addClass('is-valid');
  } else {
    $('.registration-faktura-street-input').removeClass('is-valid');
  }
});

// ---------------------------- faktura street end --------------------------------------------------


// ---------------------------- faktura zipcode start --------------------------------------------------

$(".registration-faktura-zipcode-input").on('input', function() {
  var faktura_zipcode = $(this).val();
  if (faktura_zipcode.length === 0) {
    $('.registration-faktura-zipcode-input').removeClass('is-invalid is-valid');
  } else if (faktura_zipcode.length != 5) {
    $('.registration-faktura-zipcode-input').addClass('is-invalid').removeClass('is-valid');
  } else {
    $('.registration-faktura-zipcode-input').removeClass('is-invalid').addClass('is-valid');
  }
});
// ---------------------------- faktura zipcode end --------------------------------------------------

//------------------------------dodej first name start------------------------------------------


$(".registration-dodej-firstname-input").on('input', function() {
  var dodej_first_name = $(this).val();
  if (dodej_first_name.length > 1) {
    $('.registration-dodej-firstname-input').addClass('is-valid');
  } else {
    $('.registration-dodej-firstname-input').removeClass('is-valid');
  }
});

// ---------------------------- dodej first name end --------------------------------------------------

//------------------------------dodej last name start------------------------------------------


$(".registration-dodej-lastname-input").on('input', function() {
  var dodej_last_name = $(this).val();
  if (dodej_last_name.length > 1) {
    $('.registration-dodej-lastname-input').addClass('is-valid');
  } else {
    $('.registration-dodej-lastname-input').removeClass('is-valid');
  }
});

// ---------------------------- dodej last name end --------------------------------------------------

//------------------------------dodej company start------------------------------------------


$(".registration-dodej-company-input").on('input', function() {
  var dodej_company_name = $(this).val();
  if (dodej_company_name.length > 1) {
    $('.registration-dodej-company-input').addClass('is-valid');
  } else {
    $('.registration-dodej-company-input').removeClass('is-valid');
  }
});

// ---------------------------- dodej company end --------------------------------------------------


//------------------------------dodej city start------------------------------------------


$(".registration-dodej-city-input").on('input', function() {
  var dodej_city_name = $(this).val();
  if (dodej_city_name.length > 1) {
    $('.registration-dodej-city-input').addClass('is-valid');
  } else {
    $('.registration-dodej-city-input').removeClass('is-valid');
  }
});

// ---------------------------- dodej city end --------------------------------------------------

//------------------------------dodej city start------------------------------------------


$(".registration-dodej-street-input").on('input', function() {
  var dodej_street = $(this).val();
  if (dodej_street.length > 1) {
    $('.registration-dodej-street-input').addClass('is-valid');
  } else {
    $('.registration-dodej-street-input').removeClass('is-valid');
  }
});

// ---------------------------- dodej city end --------------------------------------------------


// ---------------------------- dodej zipcode start --------------------------------------------------

$(".registration-dodej-zipcode-input").on('input', function() {
  var dodej_zipcode = $(this).val();
  if (dodej_zipcode.length === 0) {
    // Field is empty, so remove validation
    $('.registration-dodej-zipcode-input').removeClass('is-invalid is-valid');
  } else if (dodej_zipcode.length != 5) {
    // Field is not empty but not valid, so add invalid class and remove valid class
    $('.registration-dodej-zipcode-input').addClass('is-invalid').removeClass('is-valid');
  } else {
    // Field is valid, so add valid class and remove invalid class
    $('.registration-dodej-zipcode-input').removeClass('is-invalid').addClass('is-valid');
  }
});
// ---------------------------- dodej zipcode end --------------------------------------------------

//------------------------------dodej info start------------------------------------------

$(".registration-dodej-info-input").on('input', function() {
  var dodej_info = $(this).val();
  if (dodej_info.length > 1) {
    $('.registration-dodej-info-input').addClass('is-valid');
  } else {
    $('.registration-dodej-info-input').removeClass('is-valid');
  }
});

// ---------------------------- dodej info end --------------------------------------------------


// ----------------------------- phonenumber control registration form start---------------------------------------

$('.registration-dodej-phone-input').on('input', function() {
  var phone_number = $(this).val();
  $('.registration-dodej-phone-input').removeClass('is-valid is-invalid');
  $('.registration-dodej-phone-code-input').removeClass('is-valid is-invalid');

  if (phone_number.length === 0) {
    // Do nothing if the phone number has 0 characters
  } else if (phone_number.length === 9) {
    $('.registration-dodej-phone-input').removeClass('is-invalid').addClass('is-valid');
    $('.registration-dodej-phone-code-input').addClass('is-valid');
  } else {
    $('.registration-dodej-phone-input').removeClass('is-valid').addClass('is-invalid');
    $('.registration-dodej-phone-code-input').removeClass('is-valid')
  }
});

// ----------------------------- phonenumber control registration form end---------------------------------------
