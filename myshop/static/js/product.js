
$('.add-brand-input').on('input', function() {
    var brand = $(this).val();
    var csrf_token = $('input[name=csrf_token]').val();

    $.ajax({
        url: '/products/check-brand',
        method: 'POST',
        data: {'brand_name': brand, 'csrf_token': csrf_token},
        success: function(data) {
            if (data == 'taken') {
                $('.add-brand-validation-text').text("Tato značka je již zaregistrovaná v naší databázi.").show();
            }
        }
    });
});
