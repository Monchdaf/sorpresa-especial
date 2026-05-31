import streamlit as st
import time

# Configuración de la pestaña
st.set_page_config(page_title="Para Lizbeth con amor", page_icon="❤️")

# --- ESTILO CSS ---
st.markdown("""
    <style>
    .stApp { 
        background-color: #ffdae3 !important;
        background-image: url('https://www.transparenttextures.com/patterns/hearts.png') !important;
    }
    
    @keyframes hearts-fall {
        0% { top: -10%; transform: translateX(0) rotate(0deg); opacity: 1; }
        100% { top: 100%; transform: translateX(100px) rotate(360deg); opacity: 0; }
    }

    .heart-drop {
        position: fixed;
        top: -10%;
        color: #ff4b6e;
        font-size: 28px;
        user-select: none;
        z-index: 9999;
        animation: hearts-fall 5s linear infinite;
    }

    h1, h2, h3, p, li { color: #5c1d2e !important; font-family: 'Georgia', serif; }
    
    .stButton>button { 
        background: linear-gradient(45deg, #ff4b6e, #ff85a2) !important; 
        color: white !important; 
        border-radius: 25px !important;
        border: none !important;
        font-weight: bold !important;
        padding: 0.8rem 3rem !important;
        box-shadow: 0px 4px 15px rgba(255, 75, 110, 0.4);
    }

    .stImage img { 
        border: 8px solid white !important; 
        border-radius: 25px !important;
        box-shadow: 0px 10px 30px rgba(0,0,0,0.15) !important;
    }
    
    /* Estilo para la línea del tiempo */
    .moment-box {
        background-color: rgba(255, 255, 255, 0.5);
        padding: 15px;
        border-left: 5px solid #ff4b6e;
        border-radius: 0 15px 15px 0;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

def lluvia_de_corazones():
    corazones_html = ""
    for i in range(25):
        left = i * 4
        delay = i * 0.3
        corazones_html += f'<div class="heart-drop" style="left: {left}%; animation-delay: {delay}s;">❤️</div>'
    st.markdown(corazones_html, unsafe_allow_html=True)

if 'paso' not in st.session_state:
    st.session_state.paso = 1

# --- FASE 1: ACCESO ---
if st.session_state.paso == 1:
    st.title("✨ Un secreto para la mejor profesional...")
    st.write("### Hola, Lizbeth...")
    profesion = st.text_input("Para entrar, dime: ¿De qué carrera te graduaste y eres la más brillante?", placeholder="Escribe aquí...")
    if st.button("Abrir mi corazón"):
        if any(x in profesion.lower() for x in ["psicolo", "psicóloga", "psicologia"]):
            st.success("Acceso concedido... Bienvenida.")
            time.sleep(1.2)
            st.session_state.paso = 2
            st.rerun()
        else:
            st.error("Pista: Es la profesión de alguien que sabe leer el alma.")

# --- FASE 2: CARGA ---
elif st.session_state.paso == 2:
    with st.status("Cargando recuerdos...", expanded=True) as s:
        st.write("❤️ Reviviendo momentos de estos 2 años...")
        time.sleep(1.2)
        st.write("✨ Recordando tu sonrisa en aquella fiesta...")
        time.sleep(1.2)
        s.update(label="¡Listo!", state="complete")
    st.session_state.paso = 3
    st.rerun()

# --- FASE 3: LA CARTA ---
elif st.session_state.paso == 3:
    lluvia_de_corazones()
    st.title("💝 Lizbeth, esto es para ti")
    
    # Añadimos la pestaña de "Nuestros Momentos"
    tab1, tab_m, tab2, tab3, tab4 = st.tabs(["👁️ Tu Mirada", "⏳ Momentos", "🎓 Tu Vocación", "🌌 Distancia", "✉️ Nota Final"])

    with tab1:
        st.write("### Lo que me atrapó de ti")
        st.write("Lizbeth, desde que nos vimos en esa fiesta, me atrapaste por completo. Tu presencia y tu bella sonrisa se quedaron grabadas en mí.")
        col1, col2 = st.columns(2)
        with col1: st.image("foto1.jpg", caption="Esa mirada ✨")
        with col2: st.image("foto2.jpg", caption="Tu sonrisa ❤️")

    with tab_m:
        st.write("### Pequeños instantes, grandes recuerdos")
        st.write("Hay cosas que he guardado en mi memoria durante estos dos años porque te hacen única:")
        
        st.markdown("""
        <div class="moment-box">
            <strong>✨ El primer encuentro:</strong> Aquella fiesta donde tu sonrisa hizo que todo lo demás desapareciera. Fue el momento exacto en que supe que no serías alguien pasajera en mi vida.
        </div>
        <div class="moment-box">
            <strong>📩 Tus palabras:</strong> Cada mensaje que me ha hecho el día, demostrándome la persona increíble y empática que eres.
        </div>
        <div class="moment-box">
            <strong>🎓 Tu esfuerzo:</strong> Ver cómo terminabas tu carrera. Ese día confirmé que serías una psicóloga brillante, no solo por tus estudios, sino por tu enorme corazón.
        </div>
        """, unsafe_allow_html=True)

    with tab2:
        st.write("### La mejor Psicóloga")
        st.write("Para mí, ya eres la mejor. Admiro tu empeño, tu enfoque hacia tus metas y tu capacidad para ayudar a los demás. Eres brillante y, además, la psicóloga más hermosa que existe.")

    with tab3:
        st.write("### La Distancia")
        st.write("No me importa la distancia. Seguiré luchando por ti y por lo que siento, porque creo firmemente en nosotros. Los kilómetros no significan nada cuando alguien te llena el alma.")

    with tab4:
        st.write("### Con todo mi amor")
        st.write("Lizbeth, espero que entiendas por qué sigo aquí. Me llenas de amor de una manera inexplicable y, a pesar de todo, mi sentimiento por ti sigue intacto.")
        if st.button("¡Me encantó! ❤️"):
            st.balloons()
