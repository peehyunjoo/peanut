$(document).ready(function () {
  var trigger = $('.hamburger'),
      overlay = $('.overlay'),
      isClosed = false;

    trigger.click(function () {
    hamburger_cross();
  });

  function hamburger_cross() {

    if (isClosed == true) {
      overlay.hide();
      trigger.removeClass('is-open');
      trigger.addClass('is-closed');
      isClosed = false;
    } else {
      overlay.show();
      trigger.removeClass('is-closed');
      trigger.addClass('is-open');
      isClosed = true;
    }
  }

  $('[data-toggle="offcanvas"]').click(function () {
    $('#wrapper').toggleClass('toggled');
  });

  $('.carrer_add').click(function(){
    for(var i = 0 ; i < 10; i++) {
      if ($(".carrer_" + i).css("display") == "none") {
        //$(".carrer_"+i).css("display","block");
        $(".carrer_" + i).show("slow");
        break;
      }
    }
  });


});



