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