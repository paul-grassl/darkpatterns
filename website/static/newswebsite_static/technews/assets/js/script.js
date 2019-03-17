// --- Begin of customization for study purposes --- //

$(document).ready(function () {
  // open modal once document is loaded
  $('#myModal').modal('show')
})
// prevent modal from closing if you click outside of it or use Esc
$('#myModal').modal({ backdrop: 'static', keyboard: false })


// require input before continuation possible
$(function () {
  $('#myForm').validate({
    rules: {
      consentForm: 'required'
    },
    messages: {
      consentForm: {
        required: 'Please select one of the options'
      }
    },
    errorElement: 'div',
    errorLabelContainer: '.errorTxt'
  })
});

$("input[type='radio']").change(function() {
  if($(this).val()=='DNA')
  {
    document.getElementById('errorTxt2').innerHTML = ''
  }
})

function directCorrect() {
  // if the form returns 'manage options' go to page 2 otherwise submit form
  var radio_value = $('input[name=consentForm]:checked').val();
  if (radio_value === 'MO') {
    sendEvent(2)
  }
  // if the form returns 'Agree' submit form
  else {
    $('#myForm').submit();
  }
};

function submitCorrect() {
  var radio_value = $('input[name=consentForm]:checked').val();
  if (radio_value === 'DNA') {
    $('#myForm').submit();
  }
  else {
    document.getElementById('errorTxt2').innerHTML = 'Please select one of the options'
  }
}

// ---- End of customization for study purposes --- //

$(function () {
    'use strict';
    // --------------------------------------------------------------------
    // PreLoader
    // --------------------------------------------------------------------
    (function () {
        $('#preloader').delay(200).fadeOut('slow');
    }());
    // --------------------------------------------------------------------
    // One Page Navigation
    // --------------------------------------------------------------------
    (function () {
        $(window).scroll(function () {
            if ($(this).scrollTop() >= 50) {
                $('nav.navbar').addClass('sticky-nav');
            }
            else {
                $('nav.navbar').removeClass('sticky-nav');
            }
        });
    }());
    // --------------------------------------------------------------------
    // jQuery for page scrolling feature - requires jQuery Easing plugin
    // --------------------------------------------------------------------
    (function () {
        $('a.page-scroll').on('click', function (e) {
            e.preventDefault();
            var $anchor = $(this);
            $('html, body').stop().animate({
                scrollTop: $($anchor.attr('href')).offset().top
            }, 1500, 'easeInOutExpo');
        });
    }());
    // -------------------------------------------------------------
    // mobile menu
    // -------------------------------------------------------------
    (function () {
        $('button.navbar-toggle').ucOffCanvasMenu({
            documentWrapper: '#main-wrapper'
            , contentWrapper: '.content-wrapper'
            , position: 'uc-offcanvas-left', // class name
            // opener         : 'st-menu-open',            // class name
            effect: 'slide-along', // class name
            closeButton: '#uc-mobile-menu-close-btn'
            , menuWrapper: '.uc-mobile-menu', // class name below-pusher
            documentPusher: '.uc-mobile-menu-pusher'
        });
    }());
    // -------------------------------------------------------------
    // top scrolling
    // -------------------------------------------------------------
    (function () {
        var offset = 220;
        var duration = 500;
        jQuery(window).scroll(function () {
            if (jQuery(this).scrollTop() > offset) {
                jQuery('.crunchify-top').fadeIn(duration);
            }
            else {
                jQuery('.crunchify-top').fadeOut(duration);
            }
        });
        jQuery('.crunchify-top').click(function (event) {
            event.preventDefault();
            jQuery('html, body').animate({
                scrollTop: 0
            }, duration);
            return false;
        });
    }());
    // --------------------------------------------------------------------
    // Search
    // --------------------------------------------------------------------
    $("#search-button, #search-icon").click(function (e) {
        e.preventDefault();
        $("#search-button, #search-form").toggle();
    });
    // --------------------------------------------------------------------
    // Carousel slider for blog page
    // --------------------------------------------------------------------
    $("#feature-news-carousel").owlCarousel({
        loop: true
        , dots: false
        , items: 1
        , autoplay: true
        , singleItem: true
            // "singleItem:true" is a shortcut for:
            // items : 1,
            // itemsDesktop : false,
            // itemsDesktopSmall : false,
            // itemsTablet: false,
            // itemsMobile : false
    });
});
// JQuery end
$(document).on('click', '.m-menu .dropdown-menu', function (e) {
    e.stopPropagation()
});
$('a').bind("click.myDisable", function() {
    return false;
});
