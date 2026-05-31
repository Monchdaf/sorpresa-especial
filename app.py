import streamlit as st
import time

# Configuración de la pestaña
st.set_page_config(page_title="Para Lizbeth con amor", page_icon="❤️")

# --- ESTILO CSS (Fondo de corazones y Lluvia de Corazones) ---
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

    /* Estilo de las pestañas */
    .stTabs [data-baseweb="tab-list"] { gap: 8px; }
    .stTabs [data-baseweb="tab"] {
        background-color: rgba(255, 255, 255, 0.4);
        border-radius: 10px 10px 0 0;
        color: #5c1d2e;
        padding: 10px 20px;
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
    st.title("✨ Un secreto para la psicóloga más linda...")
    st.write("### Hola, Lizbeth...")
    profesion = st.text_input("Para entrar, dime:¿De qué carrera te graduaste y eres la más brillante?", placeholder="Escribe aquí...")
    if st.button("Abrir mi corazón"):
        if any(x in profesion.lower() for x in ["psicolo", "psicóloga", "psicologia"]):
            st.success("Acceso concedido... Prepárate para lo que sigue.")
            time.sleep(1.5)
            st.session_state.paso = 2
            st.rerun()
        else:
            st.error("Esa no es la respuesta correcta... Pista: Es la carrera de alguien que sabe leer el alma.")

# --- FASE 2: CARGA ---
elif st.session_state.paso == 2:
    with st.status("Preparando algo especial...", expanded=True) as s:
        st.write("❤️ Buscando recuerdos de aquella fiesta...")
        time.sleep(1.5)
        st.write("✨ Analizando la sonrisa de Lizbeth...")
        time.sleep(1.5)
        st.write("📦 Enviando sentimientos a través de la distancia...")
        time.sleep(1.2)
        s.update(label="¡Todo listo!", state="complete")
    st.session_state.paso = 3
    st.rerun()

# --- FASE 3: LA CARTA ---
elif st.session_state.paso == 3:
    lluvia_de_corazones()
    st.title("💝 Lizbeth, esto es para ti")
    
    tab1, tab2, tab3, tab4 = st.tabs(["👁️ Tu Mirada", "🎓 Tu Vocación", "🌌 Distancia", "✉️ Nota Final"])

    with tab1:
        st.write("### Lo que me atrapó de ti")
        st.write(f"""
        Lizbeth, tengo que confesarte que me has llamado la atención desde el primer momento en que nuestros caminos se cruzaron. 
        **Desde que nos vimos en esa fiesta, me atrapaste.** No fue solo el momento, fue tu presencia y, sobre todo, tu bella sonrisa la que se quedó grabada en mi mente.
        
        Desde hace dos años no he dejado de pensar en tus ojos y en la forma en que iluminas todo a tu alrededor. Tus ojos reflejan una paz y una inteligencia 
        que me cautivaron desde el día uno y, sinceramente, es mi lugar favorito en el mundo.
        """)
        col1, col2 = st.columns(2)
        with col1: st.image("foto1.jpg", caption="Esa mirada que me cautivó ✨")
        with col2: st.image("foto2.jpg", caption="Tu sonrisa, mi debilidad ❤️")

    with tab2:
        st.write("### La mejor Psicóloga que el mundo tendrá")
        st.write(f"""
        Siempre te lo digo y no me voy a cansar de repetirlo: **vas a ser la mejor psicóloga.** Y no lo digo solo por decir, lo digo porque veo en ti 
        a una mujer con un corazón enorme, alguien a quien genuinamente le gusta ayudar a los demás. 
        
        Me encanta el empeño y la pasión que le metes a tu carrera, ver cómo vas enfocada hacia tus metas es algo que admiro profundamente de ti. 
        Además de ser una profesional dedicada, eres la psicóloga más bonita que existe. Tu vocación es el reflejo de la gran persona que eres por dentro.
        """)

    with tab3:
        st.write("### Sin importar los kilómetros")
        st.write(f"""
        Sé que tenemos la distancia en contra y, a veces, puede sentirse un poco difícil. Ambos tenemos trabajos, metas personales y responsabilidades 
        que nos mantienen ocupados, pero quiero que sepas algo muy importante: **no me importa la distancia.** Yo seguiré luchando por ti y por lo que siento, aunque me cueste, porque creo firmemente en lo que puede llegar a haber entre nosotros. 
        Los kilómetros son solo números cuando el sentimiento es real, y para mí, tú vales cada metro de separación.
        """)

    with tab4:
        st.write("### Con todo mi amor")
        st.write(f"""
        Lizbeth, espero que con este pequeño detalle que programé para ti, entiendas por qué me gustas tanto y por qué sigo aquí, luchando por ti día tras día. 
        
        Eres una persona que me llena de amor de una manera que no puedo explicar del todo con palabras, por eso intenté hacerlo con este código. 
        A pesar de los inconvenientes o los silencios que hemos tenido, mi sentimiento por ti no cambia. **De verdad, me llenas el alma.**
        """)
        st.markdown("---")
        if st.button("¡Me encantó! ❤️"):
            st.balloons()
            st.write("### ¡Gracias por ser tú, Lizbeth! 😊")
            st.write("Espero haberte sacado la sonrisa más grande de tu día.")
