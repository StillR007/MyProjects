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

var galleryThumbs = new Swiper('.gallery-thumbs', {
    spaceBetween: 10,
    slidesPerView: 4,
    loop: true,
    freeMode: true,
    loopedSlides: 5, //looped slides should be the same
    watchSlidesVisibility: true,
    watchSlidesProgress: true,
});

var galleryTop = new Swiper('.gallery-top', {
    spaceBetween: 10,
    loop: true,
    loopedSlides: 5, //looped slides should be the same
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },
    thumbs: {
      swiper: galleryThumbs,
    }
});