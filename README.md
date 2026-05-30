# Portfolio: Automatización de Facturación Electrónica (ARCA / ex-AFIP)

Este repositorio contiene una solución integral desarrollada en **Python** para automatizar y testear el flujo de facturación electrónica en Argentina, cubriendo desde la interfaz de usuario hasta la persistencia de datos.

### 🚀 Tipos de Pruebas Implementadas

**💻 Frontend (E2E)**
* **Flujo de Navegación:** Automatización de búsqueda de tutoriales de soporte FCE.
* **Selenium WebDriver:** Implementación de esperas explícitas y manejo de elementos dinámicos.

**🔌 API & Logic Testing**
* **Simulación SOAP/XML:** Validación de estructuras de envío para solicitud de CAE.
* **Estrategia de Contingencia:** Simulación de errores 500 y caídas de servicio para validar el comportamiento del sistema.

**🗄️ Database & Persistence**
* **Persistencia Local:** Scripts de validación para el guardado de facturas en DB cliente durante estados offline.
* **Integridad:** Verificación de estados de comprobantes entre el front y la base de datos.

### 🛠️ Stack Tecnológico
* **Lenguaje:** Python (Automatización y Scripting).
* **UI Engine:** Selenium WebDriver.
* **Testing:** Pytest para validación de lógica de negocio.
* **Protocolos:** Requests y Dicttoxml para mensajería SOAP de ARCA.

### ⚙️ Instalación 

1. **Clonar el repositorio:**
```bash
git clone https://github.com
```

2. **Instalar dependencias:**
```bash
pip install selenium requests dicttoxml pytest
```

3. **Ejecutar los tests:**
```bash
pytest
```
