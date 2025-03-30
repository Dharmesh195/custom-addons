(function ($) {
    "use strict";
    // Function to load external JS file dynamically
    function loadScript(url, callback) {
        let script = document.createElement("script");
        script.type = "text/javascript";
        script.src = url;
        script.async = true;

        script.onload = function () {
            if (callback) callback();
        };
        document.head.appendChild(script);
    }

    // Load WOW.js from CDN and initialize it
    loadScript("https://cdnjs.cloudflare.com/ajax/libs/wow/1.1.2/wow.min.js", function () {
        new WOW().init();
    });

    // Spinner
    var spinner = function () {
        setTimeout(function () {
            if ($('#spinner').length > 0) {
                $('#spinner').removeClass('show');
            }
        }, 1);
    };
    spinner();


    // Initiate the wowjs
    //    <script src="website_arclight_infotech/static/src/js/wow.js"></script>
    //    new WOW().init();

    /**
     * Animation on scroll function and init
     */
//    function aosInit() {
//        AOS.init({
//            duration: 600,
//            easing: 'ease-in-out',
//            once: true,
//            mirror: false
//        });
//    }
//    window.addEventListener('load', aosInit);


    // Sticky Navbar
    $(window).scroll(function () {
        if ($(this).scrollTop() > 300) {
            $('.sticky-top').addClass('shadow-sm').css('top', '0px');
        } else {
            $('.sticky-top').removeClass('shadow-sm').css('top', '-100px');
        }
    });


    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 300) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({ scrollTop: 0 }, 1500, 'easeInOutExpo');
        return false;
    });


    // Facts counter
    $('[data-toggle="counter-up"]').counterUp({
        delay: 10,
        time: 2000
    });


    // Testimonials carousel
    $(".testimonial-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1000,
        items: 1,
        dots: false,
        loop: true,
        nav: true,
        navText: [
            '<i class="fa fa-chevron-left"></i>',
            '<i class="fa fa-chevron-right"></i>'
        ]
    });

    const dropDownLink = document.querySelector('.custom-dropdown-link');
    const serviceDropDown = document.querySelector('.custom-dropdown-menu')
    const headerService = document.querySelector('.custom-header-service')


    let hideTimeout;

    const showDropdown = () => {
      clearTimeout(hideTimeout);
      serviceDropDown.classList.add('active', 'show');
      headerService.classList.add('d-flex');
    };

    const hideDropdown = () => {
      hideTimeout = setTimeout(() => {
        serviceDropDown.classList.remove('show');
        setTimeout(() => {
          serviceDropDown.classList.remove('active');
          headerService.classList.remove('d-flex');
        }, 200); // Matches the CSS transition duration
      }, 200); // Delay before hiding
    };

    dropDownLink.addEventListener('mouseover', showDropdown);
    serviceDropDown.addEventListener('mouseover', showDropdown);

    dropDownLink.addEventListener('mouseout', hideDropdown);
    serviceDropDown.addEventListener('mouseout', hideDropdown)



})(jQuery);

