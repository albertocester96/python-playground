
// Ascolta l'evento DOMContentLoaded
document.addEventListener("DOMContentLoaded", function() {

    // Ascolta il click sul bottone con id "file"
    document.getElementById("file").addEventListener("click", function() {

        var fileInput = document.createElement('input');
        fileInput.type = "file";
        
        //Ascolta l'evento change sull'elemento input file
        fileInput.addEventListener('change', function (event){
            var selectedFile= event.target.files[0];
            

            var formData = new FormData();
            formData.append("file", selectedFile);

            //Richiesta al server quando il bottone viene cliccato
            fetch('/upload', {
                method: 'POST', //metodo richiesta
            })

            .then(response=>response.json())
            .then(data => {
                alert("File inviato con successo");

            })

            .catch(error => console.error("Errore durante l'invio del file"));
        });

        // Simula il click sull'elemento input file
        fileInput.click();
    });
});