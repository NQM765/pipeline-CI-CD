# pipeline-CI-CD

Automatización de CI/CD para una aplicación Python simple con GitHub Actions.

---

## 📂 Estructura del proyecto

```

pipeline-CI-CD/
├── myapp.py
├── requirements.txt
├── pytest.ini
├── tests/
│   ├── **init**.py
│   └── test\_myapp.py
└── .github/
└── workflows/
└── ci.yml

````

- **myapp.py**  
  Funciones de la aplicación (por defecto, `hello()`).

- **tests/**  
  Pruebas automáticas con pytest.

- **pytest.ini**  
  Configuración de pytest (directorio de tests, patrón de archivos, PYTHONPATH).

- **.github/workflows/ci.yml**  
  Definición del pipeline CI: checkout, setup Python, instalación de dependencias y ejecución de tests.

---

## 🚀 Descripción

Este repositorio demuestra un workflow básico de **Integración Continua (CI)** usando **GitHub Actions**:

1. Cada **push** dispara el pipeline.
2. Se clona el código, se instala Python y dependencias.
3. Se ejecutan pruebas automáticas con **pytest**.
4. El pipeline falla/atraviesa según los resultados de los tests.

Este flujo garantiza que cada cambio en la rama `main` esté validado antes de integrarse.

---

## 🛠️ Tecnologías

- **Python 3.x**  
- **pytest** para pruebas automatizadas  
- **GitHub Actions** para CI

---

## 📋 Prerrequisitos

- Git instalado  
- Python 3.x instalado  
- (Opcional) Cuenta en GitHub para alojar el repositorio y activar Actions

---

## ⚙️ Instalación y uso local

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/pipeline-CI-CD.git
   cd pipeline-CI-CD

2. Ejecuta los tests localmente:

   ```bash
   pytest
   ```

---

## 🎬 Demostración de CI

Cada vez que se haga un commit/push:

```bash
git add .
git commit -m "Mensaje descriptivo"
git push origin main
```

GitHub Actions ejecutará automáticamente el pipeline definido en `.github/workflows/ci.yml`.
Revisa la pestaña **Actions** en GitHub para ver el progreso y resultados.



