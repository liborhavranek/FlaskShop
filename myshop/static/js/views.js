var productNames = $('.product-name-product-card');
var maxHeight = 0;

productNames.each(function() {
    maxHeight = Math.max(maxHeight, $(this).height());
});

productNames.height(maxHeight);


var descriptions = $('.product-description-product-card');
var maxHeight = 0;

descriptions.each(function() {
    maxHeight = Math.max(maxHeight, $(this).height());
});

descriptions.height(maxHeight);

      $(".order-delivery-collapsed-section").hide();
  $(".btn-order-collapse").click(function() {
    $(".order-delivery-collapsed-section").slideToggle();
  });
