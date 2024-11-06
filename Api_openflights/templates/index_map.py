<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Airports Map</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css" />
    <style>
        #map {
            height: 600px;
            width: 100%;
        }
    </style>
</head>
<body>
    <div class="container mt-5">
        <!-- Botón para regresar al inicio -->
        <a href="/" class="btn btn-primary mb-3"><i class="fas fa-home"></i> Inicio</a>
        <h1 class="text-center">Airports Map</h1>
        <div id="map"></div>
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
    <script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>
    <script>
        // Inicializar el mapa centrado en el mundo
        var map = L.map('map').setView([20, 0], 2);

        // Cargar el mapa base de OpenStreetMap
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        }).addTo(map);

        // Obtener los datos de los aeropuertos
        $.getJSON('/airports', function(data) {
            data.forEach(function(airport) {
                // Añadir un marcador para cada aeropuerto
                L.marker([airport.Latitude, airport.Longitude])
                    .bindPopup(`<b>${airport.Name}</b><br>${airport.City}, ${airport.Country}`)
                    .addTo(map);
            });
        });
    </script>
</body>
</html>