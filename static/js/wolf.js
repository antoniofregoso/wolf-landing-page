const objs = document.querySelectorAll('[data-animation]');
var observer = new IntersectionObserver(function(entries) {
	entries.forEach(entry => {
		animation = entry.target.dataset.animation;
		if (entry.intersectionRatio > 0) {
			entry.target.classList.add('animated',  animation);
		} else {
			entry.target.classList.remove('animated',  animation);
			}
		});
			});
	objs.forEach(obj => {
		observer.observe(obj);
});	
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
	anchor.addEventListener('click', function (e) {
	e.preventDefault();
	document.querySelector(this.getAttribute('href')).scrollIntoView({
		behavior: 'smooth'
	    });
	});
});

function wolfNav() {
	if($('#nav-wolf').hasClass('dock-wolf')){
		$('#nav-wolf').addClass('over-wolf');
		$('.nav-wolf').animate({
			width: '190px'
		}, 1000);
		$('#nav-wolf').removeClass('dock-wolf');		
	} else {
		$('#nav-wolf').removeClass('over-wolf');
		$('.nav-wolf').animate({
			width: '70px'
		}, 500);
		$('#nav-wolf').addClass('dock-wolf');
	}
	};
	
	(function($) {
		  'use strict';

		  $.fn.launchBtn = function(options) {
		    var mainBtn, panel, clicks, settings, launchPanelAnim, closePanelAnim, openPanel, boxClick;

		    mainBtn = $(".st-event-button-main");
		    panel = $(".st-event-panel");
		    clicks = 0;

		    //default settings
		    settings = $.extend({
		      openDuration: 600,
		      closeDuration: 200,
		      rotate: true
		    }, options);

		    //Open panel animation
		    launchPanelAnim = function() {
		      panel.animate({
		        opacity: "toggle",
		        height: "toggle"
		      }, settings.openDuration);
		    };

		    //Close panel animation
		    closePanelAnim = function() {
		      panel.animate({
		        opacity: "hide",
		        height: "hide"
		      }, settings.closeDuration);
		    };

		    //Open panel and rotate icon
		    openPanel = function(e) {
		      if (clicks === 0) {
		        if (settings.rotate) {
		          $(this).removeClass('rotateBackward').toggleClass('rotateForward');
		        }

		        launchPanelAnim();
		        clicks++;
		      } else {
		        if (settings.rotate) {
		          $(this).removeClass('rotateForward').toggleClass('rotateBackward');
		        }

		        closePanelAnim();
		        clicks--;
		      }
		      e.preventDefault();
		      return false;
		    };

		    //Allow clicking in panel
		    boxClick = function(e) {
		      e.stopPropagation();
		    };

		    //Main button click
		    mainBtn.on('click', openPanel);

		    //Prevent closing panel when clicking inside
		    panel.click(boxClick);

		    //Click away closes panel when clicked in document
		    $(document).click(function() {
		      closePanelAnim();
		      if (clicks === 1) {
		        mainBtn.removeClass('rotateForward').toggleClass('rotateBackward');
		      }
		      clicks = 0;
		    });
		  };
		}(jQuery));


		