from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Klasifikasi Lahan Jawa Timur",
    page_icon="🌍",
    layout="wide",
)

st.title("Klasifikasi Lahan Jawa Timur")
st.write(
    "Visualisasi peta hasil klasifikasi tutupan lahan "
    "Provinsi Jawa Timur."
)

map_path = Path("peta_folium.html")

if map_path.exists():
    html = map_path.read_text(encoding="utf-8")
    components.html(
        html,
        height=750,
        scrolling=True,
    )
else:
    st.error(
        "File peta_folium.html tidak ditemukan. "
        "Pastikan file tersedia di direktori utama repositori."
    )
