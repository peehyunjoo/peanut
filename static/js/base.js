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

  $('.career_add').click(function(){
    for(var i = 0 ; i < 10; i++) {
      if ($(".career_" + i).css("display") == "none") {
        $(".career_" + i).show("slow");
        break;
      }
    }
  });

  $('.edu_add').click(function(){
    for(var i = 0 ; i < 10; i++) {
      if ($(".edu_" + i).css("display") == "none") {
        $(".edu_" + i).show("slow");
        break;
      }
    }
  });

});



