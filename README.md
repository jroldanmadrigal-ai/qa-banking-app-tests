<<<<<<< HEAD
# qa-banking-app-tests
=======
# 🏦 QA Banking App – Automated Tests (Selenium + Pytest)

Automatización de pruebas End-to-End para una aplicación bancaria web utilizando **Python**, **Selenium WebDriver** y **Pytest**.  
Incluye validación de flujos críticos, pruebas negativas, manejo dinámico de datos y reporte profesional de bugs.

---

## 📌 Características principales

- ✔ Automatización basada en el patrón **Page Object Model (POM)**
- ✔ Pruebas positivas y negativas
- ✔ Detección automática de cuenta con menor saldo
- ✔ Validación de mensajes de error y flujos críticos
- ✔ Integración con **GitHub Actions (CI/CD)**
- ✔ Reporte PDF profesional de bug crítico encontrado en producción

---

## 📁 Estructura del Proyecto
qa-banking-app-tests/
│
├── pages/ # Page Objects (interacciones con la UI)
│ ├── base_page.py
│ ├── login_page.py
│ ├── dashboard_page.py
│ └── transfer_page.py
│
├── tests/ # Test cases
│ ├── test_login_valid.py
│ ├── test_invalid_login.py
│ └── test_transfer_insufficient_balance.py
│
├── utils/
│ ├── driver_factory.py
│ └── helpers.py
│
├── reports/
│ └── Reporte_Bug_QA.pdf
│
├── .github/workflows/
│ └── python-tests.yml # Integración CI/CD
│
├── requirements.txt
└── README.md

---


### 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/jroldanmadrigral-ai/qa-banking-app-tests.git
cd qa-banking-app-tests
>>>>>>> 8e03f23 (Add README.md documentation)
