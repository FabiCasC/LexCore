# Diseño e Implementación de un Sistema Experto Multilenguaje para el Análisis de Contratos Legales utilizando Scala, Prolog y Python

---

## Resumen

El presente proyecto propone el diseño y desarrollo de **LexCore**, un sistema experto de auditoría legal que integra tres paradigmas de programación distintos mediante el uso de los lenguajes Scala, Prolog y Python. Scala es empleado para el procesamiento funcional y la tokenización de contratos en lenguaje natural, Prolog para la representación del conocimiento jurídico y el razonamiento lógico sobre cláusulas, y Python como lenguaje de integración, modelado orientado a objetos y análisis estadístico. Esta arquitectura multilenguaje permite aprovechar las fortalezas específicas de cada tecnología, promoviendo un sistema modular, extensible y eficiente orientado a la detección automática de cláusulas abusivas en contratos laborales, civiles y comerciales bajo la legislación peruana.

**Palabras clave:** Programación multilenguaje, Scala, Prolog, Python, Sistemas expertos, Análisis de contratos, Derecho peruano, Herencia, Polimorfismo, Pandas, NumPy.

---

## Introducción

En el desarrollo moderno de software, la complejidad de los problemas exige el uso de múltiples paradigmas de programación. Ningún lenguaje, por sí solo, resulta óptimo para resolver todas las necesidades de un sistema complejo. En este contexto, la integración de lenguajes se presenta como una alternativa eficaz para maximizar el rendimiento, expresividad y mantenibilidad del software.

LexCore aborda la construcción de un sistema que combina programación funcional (Scala), lógica declarativa (Prolog) y programación orientada a objetos con análisis de datos (Python). El problema concreto que resuelve es la revisión automática de contratos en español: el sistema recibe el texto de un contrato, lo tokeniza y segmenta en cláusulas mediante Scala, valida cada cláusula contra una base de conocimiento jurídica en Prolog, y finalmente construye un modelo de dominio en Python que genera un dictamen de riesgo con un puntaje de 0 a 100 y recomendaciones legales basadas en el Código Civil peruano y la legislación laboral vigente.

La propuesta demuestra que una arquitectura multilenguaje adecuadamente estructurada puede mejorar la claridad del diseño y facilitar la resolución de problemas de alta complejidad semántica y legal.

---

## Objetivos

### Objetivo General

Diseñar e implementar un sistema experto multilenguaje que integre Scala, Prolog y Python para la detección automatizada de cláusulas riesgosas en contratos legales, aplicando principios de modularidad, separación de responsabilidades y herencia orientada a objetos.

### Objetivos Específicos

1. Implementar el módulo de tokenización y extracción de cláusulas utilizando Scala con programación funcional.
2. Desarrollar una base de conocimiento jurídica en Prolog con reglas para contratos laborales, civiles y comerciales bajo legislación peruana.
3. Diseñar una jerarquía de clases en Python que modele los distintos tipos de cláusulas mediante herencia y polimorfismo.
4. Implementar análisis estadístico de cláusulas utilizando las bibliotecas Pandas y NumPy.
5. Orquestar la comunicación entre Scala, Prolog y Python mediante un pipeline unificado.
6. Desarrollar una interfaz visual en Streamlit con gráficos Plotly para la presentación de resultados.
7. Generar un dictamen automático con puntaje de riesgo, nivel y recomendación legal final.

---

## Alcance del Proyecto

**El proyecto contempla:**

- El diseño de la arquitectura MVC del sistema.
- La definición de módulos independientes por lenguaje.
- La integración funcional entre Scala, Prolog y Python mediante subprocesos y la biblioteca PySwip.
- Una base de conocimiento con más de 25 reglas jurídicas para 4 categorías de contratos.
- Un modelo orientado a objetos con jerarquía de clases de 5 niveles (clase base + 4 subclases).
- Una interfaz visual interactiva con Streamlit y gráficos Plotly.
- La documentación técnica del sistema.

**No se contempla:**

- Procesamiento de contratos en formato PDF o imágenes (OCR).
- Consulta a fuentes legales externas en tiempo real.
- El despliegue en entornos productivos ni firma digital de dictámenes.

---

## Marco Teórico

### Scala

Lenguaje multiparadigma que combina programación funcional y orientada a objetos, ideal para el procesamiento de texto y sistemas concurrentes. En LexCore, Scala implementa el tokenizador de contratos como un ejecutable JAR que recibe texto por `stdin` y devuelve JSON estructurado por `stdout`. Utiliza `case class` para modelar cláusulas y contratos de forma inmutable, y `object` para agrupar funciones puras de transformación.

### Prolog

Lenguaje declarativo basado en lógica de predicados de primer orden, ampliamente utilizado en sistemas expertos e inferencia lógica. En LexCore, Prolog contiene la base de conocimiento jurídica del sistema: hechos sobre tipos de cláusula, artículos del Código Civil, y reglas que infieren `clausula_riesgosa(Id, Tipo, Severidad)` a partir de patrones en el texto. La integración con Python se realiza mediante la biblioteca **PySwip**, que permite ejecutar consultas Prolog directamente desde código Python.

### Python

Lenguaje interpretado de alto nivel, empleado como lenguaje de integración principal del sistema. En LexCore cumple tres roles: (1) **orquestador** del pipeline completo mediante el módulo `pipeline.py`; (2) **capa de modelo** con una jerarquía de clases orientadas a objetos que aplica herencia y polimorfismo; y (3) **analizador estadístico** mediante Pandas y NumPy para calcular perfiles de riesgo.

### Programación Orientada a Objetos — Herencia y Polimorfismo

La clase base `Clausula` define la interfaz común con el método polimórfico `evaluar()`. Cuatro subclases (`ClausulaLaboral`, `ClausulaArrendamiento`, `ClausulaServicios`, `ClausulaCompraventa`) sobrescriben este método agregando el artículo legal peruano específico y la recomendación correspondiente. El patrón **Factory Method** (`fabricar_clausula()`) instancia la subclase correcta según la categoría del contrato, desacoplando la creación de objetos del resto del sistema.

### Pandas y NumPy

**Pandas** se utiliza para construir `DataFrame` con las cláusulas evaluadas y calcular distribuciones mediante `value_counts()`. **NumPy** se emplea para el cálculo vectorial de estadísticas: `np.mean()`, `np.std()` y `np.max()` sobre los pesos de riesgo, y cálculo de longitud promedio de textos. Estas bibliotecas permiten un análisis estadístico eficiente sobre colecciones de cláusulas.

---

## Arquitectura del Sistema

El sistema sigue una arquitectura **MVC (Modelo-Vista-Controlador)** distribuida en tres lenguajes, donde cada lenguaje ocupa una capa bien definida del sistema.

```
┌─────────────────────────────────────────────────────┐
│                   VISTA (Python)                     │
│         Streamlit + Plotly  ←  view/                │
└──────────────────────┬──────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────┐
│              CONTROLADOR (Python)                    │
│   pipeline.py → scala_bridge → prolog_bridge        │
│   estadisticas / reportes / almacenamiento           │
└────────┬───────────────────────┬────────────────────┘
         │                       │
┌────────▼────────┐    ┌─────────▼──────────────────┐
│  MODELO Scala   │    │      MODELO Python          │
│  Tokenizador    │    │  Clausula (jerarquía OOP)   │
│  ContractParser │    │  Contrato + Dictamen        │
│  ClauseExtractor│    │  analizador (pandas/numpy)  │
└────────┬────────┘    └────────────────────────────┘
         │
┌────────▼────────┐
│  MODELO Prolog  │
│  hechos.pl      │
│  reglas_*.pl    │
│  consultas/     │
└─────────────────┘
```

### Flujo de Ejecución

```
Texto del contrato
       │
       ▼
[Scala] ContractParser.parsear()
   → TextNormalizer.normalizar()
   → Tokenizer.tokenizar()
   → ClauseExtractor.extraer()
   → JSON con lista de cláusulas
       │
       ▼
[Python/Prolog] validar_clausulas()   ← PySwip
   → carga hechos.pl + reglas_*.pl
   → assertz clausula(Id, Tipo, Texto)
   → query clausula_riesgosa(Id, Tipo, Severidad)
   → lista de hallazgos con severidad
       │
       ▼
[Python OOP] Contrato.cargar_desde_scala()
   → fabricar_clausula() → subclase según categoría
   → evaluar() → artículo legal + recomendación
       │
       ▼
[Python Pandas/NumPy] calcular_perfil_estadistico()
   → DataFrame, value_counts, np.mean/std/max
       │
       ▼
[Python] Dictamen.resumen()
   → score 0-100, nivel, recomendación final
       │
       ▼
[Vista Streamlit] resultados + gráfico Plotly
```

---

## Estructura del Proyecto

```
LexCore/
│
├── docs/
│   ├── arquitectura.md
│   ├── instalacion.md
│   └── documentacion_proyecto.md
│
├── integracion/
│   ├── python_scala.md
│   ├── python_prolog.md
│   ├── flujo_completo.md
│   ├── formatos_intercambio.md
│   └── errores_y_manejo.md
│
├── model/
│   ├── scala/
│   │   ├── build.sbt
│   │   └── src/main/scala/
│   │       ├── Main.scala
│   │       ├── models/
│   │       │   ├── Clause.scala
│   │       │   ├── Contract.scala
│   │       │   └── Token.scala
│   │       ├── tokenizer/
│   │       │   ├── Tokenizer.scala
│   │       │   ├── ContractParser.scala
│   │       │   └── ClauseExtractor.scala
│   │       └── utils/
│   │           └── TextNormalizer.scala
│   │
│   ├── prolog/
│   │   ├── base_conocimiento/
│   │   │   ├── hechos.pl
│   │   │   ├── reglas_civiles.pl
│   │   │   ├── reglas_laborales.pl
│   │   │   ├── reglas_comerciales.pl
│   │   │   └── reglas_generales.pl
│   │   ├── consultas/
│   │   │   ├── validar_clausula.pl
│   │   │   ├── detectar_riesgo.pl
│   │   │   └── verificar_contrato.pl
│   │   └── tests/
│   │       └── test_reglas.pl
│   │
│   ├── python/
│   │   ├── modelos/
│   │   │   ├── clausula.py      ← Clausula + 4 subclases + fábrica
│   │   │   └── contrato.py      ← Contrato + Dictamen
│   │   ├── analisis/
│   │   │   └── analizador.py    ← pandas + numpy
│   │   └── README.md
│   │
│   └── data/
│       ├── conocimiento/
│       ├── contratos/
│       ├── resultados/
│       └── sesiones/
│
├── controller/
│   ├── orquestador/
│   │   ├── pipeline.py          ← Orquestador principal
│   │   ├── scala_bridge.py      ← Comunicación con JAR Scala
│   │   └── prolog_bridge.py     ← Comunicación con Prolog (PySwip)
│   ├── analisis/
│   │   ├── estadisticas.py
│   │   ├── comparador.py
│   │   └── reportes.py
│   ├── almacenamiento/
│   │   ├── lector_json.py
│   │   └── lector_csv.py
│   └── utils/
│       ├── config.py
│       └── logger.py
│
├── view/
│   ├── app.py
│   ├── streamlit_app_diego.py   ← Interfaz visual con Plotly
│   ├── paginas/
│   │   ├── inicio.py
│   │   ├── cargar_contrato.py
│   │   ├── resultados.py
│   │   ├── estadisticas.py
│   │   └── historial.py
│   ├── componentes/
│   │   ├── tabla_clausulas.py
│   │   ├── badge_riesgo.py
│   │   └── descarga_reporte.py
│   └── assets/
│       └── estilos.css
│
├── requirements.txt
└── Readme.md
```

---

## Descripción de los Componentes

### Módulo Scala — Tokenizador de Contratos

Implementado como un ejecutable JAR compilado con `sbt assembly`. Recibe el texto completo del contrato por `stdin` junto con el `id` y `nombre` como argumentos, y devuelve por `stdout` un JSON con la lista de cláusulas extraídas. Cada cláusula incluye `id`, `tipo`, `texto`, `partes` y un `riesgo_inicial` calculado heurísticamente.

**Clases principales:**
- `Main.scala` — punto de entrada, lee stdin y llama a `ContractParser`
- `ContractParser.scala` — orquesta normalización, tokenización y extracción
- `ClauseExtractor.scala` — detecta y delimita cláusulas en el texto
- `TextNormalizer.scala` — normaliza acentos, espacios y caracteres especiales
- `Clause.scala` — `case class Clause(id, tipo, texto, partes, riesgoInicial)`

### Módulo Prolog — Base de Conocimiento Jurídica

Contiene la representación formal del conocimiento legal peruano. Se estructura en tres capas: **hechos** (tipos de cláusula, niveles de riesgo, artículos del Código Civil), **reglas** de detección por dominio jurídico, y **consultas** reutilizables.

**Archivos de reglas:**
| Archivo | Dominio | Reglas |
|---|---|---|
| `hechos.pl` | Base ontológica | tipos, niveles, artículos CC, patrones |
| `reglas_civiles.pl` | Derecho Civil | penalidades, rescisión, confidencialidad, obligaciones |
| `reglas_laborales.pl` | Derecho Laboral | horas extra, renuncia, no competencia, beneficios |
| `reglas_comerciales.pl` | Derecho Comercial | confidencialidad, arbitraje, modificación unilateral |
| `reglas_generales.pl` | General | exoneración de responsabilidad, cláusulas vagas |

**Predicado central:** `clausula_riesgosa(Id, Tipo, Severidad)` — unifica cuando una cláusula presenta riesgo, devolviendo su identificador, tipo de riesgo y nivel de severidad (`bajo`, `medio`, `alto`, `critico`).

### Módulo Python — Modelo de Dominio y Análisis

#### Jerarquía de Clases (`model/python/modelos/clausula.py`)

```
Clausula (clase base)
│  NIVELES_RIESGO = {"bajo":1, "medio":2, "alto":3, "critico":4}
│  evaluar() → dict base
│  peso_riesgo() → int
│
├── ClausulaLaboral
│     evaluar() → agrega artículo LPCL/Constitución + recomendación
│
├── ClausulaArrendamiento
│     evaluar() → agrega artículo CC 1666°-1712° + recomendación
│
├── ClausulaServicios
│     evaluar() → agrega artículo CC 1764°-1770° + recomendación
│
└── ClausulaCompraventa
      evaluar() → agrega artículo CC 1529°-1601° + recomendación

fabricar_clausula(categoria, id, tipo, texto, severidad) → Factory Method
```

#### Clase Contrato (`model/python/modelos/contrato.py`)

Modela el contrato completo como agregación de cláusulas. El método `cargar_desde_scala(scala_output, hallazgos_prolog)` construye el mapa de severidades desde los hallazgos de Prolog y usa `fabricar_clausula()` para instanciar la subclase correcta según la categoría del contrato.

#### Clase Dictamen (`model/python/modelos/contrato.py`)

Genera el veredicto final sobre un contrato. Calcula un **score de 0 a 100** descontando puntos por severidad (bajo: −5, medio: −15, alto: −25, crítico: −40) y determina el nivel de riesgo (BAJO/MEDIO/ALTO/CRITICO) con una recomendación textual con emoji.

#### Analizador Estadístico (`model/python/analisis/analizador.py`)

| Función | Descripción |
|---|---|
| `calcular_perfil_estadistico()` | `pd.DataFrame` + `value_counts()` + `np.mean/std/max` |
| `generar_dataframe_clausulas()` | DataFrame formateado para Streamlit |
| `comparar_con_promedio()` | Tendencia histórica con `np.mean()` sobre historial |

### Módulo Controlador — Pipeline de Orquestación (`controller/orquestador/pipeline.py`)

Función principal `analizar_contrato(texto, nombre, categoria)`:

1. Llama a `tokenizar_contrato()` → lanza el JAR de Scala como subproceso con `subprocess.run()`, enviando el texto por `stdin` y parseando el JSON de `stdout`.
2. Llama a `validar_clausulas()` → usa **PySwip** para cargar los archivos `.pl`, hacer `assertz` de cada cláusula y ejecutar la query `clausula_riesgosa/3`.
3. Instancia `Contrato`, llama a `cargar_desde_scala()` y evalúa todas las cláusulas.
4. Calcula el perfil estadístico con `calcular_perfil_estadistico()`.
5. Instancia `Dictamen` y obtiene el resumen con score, nivel y recomendación final.
6. Persiste resultados en JSON y CSV mediante el módulo de almacenamiento.
7. Retorna el resultado enriquecido incluyendo `score`, `nivel_riesgo` y `recomendacion_final`.

### Módulo Vista — Interfaz Streamlit

Dos interfaces disponibles:

- **`view/app.py`** — interfaz modular con páginas separadas (inicio, carga, resultados, estadísticas, historial).
- **`view/streamlit_app_diego.py`** — interfaz visual mejorada con CSS personalizado (gradientes, bordes redondeados), gráfico de torta interactivo con **Plotly Express**, tabla de cláusulas con coloreado por estado, descarga de reporte en JSON y sidebar con historial de auditorías.

---

## Metodología de Desarrollo

Se adopta una metodología **incremental por módulo**, siguiendo el orden natural del flujo de datos del sistema:

1. **Fase 1 — Módulo Scala:** implementación del tokenizador y compilación del JAR.
2. **Fase 2 — Módulo Prolog:** construcción de la base de conocimiento con hechos y reglas por dominio jurídico.
3. **Fase 3 — Módulo Python (Modelo):** diseño de la jerarquía de clases, implementación de `Contrato` y `Dictamen`.
4. **Fase 4 — Análisis estadístico:** implementación de las funciones con Pandas y NumPy.
5. **Fase 5 — Integración:** implementación del pipeline orquestador y los bridges de comunicación.
6. **Fase 6 — Vista:** desarrollo de la interfaz Streamlit con Plotly.
7. **Fase 7 — Integración final:** unificación de los tres módulos en el repositorio LexCore.

---

## Conclusiones

LexCore demuestra que una arquitectura multilenguaje bien estructurada permite resolver problemas de alta complejidad aprovechando las fortalezas específicas de cada paradigma. Scala provee un tokenizador robusto e inmutable gracias a su modelo funcional. Prolog permite expresar reglas jurídicas complejas de forma declarativa y natural, facilitando la incorporación de nuevo conocimiento legal sin modificar la lógica de negocio. Python actúa como el pegamento del sistema: su modelo orientado a objetos con herencia y polimorfismo permite un diseño extensible de la jerarquía de cláusulas, mientras que Pandas y NumPy habilitan un análisis estadístico eficiente.

La separación en capas MVC garantiza que cada componente pueda evolucionar de forma independiente: las reglas Prolog pueden enriquecerse sin tocar el modelo Python, el tokenizador Scala puede reemplazarse por un modelo NLP más avanzado sin afectar la base de conocimiento, y la vista puede rediseñarse completamente sin impactar la lógica de negocio.

---

## Referencias

- Bratko, I. *Prolog Programming for Artificial Intelligence*. 4th ed. Addison-Wesley, 2011.
- Odersky, M., Spoon, L., Venners, B. *Programming in Scala*. 5th ed. Artima, 2021.
- Lutz, M. *Learning Python*. 5th ed. O'Reilly Media, 2013.
- McKinney, W. *Python for Data Analysis*. 3rd ed. O'Reilly Media, 2022.
- Harris, C.R. et al. *Array programming with NumPy*. Nature, 585, 357–362, 2020.
- Decreto Legislativo N° 728 — Ley de Productividad y Competitividad Laboral (LPCL). Perú, 1997.
- Código Civil del Perú. Decreto Legislativo N° 295. Artículos 1238°, 1341°, 1354°-1405°, 1529°-1712°.
- Constitución Política del Perú (1993). Artículos 22°-29°: Derechos laborales fundamentales.
