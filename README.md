# Py-Administrador-de-tareas

Una aplicación de escritorio moderna para la gestión de tareas desarrollada con Python y PySide6.

![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)
![PySide6](https://img.shields.io/badge/PySide6-latest-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## ✨ Características

- 📱 Interfaz moderna y responsiva con PySide6
- 🎨 Tema claro/oscuro automático
- 📅 Calendario personalizado
- 🔔 Sistema de notificaciones
- 🎯 Prioridades con códigos de color
- 💾 Base de datos SQLite
- 🔄 Operaciones CRUD completas

## 🚀 Inicio Rápido

1. **Clonar el repositorio**
```bash
git clone https://github.com/tuusuario/Py-Administrador-de-tareas.git
cd Py-Administrador-de-tareas
```

2. **Crear entorno virtual**
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
```

3. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

4. **Ejecutar la aplicación**
```bash
python main.py
```

## 🛠️ Tecnologías

- **PySide6**: Framework GUI moderno
- **SQLite**: Base de datos local
- **darkdetect**: Detección automática del tema del sistema

## 📝 Funcionalidades

### Gestión de Tareas
- ✏️ Crear nuevas tareas
- 📖 Ver lista de tareas
- 🔄 Actualizar tareas existentes
- 🗑️ Eliminar tareas
- ✅ Marcar tareas como completadas

### Sistema de Prioridades
- 🔴 Alta: Rojo claro (#ffcdd2)
- 🟡 Media: Amarillo claro (#fff9c4)
- 🟢 Baja: Verde claro (#c8e6c9)

### Calendario
- 📅 Selector de fechas integrado
- 🎨 Diseño personalizado
- 🔍 Vista mensual clara
- 🎯 Resaltado de fechas importantes

## 📁 Estructura del Proyecto

```
taskPy/
├── main.py           # Aplicación principal y GUI
├── database.py       # Gestión de base de datos SQLite
├── custom_calendar.py # Calendario personalizado
├── requirements.txt  # Dependencias del proyecto
└── README.md         # Documentación
```

## 📦 Requisitos

- Python 3.7 o superior
- PySide6
- darkdetect
- Sistema operativo: Windows/macOS/Linux

## 🤝 Contribuir

1. Fork el proyecto
2. Crea tu rama de características (`git checkout -b feature/NuevaCaracteristica`)
3. Commit tus cambios (`git commit -m 'Añadir nueva característica'`)
4. Push a la rama (`git push origin feature/NuevaCaracteristica`)
5. Abre un Pull Request

## 📜 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

## 👥 Autores

- **Tu Nombre** - *Carlos Delgado 

- PySide6 por el framework GUI
- La comunidad de Python por sus contribuciones
