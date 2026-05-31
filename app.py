import streamlit as st
import time

# Configuración de la pestaña
st.set_page_config(page_title="Especialmente para ti", page_icon="❤️")

# --- ESTILO CSS AVANZADO (Fondo de corazones y Lluvia de Corazones) ---
st.markdown("""
    <style>
    /* Fondo con patrón de corazones */
    .stApp { 
        background-color: #ffdae3 !important;
        background-image: url('https://www.transparenttextures.com/patterns/hearts.png') !important;
    }
    
    /* Animación de corazones cayendo (Custom) */
    @keyframes hearts-fall {
        0% { top: -10%; transform: translateX(0) rotate(0deg); opacity: 1; }
        100% { top: 100%; transform: translateX(100px) rotate(360deg); opacity: 0; }
    }

    .heart-drop {
        position: fixed;
        top: -10%;
        color: #ff4b6e;
        font-size: 24px;
        user-select: none;
        z-index: 9999;
        animation: hearts-fall 4s linear infinite;
    }

    /* Estilos de texto y botones */
    h1, h2, h3, p { color: #5c1d2e !important; font-family: 'Georgia', serif; }
    .stButton>button { 
        background: linear-gradient(45deg, #ff4b6e, #ff85a2) !important; 
        color: white !important; 
        border-radius: 25px !important;
        border: none !important;
        font-weight: bold !important;
        box-shadow: 0px 4px 15px rgba(255, 75, 110, 0.4);
    }
    .stImage img { border: 5px solid white !important; border-radius: 20px !important; }
    </style>
    """, unsafe_allow_html=True)

# Función para generar la lluvia de corazones en HTML
def lluvia_de_corazones():
    corazones_html = ""
    for i in range(20): # Cantidad de corazones
        left = i * 5
        delay = i * 0.2
        corazones_html += f'<div class="heart-drop" style="left: {left}%; animation-delay: {delay}s;">❤️</div>'
    st.markdown(corazones_html, unsafe_allow_html=True)

if 'paso' not in st.session_state:
    st.session_state.paso = 1

# --- FASE 1: ACCESO ---
if st.session_state.paso == 1:
    st.title("✨ Un secreto para la psicóloga más linda...")
    profesion = st.text_input("Para entrar, dime: ¿Qué profesión está estudiando la mujer que me cautivó hace 2 años?", placeholder="Ej. Psicología")
    if st.button("Abrir Corazón"):
        if any(x in profesion.lower() for x in ["psicolo", "psicóloga", "psicologia"]):
            st.success("Acceso concedido...")
            time.sleep(1)
            st.session_state.paso = 2
            st.rerun()

# --- FASE 2: CARGA ---
elif st.session_state.paso == 2:
    with st.status("Cargando sentimientos...", expanded=True) as s:
        st.write("❤️ Preparando la lluvia de corazones...")
        time.sleep(1.5)
        s.update(label="¡Listo!", state="complete")
    st.session_state.paso = 3
    st.rerun()

# --- FASE 3: LA CARTA ---
elif st.session_state.paso == 3:
    lluvia_de_corazones() # <--- AQUÍ ACTIVAMOS LOS CORAZONES EN VEZ DE NIEVE
    st.title("💝 Para ti, con todo mi cariño")
    
    tab1, tab2, tab3, tab4 = st.tabs(["👁️ Tu Mirada", "🎓 Tu Vocación", "🌌 Distancia", "✉️ Nota Final"])

    with tab1:
        st.write("### Tu mirada y tu sonrisa")
        st.write("Tus ojos reflejan una paz y una inteligencia que me atrapan desde hace 2 años.")
        col1, col2 = st.columns(2)
        with col1: st.image("foto1.jpg", caption="Esa mirada ✨")
        with col2: st.image("foto2.jpg", caption="Hermosa ❤️")

    with tab2:
        st.write("### La futura gran Psicóloga")
        st.write("Admiro tu fuerza para luchar por tus sueños y esa chispa para ayudar a los demás.")

    with tab3:
        st.write("### La distancia")
        st.write("El mapa se vuelve pequeño cuando alguien te importa tanto.")

    with tab4:
        st.write("### Nota Final")
        st.write("Te llevo tatuada en el corazón. Eres especial, nunca lo dudes.")
        if st.button("¡Me encantó! ❤️"):
            st.balloons()
