const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

// jquery for fading out the error message
setTimeout(function () {
    $('#message').fadeOut('slow');
}, 3000);