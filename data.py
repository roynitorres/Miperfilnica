# data.py

# Plataformas individuales
platforms = [
    {
        "id":1,
        "code": "26101",
        "title": "Netflix Premium   ",
        "image": "imagenes/1.svg",
        "description": """ Servicio de streaming para 1 dispositivo | Funciona en Teléfono o TV |
         Conexión a una sola red WiFi | Servicio recomendado para 1 persona |
         Incluye PIN de privacidad de 4 dígitos .""",
        "price": "C$ 140.00"
    },
    {
        "id":2,
        "code": "261002",
        "title": "Netflix Privado",
        "image": "imagenes/2.svg",
        "description": """ Servicio de streaming para 1 dispositivo | Funciona en Teléfono o TV |
         Conexión sin Restricción de Red Wifi | Servicio recomendado para 1 persona |
         No necesita pin de acceso | Sin Actulizar Hogar.""",
        "price": "C$ 190.00"
    },
    {
        "id":3,
        "code": "261003",
        "title": "Disney+ Standard",
        "image": "imagenes/3.svg",
        "description": """ Servicio de streaming para 1 dispositivo | Funciona en Teléfono o TV |
         Conexión a una sola red WiFi | Servicio recomendado para 1 persona |
         Incluye PIN de privacidad de 4 dígitos | No incluye las transmiciones en vivo SPN de Deportes.""",
        "price": "C$ 130.00"
    },
    {
        "id":4,
        "code": "261004",
        "title": "Disney+ Premium",
        "image": "imagenes/4.svg",
        "description": """ Servicio de streaming para 1 dispositivo | Funciona en Teléfono o TV |
         Conexión a una sola red WiFi | Servicio recomendado para 1 persona |
         Incluye PIN de privacidad de 4 dígitos | Si Incluye las transmiciones en vivo SPN de Deportes.""",
        "price": "C$ 160.00"
    },
    {
        "id":5,
        "code": "261005",
        "title": "Hbo Max",
        "image": "imagenes/5.svg",
        "description": """ Servicio de streaming para 1 dispositivo | Funciona en Teléfono o TV |
         Conexión a una sola red WiFi | Servicio recomendado para 1 persona |
         Incluye PIN de privacidad de 4 dígitos """,
        "price": "C$ 90.00"
    },
    {
        "id":6,
        "code": "261006",
        "title": "Vix Premium",
        "image": "imagenes/6.svg",
        "description": """ Servicio de streaming para 1 dispositivo | Funciona en Teléfono o TV |
         Conexión a una sola red WiFi | Servicio recomendado para 1 persona |
         No Incluye PIN de privacidad """,
        "price": "C$ 100.00"
    },
    {
        "id":7,
        "code": "261007",
        "title": "Spotify Premium",
        "image": "imagenes/7.svg",
        "description": """ Servicio de streaming para 1 dispositivo | Escucha música sin anuncios |
          Escucha música sin conexión donde quieras.| Elige la canción que quieras |
         Salta canciones de forma ilimitada. """,
        "price": "C$ 120.00"
    },
    {
        "id":8,
        "code": "261008",
        "title": "Prime Video",
        "image": "imagenes/8.svg",
        "description": """ Servicio de streaming para 1 dispositivo | Funciona en Teléfono o TV |
         Conexión a una sola red WiFi | Servicio recomendado para 1 persona |
         Incluye PIN de privacidad de 6 dígitos """,
        "price": "C$ 90.00"
    },
    {
        "id":9,
        "code": "261009",
        "title": "YouTube Premium",
        "image": "imagenes/9.svg",
        "description": """YouTube y YouTube Music sin anuncios, sin conexión y en segundo plano |
          Escucha música sin conexión donde quieras.| Elige la canción que quieras |
         Salta canciones de forma ilimitada. """,
        "price": "C$ 150.00"
    },
    {
        "id":10,
        "code": "261010",
        "title": "Crunchyroll",
        "image": "imagenes/10.svg",
        "description": """ Servicio de streaming para 1 dispositivo | Funciona en Teléfono o TV |
         Conexión a una sola red WiFi | Servicio recomendado para 1 persona |
         No invluye PIN de privacidad """,
        "price": "C$ 100.00"
    },
    {
        "id":11,
        "code": "261010",
        "title": "Crunchyroll",
        "image": "imagenes/10.svg",
        "description": """ Servicio de streaming para 1 dispositivo | Funciona en Teléfono o TV |
         Conexión a una sola red WiFi | Servicio recomendado para 1 persona |
         No invluye PIN de privacidad """,
        "price": "C$ 100.00"
    },{
        "id":10,
        "code": "261010",
        "title": "Crunchyroll",
        "image": "imagenes/10.svg",
        "description": """ Servicio de streaming para 1 dispositivo | Funciona en Teléfono o TV |
         Conexión a una sola red WiFi | Servicio recomendado para 1 persona |
         No invluye PIN de privacidad """,
        "price": "C$ 100.00"
    }


    
]

# Combos Dúos
combosDuos = [
    {
        "id":1,
        "code": "CBT001",
        "title": "Conbo 1",
        "image": "imagenes/PRUEBA.svg",
        "description": "Combo de Netflix y Disney+.",
        "price": "$15.99"
    },
    {
        "id":2,
        "code": "CBT002",
        "title": "Conbo 2",
        "image": "imagenes/PRUEBA.svg",
        "description": "Combo de Prime Video y HBO.",
        "price": "$18.99"
    },
    {
        "id":3,
        "code": "CBT003",
        "title": "Conbo 3",
        "image": "imagenes/PRUEBA.svg",
        "description": "Combo de Spotify y Apple TV.",
        "price": "$14.99"
    },
    {
        "id":4,
        "code": "CBT004",
        "title": "Conbo 4",
        "image": "imagenes/PRUEBA.svg",
        "description": "Combo de Disney+ y HBO.",
        "price": "$16.99"
    },
    {
        "id":5,
        "code": "CBT005",
        "title": "Conbo 5",
        "image": "imagenes/PRUEBA.svg",
        "description": "Combo de Disney+ y HBO.",
        "price": "$16.99"
    },
    {
        "id":6,
        "code": "CBT006",
        "title": "Conbo 6",
        "image": "imagenes/PRUEBA.svg",
        "description": "Combo de Disney+ y HBO.",
        "price": "$16.99"
    },
    {
        "id":7,
        "code": "CBT07",
        "title": "Conbo 7",
        "image": "imagenes/PRUEBA.svg",
        "description": "Combo de Disney+ y HBO.",
        "price": "$16.99"
    },
    {
        "id":8,
        "code": "CBT008",
        "title": "Conbo 8",
        "image": "imagenes/PRUEBA.svg",
        "description": "Combo de Disney+ y HBO.",
        "price": "$16.99"
    }
    
]

# Combos Dúos
combosTrios = [
    {
        "id":1,
        "code": "T001",
        "title": "Trio 1",
        "image": "imagenes/PRUEBA.svg",
        "description": "Combo de Netflix y Disney+.",
        "price": "$15.99"
    },
    {
        "id":3,
        "code": "T002",
        "title": "Trio 2",
        "image": "imagenes/PRUEBA.svg",
        "description": "Combo de Prime Video y HBO.",
        "price": "$18.99"
    },
    {
        "id":4,
        "code": "T003",
        "title": "Trio 3",
        "image": "imagenes/PRUEBA.svg",
        "description": "Combo de Spotify y Apple TV.",
        "price": "$14.99"
    },
    {
        "id":5,
        "code": "T004",
        "title": "Trio 4",
        "image": "imagenes/PRUEBA.svg",
        "description": "Combo de Disney+ y HBO.",
        "price": "$16.99"
    },
    {
        "id":6,
        "code": "T005",
        "title": "Trio 5",
        "image": "imagenes/PRUEBA.svg",
        "description": "Combo de Disney+ y HBO.",
        "price": "$16.99"
    },
    {
        "id":7,
        "code": "T006",
        "title": "Trio 6",
        "image": "imagenes/PRUEBA.svg",
        "description": "Combo de Disney+ y HBO.",
        "price": "$16.99"
    },
    {
        "id":8,
        "code": "T007",
        "title": "Trio 7",
        "image": "imagenes/PRUEBA.svg",
        "description": "Combo de Disney+ y HBO.",
        "price": "$16.99"
    },
    {
        "id":9,
        "code": "T008",
        "title": "Trio 8",
        "image": "imagenes/PRUEBA.svg",
        "description": "Combo de Disney+ y HBO.",
        "price": "$16.99"
    }
    
]

# Puedes agregar más bloques como "combos tríos", promociones, etc.
