
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

$('.add-product-description-input').on('input', function() {
  var product_description = $(this).val();
  $('.add-product-description-input').removeClass('is-valid is-invalid');

  if (product_description.length === 0) {
    $('.add-product-description-validation-text').hide();

  } else if (product_description.length > 50) {
    $('.add-product-description-input').removeClass('is-invalid').addClass('is-valid');
    $('.add-product-description-validation-text').hide();
  } else {
    $('.add-product-description-input').removeClass('is-valid').addClass('is-invalid');
    $('.add-product-description-validation-text').text("Nadpis musí být dlouhý alespoň 50 znaků.").show();
  }
});

// check product price

$('.add-product-price-input').on('input', function() {
  var product_price = $(this).val();
  $('.add-product-price-input').removeClass('is-valid is-invalid');

    if (product_price > 0.1) {
    $('.add-product-price-input').removeClass('is-invalid').addClass('is-valid');
  } else {
    $('.add-product-price-input').removeClass('is-valid').addClass('is-invalid');
  }
});


// check display size

$('.add-product-display-size-input').on('input', function() {
  var product_price = $(this).val();
  $('.add-product-price-input').removeClass('is-valid is-invalid');

    if (product_price > 0.1) {
    $('.add-product-display-size-input').removeClass('is-invalid').addClass('is-valid');
  } else {
    $('.add-product-display-size-input').removeClass('is-valid').addClass('is-invalid');
  }
});

$('.add-product-image-input').on('change', function() {
  var product_image = $(this).val();

  if (product_image) {
    // User has selected a file, do something here
    $('.add-product-image-input').removeClass('is-invalid').addClass('is-valid');
  } else {
    // User has not selected a file, do something here
    $('.add-product-image-input').removeClass('is-valid').addClass('is-invalid');
  }
});

// check if obligated fields are valid all fields will to valid

$('.add-mobile-product-name-input, .add-mobile-product-subheading-input, .add-product-description-input, .add-product-price-input, .add-product-image-input').on('input change', function() {
   var productNameIsValid = $('.add-mobile-product-name-input').hasClass('is-valid');
   var productSubheadingIsValid = $('.add-mobile-product-subheading-input').hasClass('is-valid');
   var productDescriptionIsValid = $('.add-product-description-input').hasClass('is-valid');
   var productPriceIsValid = $('.add-product-price-input').hasClass('is-valid');
   var imageIsValid = $('.add-product-image-input').hasClass('is-valid');
   var obligatedFieldsIsValid = productNameIsValid && productSubheadingIsValid && productDescriptionIsValid && productPriceIsValid && imageIsValid;

  if (obligatedFieldsIsValid) {
    $('.add-product-discount-input, .add-product-stock-input, .add-product-size-input, .add-product-weight-input, .add-product-color-input, .add-product-brand-input, .add-product-category-input, .add-additional-image-input').addClass('is-valid');
  } else {
    $('.add-product-discount-input, .add-product-stock-input, .add-product-size-input, .add-product-weight-input, .add-product-color-input, .add-product-brand-input, .add-product-category-input, .add-additional-image-input').removeClass('is-valid');
  }
});