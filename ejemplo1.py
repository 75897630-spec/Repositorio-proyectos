<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Catálogo de Equipos Solares</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
</head>
<body class="container py-4">
    <h1 class="mb-4">Catálogo de Productos en Stock</h1>

    <div class="row">
        {% for p in productos %}
        <div class="col-md-4 mb-4">
            <div class="card h-100 shadow-sm">
                <div class="card-body">
                    <span class="badge bg-secondary mb-2">{{ p.categoria }}</span>
                    <h5 class="card-title">{{ p.nombre }}</h5>
                    <p class="h4 text-primary">${{ p.precio }}</p>
                    
                    <!-- Indicador de Stock impulsado por Python -->
                    {% if p.stock > 0 %}
                        <p class="text-success fw-bold">✓ Disponible ({{ p.stock }} unidades)</p>
                    {% else %}
                        <p class="text-danger fw-bold">✕ Agotado</p>
                    {% endif %}
                </div>
                
                <div class="card-footer bg-white border-0">
                    {% if p.stock > 0 %}
                        <!-- En la Fase 1: Pedido directo por WhatsApp -->
                        <a href="https://wa.me/51987654321?text=Hola,%20quisiera%20comprar%20el%20producto:%20{{ p.nombre }}" 
                           class="btn btn-success w-100" target="_blank">
                           Pedir por WhatsApp
                        </a>
                        
                        <!-- En la Fase 2 (Futuro): Botón para añadir al carrito -->
                        <!-- <button class="btn btn-primary w-100">Añadir al Carrito</button> -->
                    {% else %}
                        <button class="btn btn-secondary w-100" disabled>Sin Stock</button>
                    {% endif %}
                </div>
            </div>
        </div>
        {% endfor %}
    </div>
</body>
</html>