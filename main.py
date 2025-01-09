import streamlit as st
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import json

# Configuración de la base de datos
engine = create_engine('sqlite:///tareas.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# Definición de la tabla de tareas
class Tarea(Base):
    __tablename__ = 'tareas'
    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String, nullable=False)
    descripcion = Column(String)
    completada = Column(Boolean, default=False)

# Crear la tabla si no existe
Base.metadata.create_all(engine)

# Funciones principales
def agregar_tarea(titulo, descripcion):
    nueva_tarea = Tarea(titulo=titulo, descripcion=descripcion)
    session.add(nueva_tarea)
    session.commit()
    actualizar_tareas()

def listar_tareas():
    return session.query(Tarea).all()

def marcar_completada(tarea_id):
    tarea = session.query(Tarea).filter_by(id=tarea_id).first()
    if tarea:
        tarea.completada = True
        session.commit()
    actualizar_tareas()

def eliminar_tareas_completadas():
    session.query(Tarea).filter_by(completada=True).delete()
    session.commit()
    actualizar_tareas()

def exportar_tareas():
    tareas = listar_tareas()
    datos = [{"id": t.id, "titulo": t.titulo, "descripcion": t.descripcion, "completada": t.completada} for t in tareas]
    with open("tareas.json", "w") as file:
        json.dump(datos, file)
    st.success("Tareas exportadas a 'tareas.json'.")

def importar_tareas():
    try:
        with open("tareas.json", "r") as file:
            datos = json.load(file)
            for item in datos:
                if not session.query(Tarea).filter_by(id=item["id"]).first():
                    nueva_tarea = Tarea(
                        id=item["id"],
                        titulo=item["titulo"],
                        descripcion=item["descripcion"],
                        completada=item["completada"]
                    )
                    session.add(nueva_tarea)
            session.commit()
        st.success("Tareas importadas con éxito.")
        actualizar_tareas()
    except FileNotFoundError:
        st.error("No se encontró el archivo 'tareas.json'.")

def actualizar_tareas():
    """Actualiza la lista de tareas almacenada en session_state."""
    st.session_state["tareas"] = listar_tareas()

# Inicializar session_state para tareas si no existe
if "tareas" not in st.session_state:
    actualizar_tareas()

# Interfaz gráfica con Streamlit
st.title("Gestión de Tareas")

# Sección para agregar nueva tarea
st.header("Agregar nueva tarea")
with st.form(key="formulario_tarea"):
    titulo = st.text_input("Título")
    descripcion = st.text_area("Descripción")
    submitted = st.form_submit_button("Agregar tarea")
    if submitted:
        if titulo:
            agregar_tarea(titulo, descripcion)
            st.success("Tarea agregada con éxito.")
        else:
            st.error("El título es obligatorio.")

# Sección para listar tareas
st.header("Lista de tareas")
tareas = st.session_state["tareas"]
if tareas:
    for tarea in tareas:
        col1, col2 = st.columns([4, 1])
        with col1:
            st.write(f"**ID:** {tarea.id} | **Título:** {tarea.titulo} | {'(Completada)' if tarea.completada else '(Pendiente)'}")
        with col2:
            if not tarea.completada:
                if st.button(f"✔️ Completar", key=f"completar_{tarea.id}"):
                    marcar_completada(tarea.id)
                    # Actualizar la lista de tareas en tiempo real
                    st.session_state["tareas"] = listar_tareas()
else:
    st.info("No hay tareas pendientes.")

# Botón para eliminar tareas completadas
if st.button("Eliminar tareas completadas"):
    eliminar_tareas_completadas()
    st.success("Tareas completadas eliminadas.")

# Sección para exportar e importar tareas
st.header("Exportar e Importar tareas")
col1, col2 = st.columns(2)

with col1:
    if st.button("Exportar tareas"):
        exportar_tareas()

with col2:
    if st.button("Importar tareas"):
        importar_tareas()