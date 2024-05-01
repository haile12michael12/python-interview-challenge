$(document).ready(function () {
  // HERO SLIDER
  $('#hero-slider').owlCarousel({
    autoplay: true,
    autoplayHoverPause: true,
    loop: true,
    margin: 0,
    nav: true,
    items: 1,
    dots: false,
    smartSpeed: 700,
    navText: ['PREV', 'NEXT'],
    responsive: {
      0: {
        nav: false,
      },
      768: {
        nav: true,
      },
    },
  });
});

// PROJECT SLIDER
$('#project-slider').owlCarousel({
  autoplay: true,
  autoplayHoverPause: true,
  loop: true,
  margin: 0,
  nav: true,
  dots: true,
  smartSpeed: 700,
  navText: ['PREV', 'NEXT'],
  margin: 24,
  responsive: {
    0: {
      nav: false,
      items: 1,
      margin: 0,
    },
    768: {
      items: 2,
    },
    1140: {
      items: 2,
      center: true,
    },
  },
});

// REVIEWS
$('#reviews .owl-carousel').owlCarousel({
  loop: true,
  margin: 10,
  nav: false,
  dots: true,
  items: 1,
  smartSpeed: 700,
  autoplay: true,
  autoplayHoverPause: true,
});
