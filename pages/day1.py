import streamlit as st


st.title("Giorno 1")
st.write("Questa è la prima pagina della tua app multipagina con Streamlit.")

if "num_esercizio" not in st.session_state:
    st.session_state.num_esercizio = 0

esercizio = [
    {"numero": 1,
    "titolo": "pulley"
    },
    {"numero": 2,
    "titolo": "lat_machine"
    }
]

col1, col2 = st.columns([2,1])

with col1:
    if st.button("<-", disabled=(st.session_state.num_esercizio==0)):
        st.session_state.num_esercizio -= 1
        st.rerun()

with col2:
    if st.button("->", disabled=(st.session_state.num_esercizio==len(esercizio)-1)):
        st.session_state.num_esercizio += 1
        st.rerun()

st.write(f"{st.session_state.num_esercizio} -- {esercizio[st.session_state.num_esercizio]["titolo"]}")