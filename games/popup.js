function openPopup(imageSrc, title, descriptionFile) {
    document.getElementById('popupImage').src = imageSrc;
    document.getElementById('popupTitle').innerText = title;

    // Carica il contenuto del file di testo per la descrizione
    fetch(descriptionFile)
        .then(response => response.text())
        .then(data => {
            document.getElementById('popupDescription').innerText = data;
        });

    document.getElementById('imagePopup').style.display = 'block';
}

function closePopup() {
    document.getElementById('imagePopup').style.display = 'none';
}