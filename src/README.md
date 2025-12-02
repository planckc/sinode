# Carpeta: Sitio Generado (Output)

## ⚠️ Esta carpeta está vacía hasta que ejecutes el workflow

## Qué contendrá después de ejecutar template-injection

Una vez ejecutes el workflow `template-injection`, esta carpeta contendrá una **copia completa** de la plantilla con contenido inyectado:

```
src/
├── index.html              # Plantilla con TEXTOS modificados
├── css/
│   ├── style.css           # ⚠️ IGUAL que la plantilla original
│   └── ...
├── js/
│   ├── main.js             # ⚠️ IGUAL que la plantilla original
│   └── ...
├── images/                 # Carpeta de la plantilla
│   ├── logo.png            # ✅ REEMPLAZADO con tu logo
│   ├── hero-bg.jpg         # ✅ REEMPLAZADO con tu imagen
│   └── ...                 # Otras imágenes (originales o reemplazadas)
└── ...                     # Resto de archivos (sin modificar)
```

## Cambios que habrá aplicado la IA

### ✅ Modificaciones realizadas:

**1. Textos Reemplazados**
- Contenido genérico → Contenido de tu marca
- Solo el texto dentro de tags HTML
- Ejemplos:
  - `<h1>Generic Title</h1>` → `<h1>Tu Título</h1>`
  - `<p>Lorem ipsum...</p>` → `<p>Tu descripción...</p>`

**2. Imágenes Reemplazadas** (en su ubicación original)
- Archivos de la plantilla → Tus archivos de marca
- **Paths NO modificados** en el HTML
- Ejemplos:
  - `src/images/logo.png` (archivo reemplazado con el tuyo)
  - `<img src="images/logo.png">` (path sin cambios en HTML)

### ❌ Preservado SIN cambios:

- Estructura HTML completa (tags, clases, IDs)
- Archivos CSS (sin tocar)
- Archivos JavaScript (sin tocar)
- Atributos HTML (`src`, `href`, `class`, etc.)
- Sistema de navegación
- Animaciones e interactividad
- Estructura de carpetas
- Componentes visuales

## Ejemplo de lo que SÍ se modifica

```html
<!-- ANTES (plantilla original): -->
<h1 class="hero-title">Welcome to Our Amazing Template</h1>
<p class="hero-subtitle">Lorem ipsum dolor sit amet</p>
<img src="images/logo.png" alt="Logo" class="brand-logo">

<!-- DESPUÉS (con tu contenido): -->
<h1 class="hero-title">Transforma tu Negocio Digital</h1>
<p class="hero-subtitle">Soluciones innovadoras para empresas modernas</p>
<img src="images/logo.png" alt="Logo" class="brand-logo">
<!-- ⬆️ El path NO cambió, pero el archivo logo.png ahora es el tuyo -->
```

## Ejemplo de lo que NO se modifica

```html
<!-- Estos elementos PERMANECEN IGUALES: -->
<div class="container">  <!-- ✅ Clases preservadas -->
<script src="js/main.js"></script>  <!-- ✅ Scripts intactos -->
<link rel="stylesheet" href="css/style.css">  <!-- ✅ CSS sin tocar -->
```

## Validación post-generación

Después de que el workflow genere el sitio, verifica:

- [ ] Abre `index.html` en el navegador
- [ ] Revisa que todos los textos se hayan reemplazado correctamente
- [ ] Verifica que tus imágenes carguen (deberían verse tus logos/fotos)
- [ ] Prueba la navegación y funcionalidad
- [ ] Revisa responsive design en diferentes tamaños
- [ ] Verifica que JavaScript funcione (modals, sliders, etc.)

## Estructura de Archivos

La estructura será **idéntica** a la de `input/template/`:

```
Si la plantilla tiene:
input/template/
├── index.html
├── css/
├── js/
├── images/
└── fonts/

El output será:
src/
├── index.html       (con textos modificados)
├── css/             (copia exacta)
├── js/              (copia exacta)
├── images/          (con algunas imágenes reemplazadas)
└── fonts/           (copia exacta)
```

## Documentación generada

Junto con esta carpeta, se generarán:

- **[GUIA-CAMBIOS.md](../GUIA-CAMBIOS.md)** - Cómo hacer modificaciones futuras
- **[MAPA-INYECCION.md](../MAPA-INYECCION.md)** - Registro detallado de cambios

## Si algo salió mal

Si encuentras problemas:

1. **Textos no reemplazados**:
   - Algunos pueden estar en JavaScript (edita `src/js/*.js`)
   - Revisa `MAPA-INYECCION.md` para ver qué se modificó

2. **Imágenes no cargaron**:
   - Verifica que los nombres coincidan con los de la plantilla
   - Revisa que las imágenes estén en `src/images/` (o la carpeta que use la plantilla)

3. **Algo se rompió**:
   - Compara con `input/template/` para ver qué cambió
   - Revisa la consola del navegador (F12 → Console)

## Próximos pasos

Una vez validado el sitio:

1. **Copia esta carpeta completa** a tu ubicación final
2. **Abre con Claude Code** para futuras modificaciones
3. **Consulta GUIA-CAMBIOS.md** para saber qué puedes editar

---

**Recuerda:** Este folder contiene una copia de la plantilla con mínimas modificaciones (textos + archivos de imagen). La estructura original se preserva al 100%.
