
$('.add-brand-input, .edit-brand-input').on('input', function() {
    var brand = $(this).val();
    var csrf_token = $('input[name=csrf_token]').val();

        if (brand.charAt(0) === brand.charAt(0).toLowerCase()) {
        brand = brand.charAt(0).toUpperCase() + brand.slice(1);
        $(this).val(brand);
    }

        if (brand.length == 0) {
        $('.add-brand-validation-text, .edit-brand-validation-text').hide();
        $(this).removeClass('is-valid').removeClass('is-invalid');
        return;
    }

    if (brand.length < 2) {
        $('.add-brand-validation-text, .edit-brand-validation-text').hide();
        $(this).removeClass('is-valid').addClass('is-invalid');
        return;
    }

    $.ajax({
        url: '/products/check-brand',
        method: 'POST',
        data: {'brand_name': brand, 'csrf_token': csrf_token},
        success: function(data) {
            if (data == 'taken') {
                $('.add-brand-validation-text, .edit-brand-validation-text').text("Tato značka je již zaregistrovaná v naší databázi.").show();
                $('.add-brand-input').removeClass('is-valid').addClass('is-invalid');
            } else {
                $('.add-brand-validation-text, .edit-brand-validation-text').hide();
                $('.add-brand-input, .edit-brand-input').removeClass('is-invalid').addClass('is-valid');
            }
        }
    });
});



$('.add-category-input, .edit-category-input').on('input', function() {
    var category = $(this).val();
    var csrf_token = $('input[name=csrf_token]').val();

        if (category.charAt(0) === category.charAt(0).toLowerCase()) {
        category = category.charAt(0).toUpperCase() + category.slice(1);
        $(this).val(category);
    }

        if (category.length == 0) {
        $('.add-category-validation-text, .edit-category-validation-text').hide();
        $(this).removeClass('is-valid').removeClass('is-invalid');
        return;
    }

    if (category.length < 2) {
        $('.add-category-validation-text, .edit-category-validation-text').hide();
        $(this).removeClass('is-valid').addClass('is-invalid');
        return;
    }

    $.ajax({
        url: '/products/check-category',
        method: 'POST',
        data: {'category_name': category, 'csrf_token': csrf_token},
        success: function(data) {
            if (data == 'taken') {
                $('.add-category-validation-text, .edit-category-validation-text').text("Tato značka je již zaregistrovaná v naší databázi.").show();
                $('.add-category-input').removeClass('is-valid').addClass('is-invalid');
            } else {
                $('.add-category-validation-text, .edit-category-validation-text').hide();
                $('.add-category-input, .edit-category-input').removeClass('is-invalid').addClass('is-valid');
            }
        }
    });
});


function updateMainImage(image) {
  document.querySelector('.main-image').src = image.src;
}

// check if product name is aviable

$('.add-mobile-product-name-input').on('input', function() {
    var product = $(this).val();
    var csrf_token = $('input[name=csrf_token]').val();

        if (product.charAt(0) === product.charAt(0).toLowerCase()) {
        product = product.charAt(0).toUpperCase() + product.slice(1);
        $(this).val(product);
    }

        if (product.length == 0) {
        $('.add-mobile-product-validation-text').hide();
        $(this).removeClass('is-valid').removeClass('is-invalid');
        return;
    }

    if (product.length < 2) {
        $('.add-mobile-product-validation-text').hide();
        $(this).removeClass('is-valid').addClass('is-invalid');
        return;
    }

    $.ajax({
        url: '/products/check-product',
        method: 'POST',
        data: {'product_name': product, 'csrf_token': csrf_token},
        success: function(data) {
            if (data == 'taken') {
                $('.add-mobile-product-validation-text').text("Tento produkt je již zaregistrovaný v naší databázi.").show();
                $('.add-mobile-product-name-input').removeClass('is-valid').addClass('is-invalid');
            } else {
                $('.add-mobile-product-validation-text').hide();
                $('.add-mobile-product-name-input').removeClass('is-invalid').addClass('is-valid');
            }
        }
    });
});

// check subheading length

$('.add-mobile-product-subheading-input').on('input', function() {
  var product_subheading = $(this).val();
  $('.add-mobile-product-subheading-input').removeClass('is-valid is-invalid');

  if (product_subheading.length === 0) {
    $('.add-mobile-product-subheading-validation-text').hide();

  } else if (product_subheading.length > 20) {
    $('.add-mobile-product-subheading-input').removeClass('is-invalid').addClass('is-valid');
    $('.add-mobile-product-subheading-validation-text').hide();
  } else {
    $('.add-mobile-product-subheading-input').removeClass('is-valid').addClass('is-invalid');
    $('.add-mobile-product-subheading-validation-text').text("Podnadpis musí být dlouhý alespoň 20 znaků.").show();
  }
});

// check description length

$('.add-mobile-product-description-input').on('input', function() {
  var product_description = $(this).val();
  $('.add-mobile-product-description-input').removeClass('is-valid is-invalid');

  if (product_description.length === 0) {
    $('.add-mobile-product-description-validation-text').hide();

  } else if (product_description.length > 50) {
    $('.add-mobile-product-description-input').removeClass('is-invalid').addClass('is-valid');
    $('.add-mobile-product-description-validation-text').hide();
  } else {
    $('.add-mobile-product-description-input').removeClass('is-valid').addClass('is-invalid');
    $('.add-mobile-product-description-validation-text').text("Nadpis musí být dlouhý alespoň 50 znaků.").show();
  }
});

// check product price

$('.add-mobile-product-price-input').on('input', function() {
  var product_price = $(this).val();
  $('.add-mobile-product-price-input').removeClass('is-valid is-invalid');

    if (product_price > 0.1) {
    $('.add-mobile-product-price-input').removeClass('is-invalid').addClass('is-valid');
  } else {
    $('.add-mobile-product-price-input').removeClass('is-valid').addClass('is-invalid');
  }
});

  $('.add-mobile-product-display-resolution-input').change(function() {
      $(this).removeClass('is-invalid').addClass('is-valid');
  });

// ceck mobile display size

$('.add-mobile-product-display-size-input').on('input', function() {
  var display_size = $(this).val();
  $('.add-mobile-product-display-size-input').removeClass('is-valid is-invalid');

    if (display_size > 0.1) {
    $('.add-mobile-product-display-size-input').removeClass('is-invalid').addClass('is-valid');
  } else {
    $('.add-mobile-product-display-size-input').removeClass('is-valid').addClass('is-invalid');
  }
});


// check operating memory

$('.add-mobile-product-operating-memory-input').on('input', function() {
  var operating_memory = $(this).val();
  $('.add-mobile-product-operating-memory-input').removeClass('is-valid is-invalid');

    if (operating_memory > 0.1) {
    $('.add-mobile-product-operating-memory-input').removeClass('is-invalid').addClass('is-valid');
  } else {
    $('.add-mobile-product-operating-memory-input').removeClass('is-valid').addClass('is-invalid');
  }
});

// check memory

$('.add-mobile-product-memory-input').on('input', function() {
  var memory = $(this).val();
  $('.add-mobile-product-memory-input').removeClass('is-valid is-invalid');

    if (memory > 0.1) {
    $('.add-mobile-product-memory-input').removeClass('is-invalid').addClass('is-valid');
  } else {
    $('.add-mobile-product-memory-input').removeClass('is-valid').addClass('is-invalid');
  }
});

  $('.add-mobile-product-operating-system-input').change(function() {
      $(this).removeClass('is-invalid').addClass('is-valid');
  });

  $('.add-mobile-product-battery-capacity-input').on('input', function() {
  var battery_capacity = $(this).val();
  $('.add-mobile-product-battery-capacity-input').removeClass('is-valid is-invalid');

    if (battery_capacity > 0.1) {
    $('.add-mobile-product-battery-capacity-input').removeClass('is-invalid').addClass('is-valid');
  } else {
    $('.add-mobile-product-battery-capacity-input').removeClass('is-valid').addClass('is-invalid');
  }
});

  $('.add-mobile-product-back-camera-input').on('input', function() {
  var back_camera = $(this).val();
  $('.add-mobile-product-back-camera-input').removeClass('is-valid is-invalid');

    if (back_camera > 0.1) {
    $('.add-mobile-product-back-camera-input').removeClass('is-invalid').addClass('is-valid');
  } else {
    $('.add-mobile-product-back-camera-input').removeClass('is-valid').addClass('is-invalid');
  }
});

  $('.add-mobile-product-front-camera-input').on('input', function() {
  var front_camera = $(this).val();
  $('.add-mobile-product-front-camera-input').removeClass('is-valid is-invalid');

    if (front_camera > 0.1) {
    $('.add-mobile-product-front-camera-input').removeClass('is-invalid').addClass('is-valid');
  } else {
    $('.add-mobile-product-front-camera-input').removeClass('is-valid').addClass('is-invalid');
  }
});

 $('.add-mobile-product-processor-input').change(function() {
      $(this).removeClass('is-invalid').addClass('is-valid');
  });

   $('.add-mobile-product-processor-cores-input').on('input', function() {
  var cores = $(this).val();
  $('.add-mobile-product-processor-cores-input').removeClass('is-valid is-invalid');

    if (cores > 0.1) {
    $('.add-mobile-product-processor-cores-input').removeClass('is-invalid').addClass('is-valid');
  } else {
    $('.add-mobile-product-processor-cores-input').removeClass('is-valid').addClass('is-invalid');
  }
});

   $('.add-mobile-product-memory-card-slot-input').change(function() {
    if ($(this).is(':checked')) {
      $('.add-mobile-product-memory-card-slot-text').text('ANO').css('color', 'green');
    } else {
      $('.add-mobile-product-memory-card-slot-text').text('NE').css('color', 'red');
    }
  });

$('.add-mobile-product-wifi-input').change(function() {
    if ($(this).is(':checked')) {
      $('.add-mobile-product-wifi-text').text('ANO').css('color', 'green');
    } else {
      $('.add-mobile-product-wifi-text').text('NE').css('color', 'red');
    }
  });

$('.add-mobile-product-bluetooth-input').change(function() {
    if ($(this).is(':checked')) {
      $('.add-mobile-product-bluetooth-text').text('ANO').css('color', 'green');
    } else {
      $('.add-mobile-product-bluetooth-text').text('NE').css('color', 'red');
    }
  });

$('.add-mobile-product-nfc-input').change(function() {
    if ($(this).is(':checked')) {
      $('.add-mobile-product-nfc-text').text('ANO').css('color', 'green');
    } else {
      $('.add-mobile-product-nfc-text').text('NE').css('color', 'red');
    }
  });

$('.add-mobile-product-esim-input').change(function() {
    if ($(this).is(':checked')) {
      $('.add-mobile-product-esim-text').text('ANO').css('color', 'green');
    } else {
      $('.add-mobile-product-esim-text').text('NE').css('color', 'red');
    }
  });

$('.add-mobile-product-face-id-input').change(function() {
    if ($(this).is(':checked')) {
      $('.add-mobile-product-face-id-text').text('ANO').css('color', 'green');
    } else {
      $('.add-mobile-product-face-id-text').text('NE').css('color', 'red');
    }
  });

$('.add-mobile-product-touch-screen-input').change(function() {
  if ($(this).is(':checked')) {
    $('.add-mobile-product-touch-screen-text').text('ANO').css('color', 'green');
  } else {
    $('.add-mobile-product-touch-screen-text').text('NE').css('color', 'red');
  }
});

$('.add-mobile-product-convertible-input').change(function() {
  if ($(this).is(':checked')) {
    $('.add-mobile-product-convertible-text').text('ANO').css('color', 'green');
  } else {
    $('.add-mobile-product-convertible-text').text('NE').css('color', 'red');
  }
});

// Trigger the change event on page load to update the initial state
$('.add-mobile-product-touch-screen-input').change();
$('.add-mobile-product-convertible-input').change();
$('.add-mobile-product-face-id-input').change();
$('.add-mobile-product-esim-input').change();
$('.add-mobile-product-nfc-input').change();
$('.add-mobile-product-bluetooth-input').change();
$('.add-mobile-product-wifi-input').change();
$('.add-mobile-product-memory-card-slot-input').change();


$('.add-mobile-product-image-input').on('change', function() {
  var product_image = $(this).val();

  if (product_image) {
    // User has selected a file, do something here
    $('.add-mobile-product-image-input').removeClass('is-invalid').addClass('is-valid');
  } else {
    // User has not selected a file, do something here
    $('.add-mobile-product-image-input').removeClass('is-valid').addClass('is-invalid');
  }
});


// check if obligated fields are valid all fields will to valid

$('.add-mobile-product-name-input, .add-mobile-product-subheading-input, .add-mobile-product-description-input, .add-mobile-product-price-input, .add-mobile-product-display-size-input, .add-mobile-product-image-input').on('input change', function() {
   var productNameIsValid = $('.add-mobile-product-name-input').hasClass('is-valid');
   var productSubheadingIsValid = $('.add-mobile-product-subheading-input').hasClass('is-valid');
   var productDescriptionIsValid = $('.add-mobile-product-description-input').hasClass('is-valid');
   var productPriceIsValid = $('.add-mobile-product-price-input').hasClass('is-valid');
   var productDisplaySizeIsValid = $('.add-mobile-product-display-size-input').hasClass('is-valid');
   var productOperatingMemoryIsValid = $('.add-mobile-product-operating-memory-input').hasClass('is-valid');
   var productMemoryIsValid = $('.add-mobile-product-memory-input').hasClass('is-valid');
   var imageIsValid = $('.add-mobile-product-image-input').hasClass('is-valid');
   var obligatedFieldsIsValid = productNameIsValid && productSubheadingIsValid && productDescriptionIsValid && productPriceIsValid && productDisplaySizeIsValid && productOperatingMemoryIsValid && productMemoryIsValid && imageIsValid;

  if (obligatedFieldsIsValid) {
    $('.add-mobile-product-discount-input, .add-mobile-product-stock-input, .add-mobile-product-sizes-input, .add-product-weight-input, .add-mobile-product-color-input, .add-mobile-product-brand-input, .add-mobile-product-category-input, .add-mobile-product-display-resolution-input, .add-mobile-product-operating-system-input, .add-mobile-product-battery-capacity-input, .add-mobile-product-back-camera-input, .add-mobile-product-front-camera-input, .add-mobile-product-processor-input, .add-mobile-product-processor-cores-input, .add-mobile-additional-image-input').addClass('is-valid');
  } else {
    $('.add-mobile-product-discount-input, .add-mobile-product-stock-input, .add-mobile-product-sizes-input, .add-product-weight-input, .add-mobile-product-color-input, .add-mobile-product-brand-input, .add-mobile-product-category-input, .add-mobile-product-display-resolution-input, .add-mobile-product-operating-system-input, .add-mobile-product-battery-capacity-input, .add-mobile-product-back-camera-input, .add-mobile-product-front-camera-input, .add-mobile-product-processor-input, .add-mobile-product-processor-cores-input, .add-mobile-additional-image-input').removeClass('is-valid');
  }
});
