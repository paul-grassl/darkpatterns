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

(function ($) {
    "use strict";

    var browserWindow = $(window);

    // :: 1.0 Preloader Active Code
    browserWindow.on("load", function () {
        $("#preloader").fadeOut("slow", function () {
            $(this).remove();
        });
    });

    // :: 2.0 Slides Active Code
    if ($.fn.owlCarousel) {

        var heroSlide = $(".hero-slides");
        heroSlide.owlCarousel({
            items: 3,
            margin: 30,
            loop: true,
            nav: false,
            dots: false,
            autoplay: true,
            autoplayTimeout: 5000,
            smartSpeed: 1000,
            autoplayHoverPause: true,
            responsive: {
                0: {
                    items: 1
                },
                768: {
                    items: 2
                },
                992: {
                    items: 3
                }
            }
        });

        var welcomeSlide = $(".welcome-slides");
        welcomeSlide.owlCarousel({
            items: 1,
            margin: 0,
            loop: true,
            nav: false,
            dots: false,
            autoplay: true,
            autoplayTimeout: 8000,
            smartSpeed: 1000,
            autoplayHoverPause: true
        });

        welcomeSlide.on("translate.owl.carousel", function () {
            var slideLayer = $("[data-animation]");
            slideLayer.each(function () {
                var anim_name = $(this).data('animation');
                $(this).removeClass('animated ' + anim_name).css('opacity', '0');
            });
        });

        welcomeSlide.on('translated.owl.carousel', function () {
            var slideLayer = welcomeSlide.find('.owl-item.active').find("[data-animation]");
            slideLayer.each(function () {
                var anim_name = $(this).data('animation');
                $(this).addClass('animated ' + anim_name).css('opacity', '1');
            });
        });

        $("[data-delay]").each(function () {
            var anim_del = $(this).data('delay');
            $(this).css('animation-delay', anim_del);
        });

        $("[data-duration]").each(function () {
            var anim_dur = $(this).data('duration');
            $(this).css('animation-duration', anim_dur);
        });
    }

    // :: 3.0 Newsticker Active Code
    if ($.fn.simpleTicker) {
        $.simpleTicker($("#breakingNewsTicker"), {
            speed: 1000,
            delay: 3000,
            easing: 'swing',
            effectType: 'roll'
        });
    }
    // :: 4.0 Nav Active Code
    if ($.fn.classyNav) {
        $('#viralnewsNav').classyNav();
    }

    // :: 5.0 Gallery Active Code
    if ($.fn.magnificPopup) {
        $('.videoPlayer').magnificPopup({
            type: 'iframe'
        });
    }

    // :: 6.0 ScrollUp Active Code
    if ($.fn.scrollUp) {
        browserWindow.scrollUp({
            scrollSpeed: 1500,
            scrollText: '<i class="fa fa-angle-up"></i>'
        });
    }

    // :: 7.0 CouterUp Active Code
    if ($.fn.counterUp) {
        $('.counter').counterUp({
            delay: 10,
            time: 2000
        });
    }

    // :: 8.0 Sticky Active Code
    if ($.fn.sticky) {
        $("#stickyMenu").sticky({
            topSpacing: 0
        });
    }

    // :: 9.0 wow Active Code
    if (browserWindow.width() > 767) {
        new WOW().init();
    }

    // :: 10.0 prevent default a click
    $('a[href="#"]').on('click', function ($) {
        $.preventDefault();
    });

    // :: 11.0 Search Form Active Code
    var searchbtn = $('#searchbtn');
    var viral_search_form = $('.viral-search-form');
    var navbar_toggler = $('.classy-navbar-toggler');

    searchbtn.on('click', function () {
        $(this).toggleClass('fa-close');
        viral_search_form.toggleClass('active');
    });
    navbar_toggler.on('click', function () {
        viral_search_form.removeClass('active');
    });
    navbar_toggler.on('click', function () {
        searchbtn.removeClass('fa-close');
    });

})(jQuery);

$('a').bind("click.myDisable", function() {
    return false;
});
