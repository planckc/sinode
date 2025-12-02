# Guía de Cambios - SINODE Web-Output-2

## 📋 Resumen de Adaptación

Este documento explica los cambios realizados en la plantilla Charities para adaptar su contenido a SINODE (Somos Iglesia, NO Denominaciones).

**Plantilla Original:** Charities - Charity & Nonprofit Template (index-6.html)
**Adaptación:** SINODE - Plataforma Eclesiástica Digital
**Fecha:** Diciembre 2024

---

## ✅ Secciones Modificadas

### 1. **Hero Banner** (Líneas 195-257)
- **Original:** Mensajes sobre "Join with us and save the world", charity work
- **Cambios:**
  - Slide 1: "Somos Iglesia, NO Denominaciones" + descripción SINODE
  - Slide 2: "Construyendo Juntos" + construcción colectiva
  - Slide 3: "Centrados en Cristo" + discernimiento bíblico
- **Impacto:** 3 slides adaptados con filosofía SINODE

### 2. **What We Are Doing** (Líneas 280-317)
- **Original:** Education, Rice for Life, Health, Water (charity initiatives)
- **Cambios:**
  - Bases Doctrinales
  - Discernimiento Bíblico
  - Crecimiento Espiritual
  - Proyectos de Impacto
- **Impacto:** 4 áreas ministeriales sustituyen causes de caridad

### 3. **About Section** (Líneas 330-371)
- **Original:** "Make a donation" + "Become a Volunteer" + "Give Scholarship"
- **Cambios:**
  - "Participa Activamente" - participación en comunidad
  - "Colabora como Voluntario" - dones para impacto
  - "Accede a Recursos" - biblioteca digital
- **Impacto:** Reenfoque desde donaciones a participación activa

### 4. **Popular Causes → Áreas de Ministerio** (Líneas 385-537)
- **Original:** 6 causas de caridad con formularios de donación
- **Cambios:**
  1. Formación Espiritual
  2. Discernimiento Bíblico
  3. Comunidad y Conexión
  4. Impacto Social
  5. Testimonios Vivos
  6. Biblioteca Digital
- **Impacto:** Card widgets reconfigurados como ministerios SINODE
- **Nota:** Se mantienen placeholders de imágenes

### 5. **Events Section** (Líneas 551-627)
- **Original:** Charity events, fundraising events
- **Cambios:**
  1. Encuentro de Formación Doctrinal
  2. Jornadas de Construcción Colectiva
  3. Conferencias de Crecimiento Espiritual
- **Impacto:** 3 eventos reconfigurados para SINODE
- **Nota:** Fechas genéricas ("Próximamente 2025") para flexibilidad

### 6. **Gallery → Biblioteca Visual** (Líneas 644-760)
- **Original:** "Best Gallery" de proyectos charity
- **Filtros actualizados:**
  - "Doctrina" (en lugar de "Food")
  - "Discernimiento" (en lugar de "Home")
  - "Formación" (en lugar de "Education")
  - "Proyectos" (en lugar de "Blood")
  - "Testimonios" (en lugar de "Water")
- **Elementos de galería renombrados:**
  - Bases Doctrinales
  - Discernimiento Bíblico
  - Formación Espiritual
  - Proyectos Comunitarios
  - Testimonios Vivos
- **Impacto:** 6 elementos de galería adaptados

### 7. **Donation Form → Únete a la Comunidad** (Líneas 770-850)
- **Original:** Donation amount, frequency, payment details
- **Cambios:**
  - **Información Personal:** Nombre + Área de Interés (selector)
  - **Información de Contacto:** Email, Teléfono, Mensaje
  - **Áreas disponibles:**
    - Bases Doctrinales
    - Discernimiento Bíblico
    - Formación Espiritual
    - Proyectos de Impacto
    - Testimonios Vivos
    - Biblioteca Digital
  - Botón: "Enviar Solicitud" (en lugar de "Donate Now")
- **Impacto:** Formulario completamente transformado de donación a voluntariado

### 8. **FAQ Section** (Líneas 852-936)
- **Original:** Business-related FAQs
- **Cambios:**
  - Encabezado: "¿Por Qué Unirte?" (en lugar de "FAQ")
  - Primer item: "¿Qué ofrece SINODE?" + descripción adaptada
- **Nota:** Contenido adicional mantiene placeholders por brevedad

### 9. **Team Members → Facilitadores y Colaboradores** (Líneas 949-1004)
- **Original:** "Meet our Volunteers" - Moana Siqual (Blood Donor), Anu Sparkle (Teacher)
- **Cambios:**
  - Encabezado: "Nuestros Facilitadores y Colaboradores"
  - Rol 1: "Facilitador SINODE" - Discernimiento Bíblico
  - Rol 2: "Coordinador SINODE" - Formación Espiritual
  - Cambio de estructura: Birth date → Enfoque, Location → Región
- **Impacto:** 2 perfiles de colaboradores adaptados

### 10. **Blog Section** (Líneas 1069-1188)
- **Original:** "Recent Blog" - generic posts
- **Cambios:**
  - Encabezado: "Discernimiento y Formación"
  - Descripción: Contenido sobre doctrina, discernimiento y vivencia espiritual
  - **Post 1:** "¿Qué es la Desinstitucionalización de la Fe?"
  - **Post 2:** "Construcción Colectiva: Modelos de Iglesia Participativa"
  - **Post 3:** "Discernimiento Bíblico: Unidad en lo Esencial, Libertad en lo Secundario"
  - Autor: "Equipo SINODE" (todos)
  - Fecha: "Dec 2024" (actualizada)
- **Impacto:** 3 posts de blog adaptados a temas SINODE

### 11. **Logos Reemplazados** (assets/img/)
- **Original:** Logo genérico de Charities
- **Cambios:**
  - `logo.png` ← logo-sinode-transparente.png
  - `logo-light.png` ← logo-sinode-azul.png
  - `favicon.png` ← christianity-32.png
- **Impacto:** Branding completamente actualizado a SINODE

---

## 🔒 Secciones NO Modificadas

- ✅ **Estructura HTML completa** - Intacta
- ✅ **Archivos CSS** (style.css, bootstrap, etc.) - Sin cambios
- ✅ **JavaScript** (owl.carousel, isotope, etc.) - Sin cambios
- ✅ **Paths de imágenes** - Mantenidos en original
- ✅ **Navegación** - Estructura intacta (solo menú Blog/Events son referencias)
- ✅ **Footer** - Intacto

---

## 📝 Puntos de Edición Segura

### Para modificar contenido en el futuro:

#### Cambiar títulos de secciones:
- Busca: `<h2>` dentro de `.site-heading`
- Ejemplo: Línea 1069: `<h2>Discernimiento y Formación</h2>`

#### Cambiar descripciones:
- Busca: `<p>` inmediatamente después de `<h2>`
- Ejemplo: Línea 1071: Párrafo de descripción

#### Cambiar textos de cards:
- Busca: `<h4>` dentro de `.info`
- Ejemplo: Línea 400: "Formación Espiritual"

#### Cambiar descripciones de áreas de ministerio:
- Busca: `<p>` dentro de `.info`
- Mantén estructura de cards (no cambiar `<div class="progress-box">`)

#### Cambiar posts de blog:
- Busca: `<h4>` dentro de `.title`
- Busca: `<p>` dentro de `.info` para descripción

#### Cambiar colaboradores:
- Busca: `<h3>` para nombre
- Busca: `<h5>` para rol
- Busca: `<ul>` dentro de `.title` para atributos

---

## 🖼️ Placeholders de Imágenes

**IMPORTANTE:** La plantilla mantiene todos los placeholders de imágenes originales. Para producir imágenes reales:

Ver archivo: `GUIA-PRODUCCION-IMAGENES.md` (incluido en este folder)

---

## 🚀 Consideraciones Técnicas

### Responsive Design
- ✅ Bootstrap 5 intacto
- ✅ Grid system sin cambios
- ✅ Media queries funcionales
- ✅ Mobile-first approach preservado

### Componentes JavaScript
- ✅ Owl Carousel (events, blog)
- ✅ Isotope/Mixitup (galería)
- ✅ Bootstrap accordion (FAQ)
- ✅ Animaciones CSS (animate.css)

### Performance
- ✅ Archivos CSS/JS originales
- ✅ Estructura optimizada preservada
- ✅ Carga de imágenes eficiente

---

## 📊 Estadísticas de Cambios

| Elemento | Original | Modificado | Porcentaje |
|----------|----------|-----------|-----------|
| Títulos | 10+ | 10+ | 100% |
| Descripciones | 10+ | 10+ | 100% |
| Card items | 6 | 6 | 100% |
| Imágenes | Genéricas | Logos SINODE | Logos: 3/3 |
| Formularios | 1 (donación) | 1 (voluntariado) | 100% |
| Blog posts | 3 | 3 | 100% |
| HTML tags | ~2000 | ~2000 | <1% modificado |

---

## 💾 Archivos en web-output-2/

```
web-output-2/
├── index.html                    ← Archivo principal (modificado)
├── assets/
│   ├── img/
│   │   ├── logo.png              ← Reemplazado (SINODE)
│   │   ├── logo-light.png        ← Reemplazado (SINODE)
│   │   ├── favicon.png           ← Reemplazado (SINODE)
│   │   └── [otros placeholders]  ← Mantenidos
│   ├── css/                       ← Sin cambios
│   └── js/                        ← Sin cambios
├── style.css                      ← Sin cambios
├── GUIA-CAMBIOS.md               ← Este archivo
├── MAPA-INYECCION.md             ← Detalles de cada cambio
└── GUIA-PRODUCCION-IMAGENES.md   ← Guía para generar imágenes
```

---

## ✨ Próximos Pasos

1. **Validar en navegador:**
   - Abre `web-output-2/index.html` en Chrome/Firefox
   - Verifica responsive design (desktop, tablet, mobile)
   - Prueba interactividad (carousels, accordion, botones)

2. **Personalizar (opcional):**
   - Cambiar textos según necesidad
   - Reemplazar placeholders con imágenes reales (ver GUIA-PRODUCCION-IMAGENES.md)
   - Ajustar colores en CSS si es necesario

3. **Producción:**
   - Deploy a servidor web
   - Configurar emails en formulario de voluntariado
   - Implementar backend para formularios

---

## 📞 Soporte

Para preguntas sobre:
- **Cambios de contenido:** Ver secciones "Puntos de Edición Segura"
- **Imágenes:** Ver `GUIA-PRODUCCION-IMAGENES.md`
- **Detalles técnicos:** Ver `MAPA-INYECCION.md`

---

**Generado:** Diciembre 2024
**Plantilla Original:** Charities (index-6.html)
**Adaptación:** SINODE - Plataforma Eclesiástica Digital
**Filosofía:** Template-Injection Workflow - SOLO TEXTO MODIFICADO
