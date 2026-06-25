# 🏛️ Sistema de Gestión Notarial 105 (Versión Estática)

Este repositorio contiene la **versión 100% estática** del Sistema de Gestión Notarial 105. 

Originalmente diseñado con una arquitectura cliente-servidor usando Python (Flask) y PostgreSQL, este proyecto ha sido refactorizado para ejecutarse exclusivamente en el navegador web del cliente mediante **HTML, CSS (Bootstrap 5) y JavaScript Vainilla**.

Esta versión fue creada para propósitos de demostración y evaluación, garantizando que el sistema pueda ser probado a largo plazo sin depender de costos de alojamiento de servidores o mantenimiento de bases de datos activas.

---

## 👥 Equipo de Desarrollo
Proyecto desarrollado por estudiantes de la **Escuela Superior de Cómputo (ESCOM - IPN)**:
* Jesús Alfonso Barrios Torres
* Derek
* Uriel
* Paola
* Dani

---

## ⚙️ Arquitectura y Tecnologías
Al ser una aplicación puramente frontend, el sistema simula las operaciones de backend de la siguiente manera:
* **Interfaz:** HTML5 y CSS3 (Bootstrap 5).
* **Lógica y Enrutamiento:** JavaScript Vainilla.
* **Persistencia de Datos (Mocking):** Se utiliza la API de `localStorage` del navegador para simular una base de datos relacional (almacenando usuarios, clientes, escrituras, etc., en formato JSON).
* **Sesiones:** Se utiliza `sessionStorage` para manejar el estado de autenticación de los roles (Notario, Abogado, Cliente).

> **⚠️ Nota Técnica:** Debido a la naturaleza del `localStorage`, los datos generados o modificados durante la sesión se guardan de forma local en el dispositivo y navegador de quien realiza la prueba. No hay sincronización en la nube ni concurrencia entre múltiples usuarios en distintos equipos.

---

## 🚀 Cómo probar el sistema

No se requiere instalación de dependencias, entornos virtuales ni servidores locales.

**Opción 1: GitHub Pages (Recomendado)**
Simplemente ingresa al enlace público del despliegue:
`[AQUÍ_PEGA_TU_LINK_DE_GITHUB_PAGES]`

**Opción 2: Ejecución Local**
1. Clona este repositorio o descarga el código fuente.
2. Abre la carpeta del proyecto.
3. Haz doble clic en el archivo `index.html` para abrirlo en cualquier navegador web moderno.

---

## 🔑 Credenciales de Prueba (Seed)

Para facilitar la evaluación, el sistema cuenta con un *script* de inicialización silenciosa que precarga cuentas de demostración en el navegador si no detecta datos previos. 

Puedes utilizar las siguientes credenciales para probar los diferentes flujos y vistas según el nivel de acceso:

| Rol | Correo Electrónico | Contraseña / Acceso |
| :--- | :--- | :--- |
| **Notario** (Admin) | `notario@notaria105.com` | `notario123` |
| **Abogado** (Staff) | `abogado@notaria105.com` | `abogado123` |
| **Cliente** (Ciudadano) | `cliente@example.com` | **CURP:** `PELJ850303HDFRPN03` |

*(El sistema también incluye una escritura de "Fe de Hechos" precargada para poder visualizar el funcionamiento del Dashboard inmediatamente después del primer inicio de sesión).*

---

## 📂 Estructura Principal del Proyecto
* `index.html`: Punto de entrada y Login general.
* `login_cliente.html`: Acceso exclusivo para el Portal Ciudadano.
* `dashboard.html`: Panel principal para empleados.
* `portal_cliente.html`: Vista de seguimiento de trámites para ciudadanos.
* `/js/db.js`: Motor de base de datos simulada en `localStorage` y script de inicialización (Seed).
* `/js/nav.js`: Controlador dinámico de la barra de navegación según el rol activo.
