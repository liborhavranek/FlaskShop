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