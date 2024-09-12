# pracial-1_HPIV

---

# **Gestión de Eventos**

**Descripción**

**Gestión de Eventos** es una aplicación web para la administración de eventos. Permite a los usuarios listar, crear, editar y eliminar eventos de manera sencilla. La aplicación está construida con Django y proporciona una interfaz intuitiva para la gestión de eventos en tiempo real.

## **Características**

- **Listar Eventos**: Visualiza todos los eventos disponibles en una lista.
- **Crear Eventos**: Agrega nuevos eventos con facilidad.
- **Editar Eventos**: Modifica los detalles de eventos existentes.
- **Eliminar Eventos**: Elimina eventos que ya no sean necesarios.

## **Tecnologías Utilizadas**

- **Django**: Framework web de Python para el desarrollo rápido y limpio de aplicaciones.
- **Python**: Lenguaje de programación utilizado para desarrollar la lógica de la aplicación.
- **HTML/CSS**: Tecnologías de frontend para diseñar y estructurar las páginas web.

## **Instalación**

Sigue estos pasos para configurar el proyecto en tu entorno local:

1. **Clona el repositorio**:

   ```bash
   git clone https://github.com/ekkology/pracial-1_HPIV.git
   cd gestio_de_eventos
   ```
2. **Crea un entorno virtual**:

   ```bash
   conda activate  dj_conda
   # o en caso que quieras usar alternativas a conda 
   source env/bin/activate 
   ```
3. **Instala las dependencias**:

   ```bash
   pip install -r requirements.txt
   ```
4. **Aplica las migraciones de la base de datos**:

   ```bash
   python manage.py migrate
   ```
5. **Inicia el servidor de desarrollo**:

   ```bash
   python manage.py runserver
   ```
6. **Accede a la aplicación**:

   Abre tu navegador y visita `http://127.0.0.1:8000/` para ver la aplicación en funcionamiento.

## **Uso**

- **Listar Eventos**: Visita `http://127.0.0.1:8000/eventos/` para ver todos los eventos.
- **Crear Evento**: Utiliza el enlace en la página de eventos para acceder al formulario de creación.
- **Editar Evento**: Haz clic en el enlace de edición junto al evento que deseas modificar.
- **Eliminar Evento**: En la página de edición, encontrarás la opción para eliminar el evento.
