# SINODE Landing Page - Instrucciones para Claude

## Estado del Proyecto: COMPLETADO

Landing page para SINODE (Somos Iglesia, NO Denominaciones) desarrollada mediante inyección de contenido en una plantilla HTML profesional de ThemeForest.

## Estructura Actual

```
template-injection-demo/
├── .claude/                # Configuración Claude Code
├── docs/                   # Documentación del proyecto
│   ├── GUIA-IMAGENES.md   # Guía para gestionar imágenes y textos
│   ├── ESTADO-PROYECTO.md # Estado del proyecto
│   └── ...
├── input/                  # Archivos de entrada
│   ├── brand/             # Contenido de marca (colores, logos, tono)
│   └── template/          # Plantilla HTML original
├── scripts/               # Scripts de Python (tests, verificación)
├── screenshots/           # Capturas de pantalla
├── web-output-2/          # SITIO WEB FINAL
└── README.md              # Documentación principal
```

## Archivo Principal

El sitio web está en:
```
web-output-2/index.html
```

## Paleta de Colores Oficial

| Color | Código | Uso |
|-------|--------|-----|
| Azul profundo | `#1E3A8A` | Títulos, headers, fondos principales |
| Verde esperanza | `#10B981` | Acentos, iconos, enlaces destacados |
| Blanco | `#FFFFFF` | Fondos |
| Gris | `#6B7280` | Texto secundario |

**IMPORTANTE:** No usar amarillo/dorado (#c9a03f). Ya fue reemplazado por verde.

## Reglas de Edición

### Permitido
- Modificar textos dentro de tags HTML
- Reemplazar imágenes manteniendo el mismo nombre
- Ajustar colores usando la paleta oficial
- Agregar nuevas secciones siguiendo el patrón existente

### No Permitido
- Modificar estructura de carpetas
- Cambiar paths de imágenes en el HTML
- Eliminar secciones sin consultarlo
- Usar colores fuera de la paleta

## Secciones del Sitio

1. Header - Navegación con logo y menú
2. Banner - Slider principal
3. Somos Iglesia - 4 versículos
4. No Somos - Aclaración
5. Fundamentos - Cimientos de la fe
6. Comunidad - Un cuerpo, muchos miembros
7. Participa - Proyectos con estados de avance
8. CTA Doctrina - Enlace a doctrina.sinode.org
9. Blog - Artículos y reflexiones
10. Galería - Biblioteca visual
11. Banner Misión - Mensaje de impacto
12. Únete - Formulario + FAQ
13. Facilitadores - Equipo
14. Partners - Logos
15. Footer - Contacto y enlaces

## Commits Realizados

- `7caa27e` - Reemplazar color dorado por verde esperanza
- `a2e62c6` - Mejoras estructurales y contenido actualizado
- `718d59c` - Iconos, colores y mayúsculas corregidos
- `6ccbbe4` - Navegación interna, FAQ y footer reestructurados
- `fa8538f` - Aplicar paleta de colores SINODE
- `26ce554` - Initial commit: SINODE landing page

## Para Modificaciones Futuras

Ver la guía completa en `docs/GUIA-IMAGENES.md` para:
- Cambiar el logo
- Reemplazar imágenes placeholder
- Modificar textos
- Personalizar colores

## Enlaces

- Repositorio: https://github.com/planckc/sinode
- Doctrina SINODE: https://doctrina.sinode.org

---

**Última actualización:** 2025-12-02
**Estado:** Sitio web completado, pendiente de personalización de imágenes
