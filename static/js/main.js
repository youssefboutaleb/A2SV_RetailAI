(function($) {
	"use strict"

	

	///////////////////////////
	// Scrollspy
	$('body').scrollspy({
		target: '#nav',
		offset: $(window).height() / 2
	});

	///////////////////////////
	// Smooth scroll
	$("#nav .main-nav a[href^='#']").on('click', function(e) {
		e.preventDefault();
		var hash = this.hash;
		$('html, body').animate({
			scrollTop: $(this.hash).offset().top
		}, 600);
	});

	$('#back-to-top').on('click', function(){
		$('body,html').animate({
			scrollTop: 0
		}, 600);
	});

	///////////////////////////
	// Btn nav collapse
	$('#nav .nav-collapse').on('click', function() {
		$('#nav').toggleClass('open');
	});

	///////////////////////////
	// Mobile dropdown
	$('.has-dropdown a').on('click', function() {
		$(this).parent().toggleClass('open-drop');
	});

	///////////////////////////
	// On Scroll
	$(window).on('scroll', function() {
		var wScroll = $(this).scrollTop();

		// Fixed nav
		wScroll > 1 ? $('#nav').addClass('fixed-nav') : $('#nav').removeClass('fixed-nav');

		// Back To Top Appear
		wScroll > 700 ? $('#back-to-top').fadeIn() : $('#back-to-top').fadeOut();
	});

	

	
	

	

})(jQuery);
document.getElementById('csv-upload-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission

    console.log('Form submitted'); // Add this line to check if the event listener is triggered
    
    const formData = new FormData();
    const fileInput = document.getElementById('csv-file');
    formData.append('csv-file', fileInput.files[0]); // 'csv-file' should match your server's file input name
    console.log(formData); 
    // Send the uploaded CSV file to the server for processing
    fetch('/api/process-csv', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        // Handle the response (e.g., display generated graphs on the website)
    })
    .catch(error => {
        console.error('Error uploading CSV:', error);
    });
});

