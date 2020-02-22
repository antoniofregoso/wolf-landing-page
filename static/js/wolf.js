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

