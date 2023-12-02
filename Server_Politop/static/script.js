
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
            body: formData
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

            //dati per grafico
            var chartElement = document.getElementById("chart");

            if (chartElement) {
                var data_chart = google.visualization.arrayToDataTable([
                    ['Strumento', 'valore'],
                    [data.strumento_maggiore, data.consumo_compressori]
                ])

            //Opzioni grafico
                
            //Creazione grafico
            var chart = new google.visualization.ColumnChart(chartElement);
            chart.draw(data_chart);
                
            } else {
                console.error("L'elemento chart non è stato caricato")
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