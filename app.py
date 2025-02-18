import streamlit as st
import os
from supabase import create_client, Client
import utils

st.set_page_config(page_title="Scheda Palestra", page_icon="💪")

st.sidebar.title("Navigazione")
st.sidebar.write("Seleziona una pagina dal menu.")

st.title("🏠 Home Page")
st.write("Benvenuto nella mia app multipagina con Streamlit! Usa la sidebar per navigare.")

# Initialize connection.
# Uses st.cache_resource to only run once.
@st.cache_resource
def init_connection():
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    return create_client(url, key)

# Funzione per scaricare il file dal bucket
@st.cache_resource
def download_file(bucket_name, file_name, folder=os.getcwd()):
    # Scarica il file dal bucket
    response = supabase.storage.from_(bucket_name).download(file_name)
    try:
        # Crea un percorso di salvataggio nella root dell'app
        file_path = os.path.join(folder, file_name)  # Percorso nella root dell'app
        with open(file_path, "wb") as f:
            f.write(response)
        return file_path
    except:
        st.error(f"Errore nel recupero del file: {response.status_code}")
        return None

@st.cache_resource
def download_gif_files(bucket_name: str, download_folder: str):
    # Ottieni la lista dei file nel bucket
    response = supabase.storage.from_(bucket_name).list()
    
    # Filtra i file con estensione .gif
    gif_files = [file['name'] for file in response if file['name'].endswith('.gif')]
    
    if not gif_files:
        print("Nessun file GIF trovato.")
        return
    
    # Crea la cartella di download se non esiste
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)
    
    # Scarica ogni file GIF
    for gif_file in gif_files:
        if not os.path.exists(f"{download_folder}/{gif_file}"):
            print(f"Scaricando il file: {gif_file}")
            file_data = supabase.storage.from_(bucket_name).download(gif_file)
            

            # Salva il file nella cartella di download
            file_path = os.path.join(download_folder, gif_file)
            with open(file_path, "wb") as f:
                f.write(file_data)
                utils.resize_gif(file_path, file_path, (300, 300))

supabase = init_connection()

bucket_name= 'antonio'
file_name='1_scheda.csv'

file_list_response = supabase.storage.from_('antonio').list()
# print(file_list_response[2])
file = download_file(bucket_name, file_name)
download_gif_files(bucket_name, 'images')