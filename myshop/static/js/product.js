
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

$('.add-product-input').on('input', function() {
    var product = $(this).val();
    var csrf_token = $('input[name=csrf_token]').val();

        if (product.charAt(0) === product.charAt(0).toLowerCase()) {
        product = product.charAt(0).toUpperCase() + product.slice(1);
        $(this).val(product);
    }

        if (product.length == 0) {
        $('.add-product-validation-text').hide();
        $(this).removeClass('is-valid').removeClass('is-invalid');
        return;
    }

    if (product.length < 2) {
        $('.add-product-validation-text').hide();
        $(this).removeClass('is-valid').addClass('is-invalid');
        return;
    }

    $.ajax({
        url: '/products/check-product',
        method: 'POST',
        data: {'product_name': product, 'csrf_token': csrf_token},
        success: function(data) {
            if (data == 'taken') {
                $('.add-product-validation-text').text("Tento produkt je již zaregistrovaný v naší databázi.").show();
                $('.add-product-input').removeClass('is-valid').addClass('is-invalid');
            } else {
                $('.add-product-validation-text').hide();
                $('.add-product-input').removeClass('is-invalid').addClass('is-valid');
            }
        }
    });
});

// check subheading length

$('.add-product-subheading-input').on('input', function() {
  var product_subheading = $(this).val();
  $('.add-product-subheading-input').removeClass('is-valid is-invalid');

  if (product_subheading.length === 0) {
    $('.add-product-subheading-validation-text').hide();

  } else if (product_subheading.length > 20) {
    $('.add-product-subheading-input').removeClass('is-invalid').addClass('is-valid');
    $('.add-product-subheading-validation-text').hide();
  } else {
    $('.add-product-subheading-input').removeClass('is-valid').addClass('is-invalid');
    $('.add-product-subheading-validation-text').text("Podnadpis musí být dlouhý alespoň 20 znaků.").show();
  }
});