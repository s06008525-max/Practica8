# 🗄️ Práctica 8: Normalización de Bases de Datos

**Instituto Politécnico Nacional (IPN) - Escuela Superior de Cómputo (ESCOM)**
**Programa:** Ingeniería en Inteligencia Artificial / 2020[cite: 1]
**Unidad de Aprendizaje:** Bases de Datos[cite: 1]

---

## 👥 Integrantes del Equipo
* Derek Calvario Santiago
* Jesús Alfonso Barrios Torres
* Minerva Aguilar López

## 🎯 Objetivo del Proyecto
El objetivo principal de esta práctica es aplicar los conceptos y técnicas de normalización de bases de datos sobre conjuntos de datos reales[cite: 1]. El proyecto lleva estructuras desnormalizadas desde su estado original (obtenidas de Kaggle) hasta la Tercera Forma Normal (3FN)[cite: 1]. 

Esto nos permite comprender las anomalías de inserción, actualización y eliminación que surgen en bases de datos desnormalizadas, y cómo la normalización resuelve estos problemas mejorando la integridad, consistencia y eficiencia del modelo de datos[cite: 1].

## 📊 Datasets Analizados
El proceso de normalización se aplicó sobre tres conjuntos de datos:
1. **Netflix Movies and TV Shows**[cite: 1]
2. **E-commerce Sales Data**[cite: 1]
3. **Hospital Patient Records**[cite: 1]

## 📂 Arquitectura del Repositorio
El repositorio está estructurado de la siguiente manera para mantener un orden lógico entre los datos, el código y la infraestructura, cumpliendo con los requerimientos de la práctica[cite: 1]:

* `📁 data/`: Contiene los datasets originales (en formato CSV/Excel) y los archivos exportados con los datos ya normalizados[cite: 1].
* `📁 docs/`: Documentación detallada del proyecto, incluyendo el análisis de los datos originales, el proceso de normalización paso a paso (1FN, 2FN, 3FN) y los Diagramas Entidad-Relación[cite: 1].
* `📁 scripts/`: Scripts de automatización (ej. Python) encargados de leer, procesar, limpiar y dividir los datos según las reglas de normalización[cite: 1].
* `📁 sql/`: Archivos con sentencias SQL, divididos en scripts DDL (para la creación de esquemas y tablas) y scripts DML (para la inserción de datos transformados)[cite: 1].
* `📄 Dockerfile`: Configuración para la creación de la imagen del contenedor de la aplicación[cite: 1].
* `📄 docker-compose.yml`: Archivo de orquestación para levantar múltiples contenedores (la base de datos con sus volúmenes y la aplicación), configurando redes y puertos[cite: 1].
* `📄 requirements.txt`: Listado de dependencias necesarias para ejecutar los scripts (como pandas, SQLAlchemy, etc.)[cite: 1].
* `📄 README.md`: Este archivo de documentación principal.

## 🚀 Instrucciones de Despliegue (Docker)
Para facilitar la portabilidad y reproducibilidad, la solución completa se encuentra contenerizada[cite: 1].

1. Clona este repositorio en tu máquina local:
   ```bash
   git clone [https://github.com/ingmatmus7-ai/Pr-ctica-8.git](https://github.com/ingmatmus7-ai/Pr-ctica-8.git)
