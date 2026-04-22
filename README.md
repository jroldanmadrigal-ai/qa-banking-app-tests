<<<<<<< HEAD
# qa-banking-app-tests
=======
# 🏦 QA Automated Testing – HomeBanking Demo App

Este proyecto contiene un conjunto completo de **pruebas manuales, automatizadas y análisis del DOM** para la aplicación:

🔗 https://homebanking-demo-tests.netlify.app/

Incluye:

- ✔️ Pruebas funcionales (manuales)
- ✔️ Pruebas automatizadas con Selenium + PyTest
- ✔️ Validaciones de UI, transferencia, login y dashboard
- ✔️ Manejo de modales, esperas explícitas y sincronización
- ✔️ Pipeline CI/CD con GitHub Actions
- ✔️ Reporte profesional en PDF
- ✔️ Análisis de performance y network con Chrome DevTools

---


## 📁 Estructura del Proyecto
qa-banking-app-tests/
│
├── pages/ → Page Objects (Login, Dashboard, Transfer)
├── tests/ → Pruebas automatizadas PyTest
├── utils/ → Driver factory, helpers
├── requirements.txt → Dependencias
├── README.md → Documentación
└── QA_Full_Test_Report_HomeBanking.pdf

---

---

## 🧪 Pruebas Implementadas

### ✔️ Login Tests
- test_valid_login  
- test_invalid_login  

### ✔️ Dashboard Tests
- Verificación de saldos  
- Validación de elementos visibles  

### ✔️ Transfer Tests
- Transferencia válida  
- Transferencia con saldo insuficiente (con modal)  
- Validación de errores  

---

## 🐞 Corrección de Falso Positivo

Durante la automatización se identificó inicialmente un supuesto bug de sobregiro.  
Tras una segunda validación manual se determinó:

❗ No era un bug  
✔️ La app sí valida correctamente  
✔️ La automatización estaba capturando el error antes del modal  

Se ajustó la sincronización del test para alinearlo con el comportamiento real.

---

## ⚙️ GitHub Actions (CI)

Este proyecto ejecuta los tests automáticamente con cada push:

.github/
└── workflows/
└── python-tests.yml


---

## 📄 Reporte en PDF

Incluye:
- Pruebas manuales
- Resultados automatizados
- Análisis del DOM (Performance + Network)
- Conclusiones QA

Archivo: **QA_Full_Test_Report_HomeBanking.pdf**
