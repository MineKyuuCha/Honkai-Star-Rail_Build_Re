import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from googletrans import Translator

# -----------------------
# Load dataset
# -----------------------
df = pd.read_csv("dataset_build.csv")

# -----------------------
# Setting   UI
# -----------------------
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://raw.githubusercontent.com/MineKyuuCha/Honkai-Star-Rail_Build_Re/main/Robin.jpeg");
    background-size: cover;
    filter: brightness(70%);
}
.block-container {
    background-color: rgba(0, 0, 0, 0.5);
    padding: 20px;
    border-radius: 10px;
}
.big-font {
    font-size:36px !important;
    color: white;
}
h1, h2, h3, h4, h5, h6, p, div, span {
    color: white;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# -----------------------
# Choose Language (default English)
# -----------------------
lang = st.selectbox("Choose Language", ["English", "Indonesia"], index=0)

translator = Translator()

preserve_words = ["Relic", "Planar", "Rope", "Build"]

def smart_translate(text):
    if lang == "Indonesia":
        for word in preserve_words:
            text = text.replace(word, f"##{word}##")
        try:
            translated = translator.translate(text, dest='id').text
            for word in preserve_words:
                translated = translated.replace(f"##{word}##", word)
            translated = translated.replace("#", "")
            return translated
        except:
            return text
    return text

# -----------------------
# Query
# -----------------------
if 'user_input' not in st.session_state:
    st.session_state.user_input = ''

title_text = "Honkai Star Rail - Character Build Recommendation" if lang == "English" else "Rekomendasi Build Karakter Honkai Star Rail"
st.title(title_text)

st.session_state.user_input = st.text_input(smart_translate("Input Comment / ask build"), value=st.session_state.user_input)

if st.session_state.user_input:
    tfidf = TfidfVectorizer(stop_words="english")
    tfidf_matrix = tfidf.fit_transform(df['komentar'])
    input_vec = tfidf.transform([st.session_state.user_input])
    sim_scores = cosine_similarity(input_vec, tfidf_matrix).flatten()

    df['similarity'] = sim_scores
    top_match = df.sort_values(by='similarity', ascending=False).iloc[0]

    if top_match['similarity'] < 0.1:
        st.warning(smart_translate("You sure not typo ?"))
    else:
        st.subheader(smart_translate(f"Recommended build for: {top_match['karakter']} "))

        st.image(top_match['gambar_karakter'], width=700)
        st.markdown(f"<div class='big-font'>{top_match['karakter']} ⭐⭐⭐⭐⭐</div>", unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)
        with col1:
            st.image(top_match['gambar_path'], width=100, caption="Path")
        with col2:
            st.image(top_match['gambar_element'], width=100, caption="Element")
        with col3:
            st.write(smart_translate("Type:"), top_match['tipe_build'])

        st.subheader(smart_translate("Build Description"))
        deskripsi = top_match['deskripsi_build']
        st.write(smart_translate(deskripsi))

        st.subheader("Relic")
        st.write(top_match['relic_set'])
        st.image(top_match['gambar_relic'], width=100)

        st.subheader("Planar")
        st.write(top_match['planar_set'])
        st.image(top_match['gambar_planar'], width=100)

        st.subheader("Lightcone")
        st.write(top_match['lightcone'])
        st.image(top_match['gambar_lightcone'], width=180)

        st.subheader(smart_translate("Team Recommendation"))
        team_imgs = top_match['gambar_team_rekomendasi'].split(';')
        team_names = top_match['team_rekomendasi'].split(';')
        cols = st.columns(len(team_imgs))
        for i, img in enumerate(team_imgs):
            cols[i].image(img, width=180, caption=team_names[i])
