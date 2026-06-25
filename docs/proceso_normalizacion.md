# 2. Diagramas ER y Relacionales

En esta sección se presenta la conceptualización gráfica de las bases de datos transformadas. A partir de la normalización a 3FN, se diseñaron los Esquemas de Definición de Datos (DDL) en PostgreSQL. A continuación, se detallan los Modelos Relacionales y los Diagramas Entidad-Relación Extendidos (EER) resultantes, demostrando la integridad referencial mediante Llaves Primarias (PK) y Llaves Foráneas (FK).

---

## 2.1 Modelo Relacional: Dataset 1 - Netflix Movies and TV Shows

### Descripción de la Arquitectura
El modelo relacional para este conjunto de datos se caracteriza por resolver múltiples relaciones de **Muchos a Muchos (M:N)**. Dado que una película/serie puede tener múltiples directores, actores, países y géneros, y a su vez, estos pueden participar en múltiples obras, se implementó un diseño en estrella descentralizado:
* **Entidad Central:** `shows` (Llave primaria alfanumérica `show_id`).
* **Entidades Fuertes (Dimensiones):** `directors`, `actors`, `countries` y `genres`. Todas cuentan con un identificador numérico autoincremental (PK) y una restricción `UNIQUE NOT NULL` en sus nombres para evitar duplicidad en el catálogo.
* **Entidades Asociativas (Tablas Puente):** `show_director`, `show_actor`, `show_country` y `show_genre`. Estas tablas rompen la relación M:N. Su característica principal es que poseen una **Llave Primaria Compuesta**, formada por la combinación de las dos llaves foráneas que reciben, garantizando que no existan registros duplicados exactos (ej. el mismo actor registrado dos veces en la misma película).

### Diagrama EER y Relacional
![Diagrama Relacional Netflix](ruta/a/tu/diagrama_netflix.png)

---

## 2.2 Modelo Relacional: Dataset 2 - E-commerce Sales

### Descripción de la Arquitectura
Este modelo sigue una estructura transaccional clásica de ventas (Cabecera - Detalle), optimizada para evitar la redundancia de datos descriptivos. 
* **Entidades Fuertes (Catálogos):** `customers` y `products`. Almacenan la información estática. Un cliente tiene un país definido y un código de stock (`stock_code`) tiene una descripción inmutable.
* **Entidad de Cabecera (Transacción Principal):** `invoices`. Representa el momento de la compra. Tiene una relación **1 a Muchos (1:N)** con los clientes, ya que un cliente (`customer_id` como FK) puede tener múltiples facturas, pero una factura pertenece a un solo cliente.
* **Entidad de Detalle (Transacción Débil):** `invoice_details`. Es la tabla más granular. Resuelve la relación M:N entre facturas y productos. Utiliza una llave primaria serial (`detail_id`) e importa `invoice_no` y `stock_code` como llaves foráneas para registrar la cantidad (`quantity`) y el precio unitario (`unit_price`) exactos en el momento de esa transacción específica.

### Diagrama EER y Relacional
![Diagrama Relacional E-commerce](ruta/a/tu/diagrama_ecommerce.png)

---

## 2.3 Modelo Relacional: Dataset 3 - Hospital Patient Records

### Descripción de la Arquitectura
El modelo médico fue diseñado para separar la demografía del paciente de la infraestructura hospitalaria y el evento clínico, garantizando que el expediente no se duplique por cada ingreso.
* **Entidades Fuertes:** * `patients`: Aísla todos los biomarcadores e información demográfica (edad, BMI, género, etnia, peso, altura) bajo un `patient_id` único.
  * `icus`: Cataloga las Unidades de Cuidados Intensivos, mapeando el tipo de unidad (`icu_type`) con su hospital respectivo (`hospital_id`).
* **Entidad Transaccional:** `encounters`. Funciona como el evento temporal que une a las entidades. Tiene relaciones **1 a Muchos (1:N)** tanto con `patients` como con `icus`. Es decir, un paciente puede tener múltiples encuentros a lo largo del tiempo, y una unidad UCI alberga múltiples encuentros. La tabla conserva como atributos propios solo los datos médicos de ese evento puntual (ej. si fue cirugía electiva, fuente de admisión y diagnóstico APACHE 2).

### Diagrama EER y Relacional
![Diagrama Relacional Hospitales](ruta/a/tu/diagrama_hospitales.png)
