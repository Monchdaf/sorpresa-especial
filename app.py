import streamlit as st
import time

# Configuración estética de la pestaña
st.set_page_config(page_title="Para alguien muy especial", page_icon="💌")

# --- AJUSTE DE COLORES (CSS) ---
# Forzamos textos oscuros, fondo rosa suave y botones estilizados
st.markdown("""
    <style>
    /* Fondo de la app */
    .stApp { 
        background-color: #fff0f3 !important; 
    }
    
    /* Forzar color oscuro en títulos y textos para que se lean perfectamente */
    h1, h2, h3, h4, h5, h6, p, label, .stMarkdown { 
        color: #4a1525 !important; 
        font-family: 'Helvetica Neue', Arial, sans-serif;
    }
    
    /* Estilo del título principal */
    h1 {
        font-family: 'Georgia', serif;
        font-weight: bold;
    }

    /* Estilo del botón "Verificar" y "Me encantó" */
    .stButton>button { 
        background-color: #ff4b6b !important; 
        color: white !important; 
        border-radius: 20px !important;
        border: none !important;
        padding: 0.5rem 2rem !important;
        font-weight: bold !important;
    }
    
    /* Efecto al pasar el mouse por el botón */
    .stButton>button:hover {
        background-color: #e63e5d !important;
        color: white !important;
    }
    
    /* Ajuste para el cuadro donde escribe su nombre */
    input {
        color: #4a1525 !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("✨ Un secreto guardado en código...")

# --- DINÁMICA INICIAL ---
if 'paso' not in st.session_state:
    st.session_state.paso = 1

if st.session_state.paso == 1:
    st.subheader("Fase 1: La prueba de identidad")
    nombre = st.text_input("¿Cómo se llama la persona más linda de este mundo? (Pista: Eres tú)")
    if st.button("Verificar"):
        if nombre.strip() != "":
            st.success(f"¡Identidad confirmada! Hola, {nombre} ❤️")
            time.sleep(1.5)
            st.session_state.paso = 2
            st.rerun()

elif st.session_state.paso == 2:
    st.subheader("Fase 2: Un pequeño juego")
    st.write("Haz clic en el corazón para cargar la carta de amor:")
    
    col1, col2, col3 = st.columns([1,1,1])
    with col2:
        if st.button("❤️"):
            with st.status("Cargando cosas que me gustan de ti...", expanded=True) as status:
                st.write("Buscando recuerdos...")
                time.sleep(1)
                st.write("Analizando tu sonrisa...")
                time.sleep(1)
                st.write("Contando tus virtudes (son demasiadas)...")
                time.sleep(1)
                status.update(label="¡Listo!", state="complete", expanded=False)
            st.session_state.paso = 3
            st.rerun()

elif st.session_state.paso == 3:
    # --- LA CARTA INTERACTIVA ---
    st.balloons()
    st.header("Lo que más me gusta de ti...")
    
    # Usando pestañas para organizar la carta
    tab1, tab2, tab3 = st.tabs(["💫 Tu Esencia", "😊 Tu Sonrisa", "✉️ Mi Mensaje"])
    
    with tab1:
        st.write("### No es solo lo que haces, es quién eres.")
        st.write("Me encanta tu forma de ver la vida y la calma que transmites.")
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJpZzR6bm1ueXp4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4JnB0PWEmZXA9djFfaW50ZXJuYWxfZ2lmX2J5X2lkJmN0PWc/l41lTfuxV6mN8tF4s/giphy.gif", width=300)

    with tab2:
        st.write("### Tu sonrisa es mi lugar favorito.")
        st.write("Podría estar horas escuchándote reír. Es, sin duda, lo mejor de mis días.")

    with tab3:
        st.write("### Para terminar...")
        st.info("Hice este pequeño código porque una persona tan especial no merece un mensaje común.")
        st.write("**¿Te gustó esta sorpresa?**")
        if st.button("¡Me encantó!"):
            st.snow()
            st.write("¡Misión cumplida! Me hiciste el día con esa respuesta. 😊")
