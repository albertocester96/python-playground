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
                
                //aggiorna contenuto html
                var consumo_maggiore = document.getElementById("consumo-maggiore")
                if (consumo_maggiore) {
                    consumo_maggiore.innerText = data.consumo_maggiore + " %";
                } else {
                    console.error("L'elemento 'consumo-maggiore' non è stato trovato.");
                }
              
                
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
