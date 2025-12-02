/* ===================================================================
    
  Theme Name:  Koyta - Personal Portfolio HTML Template
  Author: themetum
  Description: Koyta is a personal portfolio html template.
  Version: 1.0
    
* ================================================================= */
(function($) {
    "use strict";

    $(document).on('ready', function() {

		
        /* ==================================================
            # Smooth Scroll
         ===============================================*/
        $("body").scrollspy({
            target: ".navbar-collapse",
            offset: 200
        });
        $('a.smooth-menu').on('click', function(event) {
            var $anchor = $(this);
            var headerH = '65';
            $('html, body').stop().animate({
                scrollTop: $($anchor.attr('href')).offset().top - headerH + "px"
            }, 1500, 'easeInOutExpo');
            event.preventDefault();
        });


        /* ==================================================
            Preloader Init
         ===============================================*/
        $(window).on('load', function() {
            // Animate loader off screen
            $(".se-pre-con").fadeOut("slow");
        });


        

    }); // end document ready function
})(jQuery); // End jQuery