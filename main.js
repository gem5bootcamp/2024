// === very broken ===
var slider_html = document.querySelector('.slider-html');
var slides_length = 24;
var i = 0;



function prev(){
	if(i <= 0) i = slides_length;
	i--;

	return setSlide();
}

function next(){
	if(i >= slides.length-1) i = -1;
	i++;
	return setSlide();
}

function setSlide(url, anchorId){
    i = int(anchorId);
	return slider_html.setAttribute('src', url);

}



function loadUrlIntoIframe(anchorId, iframeId) {
    // Get the anchor element by its ID
    const anchorElement = document.getElementById(anchorId);

    // Get the iframe element by its ID
    const iframeElement = document.getElementById(iframeId);

    // Check if both elements exist and are of correct types
    if (anchorElement && anchorElement.tagName === 'A' &&
        iframeElement && iframeElement.tagName === 'IFRAME') {

        // Prevent the default action of the anchor tag
        anchorElement.addEventListener('click', function(event) {
            event.preventDefault(); // Stop the link from opening in a new page

            // Get the URL from the href attribute
            const url = anchorElement.href;

            // Set the URL to the iframe's src attribute
            iframeElement.src = url;
        });
    } else {
        console.error('Invalid anchor or iframe element');
    }
}

