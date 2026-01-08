# data.py

# Plataformas individuales
platforms = [
    {
        "id":1,
        "code": "26101",
        "title": "Netflix Premium ",
        "image": "imagenes/Individuales/1.svg",
        "description": """ Servicio de streaming para 1 dispositivo | Funciona en Teléfono o TV |
         Conexión a una sola red WiFi | Servicio recomendado para 1 persona |
         Incluye PIN de privacidad de 4 dígitos .""",
        "price": "140.00",
        "currency": "C$",
        "period": "mes"

    },
    {
        "id":2,
        "code": "261002",
        "title": "Netflix Privado",
        "image": "imagenes/Individuales/2.svg",
        "description": """ Servicio de streaming para 1 dispositivo | Funciona en Teléfono o TV |
         Conexión sin Restricción de Red Wifi | Servicio recomendado para 1 persona |
         No necesita pin de acceso | Sin Actulizar Hogar.""",
        "price": "190.00",
        "currency": "C$",
        "period": "mes"
    },
    {
        "id":3,
        "code": "261003",
        "title": "Disney+ Standard",
        "image": "imagenes/Individuales/3.svg",
        "description": """ Servicio de streaming para 1 dispositivo | Funciona en Teléfono o TV |
         Conexión a una sola red WiFi | Servicio recomendado para 1 persona |
         Incluye PIN de privacidad de 4 dígitos | No incluye las transmiciones en vivo SPN de Deportes.""",
        "price": "130.00",
        "currency": "C$",
        "period": "mes"
    },
    {
        "id":4,
        "code": "261004",
        "title": "Disney+ Premium",
        "image": "imagenes/Individuales/4.svg",
        "description": """ Servicio de streaming para 1 dispositivo | Funciona en Teléfono o TV |
         Conexión a una sola red WiFi | Servicio recomendado para 1 persona |
         Incluye PIN de privacidad de 4 dígitos | Si Incluye las transmiciones en vivo SPN de Deportes.""",
        "price": "160.00",
        "currency": "C$",
        "period": "mes"
    },
    {
        "id":5,
        "code": "261005",
        "title": "Hbo Max",
        "image": "imagenes/Individuales/5.svg",
        "description": """ Servicio de streaming para 1 dispositivo | Funciona en Teléfono o TV |
         Conexión a una sola red WiFi | Servicio recomendado para 1 persona |
         Incluye PIN de privacidad de 4 dígitos """,
        "price": "90.00",
        "currency": "C$",       
        "period": "mes"
    },
    {
        "id":6,
        "code": "261006",
        "title": "Vix Premium",
        "image": "imagenes/Individuales/6.svg",
        "description": """ Servicio de streaming para 1 dispositivo | Funciona en Teléfono o TV |
         Conexión a una sola red WiFi | Servicio recomendado para 1 persona |
         No Incluye PIN de privacidad """,
        "price": "100.00",
        "currency": "C$",
        "period": "mes"
    },
    {
        "id":7,
        "code": "261007",
        "title": "Spotify Premium",
        "image": "imagenes/Individuales/7.svg",
        "description": """ Servicio de streaming para 1 dispositivo | Escucha música sin anuncios |
          Escucha música sin conexión donde quieras.| Elige la canción que quieras |
         Salta canciones de forma ilimitada. """,
        "price": "120.00",
        "currency": "C$",
        "period": "mes"
    },
    {
        "id":8,
        "code": "261008",
        "title": "Prime Video",
        "image": "imagenes/Individuales/8.svg",
        "description": """ Servicio de streaming para 1 dispositivo | Funciona en Teléfono o TV |
         Conexión a una sola red WiFi | Servicio recomendado para 1 persona |
         Incluye PIN de privacidad de 6 dígitos """,
        "price": "90.00",
        "currency": "C$",
        "period": "mes"
    },
    {
        "id":9,
        "code": "261009",
        "title": "YouTube Premium",
        "image": "imagenes/Individuales/9.svg",
        "description": """YouTube y YouTube Music sin anuncios, sin conexión y en segundo plano |
          Escucha música sin conexión donde quieras.| Elige la canción que quieras |
         Salta canciones de forma ilimitada. """,
        "price": "150.00",
        "currency": "C$",
        "period": "mes"
    },
    {
        "id":10,
        "code": "261010",
        "title": "Crunchyroll",
        "image": "imagenes/Individuales/10.svg",
        "description": """ Servicio de streaming para 1 dispositivo | Funciona en Teléfono o TV |
         Conexión a una sola red WiFi | Servicio recomendado para 1 persona |
         No invluye PIN de privacidad """,
        "price": "100.00",
        "currency": "C$",
        "period": "mes"
    },
    
    
]

# Combos Dúos
combosDuos = [
    {
        "id":1,
        "code": "CBT001",
        "title": "Combo Ani-Flix",
        "image": "imagenes/CombosDuos/11.svg",
        "description": "Netflix y Crunchyroll",
        "price_original":"240.00",
        "price": "220.00",
        "ahorro":"20",
        "currency": "C$",
        "period": "mes"
    },
    {
        "id":2,
        "code": "CBT002",
        "title": "Combo Max-Flix",
        "image": "imagenes/CombosDuos/12.svg",
        "description": "Netflix + Hbo Max",
        "price_original":"230.00",
        "price": "220.00",
        "ahorro":"10",
        "currency": "C$",
        "period": "mes"
    },
    {
        "id":3,
        "code": "CBT003",
        "title": "Combo Prime-Flix",
        "image": "imagenes/CombosDuos/13.svg",
        "description": "Netflix + Prime Video",
        "price_original":"230.00",
        "price": "220.00",
        "ahorro":"10",
        "currency": "C$",
        "period": "mes"
    },
    {
        "id":4,
        "code": "CBT004",
        "title": "Combo Sound-Flix",
        "image": "imagenes/CombosDuos/14.svg",
        "description": "Netflix + Spotify",
        "price_original":"260.00",
        "price": "250.00",
        "ahorro":"10",
        "currency": "C$",
        "period": "mes"
    },
    {
        "id":5,
        "code": "CBT005",
        "title": "Combo Disney-Flix",
        "image": "imagenes/CombosDuos/15.svg",
        "description": "Netflix + Disney Standar",
        "price_original":"270.00",
        "price": "260.00",
        "ahorro":"10",
        "currency": "C$",
        "period": "mes"
    },
    {
        "id":6,
        "code": "CBT006",
        "title": "Combo Disney-Flix Premium",
        "image": "imagenes/CombosDuos/16.svg",
        "description": "Netflix + Disney Premium",
        "price_original":"300.00",
        "price": "290.00",
        "ahorro":"10",
        "currency": "C$",
        "period": "mes"
    },
    {
        "id":7,
        "code": "CBT07",
        "title": "Combo YouFlix",
        "image": "imagenes/CombosDuos/17.svg",
        "description": "Netflix + Youtube Premium",
        "price_original":"290.00",
        "price": "280.00",
        "ahorro":"10",
        "currency": "C$",
        "period": "mes"
    },
    {
        "id":8,
        "code": "CBT008",
        "title": "Combo VixFlix",
        "image": "imagenes/CombosDuos/18.svg",
        "description": "Netflix + Vix Premium",
        "price_original":"240.00",
        "price": "220.00",
        "ahorro":"20",
        "currency": "C$",
        "period": "mes"
    },
    {
        "id":9,
        "code": "CBT008",
        "title": "Combo PrimeMax",
        "image": "imagenes/CombosDuos/19.svg",
        "description": "Prime Video + Hbo Max",
        "price_original":"180.00",
        "price": "180.00",
        "ahorro":"0",
        "currency": "C$",
        "period": "mes"
    },
    {
        "id":10,
        "code": "CBT008",
        "title": "Combo SoundMagic",
        "image": "imagenes/CombosDuos/20.svg",
        "description": "Spotify + Disney Standar",
        "price_original":"250.00",
        "price": "240.00",
        "ahorro":"10",
        "currency": "C$",
        "period": "mes"
    }
    
]

# Combos Dúos
combosTrios = [
    {
        "id":1,
        "code": "CT2601",
        "title": "Combo AniSound",
        "image": "imagenes/ComboTrio/21.svg",
        "description": "Netflix + Crunchyroll + Spotify",
        "price_original":"360.00",
        "price": "340.00",
        "ahorro":"20",
        "currency": "C$",
        "period": "mes"
    },
    {
        "id":2,
        "code": "CT2601",
        "title": "Combo MaxLatino",
        "image": "imagenes/ComboTrio/22.svg",
        "description": "Netflix + Vix + Hbo Max",
        "price_original":"330.00",
        "price": "310.00",
        "ahorro":"20",
        "currency": "C$",
        "period": "mes"
    },
    {
        "id":3,
        "code": "CT2601",
        "title": "Combo TripleMax",
        "image": "imagenes/ComboTrio/23.svg",
        "description": "Netflix + Prime Video + Hbo Max",
        "price_original":"320.00",
        "price": "300.00",
        "ahorro":"20",
        "currency": "C$",
        "period": "mes"
    },
    {
        "id":4,
        "code": "CT2604",
        "title": "Combo MagicSound+",
        "image": "imagenes/ComboTrio/24.svg",
        "description": "Netflix + Disney Premium + Spotify",
        "price_original":"420.00",
        "price": "400.00",
        "ahorro":"20",
        "currency": "C$",
        "period": "mes"
    },
    {
        "id":5,
        "code": "CT2604",
        "title": "Combo UltraPlay",
        "image": "imagenes/ComboTrio/25.svg",
        "description": "Netflix + Disney Premium + youtube Premium",
        "price_original":"450.00",
        "price": "430.00",
        "ahorro":"20",
        "currency": "C$",
        "period": "mes"
    },
    {
        "id":6,
        "code": "CT2604",
        "title": "Combo FamilyMax",
        "image": "imagenes/ComboTrio/26.svg",
        "description": "Netflix + Disney Standar + Hbo Max",
        "price_original":"360.00",
        "price": "340.00",
        "ahorro":"20",
        "currency": "C$",
        "period": "mes"
    },
    {
        "id":7,
        "code": "CT2604",
        "title": "Combo FamilyPrime",
        "image": "imagenes/ComboTrio/27.svg",
        "description": "Netflix + Disney Standar + Prime Video",
        "price_original":"360.00",
        "price": "340.00",
        "ahorro":"20",
        "currency": "C$",
        "period": "mes"
    },
    {
        "id":8,
        "code": "CT2604",
        "title": "Combo SoundMax",
        "image": "imagenes/ComboTrio/28.svg",
        "description": "Spotify + Hbo Max + Prime Video",
        "price_original":"300.00",
        "price": "300.00",
        "ahorro":"0",
        "currency": "C$",
        "period": "mes"
    },
    {
        "id":9,
        "code": "CT2604",
        "title": "Combo LatinoMax",
        "image": "imagenes/ComboTrio/29.svg",
        "description": "Vix + Hbo Max + Prime Video",
        "price_original":"280.00",
        "price": "270.00",
        "ahorro":"10",
        "currency": "C$",
        "period": "mes"
    },
    {
        "id":10,
        "code": "CT2604",
        "title": "Combo CineFamily",
        "image": "imagenes/ComboTrio/30.svg",
        "description": "Disney Premium+ Hbo Max + Prime Video",
        "price_original":"340.00",
        "price": "320.00",
        "ahorro":"20",
        "currency": "C$",
        "period": "mes"
    }
    
]

# Puedes agregar más bloques como "combos tríos", promociones, etc.
