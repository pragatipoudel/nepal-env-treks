$(function() {

    // Elevate the nav bar on scroll.
    const nav = $('nav');
    $(window).scroll(function() {
        if ($(this).scrollTop() > 32) {
            nav.addClass('elevated');
        } else {
            nav.removeClass('elevated');
        }
    });
});