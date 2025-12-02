# SINODE - Landing Page

**Somos Iglesia, NO Denominaciones**

Landing page para SINODE, una comunidad cristiana enfocada en la edificación del cuerpo de Cristo más allá de las barreras denominacionales.

## Vista previa

El sitio está disponible en `web-output-2/index.html`. Para previsualizarlo:

```bash
cd web-output-2
python -m http.server 8080
```

Luego abre: http://localhost:8080

## Estructura del proyecto

```
template-injection-demo/
├── .claude/                    # Configuración de Claude Code
│   └── CLAUDE.md              # Instrucciones del proyecto
├── docs/                       # Documentación
│   ├── GUIA-IMAGENES.md       # Guía para gestionar imágenes y textos
│   ├── ESTADO-PROYECTO.md     # Estado del proyecto
│   ├── GUIA-CAMBIOS.md        # Historial de cambios
│   └── ...
├── input/                      # Archivos de entrada
│   ├── brand/                 # Contenido de marca
│   │   ├── colores.md        # Paleta de colores oficial
│   │   ├── logo/             # Logos SINODE
│   │   └── tono-voz.md       # Guía de tono y voz
│   └── template/              # Plantilla HTML original
├── scripts/                    # Scripts de utilidad
│   ├── test_*.py              # Tests de Playwright
│   └── verificacion_*.py      # Scripts de verificación
├── screenshots/                # Capturas de pantalla
├── web-output-2/              # SITIO WEB FINAL
│   ├── index.html             # Página principal
│   ├── assets/                # CSS, JS, imágenes
│   └── style.css              # Estilos personalizados
├── README.md                   # Este archivo
├── SETUP.md                    # Instrucciones de setup
└── LICENSE                     # Licencia
```

## Personalización

### Imágenes y Logo
Ver la guía completa en: [docs/GUIA-IMAGENES.md](docs/GUIA-IMAGENES.md)

**Resumen rápido:**
- Logo: Reemplazar `web-output-2/assets/img/logo.png`
- Imágenes: Reemplazar archivos en `web-output-2/assets/img/`

### Colores oficiales

| Color | Código | Uso |
|-------|--------|-----|
| Azul profundo | `#1E3A8A` | Títulos, headers |
| Verde esperanza | `#10B981` | Acentos, iconos |
| Blanco | `#FFFFFF` | Fondos |
| Gris | `#6B7280` | Texto secundario |

## Secciones del sitio

1. **Header** - Navegación con logo y menú
2. **Banner** - Slider principal con mensaje de bienvenida
3. **Somos Iglesia** - 4 versículos bíblicos fundamentales
4. **No somos** - Aclaración de lo que SINODE NO es
5. **Fundamentos** - Los cimientos de la fe
6. **Comunidad** - Un cuerpo, muchos miembros
7. **Participa** - Proyectos activos con estados de avance
8. **CTA Doctrina** - Llamado a profundizar en doctrina.sinode.org
9. **Blog** - Artículos y reflexiones
10. **Galería** - Biblioteca visual
11. **Banner misión** - Mensaje de impacto
12. **Únete** - Formulario de contacto + FAQ
13. **Facilitadores** - Equipo SINODE
14. **Partners** - Logos de aliados
15. **Footer** - Información de contacto y enlaces

## Tecnologías

- HTML5, CSS3, JavaScript
- Bootstrap 3
- Font Awesome 5
- Owl Carousel
- Isotope (galería)

## Enlaces

- Sitio principal: [sinode.org](https://sinode.org)
- Doctrina: [doctrina.sinode.org](https://doctrina.sinode.org)
- Repositorio: [github.com/planckc/sinode](https://github.com/planckc/sinode)

## Commits recientes

- `7caa27e` - Reemplazar color dorado por verde esperanza
- `a2e62c6` - Mejoras estructurales y contenido actualizado
- `718d59c` - Iconos, colores y mayúsculas corregidos
- `6ccbbe4` - Navegación interna, FAQ y footer reestructurados
- `fa8538f` - Aplicar paleta de colores SINODE

## Licencia

Este proyecto utiliza una plantilla de ThemeForest modificada para SINODE.
