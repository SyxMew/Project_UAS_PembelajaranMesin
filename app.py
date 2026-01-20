import streamlit as st
import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np
import pandas as pd
import plotly.express as px
import time

# ==========================================
# 1. KONFIGURASI HALAMAN
# ==========================================
st.set_page_config(
    page_title="MangoDoctor Dark AI",
    page_icon="🥭",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# 2. CUSTOM CSS (DARK MODE & TEXT FIX)
# ==========================================
st.markdown("""
    <style>
    /* --- 1. MEMAKSA BACKGROUND GELAP & TEKS TERANG --- */
    .stApp {
        background-color: #0E1117; /* Hitam Gelap */
        color: #FAFAFA; /* Teks Putih Terang */
    }
    
    /* Memaksa semua heading menjadi putih/hijau neon */
    h1 { color: #00E676 !important; font-weight: 800; }
    h2, h3 { color: #69F0AE !important; }
    p, li, span, div { color: #E0E0E0; } /* Teks paragraf abu terang */

    /* --- 2. SIDEBAR STYLING --- */
    section[data-testid="stSidebar"] {
        background-color: #161B22; /* Sedikit lebih terang dari bg utama */
        border-right: 1px solid #30363D;
    }
    
    /* --- 3. KOMPONEN CUSTOM --- */
    /* Tombol Neon */
    .stButton>button {
        background: linear-gradient(45deg, #00C853, #64DD17);
        color: #000000; /* Teks tombol hitam agar kontras */
        border-radius: 10px;
        font-weight: bold;
        border: none;
        box-shadow: 0px 0px 10px rgba(0, 230, 118, 0.4);
        transition: 0.3s;
    }
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0px 0px 20px rgba(0, 230, 118, 0.7);
        color: #000;
    }

    /* Kotak Hasil (Card Style) */
    .result-card {
        background-color: #161B22;
        border: 1px solid #30363D;
        border-radius: 15px;
        padding: 25px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    }

    /* Styling Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #21262D;
        border-radius: 5px;
        color: white;
    }
    .stTabs [aria-selected="true"] {
        background-color: #00E676 !important;
        color: black !important;
        font-weight: bold;
    }
    
    /* Kotak Upload */
    .stFileUploader {
        border: 1px dashed #30363D;
        border-radius: 10px;
        padding: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 3. DATA & LOGIKA
# ==========================================
CLASS_NAMES = [
    'Anthracnose', 'Bacterial Canker', 'Cutting Weevil', 
    'Die Back', 'Gall Midge', 'Healthy', 
    'Powdery Mildew', 'Sooty Mould'
]

DISEASE_INFO = {
    'Anthracnose': {
        'desc': 'Bintik hitam pada daun/buah akibat jamur. Menyebar cepat saat lembab.',
        'solusi': 'Potong bagian sakit. Semprot fungisida (Mancozeb).',
        'status': '🔴 BAHAYA'
    },
    'Bacterial Canker': {
        'desc': 'Luka kanker pada batang/daun. Daun menguning dan rontok.',
        'solusi': 'Gunakan bakterisida tembaga (Copper). Hindari luka pada pohon.',
        'status': '🔴 BAHAYA'
    },
    'Cutting Weevil': {
        'desc': 'Daun muda terpotong-potong akibat gigitan kumbang.',
        'solusi': 'Kumpulkan kumbang manual. Gunakan insektisida kontak.',
        'status': '🟠 WASPADA'
    },
    'Die Back': {
        'desc': 'Ranting mati mengering dari ujung ke pangkal.',
        'solusi': 'Pangkas ranting mati + 3cm bagian sehat. Oles pasta penutup luka.',
        'status': '🔴 BAHAYA'
    },
    'Gall Midge': {
        'desc': 'Bintil-bintil (kutil) pada permukaan daun.',
        'solusi': 'Insektisida sistemik. Musnahkan daun yang parah.',
        'status': '🟠 WASPADA'
    },
    'Healthy': {
        'desc': 'Daun segar, hijau merata, tanpa bercak.',
        'solusi': 'Lanjutkan perawatan rutin (air & pupuk).',
        'status': '🟢 SEHAT'
    },
    'Powdery Mildew': {
        'desc': 'Serbuk putih seperti tepung pada daun/bunga.',
        'solusi': 'Semprot belerang/sulfur di pagi hari.',
        'status': '🟠 WASPADA'
    },
    'Sooty Mould': {
        'desc': 'Lapisan hitam seperti jelaga (biasanya karena kutu).',
        'solusi': 'Basmi kutu daun dulu, lalu cuci jelaga dengan air sabun.',
        'status': '🟡 RINGAN'
    }
}

@st.cache_resource
def load_model():
    try:
        model = tf.keras.models.load_model('Model_Mangga.keras')
        return model
    except Exception as e:
        return None

def predict_image(model, image):
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.LANCZOS)
    img_array = np.asarray(image) / 255.0
    img_reshape = np.expand_dims(img_array, axis=0)
    prediction = model.predict(img_reshape)
    return prediction[0]

# ==========================================
# 4. TAMPILAN UTAMA
# ==========================================

with st.sidebar:
    st.markdown("## ⚙️ Control Panel")
    st.write("Aplikasi deteksi penyakit tanaman mangga berbasis AI.")
    
    st.markdown("---")
    st.info("💡 **Tips Foto:** Pastikan daun terlihat jelas, fokus, dan tidak terlalu gelap.")
    st.markdown("---")
    st.caption("Mode: Dark Cyberpunk")

col_title1, col_title2 = st.columns([0.15, 0.85])
with col_title1:
    st.markdown("<div style='font-size: 40px;'>🥭</div>", unsafe_allow_html=True)
with col_title2:
    st.title("Mango AI Doctor")
    st.markdown("*Intelligent Plant Disease Detection System*")

model = load_model()

if not model:
    st.error("⚠️ Model 'Model_Mangga.keras' tidak ditemukan/rusak.")
else:
    st.markdown("### 📸 Upload Foto Daun")
    file = st.file_uploader("", type=["jpg", "png", "jpeg"])

    if file is not None:
        col1, col2 = st.columns([1, 1.2], gap="large")
        
        with col1:
            st.markdown("#### Preview Gambar")
            image = Image.open(file)
            st.image(image, use_container_width=True, caption="Input Image")
            
            analyze = st.button("🚀 SCAN PENYAKIT", use_container_width=True)
        
        if analyze:
            with col2:
                with st.spinner('Scanning neural patterns...'):
                    time.sleep(1) # Efek visual
                    predictions = predict_image(model, image)
                    class_idx = np.argmax(predictions)
                    confidence = np.max(predictions)
                    label = CLASS_NAMES[class_idx]
                    
                    data_info = DISEASE_INFO.get(label, {})

                st.markdown(f"""
                <div class="result-card">
                    <h4 style="margin-bottom:0; color:#8b949e;">Terdeteksi:</h4>
                    <h1 style="margin-top:0; color:#00E676; font-size: 3em;">{label}</h1>
                    <hr style="border-color: #30363D;">
                    <div style="display:flex; justify-content:space-between;">
                        <span>Keyakinan AI: <b style="color:white;">{confidence*100:.1f}%</b></span>
                        <span style="background-color: #21262D; padding: 2px 10px; border-radius: 5px; border: 1px solid #00E676;">{data_info.get('status', '')}</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                tab1, tab2 = st.tabs(["💊 Solusi & Info", "📊 Statistik Data"])

                with tab1:
                    st.markdown(f"""
                    <div style="background-color: #0d1117; padding: 15px; border-radius: 10px; border: 1px solid #30363D;">
                        <h4 style="color: #58a6ff;">Gejala Klinis:</h4>
                        <p>{data_info.get('desc', '-')}</p>
                        <h4 style="color: #58a6ff;">Tindakan Pengobatan:</h4>
                        <p style="color: #FAFAFA; font-weight: bold;">{data_info.get('solusi', '-')}</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    if label == "Healthy":
                        st.balloons()

                with tab2:
                    df = pd.DataFrame({'Kelas': CLASS_NAMES, 'Probabilitas': predictions})
                    
                    fig = px.bar(
                        df, x='Probabilitas', y='Kelas', orientation='h',
                        color='Probabilitas',
                        color_continuous_scale=['#0D47A1', '#00E676']
                    )
                    fig.update_layout(
                        template="plotly_dark", 
                        plot_bgcolor='rgba(0,0,0,0)', 
                        paper_bgcolor='rgba(0,0,0,0)', 
                        font=dict(color="#E6EDF3"),
                        margin=dict(l=0, r=0, t=30, b=0),
                        height=300
                    )
                    st.plotly_chart(fig, use_container_width=True)