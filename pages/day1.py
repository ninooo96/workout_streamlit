import streamlit as st
import pandas as pd
import time
from PIL import Image

import utils


st.title("Giorno 1")

if "num_esercizio" not in st.session_state:
    st.session_state.num_esercizio = 0

scheda = utils.get_scheda('1_scheda.csv')

if st.session_state.num_esercizio>=0:
    col_1, col_2 = st.columns([1,2])

    with col_1:
        try:
            st.image(f"images/{scheda.iloc[st.session_state.num_esercizio].tolist()[0].lower()}.gif")
        except:
            st.image(Image.open(f"images/image_not_found.gif"))
    with col_2:
        st.markdown(f"**:blue[{scheda.iloc[st.session_state.num_esercizio].tolist()[0]}]**")
        st.markdown(f"**:blue[{scheda.iloc[st.session_state.num_esercizio].tolist()[1]}]**")
        st.markdown(f"**:blue[{scheda.iloc[st.session_state.num_esercizio].tolist()[2]}]**")
        st.markdown(f"**:blue[{scheda.iloc[st.session_state.num_esercizio].tolist()[3]}]**")

# Aggiungi CSS personalizzato per controllare la dimensione dei bottoni

col1, col2= st.columns(2)

# with col1:
if col1.button("<-", use_container_width=True, disabled=(st.session_state.num_esercizio==0)):
    st.session_state.num_esercizio -= 1
    st.rerun()

if col2.button("->", use_container_width=True, disabled=(st.session_state.num_esercizio==scheda.shape[0]-1)):
    st.session_state.num_esercizio += 1
    st.rerun()

if "stop_timer" not in st.session_state:
    st.session_state.stop_timer = False

col1, col2 = st.columns(2)
with col1:
    if st.button("Avvia timer"):
        N = 60
        timer = st.empty()
        for secs in range(N,0,-1):
            if st.session_state.stop_timer==False:
                mm, ss = secs//60, secs%60
                timer.metric("Countdown", f"{mm:02d}:{ss:02d}")
                time.sleep(1)
            else:
                print(st.session_state.stop_timer)
                st.session_state.stop_timer = False
                break
        

with col2:
    if st.button("Stop timer", disabled=False, type="primary"):
        st.session_state.stop_timer = True
        st.rerun()