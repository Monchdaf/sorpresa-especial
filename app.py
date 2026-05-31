import streamlit as st
import time

# Configuración de la pestaña
st.set_page_config(page_title="Especialmente para ti", page_icon="❤️")

# --- ESTILO CSS (Fondo de corazones y tonos vino/rosa) ---
st.markdown("""
    <style>
    .stApp { 
        background-color: #fff0f3 !important;
        background-image: url('https://www.transparenttextures.com/patterns/hearts.png') !important;
    }
    h1, h2, h3, h4, p, label { 
        color: #5c1d2e !important; 
        font-family: 'Georgia', serif;
    }
    .stButton>button { 
        background: linear-gradient(45deg, #ff4b6e, #ff85a2) !important; 
        color: white !important; 
        border-radius: 25px !important;
        border: none !important;
        padding: 0.6rem 2.5rem !important;
        box-shadow: 0px 4px 10px rgba(255, 75, 110, 0.2);
    }
    /* Estilo para las fotos */
    .img-container img {
        border-radius: 20px !important;
        box-shadow: 0px 10px 25px rgba(0,0,0,0.2) !important;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

if 'paso' not in st.session_state:
    st.session_state.paso = 1

# --- FASE 1: ACCESO ---
if st.session_state.paso == 1:
    st.title("✨ Un secreto para la psicóloga más linda...")
    profesion = st.text_input("Para entrar, dime: ¿Qué profesión está estudiando la mujer que me cautivó hace 2 años?", placeholder="Ej. Psicología")
    if st.button("Abrir Corazón"):
        if any(x in profesion.lower() for x in ["psicolo", "psicóloga", "psicologia"]):
            st.success("Acceso concedido... Prepárate.")
            time.sleep(2)
            st.session_state.paso = 2
            st.rerun()
        else:
            st.info("Pista: Ella tiene el don de escuchar y entender el alma.")

# --- FASE 2: CARGA ---
elif st.session_state.paso == 2:
    st.subheader("⌛ Analizando sentimientos...")
    with st.status("Conectando con los recuerdos...", expanded=True) as s:
        st.write("🔍 Buscando la mirada más inteligente y dulce...")
        time.sleep(1.5)
        st.write("❤️ Recordando por qué ella es tan especial...")
        time.sleep(1.5)
        s.update(label="¡Listo! Entrando...", state="complete")
    st.session_state.paso = 3
    st.rerun()

# --- FASE 3: LA CARTA ---
elif st.session_state.paso == 3:
    st.balloons()
    st.title("💝 Para ti, con todo mi cariño")
    
    tab1, tab2, tab3, tab4 = st.tabs(["👁️ Tu Mirada", "🎓 Tu Vocación", "🌌 Distancia", "✉️ Nota Final"])

    with tab1:
        st.write("### Tu mirada y tu sonrisa")
        st.write("Te lo he dicho y te lo repito: tienes una luz increíble. Tus ojos reflejan una paz y una inteligencia que me atrapan desde hace 2 años.")
        
        # Galería de fotos
        col1, col2 = st.columns(2)
        with col1:
            st.image("foto1.jpg", caption="Esa mirada que lo dice todo ✨")
        with col2:
            st.image("foto2.jpg", caption="Simplemente hermosa ❤️")

    with tab2:
        st.write("### La futura gran Psicóloga")
        st.write("Me llena de orgullo ver tu dedicación. Tienes esa chispa para ayudar y entender a los demás, y sé que serás una profesional brillante.")
        st.write("Admiro tu fuerza para luchar por tus sueños a pesar de todo.")

    with tab3:
        st.write("### Los kilómetros no importan")
        st.write("Vivimos lejos, es verdad. Pero cuando alguien te importa tanto como tú a mí, el mapa se vuelve pequeño.")
        st.write("La distancia solo es una prueba para ver qué tan lejos puede llegar un sentimiento real.")

    with tab4:
        st.write("### Algo de mi para ti")
        st.write("Sé que hemos tenido pausas, silencios y momentos difíciles. A veces me canso de la intermitencia, pero luego te veo, te recuerdo y me doy cuenta de que **te llevo tatuada en el corazón**.")
        st.write("Eres especial, nunca lo dudes.")
        if st.button("¡Me encantó! ❤️"):
            st.snow()
            st.write("Gracias por existir y por ser parte de mi vida estos 2 años. 😊")
