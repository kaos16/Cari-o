
import streamlit as st

st.set_page_config(page_title="Para mi Mudosa 💖", page_icon="💘", layout="centered")

st.markdown("""
    <style>
    .titulo {
        font-size: 48px;
        text-align: center;
        color: #ff3366;
        font-weight: bold;
        margin-top: 30px;
    }
    .corazon {
        text-align: center;
        font-size: 70px;
        animation: latido 1s infinite;
        margin-bottom: 30px;
    }
    @keyframes latido {
        0% {transform: scale(1);}
        50% {transform: scale(1.3);}
        100% {transform: scale(1);}
    }
    .mensaje {
        background-color: #fff0f5;
        border-radius: 15px;
        padding: 30px;
        font-size: 20px;
        color: #333;
        margin-top: 20px;
        line-height: 1.6;
    }
    .firma {
        margin-top: 60px;
        text-align: center;
        color: gray;
        font-style: italic;
        font-size: 18px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='titulo'>💘💘💘 Para mi Mudosa 💘💘💘</div>", unsafe_allow_html=True)
st.markdown("<div class='corazon'>❤️ 💖 💗 💘 💝 💓 💞</div>", unsafe_allow_html=True)

if st.button("💌 Ver mensaje 💌"):
    with st.expander("💬 Mensaje de amor"):
        st.markdown("""
            <div class='mensaje'>
            Mi preciosa mudosa 💕<br><br>
            Desde aquel 5 de junio del 2023, mi mundo cambió para siempre. Cada día contigo es una aventura hermosa llena de ternura, sonrisas, abrazos y sueños compartidos.<br><br>
            Tu risa es mi melodía favorita, tus ojos mi lugar favorito y tu amor mi fuerza más grande. Eres mi compañera, mi cómplice, mi todo. Gracias por estar, por quedarte, por amarme tal como soy.<br><br>
            Esta pequeña app es solo un detalle digital, pero en cada línea de código está mi corazón entero para ti.
            <br><br>Te amo más de lo que las palabras pueden decir... para siempre tuyo ❤️
            </div>
        """, unsafe_allow_html=True)

if st.button("🎶 Escuchar 'Solo tú' de Luis Miguel 🎶"):
    st.markdown("""
        <div style='text-align: center; margin-top: 20px;'>
            <a href='https://youtu.be/_wEsG3st3X8?si=kAJbIi1Ac3ENW0Ia' target='_blank'>
                👉 Haz clic aquí para escuchar la canción 🎵
            </a>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<div class='firma'>Con todo mi amor, tu Emmanuel 🌹</div>", unsafe_allow_html=True)
