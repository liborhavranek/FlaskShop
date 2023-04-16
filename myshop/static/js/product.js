
$('.add-brand-input').on('input', function() {
    var brand = $(this).val();
    var csrf_token = $('input[name=csrf_token]').val();

        if (brand.charAt(0) === brand.charAt(0).toLowerCase()) {
        brand = brand.charAt(0).toUpperCase() + brand.slice(1);
        $(this).val(brand);
    }

        if (brand.length == 0) {
        $('.add-brand-validation-text').hide();
        $(this).removeClass('is-valid').removeClass('is-invalid');
        return;
    }

    if (brand.length < 2) {
        $('.add-brand-validation-text').hide();
        $(this).removeClass('is-valid').addClass('is-invalid');
        return;
    }

    $.ajax({
        url: '/products/check-brand',
        method: 'POST',
        data: {'brand_name': brand, 'csrf_token': csrf_token},
        success: function(data) {
            if (data == 'taken') {
                $('.add-brand-validation-text').text("Tato značka je již zaregistrovaná v naší databázi.").show();
                $('.add-brand-input').removeClass('is-valid').addClass('is-invalid');
            } else {
                $('.add-brand-validation-text').hide();
                $('.add-brand-input').removeClass('is-invalid').addClass('is-valid');
            }
        }
    });
});
