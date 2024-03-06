let timeoutId;

function searchAlt() {
    clearTimeout(timeoutId);
    timeoutId = setTimeout(function() {
        var input = document.getElementById('searchInput').value.trim().toLowerCase();
        var images = document.getElementsByTagName('img');
        var results = document.getElementById('results');
        results.innerHTML = '';

        for (var i = 0; i < images.length; i++) {
            var alt = images[i].getAttribute('alt').toLowerCase();
            if (alt.includes(input)) {
                var imgResult = document.createElement('img');
                imgResult.src = images[i].src;
                results.appendChild(imgResult);
            }
        }
    }, 300); // Imposta un ritardo di 300ms prima di eseguire la ricerca
}