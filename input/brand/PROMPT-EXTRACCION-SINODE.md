# PROMPT: Extracción de Identidad Misional de SINODE

## 🎯 Contexto General

### ¿Qué estamos construyendo?
Estamos creando una **web informativa** para SINODE usando el workflow `template-injection`. Esta web será de **alto nivel presentacional**, cuyo objetivo es que la audiencia comprenda:
- **Quién es SINODE** (identidad)
- **Qué hace SINODE** (misión)
- **Por qué existe SINODE** (propósito)

**Importante:** NO estamos construyendo la wiki de contenidos detallados. La wiki ya existe en `doctrina.sinode.org`.

### ¿Qué diferencia hay entre la web informativa y la wiki?

| Aspecto | Web Informativa (a construir) | Wiki (doctrina.sinode.org) |
|---------|-------------------------------|---------------------------|
| Propósito | Presentar la identidad de SINODE | Repositorio de contenido detallado |
| Nivel | Alto nivel (categorías) | Detalle (artículos, doctrinas individuales) |
| Audiencia | Personas que descubren SINODE | Miembros que estudian/profundizan |
| Ejemplo | "Por qué la doctrina es importante" | "Doctrina de la Trinidad - versículo por versículo" |

---

## 🎯 Tu Misión

### Objetivo Principal
Visitar la URL **`doctrina.sinode.org`** y extraer información de **alto nivel** sobre la estructura del sitio, sus secciones principales y la esencia misional que cada sección representa.

### Enfoque Crítico
- ✅ **ALTO NIVEL** - Quedarte en la capa de categorías/secciones
- ✅ **IDENTIDAD MISIONAL** - Extraer qué ES y qué HACE SINODE
- ❌ **NO profundizar** en contenidos detallados (artículos individuales, doctrinas específicas)

---

## 📋 Metodología de Trabajo

### Paso 1: Análisis Estructural del Sitio

1. Visita `doctrina.sinode.org`
2. Examina el **menú principal** de navegación
3. Identifica todas las secciones principales del sitio
4. Lista las secciones encontradas

**Ejemplo:**
```
Menú principal encontrado:
1. Inicio
2. Acerca de SINODE
3. Doctrina
4. Proyectos
5. Biblioteca
6. Territorios
7. Contacto
```
Importante : NO te limites a esas secciones son solo de ejemplo, debes extraerlas tu mismo 

### Paso 2: Extracción por Sección

Para **CADA sección** del menú principal, extrae:

#### A. Título de la Sección
El nombre exacto como aparece en el menú

#### B. Descripción General
- ¿De qué trata esta sección?
- ¿Qué tipo de contenido presenta?
- ¿Cómo se posiciona en el sitio?

#### C. Propósito
- ¿Para qué existe esta sección?
- ¿Qué necesidad atiende?

#### D. Importancia para la Identidad de SINODE
- ¿Por qué esta sección es relevante para entender SINODE?
- ¿Qué aspecto de la identidad misional representa?

**Ejemplo de Extracción (Ficticio):**

```markdown
### 3. Doctrina

**Descripción:**
Sección dedicada al marco doctrinal de SINODE. Presenta las bases teológicas y el sistema de clasificación doctrinal (fundamental, denominacional, de error). Incluye artículos sobre doctrinas específicas.

**Propósito:**
Establecer claridad doctrinal y proveer un marco de discernimiento bíblico para la comunidad.

**Importancia para la Identidad de SINODE:**
La doctrina es central en SINODE porque define su postura teológica como movimiento que rechaza estructuras denominacionales pero mantiene firmeza en principios bíblicos fundamentales. Esta sección refleja el valor de "unidad en lo esencial, libertad en lo no esencial".
```

### Paso 3: Caso Especial - Sección "Doctrina"

La sección "Doctrina" probablemente contenga **muchos artículos detallados** sobre doctrinas individuales.

**⚠️ RESTRICCIÓN CRÍTICA:**
- ❌ **NO entres** al detalle de cada doctrina individual
- ❌ **NO extraigas** listados completos de doctrinas
- ✅ **SÍ explica** a nivel general:
  - Por qué la doctrina es importante para SINODE
  - Qué representa esta sección en el contexto de la identidad
  - Enfoque general del marco doctrinal (categorías principales)

**Ejemplo de lo que SÍ hacer:**
> "La sección Doctrina organiza las creencias en tres categorías: Fundamentales (no negociables), Denominacionales (legítimas pero secundarias), y de Error (contrarias al evangelio). Este sistema refleja el principio de SINODE de unidad en lo esencial y libertad en lo no esencial."

**Ejemplo de lo que NO hacer:**
> ❌ "Doctrina de la Trinidad: [5000 palabras explicando la doctrina con versículos]"
> ❌ Lista de 50 doctrinas con detalles individuales

---

## 🚫 Restricciones Críticas

### ❌ QUÉ NO HACER

1. **NO profundizar en contenidos individuales**
   - No extraigas artículos completos
   - No listes todas las doctrinas con detalles
   - No copies contenido extenso de ninguna página individual

2. **NO generar múltiples archivos**
   - Solo genera `input/brand/extraccion-doctrina-sinode.md`

3. **NO hacer cruces con información existente**
   - No leas archivos de `input/brand/` existentes
   - No compares ni valides contra otros documentos
   - Eso lo hará el usuario después

4. **NO inventar información**
   - Solo extrae lo que realmente existe en el sitio
   - Si una sección no está clara, indícalo

### ✅ QUÉ SÍ HACER

1. **QUEDARSE EN ALTO NIVEL**
   - Nivel de categorías/secciones del menú principal
   - Descripciones generales de cada sección
   - Esencia misional y propósito

2. **SÍ explicar cada sección del menú principal**
   - Todas las secciones visibles en la navegación
   - Qué representa cada una para la identidad de SINODE

3. **SÍ capturar la esencia misional**
   - Qué ES SINODE (identidad)
   - Qué HACE SINODE (misión)
   - Por qué EXISTE SINODE (propósito)

4. **SÍ enfocarse en información presentacional**
   - Información relevante para una web informativa
   - Contenido que ayude a la audiencia a comprender SINODE

---

## ✅ Criterios de Éxito

Tu tarea se considerará exitosa si el archivo `extraccion-doctrina-sinode.md` contiene:

### 1. Análisis Estructural Completo
- ✅ Lista completa de secciones del menú principal
- ✅ Todas las secciones analizadas (no omitiste ninguna)

### 2. Extracción por Sección
- ✅ Cada sección tiene: Descripción, Propósito, Importancia
- ✅ Las descripciones son de ALTO NIVEL (no entraste en detalles)
- ✅ Se mantiene el enfoque en identidad misional

### 3. Síntesis de Identidad
- ✅ Hay una síntesis que resume QUÉ ES y QUÉ HACE SINODE
- ✅ Los elementos clave están identificados

### 4. Restricciones Respetadas
- ✅ NO profundizaste en doctrinas individuales
- ✅ NO generaste múltiples archivos
- ✅ NO hiciste cruces con información existente
- ✅ Te mantuviste en alto nivel

---

## 📌 Recordatorios Finales

### Enfoque Mental
Es un **"mapa de alto nivel"** del sitio doctrina.sinode.org, donde alguien que nunca ha escuchado de SINODE pueda leer y entender:

- "Ah, SINODE es un movimiento de iglesia sin denominaciones"
- "Ah, tienen estas 7 áreas principales de enfoque"
- "Ah, por eso la doctrina/proyectos/territorios son importantes para ellos"

**NO estás** creando una copia del sitio ni extrayendo todo su contenido.

**SÍ estás** creando un resumen estructural de alto nivel enfocado en identidad misional.

### Diferencia Web Informativa vs Wiki
Recuerda:
- **Wiki (doctrina.sinode.org):** "Aquí están las 50 doctrinas explicadas en detalle"
- **Web informativa (a construir):** "Por qué la doctrina es importante para SINODE como movimiento"

Tu extracción debe servir para la web informativa, NO para replicar la wiki.

---

## 🚀 ¡Adelante!

Ve a `doctrina.sinode.org`, analiza su estructura, extrae la identidad misional de alto nivel, y genera `input/brand/extraccion-doctrina-sinode.md` siguiendo el formato especificado.

**¡Éxito en tu misión!**
