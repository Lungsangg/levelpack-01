import streamlit as st
from upload_to_drive import main as upload_sync
from download_from_drive import main as download_sync


def upload():
    upload_sync()


def download():
    download_sync()


if __name__ == "__main__":
    col1, col2 = st.columns(2)

    with col1:
        st.button('upload to gdrive', on_click=upload)

    with col2:
        st.button('download from gdrive', on_click=download)
