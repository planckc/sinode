# Guía de Modificaciones Futuras

## ⚠️ Nota Importante

Este archivo se generará automáticamente DESPUÉS de ejecutar el workflow `template-injection`.

Contendrá instrucciones específicas sobre:
- Cómo modificar textos del sitio
- Dónde encontrar cada sección de contenido
- Qué archivos NO debes tocar
- Cómo actualizar imágenes
- Cómo ajustar colores

## Vista Previa del Contenido

Una vez ejecutado el workflow, este archivo incluirá:

### 1. Estructura del Sitio Generado

```
src/
├── index.html              # Página principal
├── about.html              # Página About (si existe)
├── contact.html            # Página Contact (si existe)
├── css/
│   ├── style.css          # ⚠️ Contiene variables de color
│   └── ...
├── js/
│   └── ...                # ⚠️ NO MODIFICAR (funcionalidad)
└── ...
```

### 2. Puntos de Modificación Segura

#### Textos
- `index.html` líneas XX-YY: Hero section
- `index.html` líneas XX-YY: About section
- `index.html` líneas XX-YY: Services section
- `about.html` líneas XX-YY: Company info

#### Imágenes
- Logo: `src/images/logo.png` → referenciado en línea XX
- Hero image: `src/images/hero-bg.jpg` → línea YY
- Team photo: `src/images/about-team.jpg` → línea ZZ

**Nota:** Los paths exactos dependerán de la estructura de tu plantilla.

### 3. Archivos que NO Debes Modificar

❌ **NUNCA modificar:**
- Archivos JavaScript en `src/js/`
- Estructura HTML (tags, clases, IDs)
- Componentes visuales (cards, buttons, modals)
- Grid/flexbox layouts
- Archivos de frameworks (bootstrap, jquery, etc.)

### 4. Cómo Hacer Cambios Comunes

#### Cambiar un Título
```html
<!-- Busca en src/index.html: -->
<h1>Tu Título Actual</h1>

<!-- Cambia solo el texto: -->
<h1>Nuevo Título</h1>
```

#### Actualizar una Imagen
```bash
# Opción 1: Reemplazar archivo en su ubicación original (mantén mismo nombre)
cp nueva-foto.jpg src/images/hero-bg.jpg

# Opción 2: Agregar nueva imagen
cp nueva-foto.jpg src/images/nueva-foto.jpg
# Luego edita src/index.html y cambia el atributo src=""
```

#### Modificar Colores (Solo si la plantilla usa variables CSS)
```css
/* En src/css/style.css (si la plantilla lo soporta): */
:root {
  --color-primary: #3B82F6;    /* Cambia este valor */
  --color-secondary: #8B5CF6;  /* Y este */
}
```

⚠️ **Nota:** El workflow NO modifica colores. Esto debe hacerse manualmente si lo necesitas.

### 5. Validación Después de Cambios

Después de cualquier modificación:

1. **Abre en navegador** y prueba
2. **Verifica responsive** (mobile/tablet)
3. **Testa funcionalidad** (menús, modals, forms)
4. **Revisa console** del navegador (F12 → Console)

### 6. Cuándo Volver a Ejecutar el Workflow

Ejecuta de nuevo `template-injection` si:
- Actualizas TODO el contenido textual
- Quieres probar otra variante de la plantilla
- Necesitas regenerar el sitio desde cero

Para cambios pequeños (1-2 textos o imágenes), edita manualmente.

---

**Recuerda:** Este archivo se generará con instrucciones específicas de TU sitio después de ejecutar el workflow.
