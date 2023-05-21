$('.add-notebook-hdd-capacity-input').hide();
$('.add-notebook-hdd-capacity-label').hide();

    // Listen for changes in the HDD checkbox state
    $('.add-notebook-hdd-disk-input').change(function() {
        if ($(this).is(':checked')) {
            // Checkbox is checked, show the HDD capacity field
            $('.add-notebook-hdd-capacity-input').show();
            $('.add-notebook-hdd-capacity-label').show();
        } else {
            // Checkbox is not checked, hide the HDD capacity field
            $('.add-notebook-hdd-capacity-input').hide();
            $('.add-notebook-hdd-capacity-label').hide();
        }
    });


$('.add-notebook-ssd-capacity-input').hide();
$('.add-notebook-ssd-capacity-label').hide();

    // Listen for changes in the HDD checkbox state
    $('.add-notebook-ssd-disk-input').change(function() {
        if ($(this).is(':checked')) {
            // Checkbox is checked, show the HDD capacity field
            $('.add-notebook-ssd-capacity-input').show();
            $('.add-notebook-ssd-capacity-label').show();
        } else {
            // Checkbox is not checked, hide the HDD capacity field
            $('.add-notebook-ssd-capacity-input').hide();
            $('.add-notebook-ssd-capacity-label').hide();
        }
    });


  $('.add-notebook-light-keyboard-input').change(function() {
    if ($(this).is(':checked')) {
      $('.add-notebook-product-light-keyboard-text').text('ANO').css('color', 'green');
    } else {
      $('.add-notebook-product-light-keyboard-text').text('NE').css('color', 'red');
    }
  });

  $('.add-notebook-num-keyboard-input').change(function() {
    if ($(this).is(':checked')) {
      $('.add-notebook-product-num-keyboard-text').text('ANO').css('color', 'green');
    } else {
      $('.add-notebook-product-num-keyboard-text').text('NE').css('color', 'red');
    }
  });

  $('.add-notebook-touch-screen-input').change(function() {
    if ($(this).is(':checked')) {
      $('.add-notebook-product-touch-screen-text').text('ANO').css('color', 'green');
    } else {
      $('.add-notebook-product-touch-screen-text').text('NE').css('color', 'red');
    }
  });

  $('.add-notebook-finger-print-reader-input').change(function() {
    if ($(this).is(':checked')) {
      $('.add-notebook-product-fingerprint-reader-text').text('ANO').css('color', 'green');
    } else {
      $('.add-notebook-product-fingerprint-reader-text').text('NE').css('color', 'red');
    }
  });

  $('.add-notebook-memory-card-reader-input').change(function() {
    if ($(this).is(':checked')) {
      $('.add-notebook-product-memory-card-reader-text').text('ANO').css('color', 'green');
    } else {
      $('.add-notebook-product-memory-card-reader-text').text('NE').css('color', 'red');
    }
  });

  $('.add-notebook-usb-c-charging-input').change(function() {
    if ($(this).is(':checked')) {
      $('.add-notebook-product-usb-c-charging-text').text('ANO').css('color', 'green');
    } else {
      $('.add-notebook-product-usb-c-charging-text').text('NE').css('color', 'red');
    }
  });

  $('.add-notebook-audio-jack-input').change(function() {
    if ($(this).is(':checked')) {
      $('.add-notebook-product-audio-jack-text').text('ANO').css('color', 'green');
    } else {
      $('.add-notebook-product-audio-jack-text').text('NE').css('color', 'red');
    }
  });

  $('.add-notebook-usb-30-input').change(function() {
    if ($(this).is(':checked')) {
      $('.add-notebook-product-usb-30-text').text('ANO').css('color', 'green');
    } else {
      $('.add-notebook-product-usb-30-text').text('NE').css('color', 'red');
    }
  });

  $('.add-notebook-usb-20-input').change(function() {
    if ($(this).is(':checked')) {
      $('.add-notebook-product-usb-20-text').text('ANO').css('color', 'green');
    } else {
      $('.add-notebook-product-usb-20-text').text('NE').css('color', 'red');
    }
  });


  $('.add-notebook-cd-dvd-drive-input').change(function() {
    if ($(this).is(':checked')) {
      $('.add-notebook-product-cd-dvd-drive-text').text('ANO').css('color', 'green')
         } else {
      $('.add-notebook-product-cd-dvd-drive-text').text('NE').css('color', 'red');
    }
  });


    $('.add-notebook-light-keyboard-input').change();
    $('.add-notebook-product-num-keyboard-input').change();
    $('.add-notebook-touch-screen-input').change();
    $('.add-notebook-finger-print-reader-input').change();
    $('.add-notebook-memory-card-reader-input').change();
    $('.add-notebook-usb-c-charging-input').change();
    $('.add-notebook-audio-jack-input').change();
    $('.add-notebook-usb-30-input').change();
    $('.add-notebook-usb-20-input').change();
    $('.add-notebook-cd-dvd-drive-input').change();

//    add notebook input

    $('.add-notebook-product-name-input').on('input', function() {
    var product = $(this).val();
    var csrf_token = $('input[name=csrf_token]').val();

        if (product.charAt(0) === product.charAt(0).toLowerCase()) {
        product = product.charAt(0).toUpperCase() + product.slice(1);
        $(this).val(product);
    }

        if (product.length == 0) {
        $('.add-notebook-product-validation-text').hide();
        $(this).removeClass('is-valid').removeClass('is-invalid');
        return;
    }

    if (product.length < 2) {
        $('.add-notebook-product-validation-text').hide();
        $(this).removeClass('is-valid').addClass('is-invalid');
        return;
    }

    $.ajax({
        url: '/products/check-product',
        method: 'POST',
        data: {'product_name': product, 'csrf_token': csrf_token},
        success: function(data) {
            if (data == 'taken') {
                $('.add-notebook-product-validation-text').text("Tento produkt je již zaregistrovaný v naší databázi.").show();
                $('.add-notebook-product-name-input').removeClass('is-valid').addClass('is-invalid');
            } else {
                $('.add-notebook-product-validation-text').hide();
                $('.add-notebook-product-name-input').removeClass('is-invalid').addClass('is-valid');
            }
        }
    });
});


// check subheading length

$('.add-notebook-product-subheading-input').on('input', function() {
  var product_subheading = $(this).val();
  $('.add-notebook-product-subheading-input').removeClass('is-valid is-invalid');

  if (product_subheading.length === 0) {
    $('.add-notebook-product-subheading-validation-text').hide();

  } else if (product_subheading.length > 20) {
    $('.add-notebook-product-subheading-input').removeClass('is-invalid').addClass('is-valid');
    $('.add-notebook-product-subheading-validation-text').hide();
  } else {
    $('.add-notebook-product-subheading-input').removeClass('is-valid').addClass('is-invalid');
    $('.add-notebook-product-subheading-validation-text').text("Podnadpis musí být dlouhý alespoň 20 znaků.").show();
  }
});


// check description length

$('.add-notebook-product-description-input').on('input', function() {
  var product_description = $(this).val();
  $('.add-notebook-product-description-input').removeClass('is-valid is-invalid');

  if (product_description.length === 0) {
    $('.add-notebook-product-description-validation-text').hide();

  } else if (product_description.length > 50) {
    $('.add-notebook-product-description-input').removeClass('is-invalid').addClass('is-valid');
    $('.add-notebook-product-description-validation-text').hide();
  } else {
    $('.add-notebook-product-description-input').removeClass('is-valid').addClass('is-invalid');
    $('.add-notebook-product-description-validation-text').text("Nadpis musí být dlouhý alespoň 50 znaků.").show();
  }
});


// check product price

$('.add-notebook-product-price-input').on('input', function() {
  var product_price = $(this).val();
  $('.add-notebook-product-price-input').removeClass('is-valid is-invalid');

    if (product_price > 0.1) {
    $('.add-notebook-product-price-input').removeClass('is-invalid').addClass('is-valid');
  } else {
    $('.add-notebook-product-price-input').removeClass('is-valid').addClass('is-invalid');
  }
});

  $('.add-notebook-product-display-resolution-input').change(function() {
      $(this).removeClass('is-invalid').addClass('is-valid');
  });

// ceck mobile display size

$('.add-notebook-product-display-size-input').on('input', function() {
  var display_size = $(this).val();
  $('.add-notebook-product-display-size-input').removeClass('is-valid is-invalid');

    if (display_size > 0.1) {
    $('.add-notebook-product-display-size-input').removeClass('is-invalid').addClass('is-valid');
  } else {
    $('.add-notebook-product-display-size-input').removeClass('is-valid').addClass('is-invalid');
  }
});

// check operating memory

$('.add-notebook-product-operating-memory-input').on('input', function() {
  var operating_memory = $(this).val();
  $('.add-notebook-product-operating-memory-input').removeClass('is-valid is-invalid');

    if (operating_memory > 0.1) {
    $('.add-notebook-product-operating-memory-input').removeClass('is-invalid').addClass('is-valid');
  } else {
    $('.add-notebook-product-operating-memory-input').removeClass('is-valid').addClass('is-invalid');
  }
});

// check memory

$('.add-notebook-display-frequency-input').on('input', function() {
  var memory = $(this).val();
  $('.add-notebook-display-frequency-input').removeClass('is-valid is-invalid');

    if (memory > 0.1) {
    $('.add-notebook-display-frequency-input').removeClass('is-invalid').addClass('is-valid');
  } else {
    $('.add-notebook-display-frequency-input').removeClass('is-valid').addClass('is-invalid');
  }
});


$('.add-notebook-display-nits-input').on('input', function() {
  var memory = $(this).val();
  $('.add-notebook-display-nits-input').removeClass('is-valid is-invalid');

    if (memory > 0.1) {
    $('.add-notebook-display-nits-input').removeClass('is-invalid').addClass('is-valid');
  } else {
    $('.add-notebook-display-nits-input').removeClass('is-valid').addClass('is-invalid');
  }
});

$('.add-notebook-processor-cores-input').on('input', function() {
  var memory = $(this).val();
  $('.add-notebook-processor-cores-input').removeClass('is-valid is-invalid');

    if (memory > 0.1) {
    $('.add-notebook-processor-cores-input').removeClass('is-invalid').addClass('is-valid');
  } else {
    $('.add-notebook-processor-cores-input').removeClass('is-valid').addClass('is-invalid');
  }
});

$('.add-notebook-graphics-card-memory-input').on('input', function() {
  var memory = $(this).val();
  $('.add-notebook-graphics-card-memory-input').removeClass('is-valid is-invalid');

    if (memory > 0.1) {
    $('.add-notebook-graphics-card-memory-input').removeClass('is-invalid').addClass('is-valid');
  } else {
    $('.add-notebook-graphics-card-memory-input').removeClass('is-valid').addClass('is-invalid');
  }
});

$('.add-notebook-product-battery-capacity-input').on('input', function() {
  var memory = $(this).val();
  $('.add-notebook-product-battery-capacity-input').removeClass('is-valid is-invalid');

    if (memory > 0.1) {
    $('.add-notebook-product-battery-capacity-input').removeClass('is-invalid').addClass('is-valid');
  } else {
    $('.add-notebook-product-battery-capacity-input').removeClass('is-valid').addClass('is-invalid');
  }
});


$('.add-notebook-usb-ports-input').on('input', function() {
  var memory = $(this).val();
  $('.add-notebook-usb-ports-input').removeClass('is-valid is-invalid');

    if (memory > 0.1) {
    $('.add-notebook-usb-ports-input').removeClass('is-invalid').addClass('is-valid');
  } else {
    $('.add-notebook-usb-ports-input').removeClass('is-valid').addClass('is-invalid');
  }
});

$('.add-notebook-hdmi-ports-input').on('input', function() {
  var memory = $(this).val();
  $('.add-notebook-hdmi-ports-input').removeClass('is-valid is-invalid');

    if (memory > 0.1) {
    $('.add-notebook-hdmi-ports-input').removeClass('is-invalid').addClass('is-valid');
  } else {
    $('.add-notebook-hdmi-ports-input').removeClass('is-valid').addClass('is-invalid');
  }
});


$('.add-notebook-product-image-input').on('change', function() {
  var product_image = $(this).val();

  if (product_image) {
    // User has selected a file, do something here
    $('.add-notebook-product-image-input').removeClass('is-invalid').addClass('is-valid');
  } else {
    // User has not selected a file, do something here
    $('.add-notebook-product-image-input').removeClass('is-valid').addClass('is-invalid');
  }
});


$('.add-notebook-additional-image-input').on('change', function() {
  var product_image = $(this).val();

  if (product_image) {
    // User has selected a file, do something here
    $('.add-notebook-additional-image-input').removeClass('is-invalid').addClass('is-valid');
  } else {
    // User has not selected a file, do something here
    $('.add-notebook-additional-image-input').removeClass('is-valid').addClass('is-invalid');
  }
});


  $('.add-notebook-operating-system-input').change(function() {
      $(this).removeClass('is-invalid').addClass('is-valid');
  });


  $('.add-notebook-display-resolution-input').change(function() {
      $(this).removeClass('is-invalid').addClass('is-valid');
  });

   $('.add-notebook-display-type-input').change(function() {
      $(this).removeClass('is-invalid').addClass('is-valid');
  });

    $('.add-notebook-processor-input').change(function() {
      $(this).removeClass('is-invalid').addClass('is-valid');
  });


  $('.add-notebook-graphics-card-input').change(function() {
      $(this).removeClass('is-invalid').addClass('is-valid');
  });

   $('.add-notebook-product-construction-input').change(function() {
      $(this).removeClass('is-invalid').addClass('is-valid');
  });




$('.add-notebook-product-name-input, .add-notebook-product-subheading-input, .add-mobile-notebook-description-input, .add-notebook-product-price-input, .add-notebook-product-display-size-input, .add-notebook-product-operating-memory-input, .add-notebook-product-image-input').on('input change', function() {
   var productNameIsValid = $('.add-notebook-product-name-input').hasClass('is-valid');
   var productSubheadingIsValid = $('.add-notebook-product-subheading-input').hasClass('is-valid');
   var productDescriptionIsValid = $('.add-notebook-product-description-input').hasClass('is-valid');
   var productPriceIsValid = $('.add-notebook-product-price-input').hasClass('is-valid');
   var productDisplaySizeIsValid = $('.add-notebook-product-display-size-input').hasClass('is-valid');
   var productOperatingMemoryIsValid = $('.add-notebook-product-operating-memory-input').hasClass('is-valid');
   var imageIsValid = $('.add-notebook-product-image-input').hasClass('is-valid');
   var obligatedFieldsIsValid = productNameIsValid && productSubheadingIsValid && productDescriptionIsValid && productPriceIsValid && productDisplaySizeIsValid && productOperatingMemoryIsValid && imageIsValid;

  if (obligatedFieldsIsValid) {
    $('.add-notebook-product-discount-input, .add-notebook-product-stock-input, .add-notebook-product-sizes-input, .add-notebook-weight-input, .add-notebook-product-color-input, .add-notebook-product-brand-input, .add-notebook-product-category-input, .add-notebook-display-resolution-input, .add-notebook-display-frequency-input , .add-notebook-display-nits-input, .add-notebook-display-type-input, .add-notebook-processor-input, .add-notebook-processor-cores-input, .add-notebook-graphics-card-input, .add-notebook-graphics-card-memory-input, .add-notebook-operating-system-input, .add-notebook-product-construction-input, .add-notebook-product-battery-capacity-input, .add-notebook-usb-ports-input, .add-notebook-hdmi-ports-input, .add-notebook-additional-image-input').addClass('is-valid');
  } else {
    $('.add-notebook-product-discount-input, .add-notebook-product-stock-input, .add-notebook-product-sizes-input, .add-notebook-weight-input, .add-notebook-product-color-input, .add-notebook-product-brand-input, .add-notebook-product-category-input, .add-notebook-display-resolution-input, .add-notebook-display-frequency-input , .add-notebook-display-nits-input, .add-notebook-display-type-input, .add-notebook-processor-input, .add-notebook-processor-cores-input, .add-notebook-graphics-card-input, .add-notebook-graphics-card-memory-input, .add-notebook-operating-system-input, .add-notebook-product-construction-input, .add-notebook-product-battery-capacity-input, .add-notebook-usb-ports-input, .add-notebook-hdmi-ports-input, .add-notebook-additional-image-input').removeClass('is-valid');
  }
});