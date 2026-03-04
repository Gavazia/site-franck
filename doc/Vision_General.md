# Visión General y Experiencia del Usuario: Portafolio de Franck Bietry

Esta es la brújula conceptual de nuestro proyecto. Aquí describimos, en lenguaje natural, qué es lo que estamos construyendo, para quién es, cómo se siente usarlo y cuál es el impacto final que buscamos.

## 1. ¿Qué estamos creando y para quién es?
Estamos construyendo la "identidad digital maestra" de **Franck Bietry**, un destacado profesor universitario e investigador. Más que un simple blog, es un Portafolio Académico de alto calibre. 

Este sitio no está diseñado para el público en general; su audiencia objetivo es muy específica:
*   **Académicos e Investigadores**: Buscan acceso rápido y claro a sus "papers", reseñas y publicaciones.
*   **Alumnos**: Necesitan encontrar información sobre sus clases o recursos.
*   **Decanos y Reclutadores**: Entrarán a la web buscando validar su autoridad, su trayectoria (el "parcour") y en qué instituciones ha colaborado.

## 2. La Interfaz Pública (Lo que ven los visitantes)
Cuando alguien busque "Franck Bietry" en Google, el objetivo es que el sitio esté indexado al **100% en la posición #1** gracias a nuestro riguroso SEO y esquemas de datos estructurados para los buscadores (JSON-LD).

Esa persona hará clic y entrará a una experiencia que definimos como **"Glassmorphism Innovador" (Cristal sobre Hielo)**:
*   **La Estética**: No será el típico fondo blanco aburrido. El fondo tendrá tonos sutiles o gradientes muy elegantes inspirados en el hielo o temas oscuros muy sobrios. Por encima de esto flotarán contenedores (cartas y menús) que lucen como cristal esmerilado (`backdrop-blur`). Detrás del cristal, todo se ve ligeramente difuminado, creando una sensación de profundidad y 3D acentuada por sombras claras alrededor de las cajas. Las tipografías negras (o muy oscuras) se leerán con perfecta claridad sobre estos "cristales".
*   **El Recibimiento (Home)**: Lo primero que verán será una presentación impecable de quién es Franck. Todo su peso profesional de un solo vistazo, rematado en la parte inferior por un carrusel que se desplaza suavemente de forma horizontal, mostrando los logotipos de todas las instituciones de prestigio con las que ha trabajado.
*   **Su Trayectoria (Parcour)**: Una sección visualmente exquisita donde el visitante baja por la pantalla (hace scroll) y mágicamente van revelándose (con transiciones suaves en 3D dictadas por Framer Motion) los eventos, clases y años críticos de su carrera.
*   **Publicaciones y Blog**: Mientras el inicio es muy visual, estas secciones rinden tributo a la legibilidad. Muy limpias, textos grandes (usando tipografías e iconos premium de Phosphor Icons) y botones claros para descargar los PDFs o leer más sin distracciones.

## 3. La Interfaz Privada (El Asistente de Franck)
La magia real de este sitio no está solo en el cristal; está en cómo Franck lo administra. 

Hemos desechado sistemas prehistóricos como WordPress. Construimos para Franck la ruta `/admin-franck`, blindada por su contraseña. Una vez dentro, la experiencia se rige por la "fricción cero":

*   **Editor Visual Minimalista**: Franck no verá paneles complejos, botones de plugins ni opciones confusas. Se encontrará con un lienzo en blanco (estilo Notion). Simplemente empieza a escribir. Quiere poner una foto: la arrastra desde su escritorio al navegador y listo, el sistema se encarga subirla a nuestra base de datos (InsForge) por detrás sin que él toque un solo código.
*   **El Agente de Inteligencia Artificial (El Co-Piloto)**: No estará solo. A su lado derecho tendrá un chat integrado directamente en el editor, potenciado por **Gemini 3.0** de Google. 
    *   Si Franck escribe un artículo rápido, puede decirle a la IA: *"Corrige mi ortografía, dale un tono académico y optimízalo para el término SEO 'Liderazgo en Universidades'"*. 
    *   La IA leerá su pantalla y le devolverá el texto pulido.
    *   Ese editor es un **asistente ejecutor**, así que Franck puede darle a un botón de "Aceptar sugerencias" y la IA escribirá y dará formato automáticamente en su documento.

## 4. Conclusión del Impacto
Estamos montando un deportivo de lujo pero sin costos de mantenimiento para el cliente (aprovechando la capa gratuita de InsForge), todo empaquetado y servido por Next.js y Hero UI. Visitantes ven prestigio e innovación visual; Franck experimenta minimalismo purista con la asistencia de Inteligencia artificial de punta. Funciona rápido, impresiona a la vista y escribe por sí solo.
