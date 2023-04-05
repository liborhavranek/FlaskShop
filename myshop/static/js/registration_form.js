// """ Libor Havránek App Copyright (C)  5.4 2023 """


$('#email').on('input', function() {
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