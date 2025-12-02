# Contexto del Proyecto: Template Injection Demo

## 🎯 Propósito de este Proyecto

Este es un **proyecto demo** del workflow `template-injection` de **claude-flows**.

**NO es un proyecto funcional**, sino una **estructura de carpetas preparada** para demostrar cómo usar el workflow de inyección de contenido en plantillas HTML profesionales.

## 🏗️ Arquitectura del Workflow

### Filosofía: IA como "Inyector de TEXTO ÚNICAMENTE"

Este workflow es **único** en el ecosistema claude-flows:

- ❌ **NO genera código frontend** desde cero
- ❌ **NO usa** el skill `frontend-design`
- ❌ **NO modifica** estructura HTML o componentes visuales
- ⚠️ **SÍ reemplaza imágenes** PERO en su ubicación original de la plantilla
- ❌ **NO modifica paths** de imágenes (se mantienen iguales)
- ❌ **NO crea carpetas nuevas** para assets
- ✅ **SÍ preserva** diseño profesional original AL 100%
- ✅ **SÍ inyecta** SOLO contenido TEXTUAL quirúrgicamente
- ✅ **SÍ respeta** integridad técnica y visual ABSOLUTA

**Rol de la IA:** Reemplazador de textos + Reemplazador de imágenes (en su ubicación original).

## 📁 Estructura del Proyecto

```
template-injection-demo/
│
├── input/                          # 📥 INPUTS (usuario coloca aquí)
│   ├── template/                   # Plantilla Envato/ThemeForest COMPLETA
│   │   ├── index.html             # ⚠️ SE COPIA TAL CUAL
│   │   ├── index-2.html           # ⚠️ SE COPIA TAL CUAL
│   │   ├── css/                   # ⚠️ SE COPIA TAL CUAL
│   │   ├── js/                    # ⚠️ SE COPIA TAL CUAL
│   │   ├── images/                # ⚠️ SE COPIA TAL CUAL
│   │   └── documentation.html     # ⚠️ SE COPIA TAL CUAL
│   │
│   └── brand/                      # Contenido de marca
│       ├── textos.md              # Contenido textual
│       └── imagenes/              # Imágenes de marca (logo, fotos, etc.)
│
├── src/                            # 📤 OUTPUT (generado por workflow)
│   └── [Copia exacta de plantilla con SOLO textos modificados]
│
├── .claude/
│   └── CLAUDE.md                   # Este archivo
│
├── GUIA-CAMBIOS.md                 # Guía para modificaciones futuras
├── MAPA-INYECCION.md               # Registro de cambios de TEXTO realizados
├── README.md                       # Instrucciones de uso
├── SETUP.md                        # Setup instructions
└── .gitignore                      # Git config
```

## 🔄 Flujo de Trabajo

### 1. Preparación (Usuario)
- Descargar plantilla HTML de Envato/ThemeForest
- Colocar plantilla **COMPLETA** en `input/template/`
- Preparar contenido en `input/brand/`:
  - `textos.md` - Contenido textual
  - `imagenes/` - Imágenes de marca (logo, fotos, etc.)

### 2. Análisis (IA - Explore subagent)
- Explorar estructura de `input/template/`
- Leer documentación de plantilla
- Identificar variantes disponibles (index1, index2, etc.)
- Recomendar variante óptima según contenido de marca

### 3. Selección (Usuario)
- Revisar recomendaciones de la IA
- Seleccionar variante de plantilla a usar

### 4. Copia Completa (IA - Bash)
- **Copiar TODA la plantilla** a `src/` SIN modificar NADA
- Preservar estructura completa: HTML, CSS, JS, images/, assets/

### 5. Mapeo de Contenido (IA - Read + Grep)
- **Textos**: Identificar placeholders en HTML (`<h1>`, `<p>`, etc.)
- **Imágenes**: Identificar qué imágenes de la plantilla reemplazar
  - La plantilla tiene su propia carpeta (ej: `src/images/`)
  - Usuario trae imágenes en `input/brand/imagenes/`
  - Mapear qué archivo de marca reemplaza a cuál de la plantilla

### 6. Inyección de Contenido (IA - Edit + Bash)
- **Textos**: Reemplazo quirúrgico con Edit tool
  - Modificar contenido de tags HTML (inner text)
  - **NO modificar**: atributos, paths, src, href

- **Imágenes**: Reemplazo de archivos (Bash)
  - **Copiar** imágenes de usuario a carpeta de plantilla
  - Ejemplo: `input/brand/imagenes/logo.png` → `src/images/logo.png`
  - **NO modificar paths** en el HTML
  - **Respetar estructura** de carpetas de la plantilla

### 7. Validación (IA - code-reviewer)
- Verificar sintaxis HTML (que no se rompió)
- Verificar que SOLO se modificó texto
- Confirmar que paths originales están intactos
- Generar checklist de QA

### 8. Documentación (IA - Write)
- Generar `GUIA-CAMBIOS.md`
- Crear `MAPA-INYECCION.md` (SOLO cambios de texto)
- Documentar qué textos se reemplazaron

## 🛠️ Componentes Clave del Workflow

### Subagents utilizados:
1. **Explore** - Análisis de plantilla y variantes
2. **code-reviewer** - Validación técnica (opcional)

### Tools utilizados:
- **Read** - Leer HTML, documentación, contenido de marca
- **Grep** - Buscar placeholders de TEXTO únicamente
- **Edit** - Modificación quirúrgica de TEXTO
- **Write** - Generar documentación
- **Bash** - Copiar plantilla completa a src/

### ❌ Componentes NO utilizados:
- **frontend-design skill** - Va contra la filosofía
- **code-architect** - No se diseña arquitectura nueva

## ⚡ Ejecución del Workflow

Cuando ejecutes el workflow `template-injection` en claude-flows:

```bash
/template-injection
```

El sistema:
1. Te pedirá confirmar inputs
2. Analizará la plantilla
3. Te recomendará variante
4. Esperará tu selección
5. **Copiará TODO** de `input/template/` a `src/`
6. Ejecutará inyección de **SOLO TEXTO**
7. Generará documentación
8. Te mostrará resultado en `src/`

## 🎯 Casos de Uso Ideales

Este workflow es perfecto para:

- ✅ **Plantillas de Envato/ThemeForest** totalmente funcionales
- ✅ **Sitios corporativos** donde solo cambias textos
- ✅ **Landing pages premium** con diseño perfecto
- ✅ Proyectos donde **el diseño NO se toca**
- ✅ Plantillas con **imágenes genéricas pero aceptables**

## ❌ Cuándo NO usar este workflow

- Si necesitas cambiar **imágenes** → Hazlo manualmente después
- Si necesitas **rediseño visual** → Usa workflow `landing-page`
- Si la plantilla es **React/Vue/Angular** → Requiere workflow diferente
- Si quieres **modificar colores** → Hazlo manualmente después

## 🔐 Consideraciones Técnicas

### Preservación ABSOLUTA de:
- Estructura HTML completa (100%)
- Todos los atributos HTML
- Componentes visuales (cards, buttons, modals)
- Sistema JavaScript completo
- Archivos CSS sin modificar
- **TODAS las imágenes y paths originales**
- Animaciones e interactividad
- Responsive design
- **Assets folder completo**

### Modificaciones permitidas:
- ✅ Inner text de tags HTML: `<h1>Texto aquí</h1>`
- ✅ Contenido de párrafos: `<p>Texto aquí</p>`
- ✅ Textos de enlaces: `<a href="#">Texto aquí</a>`
- ✅ Textos de botones: `<button>Texto aquí</button>`
- ✅ **Archivos de imágenes**: Reemplazar en su carpeta original
  - Ejemplo: `src/images/logo.png` se reemplaza con `input/brand/imagenes/logo.png`
  - **NO se modifica** el path en el HTML
  - Se mantiene la estructura de carpetas de la plantilla

### Modificaciones PROHIBIDAS:
- ❌ Atributos HTML (`class`, `id`, `src`, `href`)
- ❌ Archivos CSS (ni siquiera variables)
- ❌ Archivos JavaScript
- ❌ Tags `<img>` y sus atributos
- ❌ Estructura de carpetas
- ❌ Paths de archivos en el HTML
- ❌ Crear carpetas nuevas para assets

## 📊 Diferencias vs Otros Workflows

| Aspecto | landing-page | template-injection |
|---------|-------------|-------------------|
| Diseño | Generado por IA | Plantilla profesional 100% preservada |
| Imágenes | Generadas/requeridas | De la plantilla (NO se tocan) |
| CSS | Generado | De la plantilla (NO se toca) |
| JavaScript | Generado | De la plantilla (NO se toca) |
| Input | Descripción de proyecto | Plantilla + Textos de marca |
| Componente clave | frontend-design | Bash (copy) + Edit (texto) |
| Modificación | Total (código nuevo) | Mínima (solo texto) |
| Tiempo | 2-4 horas | 30-45 minutos |

## 🚀 Próximos Pasos

1. **Preparar inputs**: Coloca plantilla completa y textos de marca
2. **Ejecutar workflow**: `/template-injection` en claude-flows
3. **Validar resultado**: Abrir `src/index.html` en navegador
4. **Modificaciones manuales**: Si necesitas cambiar imágenes, hazlo después manualmente

## 📝 Notas de Mantenimiento

### Para cambiar textos después:
- Edita directamente `src/index.html`
- Busca el texto actual y cámbialo

### Para cambiar imágenes después:
- **Opción 1**: Reemplaza archivos en `src/images/` (mantén mismo nombre)
- **Opción 2**: Edita `src/index.html` y cambia el `src=""` del `<img>`

### Para cambiar colores después:
- Edita `src/css/style.css` manualmente
- Busca variables CSS (`:root`) o colores específicos

---

**Workflow generado por:** `template-injection`
**Sistema:** claude-flows v1.2.0
**Fecha:** 2025-11-28
**Filosofía:** CERO modificaciones estructurales. SOLO texto.
