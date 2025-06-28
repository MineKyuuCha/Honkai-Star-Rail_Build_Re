# Honkai Star Rail - Character Build Recommendation

## 📚 Description

This is a web-based application that provides character build recommendations for Honkai Star Rail based on user input (comments or questions). Built with Streamlit, it uses NLP (TF-IDF + cosine similarity) techniques to match user input to the character build database.

Features:
- Build recommendations based on user comments or queries
- Displays character images, relics, planar sets, lightcones, and team recommendations
- Multi-language support (English and Indonesian)
- UI with background wallpaper and clean layout

## 🚀 How to Run

1. **Clone this repository**:
2.     ```bash
             git clone https://github.com/MineKyuuCha/Honkai-Star-Rail_Build_Re.git
             cd Honkai-Star-Rail_Build_Re



3.  Install dependencies:

   pip install -r requirements.txt




4.  Run the Streamlit app:
   streamlit run streamlit_app.py




6.  Project Structure


   ├── dataset_build.csv

   ├── streamlit_app.py

   ├── requirements.txt

   ├── README.md




7.  📝Notes The initial dataset is provided in dataset_build.csv. You can expand it by adding more characters, builds, relics, planars, etc.

   You can change the background wallpaper by modifying the URL in the page_bg_img section in streamlit_app.py.

   Future improvements may include auto-scraping forum comments and generating builds dynamically.




8. 🤝Contributing
   Pull requests and suggestions are welcome!

