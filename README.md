
# Aplicación de Gestión de Tareas con Streamlit

## Descripción

Esta es una aplicación de gestión de tareas desarrollada en **Python** con interfaz gráfica usando **Streamlit** y persistencia de datos en una base de datos **SQLite** mediante **SQLAlchemy**. La aplicación permite a los usuarios gestionar sus tareas diarias mediante las siguientes funcionalidades:

- Agregar nuevas tareas con título y descripción.
- Listar tareas pendientes y completadas.
- Marcar tareas como completadas.
- Eliminar todas las tareas completadas.
- Exportar las tareas a un archivo JSON.
- Importar tareas desde un archivo JSON.
- Persistencia de datos en base de datos SQLite.
- Actualización automática de la interfaz al completar, eliminar o importar tareas.

<img src="https://github.com/dev-ccazares/crud_tareas/blob/main/captura.png" alt="Captura del proyecto" width="500">

## Requisitos

- Python 3.8 o superior
- Librerías necesarias:

  ```bash
  pip install streamlit sqlalchemy
  ```

## Cómo ejecutar la aplicación

1. Clona este repositorio o copia el archivo principal.
2. Abre una terminal en el directorio donde se encuentra el archivo.
3. Ejecuta el siguiente comando:

   ```bash
   streamlit run main.py
   ```

4. Se abrirá una ventana en tu navegador con la interfaz de la aplicación.

## Estructura del código

El código está dividido en las siguientes secciones:

1. **Configuración de la base de datos**:  
   Se utiliza **SQLAlchemy** para definir la tabla de tareas y gestionar la conexión con la base de datos SQLite.

2. **Funciones principales**:  
   - `agregar_tarea`: Agrega una nueva tarea a la base de datos.
   - `listar_tareas`: Lista todas las tareas almacenadas.
   - `marcar_completada`: Marca una tarea como completada.
   - `eliminar_tareas_completadas`: Elimina todas las tareas que han sido completadas.
   - `exportar_tareas`: Exporta las tareas a un archivo JSON.
   - `importar_tareas`: Importa tareas desde un archivo JSON.
   - `actualizar_tareas`: Actualiza la lista de tareas en la interfaz.

3. **Interfaz gráfica**:  
   Se utiliza **Streamlit** para crear una interfaz intuitiva que permite al usuario interactuar con las funcionalidades mencionadas.

## Funcionalidades

### 1. Agregar Tareas

Permite agregar una nueva tarea ingresando un título y una descripción. Al hacer clic en "Agregar tarea", la tarea se guarda en la base de datos y la lista se actualiza automáticamente.

### 2. Listar Tareas

Muestra todas las tareas almacenadas en la base de datos. Cada tarea se muestra con su **ID**, **título** y **estado** (Pendiente o Completada).

### 3. Marcar Tareas como Completadas

Cada tarea pendiente tiene un botón "Completar". Al hacer clic en este botón, el estado de la tarea cambia a "Completada" y la lista se actualiza automáticamente.

### 4. Eliminar Tareas Completadas

Permite eliminar todas las tareas que ya han sido marcadas como completadas. La lista se actualiza automáticamente tras eliminar las tareas.

### 5. Exportar Tareas

Permite exportar todas las tareas almacenadas a un archivo JSON llamado `tareas.json`.

### 6. Importar Tareas

Permite importar tareas desde un archivo JSON llamado `tareas.json`. Las tareas importadas se muestran inmediatamente en la lista.
