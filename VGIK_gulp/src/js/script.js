/*jslint browser */
/*global window */
/*global $ */

$(window).scroll(function () {
    'use strict';
    if ($(window).scrollTop() > 360) {
        $('nav').addClass('scroll');
    } else {
        $('nav').removeClass('scroll');
    }
});


$(window).scroll(function () {
    'use strict';
    if ($(window).scrollTop() > 70) {
        $('.nav-mini').addClass('scroll');
    } else {
        $('.nav-mini').removeClass('scroll');
    }
});

$(document).ready(function () {
    'use strict';
    $('.nav-mini__burger').click(function () {
        $('.nav-mini__burger, .nav-mini__menu').toggleClass('active');
        $('body').toggleClass('lock');
    });
});