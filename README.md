# Práctica 8: Normalización de Bases de Datos

**Instituto Politécnico Nacional (IPN) - Escuela Superior de Cómputo (ESCOM)**
**Carrera:** Ingeniería en Inteligencia Artificial 

Este repositorio contiene la solución completa para la Práctica 8, enfocada en la aplicación de conceptos y técnicas de normalización sobre conjuntos de datos reales. El sistema lleva estructuras desnormalizadas desde su estado original hasta la Tercera Forma Normal (3FN), automatizando el proceso mediante scripts de Python y desplegando la solución en un entorno contenerizado con Docker y PostgreSQL.

**Unidad de Aprendizaje:** Bases de Datos
**Profesor:** Gabriel Hurtado Avilés

### Integrantes:
1. Derek Calvario Santiago
2. Jesús Alfonso Barrios Torres
3. Minerva Lopez Aguilar


## Estructura del Proyecto

El proyecto sigue una arquitectura estricta para separar los datos crudos, los datos procesados, los scripts de transformación y los modelos SQL:

* **`data/raw/`**: Contiene los datasets originales descargados de Kaggle (Netflix, E-commerce, Hospitales).
* **`data/normalized/`**: Almacena los archivos CSV resultantes tras aplicar las reglas de 1FN, 2FN y 3FN.
* **`scripts/`**: Código fuente en Python para la limpieza masiva y la inyección a la base de datos.
* **`sql/ddl/`**: Scripts con el lenguaje de definición de datos (creación de tablas, PKs, FKs).
* **`sql/dml/`**: Scripts de muestra con sentencias de inserción.
* **`docs/`**: Documentación teórica y diagramas Entidad-Relación Extendidos (EER).

## Requisitos Previos

Para ejecutar este proyecto de manera local, solo es necesario contar con:
* Docker 
* Docker Compose

No es necesario instalar Python, PostgreSQL, ni dependencias (como Pandas o SQLAlchemy) en la máquina local. Todo el entorno está aislado y gestionado por los contenedores.

## Instrucciones de Ejecución

### 1. Levantar los contenedores
En la raíz del proyecto, inicialice la red privada, el volumen de datos y los contenedores de la aplicación y la base de datos:

```bash
docker-compose up -d --build
```

**Evidencia de Contenedores en Ejecución:**


<img width="719" height="92" alt="111" src="https://github.com/user-attachments/assets/ccc55099-3c03-4fd8-8bd9-e99e161fd46f" />



### 2. Ejecutar la normalización (Transformación a 3FN)
Los siguientes comandos leerán los archivos crudos, resolverán las anomalías de dependencias funcionales, generarán los esquemas DDL y guardarán los datos limpios:

```bash
# Normalizar Dataset 1 (Netflix)
docker exec -it normalizacion-db-app-1 python scripts/normalize_dataset1.py

# Normalizar Dataset 2 (E-commerce)
docker exec -it normalizacion-db-app-1 python scripts/normalize_dataset2.py

# Normalizar Dataset 3 (Hospitales)
docker exec -it normalizacion-db-app-1 python scripts/normalize_dataset3.py
```

### 3. Migrar los datos a PostgreSQL
Una vez normalizados, este script construirá el modelo relacional en el motor de base de datos e inyectará todos los registros manteniendo la integridad referencial:

```bash
docker exec -it normalizacion-db-app-1 python scripts/load_database.py
```

**Evidencia de Ejecución:**

<img width="287" height="401" alt="222" src="https://github.com/user-attachments/assets/3b90ba9a-bbfa-42ee-b66e-e3fc255a89f6" />



## Comprobación del Despliegue en la Base de Datos

Para verificar que los datos residen correctamente en la base de datos PostgreSQL contenerizada, accedemos a la consola interactiva con el siguiente comando:

```bash
docker exec -it normalizacion-db-db-1 psql -U admin -d db_normalizacion
```

**Evidencia del Modelo Relacional, las tablas creadas a partir del DDL:**

<img width="270" height="281" alt="333" src="https://github.com/user-attachments/assets/b9c497f6-6cb7-4f4a-bbbb-dfac6d316051" />


**Evidencia de Integridad de Datos el medio millón de registros insertados:**

<img width="334" height="101" alt="444" src="https://github.com/user-attachments/assets/6cb6c7d8-905b-48cb-8e0f-4560265760cb" />

