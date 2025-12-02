# Guía de Gestión de Imágenes y Textos - SINODE

Esta guía explica cómo personalizar las imágenes y textos del sitio web SINODE.

## Ubicación de archivos

Todas las imágenes del sitio están en:
```
web-output-2/assets/img/
```

Los logos de marca están en:
```
input/brand/logo/
```

---

## 1. Logo del Header

### Ubicación en el código
```html
<!-- web-output-2/index.html, línea 65-67 -->
<a class="navbar-brand" href="index.html">
    <img src="assets/img/logo.png" class="logo logo-display" alt="Logo">
</a>
```

### Cómo cambiar el logo
1. Prepara tu logo en formato PNG
2. Renómbralo como `logo.png`
3. Cópialo a `web-output-2/assets/img/logo.png`

### Logos SINODE disponibles
Ya tienes estos logos listos para usar en `input/brand/logo/`:

| Archivo | Descripción | Uso recomendado |
|---------|-------------|-----------------|
| `logo-sinode-azul.png` | Fondo azul oscuro | Header con fondo claro |
| `logo-sinode-transparente.png` | Fondo transparente | Header con fondo oscuro |

**Para usar uno de estos logos:**
```bash
# Ejemplo en PowerShell
Copy-Item "input/brand/logo/logo-sinode-transparente.png" "web-output-2/assets/img/logo.png"
```

---

## 2. Imágenes Placeholder

El template usa imágenes placeholder con dimensiones específicas. Debes reemplazarlas con imágenes reales.

### Mapa de imágenes por sección

| Sección | Archivo | Dimensión | Cantidad |
|---------|---------|-----------|----------|
| **Slider/Banner principal** | `2440x1578.png` | 2440x1578 px | 3 |
| **Cards de proyectos** | `800x800.png` | 800x800 px | 6 |
| **Artículos/Blog** | `800x800.png` | 800x800 px | 3 |
| **Portfolio** | `800x800.png`, `500x700.png` | Varios | 6 |
| **Team/Facilitadores** | `800x600.png` | 800x600 px | 3 |
| **Clientes/Partners** | `150x80.png` | 150x80 px | 10 |
| **Banner CTA** | `2440x1578.png` | 2440x1578 px | 1 |

### Cómo reemplazar imágenes

**Opción A: Mantener mismo nombre (recomendado)**
1. Crea tu imagen con las dimensiones correctas
2. Renómbrala con el mismo nombre (`800x800.png`)
3. Reemplaza el archivo en `web-output-2/assets/img/`

**Opción B: Usar nombre diferente**
1. Copia tu imagen a `web-output-2/assets/img/`
2. Edita `index.html` y busca/reemplaza el nombre del archivo

---

## 3. Favicon

### Ubicación
```
web-output-2/assets/img/favicon.png
```

### Cómo cambiar
1. Crea un icono de 32x32 px o 64x64 px
2. Guárdalo como `favicon.png`
3. Reemplaza en `web-output-2/assets/img/favicon.png`

---

## 4. Modificar Textos

### Archivo principal
Todos los textos están en:
```
web-output-2/index.html
```

### Textos clave y su ubicación

| Texto | Línea aprox. | Sección |
|-------|--------------|---------|
| Título del slider | 115-150 | Banner principal |
| "Somos Iglesia" contenido | 200-300 | Sección principal |
| Citas bíblicas | 320-350 | Fundamentos |
| Títulos de proyectos | 440-570 | Edificando juntos |
| Artículos de blog | 635-685 | Artículos y reflexiones |
| Preguntas FAQ | 920-1010 | Preguntas frecuentes |
| Footer | 1320-1400 | Pie de página |

### Cómo modificar textos
1. Abre `web-output-2/index.html` en tu editor
2. Busca el texto que quieres cambiar (Ctrl+F)
3. Modifica solo el contenido entre las etiquetas HTML
4. Guarda el archivo

**Ejemplo:**
```html
<!-- Antes -->
<h2>Artículos y reflexiones</h2>

<!-- Después -->
<h2>Publicaciones de la comunidad</h2>
```

---

## 5. Colores de la marca

### Paleta oficial SINODE

| Color | Código | Uso |
|-------|--------|-----|
| Azul profundo | `#1E3A8A` | Títulos, headers, fondos principales |
| Verde esperanza | `#10B981` | Acentos, iconos, enlaces destacados |
| Blanco | `#FFFFFF` | Fondos |
| Gris | `#6B7280` | Texto secundario |

### Dónde están definidos los colores
- Estilos inline en `index.html`
- CSS principal en `web-output-2/style.css`

---

## 6. Botón "Profundizar" (esquina derecha del menú)

Este botón aparece como un cuadro con borde en el menú. **No es una imagen**, es un botón HTML.

### Ubicación en el código
```html
<!-- web-output-2/index.html, línea 92-94 -->
<li>
    <a href="#profundizar" class="btn btn-theme effect btn-sm">Profundizar</a>
</li>
```

### Cómo modificar el botón
- **Cambiar texto:** Modifica "Profundizar" por otro texto
- **Cambiar enlace:** Modifica `#profundizar` por otra URL
- **Cambiar estilo:** Modifica las clases CSS o agrega estilos inline

---

## 7. Checklist de personalización

- [ ] Logo del header (`logo.png`)
- [ ] Favicon (`favicon.png`)
- [ ] Imágenes del slider (3x `2440x1578.png`)
- [ ] Imágenes de proyectos (6x `800x800.png`)
- [ ] Imágenes de artículos (3x `800x800.png`)
- [ ] Imágenes de team (3x `800x600.png`)
- [ ] Logos de partners (10x `150x80.png`)
- [ ] Textos principales
- [ ] Información de contacto en footer

---

## 8. Previsualización

Para ver los cambios en tiempo real:

```bash
cd web-output-2
python -m http.server 8080
```

Luego abre en el navegador: `http://localhost:8080`

---

## Notas importantes

1. **Respeta las dimensiones** - Las imágenes deben tener las dimensiones indicadas para verse correctamente
2. **Formato PNG o JPG** - Usa PNG para logos con transparencia, JPG para fotos
3. **Optimiza el peso** - Comprime las imágenes para mejor rendimiento
4. **Backup** - Guarda copias de los archivos originales antes de modificar
