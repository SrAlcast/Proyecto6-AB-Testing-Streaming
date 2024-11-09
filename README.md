# 📊 Proyecto de Análisis de Streaming: Exploración y Modelado de Datos

## 📖 Descripción
Este proyecto tiene como objetivo analizar y modelar datos relacionados con una plataforma de streaming. En él, se busca extraer insights relevantes sobre el comportamiento de los usuarios, patrones de visualización y otras métricas clave que puedan ayudar en la toma de decisiones estratégicas. A través de técnicas de análisis estadístico y modelado, el proyecto proporciona una base sólida para entender mejor las tendencias de uso y rendimiento de contenido en la plataforma.

## 🗂️ Estructura del Proyecto

```
├── data/                        # Datos en formato crudo y procesado
├── notebooks/                   # Notebooks de Jupyter con el análisis
├── src/                         # Scripts de procesamiento y modelado
├── sql/                         # Archivos SQL para crear y cargar la base de datos
│   ├── creacion_bbdd.sql        # Comandos SQL para crear la base de datos
│   └── streaming_project_combined_inserts.sql # Inserts para cargar datos iniciales
├── results/                     # Gráficos y archivos de resultados
├── README.md                    # Descripción del proyecto
```

## 🛠️ Instalación y Requisitos

Este proyecto está desarrollado con Python 3.8 y requiere las siguientes bibliotecas:

- [pandas](https://pandas.pydata.org/pandas-docs/stable/) - para manipulación y análisis de datos
- [numpy](https://numpy.org/doc/) - para cálculos numéricos y manejo de arrays
- [matplotlib](https://matplotlib.org/stable/contents.html) - para visualización de datos
- [seaborn](https://seaborn.pydata.org/) - para visualización de datos estadísticos
- [SQLAlchemy](https://docs.sqlalchemy.org/en/14/) - para conectividad SQL y ORM en Python
- [sqlite3](https://docs.python.org/3/library/sqlite3.html) - para crear y gestionar bases de datos SQL

Para instalar las dependencias, es recomendable crear un entorno virtual:

```bash
# Crear entorno virtual
python3 -m venv venv

# Activar entorno virtual
source venv/bin/activate  # En MacOS/Linux
.
env\Scripts ctivate  # En Windows

# Instalar dependencias
pip install -r requirements.txt
```

## 📊 Resultados y Conclusiones

- Se han identificado patrones clave de visualización de contenido, lo que permite optimizar las recomendaciones personalizadas.
- Los datos muestran picos de uso en ciertas franjas horarias, lo cual puede guiar el despliegue de contenido y promociones.
- El análisis sugiere que ciertos géneros de contenido tienen una mayor retención de usuarios, lo que podría influir en futuras inversiones en contenido.

## 🔄 Próximos Pasos

- Expandir el análisis incluyendo más variables demográficas para obtener un perfil más detallado de los usuarios.
- Implementar un modelo de predicción de visualización de contenido para mejorar la recomendación personalizada.
- Explorar el impacto de promociones específicas en el comportamiento de visualización.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar el proyecto, por favor abre un pull request o una issue.
