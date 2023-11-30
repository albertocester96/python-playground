document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("file").addEventListener("click", function() {

        var fileInput = document.createElement('input');
        fileInput.type = "file";

        // Ascolta l'evento change sull'elemento input file
        fileInput.addEventListener('change', function(event) {
            var selectedFile = event.target.files[0];

            var formData = new FormData();
            formData.append("file", selectedFile);

            // Richiesta al server quando il bottone viene cliccato
            fetch('/upload', {
                method: 'POST',
                body: formData, // Passa l'oggetto FormData come corpo della richiesta
                // Imposta l'intestazione Content-Type
                //headers: {
                //    'Content-Type': 'multipart/form-data'
                //}
            })
            .then(response => {
                console.log("Stato:", response.status);
                return response.json();
            })
            .then(data => {
                console.log("Dati ricevuti:", data);
                alert("Operazione completata con successo");
            })
            .catch(error => {
                console.error("Errore:", error);
                alert("Si è verificato un errore");
            });
        });

        // Simula il click sull'elemento input file
        fileInput.click();
    });
});
