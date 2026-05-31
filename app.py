import streamlit as st
import time

# Configuración estética de la pestaña
st.set_page_config(page_title="Un espacio para ti", page_icon="🧠✨")

# --- AJUSTE DE COLORES (CSS MEJORADO) ---
st.markdown("""
    <style>
    /* Fondo de la app (un tono rosa pastel muy sutil y elegante) */
    .stApp { 
        background-color: #fff5f6 !important; 
    }
    
    /* Forzar color oscuro y tipografía elegante para psicóloga */
    h1, h2, h3, h4, h5, h6, p, label, .stMarkdown { 
        color: #3d1c24 !important; 
        font-family: 'Georgia', serif;
    }
    
    /* Estilo de las tarjetas de información */
    .stAlert {
        background-color: #ffe3e7 !important;
        border: 1px solid #ffb3c1 !important;
        border-radius: 15px !important;
    }

    /* Estilo de los botones */
    .stButton>button { 
        background: linear-gradient(45deg, #d94663, #ff758f) !important; 
        color: white !important; 
        border-radius: 25px !important;
        border: none !important;
        padding: 0.6rem 2.5rem !important;
        font-weight: bold !important;
        box-shadow: 0px 4px 10px rgba(217, 70, 99, 0.2);
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        background: linear-gradient(45deg, #b8324f, #d94663) !important;
        box-shadow: 0px 6px 15px rgba(217, 70, 99, 0.4);
        transform: translateY(-2px);
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🧩 Un análisis desde el corazón...")

# --- DINÁMICA DE PASOS ---
if 'paso' not in st.session_state:
    st.session_state.paso = 1

# --- FASE 1: FILTRO DE ACCESO ---
if st.session_state.paso == 1:
    st.subheader("Fase 1: Validación de acceso")
    st.write("Para entrar, ingresa la profesión de la persona que inspira este código:")
    
    profesion = st.text_input("¿Qué está estudiando la futura gran profesional que se robó mi atención hace 2 años?", placeholder="Ej. Psicología")
    
    if st.button("Validar Acceso"):
        palabras_clave = ["psicologa", "psicología", "psicóloga", "psicologia"]
        if any(clave in profesion.lower().strip() for clave in palabras_clave):
            st.success("✨ Acceso concedido. Entrando al diván de los recuerdos...")
            time.sleep(2)
            st.session_state.paso = 2
            st.rerun()
        else:
            st.error("Mmm, esa no es la respuesta. Pista: Tiene el superpoder de entender la mente y el corazón.")

# --- FASE 2: TEST DE EMPATÍA ---
elif st.session_state.paso == 2:
    st.subheader("Fase 2: Conectando impulsos")
    st.write("Haz clic en el cerebro para iniciar el escaneo de lo que hay aquí dentro por ti:")
    
    col1, col2, col3 = st.columns([1,1,1])
    with col2:
        if st.button("🧠"):
            with st.status("Procesando datos cognitivos...", expanded=True) as status:
                st.write("🔍 Buscando la mirada más bonita...")
                time.sleep(1.2)
                st.write("⚡ Analizando el impacto de su sonrisa...")
                time.sleep(1.2)
                st.write("📈 Midiendo su nivel de dedicación (Fuera de los límites)...")
                time.sleep(1.2)
                st.write("❤️ Evaluando la distancia... (Resultado: No importa).")
                time.sleep(1)
                status.update(label="¡Análisis completo!", state="complete", expanded=False)
            st.session_state.paso = 3
            st.rerun()

# --- FASE 3: EL DIAGNÓSTICO (LA CARTA) ---
elif st.session_state.paso == 3:
    st.balloons()
    st.header("📋 Diagnóstico: Me encantas.")
    
    st.write("Hace dos años que apareciste en mi mapa, y aunque a veces el camino tiene baches o silencios, quiero que leas esto hoy:")

    # Pestañas organizadas con lo que te gusta de ella
    tab1, tab2, tab3, tab4 = st.tabs(["👁️ Tu Mirada y Sonrisa", "💼 Tu Vocación", "🌌 La Distancia", "✉️ Mi Nota Especial"])
    
    with tab1:
        st.write("### Lo primero que desarma mi mundo")
        st.write("Si tuviera que describir qué me atrapa de ti, empezaría sin duda por **tus ojos y tu sonrisa**.")
        st.write("Tienes una luz increíble que se nota a kilómetros. Tu sonrisa tiene el efecto inmediato de arreglar cualquier mal día.")
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExM3Z0bXh6N3R5dGFrOHF5b3p4eXFjcHBsZDN0dWpmaXJ6dnl6ZXN4OCZwaXQ9bSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Y8S9IY7ZYiSE8/giphy.gif", width=350)

    with tab2:
        st.write("### Tu dedicación por los demás")
        st.write("Me fascina ver **lo mucho que luchas por tu trabajo y por tus metas**. Sé perfectamente que vas a ser una psicóloga brillante.")
        st.write("Esa empatía natural que tienes, esas ganas genuinas de ayudar a las personas a sanar y salir adelante, es de las cosas más admirables y hermosas que he visto en alguien.")
        st.info("💡 *Dato psicológico real:* La admiración es la base del cariño más profundo. Y yo te admiro muchísimo.")

    with tab3:
        st.write("### Kilómetros vs Sentimientos")
        st.write("Sí, es verdad que vivimos lejos. La distancia física está ahí y no la podemos negar...")
        st.write("Pero en mi mapa mental y en mi corazón, **la distancia pierde toda la fuerza**. No importa cuántos kilómetros nos separen, el cariño y la atención que sembraste en mí hace dos años no se borran con geografía.")

    with tab4:
        st.write("### Sinceramente...")
        st.write("Sé que hemos tenido nuestros inconvenientes, momentos donde nos dejamos de hablar y veces donde me canso un poco de la intermitencia... no te lo voy a negar. Pero al final del día, pongo todo en una balanza y **tú sigues ganando**.")
        st.write("Te llevo en el corazón de una forma muy bonita.")
        
        st.write("---")
        st.write("**¿Te gustó este pequeño espacio digital hecho solo para ti?**")
        if st.button("¡Me encantó! ❤️"):
            st.snow()
            st.success("¡Misión cumplida! Espero haberte sacado una sonrisa gigante hoy. Te la mereces. 😊")
