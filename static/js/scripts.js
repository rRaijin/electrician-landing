$(window).load(function() {
        $(".loaderInner").fadeOut();
        $(".loader").delay(600).fadeOut("slow");
    }
);


$(document).ready(function () {

    function heightFix() {
        $('.parallax-main-head').css('height', $(window).height());
    }

    heightFix();

    $(window).resize(function () {
        heightFix();
    });

    // $('.header-slider').bxSlider({
    //     auto: true,
    //     controls: false,
    //     mode: 'fade',
    //     randomStart: true,
    //     pager: false,
    // });

    // Closes the sidebar menu
    $("#menu-close").click(function(e) {
        e.preventDefault();
        $("#sidebar-wrapper").toggleClass("active");
        $("#menu-toggle").css('display', 'block');
    });

    // Opens the sidebar menu
    $("#menu-toggle").click(function(e) {
        $(this).css('display', 'none');
        e.preventDefault();
        $("#sidebar-wrapper").toggleClass("active");
    });

    // Scrolls to the selected menu item on the page
    $(function() {
        $('a[href*=#]:not([href=#])').click(function() {
            if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') || location.hostname == this.hostname) {

                var target = $(this.hash);
                target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
                if (target.length) {
                    $('html,body').animate({
                        scrollTop: target.offset().top
                    }, 1000);
                    return false;
                }
            }
        });
    });

});