/*first slider*/

$(document).ready(function() { $('.slider-one').not(".slick-intialized").slick({
    autoplay: true,
    autoplaySpeed: 3000,
    dots: true

});});

/*second slider*/
$(document).ready(function() { $(".slider-two").not(".slick-intialized").slick({
    // prevArrow:".site-slider.two.prev",
    // nextArrow:".site-slider.two.next",
    slidesToShow:5,
    slidesToScroll:1,
    autoplay:true,
    autoplaySpeed:2000
});});