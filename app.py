import streamlit as st
import time

# Configuración de la pestaña
st.set_page_config(page_title="Para Lizbeth con amor", page_icon="❤️")

# --- ESTILO CSS AVANZADO (Fondo, lluvia constante y ráfaga del botón) ---
st.markdown("""
    <style>
    .stApp { 
        background-color: #ffdae3 !important;
        background-image: url('https://www.transparenttextures.com/patterns/hearts.png') !important;
    }
    
    /* Lluvia constante (cae) */
    @keyframes hearts-fall {
        0% { top: -10%; transform: translateX(0) rotate(0deg); opacity: 1; }
        100% { top: 100%; transform: translateX(100px) rotate(360deg); opacity: 0; }
    }

    /* Ráfaga de celebración (sube) */
    @keyframes hearts-rise {
        0% { bottom: -10%; transform: translateX(0) scale(0.5); opacity: 1; }
        50% { opacity: 1; }
        100% { bottom: 110%; transform: translateX(150px) scale(1.5) rotate(180deg); opacity: 0; }
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

    .heart-rise {
        position: fixed;
        bottom: -10%;
        color: #de1b44;
        font-size: 35px;
        user-select: none;
        z-index: 10000;
        animation: hearts-rise 4s ease-out forwards;
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
    </style>
    """, unsafe_allow_html=True)

def lluvia_de_corazones():
    corazones_html = ""
    for i in range(25):
        left = i * 4
        delay = i * 0.3
        corazones_html += f'<div class="heart-drop" style="left: {left}%; animation-delay: {delay}s;">❤️</div>'
    st.markdown(corazones_html, unsafe_allow_html=True)

def rafaga_corazones():
    # Esta función hace que salgan corazones hacia arriba al presionar el botón
    corazones_suben = ""
    for i in range(30):
        left = (i * 3.3) + 5
        delay = (i % 5) * 0.2
        corazones_suben += f'<div class="heart-rise" style="left: {left}%; animation-delay: {delay}s;">💖</div>'
    st.markdown(corazones_suben, unsafe_allow_html=True)

if 'paso' not in st.session_state:
    st.session_state.paso = 1

if 'celebrar' not in st.session_state:
    st.session_state.celebrar = False

# --- FASE 1: ACCESO ---
if st.session_state.paso == 1:
    st.title("✨ Un secreto para la mejor profesional...")
    st.write("### Hola, Lizbeth...")
    profesion = st.text_input("Para entrar, dime: ¿De qué carrera te graduaste y eres la más brillante?", placeholder="Escribe aquí...")
    if st.button("Abrir mi corazón"):
        if any(x in profesion.lower() for x in ["psicolo", "psicóloga", "psicologia"]):
            st.success("Acceso concedido... Bienvenida, Licenciada.")
            time.sleep(1.5)
            st.session_state.paso = 2
            st.rerun()
        else:
            st.error("Mmm, esa no es la respuesta. Pista: Es la profesión de alguien que sana con las palabras.")

# --- FASE 2: CARGA ---
elif st.session_state.paso == 2:
    with st.status("Preparando algo especial...", expanded=True) as s:
        st.write("❤️ Recordando aquella fiesta donde te conocí...")
        time.sleep(1.5)
        st.write("✨ Admirando tu dedicación y tu esfuerzo...")
        time.sleep(1.5)
        st.write("📦 Acortando la distancia para ti...")
        time.sleep(1.2)
        s.update(label="¡Todo listo!", state="complete")
    st.session_state.paso = 3
    st.rerun()

# --- FASE 3: LA CARTA ---
elif st.session_state.paso == 3:
    lluvia_de_corazones()
    
    # Si activó el botón, disparamos los corazones hacia arriba
    if st.session_state.celebrar:
        rafaga_corazones()
        
    st.title("💝 Lizbeth, esto es para ti")
    
    tab1, tab2, tab3, tab4 = st.tabs(["👁️ Tu Mirada", "🎓 Tu Vocación", "🌌 Distancia", "✉️ Nota Final"])

    with tab1:
        st.write("### Lo que me atrapó de ti")
        st.write(f"""
        Lizbeth, desde hace dos años hay algo que no ha cambiado: la forma en que me cautivaste. **Desde que nos vimos en esa fiesta, me atrapaste por completo.** No fue solo el momento, fue tu presencia y, sobre todo, tu bella sonrisa la que se quedó grabada en mí. No he dejado de pensar en tus ojos; reflejan una paz y una inteligencia que me atraparon desde el primer día. Eres, sin duda, lo más bonito que mis ojos han visto.
        """)
        col1, col2 = st.columns(2)
        with col1: st.image("foto1.jpg", caption="Esa mirada que me cautivó ✨")
        with col2: st.image("foto2.jpg", caption="Tu sonrisa, mi debilidad ❤️")

    with tab2:
        st.write("### La mejor Psicóloga que existe")
        st.write(f"""
        Sé que ya terminaste tu carrera y que ahora vienen pasos importantes como tu título, pero para mí, **tú ya eres la mejor psicóloga.** Veo en ti a una mujer con una capacidad increíble para ayudar a los demás. Me encanta el empeño que le metes a todo lo que haces y cómo vas enfocada hacia tus metas. Admiro profundamente tu dedicación; ver esa pasión en ti es algo hermoso. Además de ser brillante, eres la psicóloga más bonita del mundo.
        """)

    with tab3:
        st.write("### Sin importar los kilómetros")
        st.write(f"""
        Aunque la distancia esté presente, para mí no es un obstacle insuperable. Sé que ambos tenemos trabajos, metas y responsabilidades, pero **no me importa la distancia.** Yo seguiré luchando por ti y por lo que siento, aunque me cueste. Creo firmemente que lo que hay entre nosotros es especial y puede llegar muy lejos. Los kilómetros no significan nada cuando alguien te llena tanto como tú a mí.
        """)

    with tab4:
        st.write("### Con todo mi amor")
        st.write(f"""
        Lizbeth, espero que con este detalle entiendas por qué sigo aquí y por qué sigo luchando por ti. Eres una persona que me llena de amor de una manera inexplicable. 
        
        A pesar de los inconvenientes o los silencios, mi sentimiento sigue intacto. Sigo aquí porque de verdad te quiero en mi vida. **Me llenas el alma.**
        """)
        st.markdown("---")
        if st.button("¡Me encantó! ❤️"):
            st.session_state.celebrar = True
            st.rerun()

    # Si se presionó el botón, mostramos el mensaje final abajo
    if st.session_state.celebrar:
        st.write("### ¡Gracias por ser tú, Lizbeth! 😊")
