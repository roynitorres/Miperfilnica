# data.py

# Plataformas individuales
platforms = [
    {
        "id":1,
        "code": "26101",
        "title": "Netflix Premium ",
        "image": "imagenes/Individuales/1.svg",
        "price": "140.00",
        "currency": "C$",
        "period": "mes",
        "features": {
            "Precio:": "C$ 140.00 / mes",
            "Calidad:": "Reproducción en 4K Ultra HD + HDR, la resolución más alta disponible.",
            "Dispositivos:": "1 pantalla a la vez",
            "Contenido:": "Acceso al catálogo completo sin interrupciones publicitarias.",
            "Descarga:": "Disponible para ver sin conexión",
            "Idiomas:": "Múltiples idiomas y subtítulos",
            "Suscripción:": "Mensual, cancela cuando quieras",
            "Catalogo:": "Acceso a todo el catálogo de Netflix",
            "Juegos :": "Acceso a la biblioteca completa de películas, series y juegos móviles"
        }

    },
    {
        "id":2,
        "code": "261002",
        "title": "Netflix Privado",
        "image": "imagenes/Individuales/2.svg",
        "price": "190.00",
        "currency": "C$",
        "period": "mes",
        "features": {
            "Precio:": "C$ 190.00 / mes",
            "Calidad:": "HD, Full HD, 4K",
            "Dispositivos:": "1 pantalla a la vez",
            "Contenido:": "Acceso a todo el contenido y la mismo catalogo de Netflix Premium",
            "Descarga:": "Puede descargar contenido para verlo sin conexión, aunque limitado a un solo dispositivo móvil a la vez. ",
            "Idiomas:": "Múltiples idiomas y subtítulos",
            "Suscripción:": "Mensual, cancela cuando quieras",
            "Beneficio:": "Sin actulizar hogar",
            "Nota:":"No requiere de pin de acceso"
        }
    },
    {
        "id":3,
        "code": "261003",
        "title": "Disney+ Standard",
        "image": "imagenes/Individuales/3.svg",
        "price": "130.00",
        "currency": "C$",
        "period": "mes",
        "features": {
            "Precio:": "C$ 130.00 / mes",
            "Calidad:": "HD / Full HD",
            "Conección :": "1 dipositivo a la vez",
            "Contenido:": "Películas y series de Hulu (sin interrupciones publicitarias)***",
            "Descarga:": "Disponible para ver sin conexión",
            "Idiomas:": "Múltiples idiomas y subtítulos",
            "Suscripción:": "Mensual, cancela cuando quieras",
            "Catalogo:": "Catálogo completo de Disney+ (sin interrupciones publicitarias)",
            "Nota":"No incluye las transmiciones en vivo SPN de Deportes."
        }
    },
    {
        "id":4,
        "code": "261004",
        "title": "Disney+ Premium",
        "image": "imagenes/Individuales/4.svg",
        "price": "160.00",
        "currency": "C$",
        "period": "mes",
        "features": {
            "Precio:": "C$ 160.00 / mes",
            "Calidad:": "HD / Full HD",
            "Dispositivos :": "1 dipositivo a la vez",
            "Contenido:": "Películas y series de Hulu (sin interrupciones publicitarias)***",
            "Descarga:": "Disponible para ver sin conexión",
            "Idiomas:": "Múltiples idiomas y subtítulos",
            "Suscripción:": "Mensual, cancela cuando quieras",
            "Catalogo:": "Catálogo completo de Disney+ (sin interrupciones publicitarias)",
            "Incluye":"Todos los canales de ESPN, torneos y más de 500 eventos exclusivos por mes (con interrupciones publicitarias)"
        }
    },
    {
        "id":5,
        "code": "261005",
        "title": "Hbo Max",
        "image": "imagenes/Individuales/5.svg",
        "price": "90.00",
        "currency": "C$",       
        "period": "mes",
        "features": {
            "Precio:": "C$ 90.00 / mes",
            "Calidad:": "Resolución 4K Ultra HD*",
            "Dispositivos :": "1 dipositivo a la vez",
            "Contenido:": "Series, películas y documentales",
            "Descarga:": "Disponible para ver sin conexión",
            "Idiomas:": "Múltiples idiomas y subtítulos",
            "Suscripción:": "Mensual, cancela cuando quieras"
        }
    },
    {
        "id":6,
        "code": "261006",
        "title": "Vix Premium",
        "image": "imagenes/Individuales/6.svg",
        "price": "100.00",
        "currency": "C$",
        "period": "mes",
        "features": {
            "Precio:": "C$ 100.00 / mes",
            "Calidad:": "HD / Full HD",
            "Dispositivos:": "1 dipositivo a la vez",
            "Contenido:": "Series, películas y documentales",
            "Descarga:": "Disponible",
            "Idiomas:": "Múltiples idiomas y subtítulos",
            "Nota:": "No incluye pin de privacidad",
            "Suscripción:": "Mensual, cancela cuando quieras"
        }
    },
    {
        "id":7,
        "code": "261007",
        "title": "Spotify Premium",
        "image": "imagenes/Individuales/7.svg",
        "price": "120.00",
        "currency": "C$",
        "period": "mes",
        "features": {
            "Precio:": "C$ 120.00 / mes",
            "Conexion :": "Escucha música sin anuncios",
            "Dispositivos:": "1 dipositivo a la vez",
            "Control:": "Reproduce canciones en el orden que quieras",
            "Descarga:": "Descarga contenido para escuchar en modo offline",
            "Audio:": "Disfruta de audio de alta calidad",
            "Lista de reproducción:": "Organiza la fila de reproducción",
            "Suscripción:": "Mensual, cancela cuando quieras"
        }
    },
    {
        "id":8,
        "code": "261008",
        "title": "Prime Video",
        "image": "imagenes/Individuales/8.svg",
        "price": "90.00",
        "currency": "C$",
        "period": "mes",
        "features": {
            "Precio:": "C$ 90.00 / mes",
            "Calidad:": "HD / Full HD",
            "Dispositivos:": "1 dipositivo a la vez",
            "Contenido:": "Series, películas y documentales",
            "Descarga:": "Disponible",
            "Idiomas:": "Múltiples idiomas y subtítulos",
            "Suscripción:": "Mensual, cancela cuando quieras"
        
        }
    },
    {
        "id":9,
        "code": "261009",
        "title": "YouTube Premium",
        "image": "imagenes/Individuales/9.svg",
        "price": "150.00",
        "currency": "C$",
        "period": "mes",
        "features": {
            "Precio:": "C$ 150.00 / mes",
            "Sin Anuncios:": "Disfruta de videos, Shorts y YouTube Kids sin interrupciones publicitarias.",
            "Dispositivos:": "1 dipositivo a la vez",
            "Reproducción:": "Continúa escuchando audio mientras usas otras aplicaciones o tienes la pantalla bloqueada.",
            "Descarga:": "Guarda videos y música para verlos cuando no tienes internet.",
            "YouTubeMusic:": " Incluido en la suscripción, ofrece música sin anuncios, descargas y reproducción en segundo plano para música.",
            "PiP:": "Mira videos en una pequeña ventana mientras usas otras apps en tu móvil (disponibilidad puede variar por región)",
            "Suscripción:": "Mensual, cancela cuando quieras"
        }
    },
    {
        "id":10,
        "code": "261010",
        "title": "Crunchyroll",
        "image": "imagenes/Individuales/10.svg",
        "price": "100.00",
        "currency": "C$",
        "period": "mes",
        "features": {
            "Precio:": "C$ 100.00 / mes",
            "Calidad:": "Streaming en HD y, en algunos casos, incluso 4K.",
            "Dispositivos:": "1 dipositivo a la vez",
            "Contenido:": "Nuevos episodios disponibles casi al mismo tiempo que se emiten en Japón.",
            "Descarga:": "Descarga episodios en tu dispositivo móvil para verlos sin internet.",
            "Nota:": "No incluye pin de privacidad",
            "Suscripción:": "Mensual, cancela cuando quieras"
        }
    },
    
    
]

# Combos Dúos
combosDuos = [
    {
        "id":1,
        "code": "CBT001",
        "title": "Combo Anime",
        "image": "imagenes/CombosDuos/11.svg",
        "description": "Netflix y Crunchyroll",
        "price_original":"240.00",
        "price": "220.00",
        "ahorro":"20",
        "currency": "C$",
        "period": "mes",
        "features": {
            "Beneficio principal:": "Incluye todas las características del perfil individual en ambas plataformas",
            "Incluye:": "Netflix Premium + Crunchyroll Premium",
            "Precio mensual:": "C$ 220.00 / mes",
            "Ahorro:": "Ahorra C$ 20 en comparación a comprarlos por separado",
            "Calidad:": "HD, Full HD y hasta 4K (según plataforma)",
            "Pantallas:": "1 perfil por plataforma (uso independiente)",
            "Contenido:": "Películas, series, anime y estrenos simultáneos",
            "Descargas:": "Disponible para ver sin conexión",
            "Idiomas:": "Múltiples idiomas y subtítulos",
            "Suscripción:": "Mensual, cancela cuando quieras"
        }
    },
    {
        "id":2,
        "code": "CBT002",
        "title": "Combo Basico 1",
        "image": "imagenes/CombosDuos/12.svg",
        "description": "Netflix + Hbo Max",
        "price_original":"230.00",
        "price": "220.00",
        "ahorro":"10",
        "currency": "C$",
        "period": "mes",
        "features": {
        "Beneficio principal:": "Incluye todas las características del perfil individual en ambas plataformas",
        "Incluye:": "Netflix Premium + HBO Max",
        "Precio mensual:": "C$ 220.00 / mes",
        "Ahorro:": "Ahorra C$ 10 mensuales",
        "Calidad:": "HD, Full HD y 4K Ultra HD",
        "Pantallas:": "1 perfil por plataforma",
        "Contenido:": "Series exclusivas, películas y estrenos",
        "Descargas:": "Disponible para ver sin conexión",
        "Idiomas:": "Múltiples idiomas y subtítulos",
        "Suscripción:": "Mensual, sin contratos"
    }

    },
    {
        "id":3,
        "code": "CBT003",
        "title": "Combo Basico 2",
        "image": "imagenes/CombosDuos/13.svg",
        "description": "Netflix + Prime Video",
        "price_original":"230.00",
        "price": "220.00",
        "ahorro":"10",
        "currency": "C$",
        "period": "mes",
        "features": {
        "Beneficio principal:": "Todas las funciones del perfil individual incluidas",
        "Incluye:": "Netflix Premium + Prime Video",
        "Precio mensual:": "C$ 220.00 / mes",
        "Ahorro:": "Ahorra C$ 10 al mes",
        "Calidad:": "HD / Full HD / 4K (según contenido)",
        "Pantallas:": "1 perfil por plataforma",
        "Contenido:": "Series, películas y contenido exclusivo",
        "Descargas:": "Disponible en dispositivos móviles",
        "Idiomas:": "Múltiples idiomas y subtítulos",
        "Suscripción:": "Mensual, flexible"
    }
    
    },
    {
        "id":4,
        "code": "CBT004",
        "title": "Combo Musica",
        "image": "imagenes/CombosDuos/14.svg",
        "description": "Netflix + Spotify",
        "price_original":"260.00",
        "price": "250.00",
        "ahorro":"10",
        "currency": "C$",
        "period": "mes",
         "features": {
        "Beneficio principal:": "Incluye todas las características del perfil individual",
        "Incluye:": "Netflix Premium + Spotify Premium",
        "Precio mensual:": "C$ 250.00 / mes",
        "Ahorro:": "Ahorra C$ 10 mensuales",
        "Calidad:": "Video en HD / 4K + audio de alta calidad",
        "Pantallas:": "1 perfil por plataforma",
        "Contenido:": "Películas, series y música sin anuncios",
        "Descargas:": "Disponible en ambas plataformas",
        "Experiencia:": "Entretenimiento completo: video y música",
        "Suscripción:": "Mensual, cancela cuando quieras"
    }
    
    },
    {
        "id":5,
        "code": "CBT005",
        "title": "Combo Standard Plus",
        "image": "imagenes/CombosDuos/15.svg",
        "description": "Netflix + Disney Standar",
        "price_original":"270.00",
        "price": "260.00",
        "ahorro":"10",
        "currency": "C$",
        "period": "mes",
        "features": {
        "Beneficio principal:": "Todas las funciones del perfil individual incluidas",
        "Incluye:": "Netflix Premium + Disney+ Standard",
        "Precio mensual:": "C$ 260.00 / mes",
        "Ahorro:": "Ahorra C$ 10 mensuales",
        "Calidad:": "HD / Full HD",
        "Pantallas:": "1 perfil por plataforma",
        "Contenido:": "Películas, series, Marvel, Star Wars y más",
        "Descargas:": "Disponible para ver sin conexión",
        "Idiomas:": "Múltiples idiomas y subtítulos",
        "Suscripción:": "Mensual"
    }
    
    },
    {
        "id":6,
        "code": "CBT006",
        "title": "Combo Premium Plus",
        "image": "imagenes/CombosDuos/16.svg",
        "description": "Netflix + Disney Premium",
        "price_original":"300.00",
        "price": "290.00",
        "ahorro":"10",
        "currency": "C$",
        "period": "mes",
        "features": {
       "Beneficio principal:": "Acceso completo a todas las funciones individuales",
       "Incluye:": "Netflix Premium + Disney+ Premium",
       "Precio mensual:": "C$ 290.00 / mes",
       "Ahorro:": "Ahorra C$ 10 mensuales",
       "Calidad:": "HD, Full HD y contenido premium",
       "Pantallas:": "1 perfil por plataforma",
       "Contenido:": "Incluye Disney, Pixar, Marvel, Star Wars y ESPN",
       "Descargas:": "Disponible",
       "Idiomas:": "Múltiples idiomas",
       "Suscripción:": "Mensual, sin contratos"
   }
   
    },
    {
        "id":7,
        "code": "CBT07",
        "title": "Combo Video",
        "image": "imagenes/CombosDuos/17.svg",
        "description": "Netflix + Youtube Premium",
        "price_original":"290.00",
        "price": "280.00",
        "ahorro":"10",
        "currency": "C$",
        "period": "mes",
        "features": {
        "Beneficio principal:": "Incluye todas las ventajas del perfil individual",
        "Incluye:": "Netflix Premium + YouTube Premium",
        "Precio mensual:": "C$ 280.00 / mes",
        "Ahorro:": "Ahorra C$ 10 mensuales",
        "Calidad:": "HD / Full HD / 4K",
        "Pantallas:": "1 perfil por plataforma",
        "Contenido:": "Series, películas y YouTube sin anuncios",
        "Descargas:": "Disponible en ambas plataformas",
        "Experiencia:": "Video sin interrupciones publicitarias",
        "Suscripción:": "Mensual"
    }
    
    },
    {
        "id":8,
        "code": "CBT008",
        "title": "Combo Latino",
        "image": "imagenes/CombosDuos/18.svg",
        "description": "Netflix + Vix Premium",
        "price_original":"240.00",
        "price": "220.00",
        "ahorro":"20",
        "currency": "C$",
        "period": "mes",
        "features": {
        "Beneficio principal:": "Incluye todas las funciones del perfil individual",
        "Incluye:": "Netflix Premium + ViX Premium",
        "Precio mensual:": "C$ 220.00 / mes",
        "Ahorro:": "Ahorra C$ 20 mensuales",
        "Calidad:": "HD / Full HD",
        "Pantallas:": "1 perfil por plataforma",
        "Contenido:": "Series, novelas, películas y contenido latino",
        "Descargas:": "Disponible",
        "Idiomas:": "Español y subtítulos",
        "Suscripción:": "Mensual"
    }
    
    },
    {
        "id":9,
        "code": "CBT008",
        "title": "Combo CineMax",
        "image": "imagenes/CombosDuos/19.svg",
        "description": "Prime Video + Hbo Max",
        "price_original":"180.00",
        "price": "180.00",
        "ahorro":"0",
        "currency": "C$",
        "period": "mes",
        "features": {
        "Beneficio principal:": "Todas las funciones del perfil individual incluidas",
        "Incluye:": "Prime Video + HBO Max",
        "Precio mensual:": "C$ 180.00 / mes",
        "Ahorro:": "Precio especial por combo",
        "Calidad:": "HD / Full HD / 4K",
        "Pantallas:": "1 perfil por plataforma",
        "Contenido:": "Series y películas exclusivas",
        "Descargas:": "Disponible",
        "Idiomas:": "Múltiples idiomas",
        "Suscripción:": "Mensual"
    }
    
    },
    {
        "id":10,
        "code": "CBT008",
        "title": "Combo Entretenimiento",
        "image": "imagenes/CombosDuos/20.svg",
        "description": "Spotify + Disney Standar",
        "price_original":"250.00",
        "price": "240.00",
        "ahorro":"10",
        "currency": "C$",
        "period": "mes",
        "features": {
        "Beneficio principal:": "Incluye todas las características del perfil individual",
        "Incluye:": "Spotify Premium + Disney+ Standard",
        "Precio mensual:": "C$ 240.00 / mes",
        "Ahorro:": "Ahorra C$ 10 mensuales",
        "Calidad:": "Audio premium + video HD",
        "Pantallas:": "1 perfil por plataforma",
        "Contenido:": "Música sin anuncios y entretenimiento familiar",
        "Descargas:": "Disponible en ambas plataformas",
        "Experiencia:": "Ideal para música y entretenimiento",
        "Suscripción:": "Mensual"
    }

    }
    
]

# Combos Dúos
combosTrios = [
    {
        "id":1,
        "code": "CT2601",
        "title": "Mega Combo Anime",
        "image": "imagenes/ComboTrio/21.svg",
        "description": "Netflix + Crunchyroll + Spotify",
        "price_original":"360.00",
        "price": "340.00",
        "ahorro":"20",
        "currency": "C$",
        "period": "mes",
        "features": {
        "Beneficio principal:": "Incluye todas las características del perfil individual en las tres plataformas",
        "Incluye:": "Netflix Premium + Crunchyroll Premium + Spotify Premium",
        "Precio mensual:": "C$ 340.00 / mes",
        "Ahorro:": "Ahorra C$ 20 en comparación al precio individual",
        "Calidad:": "Video HD / Full HD / 4K + audio de alta calidad",
        "Pantallas:": "1 perfil por plataforma (uso independiente)",
        "Contenido:": "Películas, series, anime y música sin anuncios",
        "Descargas:": "Disponible en todas las plataformas",
        "Experiencia:": "Entretenimiento completo: video, anime y música",
        "Suscripción:": "Mensual, cancela cuando quieras"
    }

    },
    {
        "id":2,
        "code": "CT2601",
        "title": "Mega combo Latino",
        "image": "imagenes/ComboTrio/22.svg",
        "description": "Netflix + Vix + Hbo Max",
        "price_original":"330.00",
        "price": "310.00",
        "ahorro":"20",
        "currency": "C$",
        "period": "mes",
        "features": {
        "Beneficio principal:": "Acceso total a las funciones del perfil individual",
        "Incluye:": "Netflix Premium + ViX Premium + HBO Max",
        "Precio mensual:": "C$ 310.00 / mes",
        "Ahorro:": "Ahorra C$ 20 mensuales",
        "Calidad:": "HD / Full HD / 4K (según plataforma)",
        "Pantallas:": "1 perfil por plataforma",
        "Contenido:": "Series, películas y contenido latino exclusivo",
        "Descargas:": "Disponible para ver sin conexión",
        "Idiomas:": "Español y múltiples subtítulos",
        "Suscripción:": "Mensual, sin contratos"
    }

    },
    {
        "id":3,
        "code": "CT2601",
        "title": "Mega Combo Familiar",
        "image": "imagenes/ComboTrio/23.svg",
        "description": "Netflix + Prime Video + Hbo Max",
        "price_original":"320.00",
        "price": "300.00",
        "ahorro":"20",
        "currency": "C$",
        "period": "mes",
        "features": {
        "Beneficio principal:": "Incluye todas las funciones del perfil individual",
        "Incluye:": "Netflix Premium + Prime Video + HBO Max",
        "Precio mensual:": "C$ 300.00 / mes",
        "Ahorro:": "Ahorra C$ 20 mensuales",
        "Calidad:": "HD / Full HD / 4K Ultra HD",
        "Pantallas:": "1 perfil por plataforma",
        "Contenido:": "Series, películas y estrenos exclusivos",
        "Descargas:": "Disponible en todas las plataformas",
        "Experiencia:": "Ideal para amantes del cine y series",
        "Suscripción:": "Mensual"
    }

    },
    {
        "id":4,
        "code": "CT2604",
        "title": "Mega Combo Musical",
        "image": "imagenes/ComboTrio/24.svg",
        "description": "Netflix + Disney Premium + Spotify",
        "price_original":"420.00",
        "price": "400.00",
        "ahorro":"20",
        "currency": "C$",
        "period": "mes",
        "features": {
        "Beneficio principal:": "Todas las funciones del perfil individual incluidas",
        "Incluye:": "Netflix Premium + Disney+ Premium + Spotify Premium",
        "Precio mensual:": "C$ 400.00 / mes",
        "Ahorro:": "Ahorra C$ 20 mensuales",
        "Calidad:": "Video HD / Full HD + audio premium",
        "Pantallas:": "1 perfil por plataforma",
        "Contenido:": "Películas, series, deportes y música sin anuncios",
        "Descargas:": "Disponible",
        "Experiencia:": "Ideal para toda la familia",
        "Suscripción:": "Mensual"
    }

    },
    {
        "id":5,
        "code": "CT2604",
        "title": "Mega combo Total",
        "image": "imagenes/ComboTrio/25.svg",
        "description": "Netflix + Disney Premium + youtube Premium",
        "price_original":"450.00",
        "price": "430.00",
        "ahorro":"20",
        "currency": "C$",
        "period": "mes",
        "features": {
        "Beneficio principal:": "Acceso completo a todas las funciones individuales",
        "Incluye:": "Netflix Premium + Disney+ Premium + YouTube Premium",
        "Precio mensual:": "C$ 430.00 / mes",
        "Ahorro:": "Ahorra C$ 20 mensuales",
        "Calidad:": "HD / Full HD / 4K",
        "Pantallas:": "1 perfil por plataforma",
        "Contenido:": "Entretenimiento familiar y videos sin anuncios",
        "Descargas:": "Disponible",
        "Experiencia:": "Todo en una sola suscripción",
        "Suscripción:": "Mensual, sin contratos"
    }

    },
    {
        "id":6,
        "code": "CT2604",
        "title": "Mega Combo CineMax",
        "image": "imagenes/ComboTrio/26.svg",
        "description": "Netflix + Disney Standar + Hbo Max",
        "price_original":"360.00",
        "price": "340.00",
        "ahorro":"20",
        "currency": "C$",
        "period": "mes",
        "features": {
        "Beneficio principal:": "Incluye todas las funciones del perfil individual",
        "Incluye:": "Netflix Premium + Disney+ Standard + HBO Max",
        "Precio mensual:": "C$ 340.00 / mes",
        "Ahorro:": "Ahorra C$ 20 mensuales",
        "Calidad:": "HD / Full HD",
        "Pantallas:": "1 perfil por plataforma",
        "Contenido:": "Series, películas y contenido para toda la familia",
        "Descargas:": "Disponible",
        "Idiomas:": "Múltiples idiomas",
        "Suscripción:": "Mensual"
    }

    },
    {
        "id":7,
        "code": "CT2604",
        "title": "Mega Combo Streaming",
        "image": "imagenes/ComboTrio/27.svg",
        "description": "Netflix + Disney Standar + Prime Video",
        "price_original":"360.00",
        "price": "340.00",
        "ahorro":"20",
        "currency": "C$",
        "period": "mes",
        "features": {
        "Beneficio principal:": "Todas las funciones del perfil individual incluidas",
        "Incluye:": "Netflix Premium + Disney+ Standard + Prime Video",
        "Precio mensual:": "C$ 340.00 / mes",
        "Ahorro:": "Ahorra C$ 20 mensuales",
        "Calidad:": "HD / Full HD",
        "Pantallas:": "1 perfil por plataforma",
        "Contenido:": "Películas, series y contenido familiar",
        "Descargas:": "Disponible",
        "Idiomas:": "Múltiples idiomas",
        "Suscripción:": "Mensual"
    }

    },
    {
        "id":8,
        "code": "CT2604",
        "title": "Mega combo Milenial",
        "image": "imagenes/ComboTrio/28.svg",
        "description": "Spotify + Hbo Max + Prime Video",
        "price_original":"300.00",
        "price": "300.00",
        "ahorro":"0",
        "currency": "C$",
        "period": "mes",
        "features": {
        "Beneficio principal:": "Acceso total a todas las funciones individuales",
        "Incluye:": "Spotify Premium + HBO Max + Prime Video",
        "Precio mensual:": "C$ 300.00 / mes",
        "Ahorro:": "Precio especial por combo",
        "Calidad:": "Audio premium + video HD / Full HD",
        "Pantallas:": "1 perfil por plataforma",
        "Contenido:": "Música sin anuncios y cine exclusivo",
        "Descargas:": "Disponible",
        "Experiencia:": "Ideal para entretenimiento mixto",
        "Suscripción:": "Mensual"
    }

    },
    {
        "id":9,
        "code": "CT2604",
        "title": "Mega combo LatinoMax",
        "image": "imagenes/ComboTrio/29.svg",
        "description": "Vix + Hbo Max + Prime Video",
        "price_original":"280.00",
        "price": "270.00",
        "ahorro":"10",
        "currency": "C$",
        "period": "mes",
        "features": {
        "Beneficio principal:": "Incluye todas las características del perfil individual",
        "Incluye:": "ViX Premium + HBO Max + Prime Video",
        "Precio mensual:": "C$ 270.00 / mes",
        "Ahorro:": "Ahorra C$ 10 mensuales",
        "Calidad:": "HD / Full HD",
        "Pantallas:": "1 perfil por plataforma",
        "Contenido:": "Series, novelas, películas y contenido latino",
        "Descargas:": "Disponible",
        "Idiomas:": "Español y subtítulos",
        "Suscripción:": "Mensual"
    }

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
        "period": "mes",
        "features": {
        "Beneficio principal:": "Acceso completo a todas las funciones individuales",
        "Incluye:": "Disney+ Premium + HBO Max + Prime Video",
        "Precio mensual:": "C$ 320.00 / mes",
        "Ahorro:": "Ahorra C$ 20 mensuales",
        "Calidad:": "HD / Full HD / 4K (según contenido)",
        "Pantallas:": "1 perfil por plataforma",
        "Contenido:": "Cine, series y entretenimiento familiar",
        "Descargas:": "Disponible",
        "Experiencia:": "Combo ideal para el hogar",
        "Suscripción:": "Mensual"
    }

    }
    
]

# Puedes agregar más bloques como "combos tríos", promociones, etc.
