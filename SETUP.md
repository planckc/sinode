# Configuración y Setup - Template Injection Demo

## ⚠️ Importante

Este es un **proyecto demo** del workflow `template-injection`. No es un sitio funcional hasta que:

1. Coloques una plantilla HTML en `input/template/`
2. Agregues contenido de marca en `input/brand/`
3. Ejecutes el workflow `template-injection`

## Paso 1: Preparar Plantilla HTML

### 1.1 Descargar Plantilla

Descarga una plantilla profesional de:
- [ThemeForest](https://themeforest.net/category/site-templates) (Premium)
- [Envato Elements](https://elements.envato.com/web-templates) (Suscripción)
- Plantilla propia o de otro proveedor

### 1.2 Extraer y Colocar

```bash
# Extrae el .zip de la plantilla
unzip plantilla-descargada.zip

# Copia TODO el contenido a input/template/
cp -r plantilla-descargada/* input/template/
```

**Verifica que tengas:**
```
input/template/
├── index.html          ✅
├── css/               ✅
├── js/                ✅
├── images/            ✅
└── documentation.html  ✅ (opcional pero muy útil)
```

## Paso 2: Preparar Contenido de Marca

### 2.1 Crear Archivo de Textos

Crea `input/brand/textos.md`:

```markdown
# Contenido de Marca - [Tu Empresa]

## Hero Section (Sección Principal)
**Título principal:** Transforma tu Negocio Digital
**Subtítulo:** Soluciones innovadoras para empresas modernas
**Call to Action:** Comenzar Ahora

## About (Acerca de)
**Título:** ¿Quiénes Somos?
**Descripción:**
Somos una empresa líder en transformación digital con más de 10 años de experiencia.
Ayudamos a empresas a alcanzar su máximo potencial mediante tecnología de vanguardia.

## Services / Features (Servicios)
### Servicio 1
**Título:** Consultoría Estratégica
**Descripción:** Diseñamos estrategias digitales que impulsan el crecimiento.

### Servicio 2
**Título:** Desarrollo a Medida
**Descripción:** Creamos soluciones tecnológicas personalizadas.

### Servicio 3
**Título:** Soporte Continuo
**Descripción:** Mantenimiento y optimización constante.

## Contact (Contacto)
**Email:** hola@tuempresa.com
**Teléfono:** +1 (555) 123-4567
**Dirección:** Av. Principal 123, Ciudad, País
**Horario:** Lunes a Viernes, 9:00 - 18:00

## Footer
**Copyright:** © 2025 Tu Empresa. Todos los derechos reservados.
**Slogan:** Innovación que transforma
```

### 2.2 Agregar Imágenes

Crea la carpeta y añade tus imágenes:

```bash
mkdir -p input/brand/imagenes
```

Coloca tus archivos:
```
input/brand/imagenes/
├── logo.png              # Logo de la empresa (500x500px recomendado)
├── logo-white.png        # Versión blanca del logo (para fondos oscuros)
├── hero-bg.jpg           # Imagen de fondo Hero (1920x1080px mínimo)
├── about-team.jpg        # Foto del equipo
├── servicio-1.jpg        # Imagen servicio 1
├── servicio-2.jpg        # Imagen servicio 2
└── servicio-3.jpg        # Imagen servicio 3
```

**Formatos recomendados:**
- PNG para logos (con transparencia)
- JPG para fotografías
- SVG para iconos (opcional)

### 2.3 Nombres de Archivos de Imágenes

⚠️ **IMPORTANTE:** Los nombres de tus imágenes deben coincidir con los de la plantilla.

**Recomendación:**
1. Primero explora `input/template/images/` (o la carpeta de imágenes de tu plantilla)
2. Renombra tus archivos para que coincidan con los de la plantilla
3. Ejemplo: Si la plantilla tiene `logo.png`, tu archivo debe llamarse `logo.png`

El workflow:
- **SÍ reemplazará** archivos de imagen en su ubicación original
- **NO modificará** paths en el HTML
- **NO creará** carpetas nuevas para assets

## Paso 3: Ejecutar el Workflow

### 3.1 Desde Claude Code

Si estás en el proyecto `claude-flows` con Claude Code activo:

```
/template-injection
```

### 3.2 Proceso del Workflow

El workflow ejecutará automáticamente:

1. **Análisis** (10 min)
   - Explora estructura de `input/template/`
   - Lee documentación si existe
   - Identifica variantes disponibles

2. **Selección** (5 min)
   - IA recomienda mejor variante
   - Usuario confirma o selecciona otra

3. **Mapeo** (10 min)
   - Identifica placeholders de texto
   - Detecta imágenes a reemplazar
   - Localiza variables CSS

4. **Inyección** (30 min)
   - Copia TODA la plantilla a src/
   - Reemplaza textos en HTML (solo inner text)
   - Reemplaza archivos de imágenes en su ubicación original

5. **Validación** (5 min)
   - Revisa sintaxis HTML
   - Verifica paths de assets
   - Genera checklist de QA

6. **Documentación** (10 min)
   - Crea `GUIA-CAMBIOS.md`
   - Genera `MAPA-INYECCION.md`

**Tiempo total estimado:** ~1.5 horas

## Paso 4: Validar Resultado

### 4.1 Preview en Navegador

```bash
# Abre el sitio generado
open src/index.html
# O en Windows:
start src/index.html
# O en Linux:
xdg-open src/index.html
```

### 4.2 Checklist de Validación

- [ ] **Textos**: Verifica que todo el contenido se haya reemplazado
- [ ] **Imágenes**: Confirma que tus imágenes de marca carguen
- [ ] **Navegación**: Prueba todos los enlaces
- [ ] **Responsive**: Abre en mobile/tablet
- [ ] **Funcionalidad**: Testa modals, forms, sliders
- [ ] **Performance**: Velocidad de carga aceptable

### 4.3 Si hay Problemas

Consulta:
- `MAPA-INYECCION.md` - Ver qué se modificó exactamente
- `GUIA-CAMBIOS.md` - Cómo hacer ajustes manuales

## Paso 5: Deployment (Opcional)

### 5.1 Preparar para Producción

```bash
# Optimizar imágenes (si tienes imagemin instalado)
imagemin src/images/* --out-dir=src/images
# La plantilla puede tener otras carpetas de imágenes, ajusta según corresponda
```

### 5.2 Opciones de Hosting

**Hosting estático (gratis):**
- [Netlify](https://www.netlify.com/) - Drag & drop
- [Vercel](https://vercel.com/) - Git integration
- [GitHub Pages](https://pages.github.com/) - Desde repo
- [Cloudflare Pages](https://pages.cloudflare.com/) - Edge deployment

**Hosting tradicional:**
- Cualquier servidor con Apache/Nginx
- FTP upload a hosting compartido

### 5.3 Deploy Rápido con Netlify

```bash
# Instala Netlify CLI
npm install -g netlify-cli

# Deploy
cd src/
netlify deploy --prod
```

## Paso 6: Mantenimiento

### Modificar Contenido

Para cambios futuros de texto:
```bash
# Edita directamente el HTML
nano src/index.html
# O usa tu editor favorito
```

Para cambiar imágenes:
```bash
# Reemplaza el archivo en la carpeta de la plantilla (mantén el mismo nombre)
cp nueva-imagen.jpg src/images/logo.jpg
# Ajusta el path según la estructura de tu plantilla
```

### Actualizar Contenido de Marca

Si necesitas cambios grandes:

1. Actualiza archivos en `input/brand/`
2. Ejecuta el workflow de nuevo
3. Revisa diferencias con versión anterior

## Troubleshooting

### Problema: Imágenes no cargan

**Solución:**
- Verifica que los archivos estén en la carpeta de imágenes de la plantilla (ej: `src/images/`)
- Confirma que los nombres coincidan exactamente con los que espera el HTML
- Revisa nombres de archivo (case-sensitive en Linux)

### Problema: Textos no se reemplazaron

**Solución:**
- Revisa `MAPA-INYECCION.md` para ver qué se modificó
- Algunos textos pueden estar en JavaScript (archivos `.js`)
- Contenido dinámico requiere edición manual

### Problema: Algunos textos quedaron sin reemplazar

**Solución:**
- Algunos textos pueden estar en archivos JavaScript
- Revisa `MAPA-INYECCION.md` para ver qué se modificó
- Edita manualmente los textos restantes en `src/index.html`

## Recursos Adicionales

- [Documentación Template Injection](../../docs/workflows/template-injection.md)
- [Guía de Usuario Claude Flows](../../docs/GUIA-USUARIO.md)
- [Catálogo de Workflows](../../workflows/catalog.yml)

## Soporte

Si tienes problemas:
1. Revisa `GUIA-CAMBIOS.md` en este proyecto
2. Consulta la documentación de claude-flows
3. Revisa los logs del workflow

---

**Workflow:** `template-injection`
**Versión:** 1.0.0
**Actualizado:** 2025-11-28
