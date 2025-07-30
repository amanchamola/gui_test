import streamlit as st
from PIL import Image
import base64
import os

st.set_page_config(page_title="HAPPIEST BIRTHDAY TANISHA")

def set_bg(img_path):
    with open(img_path, "rb") as img_file:
        encoded_img = base64.b64encode(img_file.read()).decode()
    st.markdown(
        f"""
        <style>
        [data-testid="stAppViewContainer"] > div:first-child {{
            background: url("data:image/jpg;base64,{encoded_img}") 50% 50%/cover no-repeat fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


background_image_path = "pictures/background_pictures/WhatsApp Image 2025-07-31 at 12.37.13 AM (3).jpeg"
if os.path.isfile(background_image_path):
    set_bg(background_image_path)
else:
    st.warning("Background image not found. Please check the path.")

folders = [
    "pictures/baby_tani",
    "pictures/Family",
    "pictures/friends",
    "pictures/beautiful_tani",
]

# image_paths = [
#     os.path.join(folder, f)
#     for folder in folders
#     for f in os.listdir(folder)
#     if f.endswith('.jpeg') and os.path.isfile(os.path.join(folder, f))
# ]

image_captions = {
    'pictures/baby_tani/WhatsApp Image 2025-07-31 at 12.25.19 AM (2).jpeg': "Baby Tani 🎂🎈 The most cutest kid i've ever seen",
    'pictures/baby_tani/WhatsApp Image 2025-07-31 at 12.21.58 AM (2).jpeg': "My favourite Picture of little Tani 📸",
    'pictures/baby_tani/WhatsApp Image 2025-07-31 at 12.25.19 AM (1).jpeg': "HAHA GuChu PUCHU BACHA ekdum ❤️",
    'pictures/baby_tani/WhatsApp Image 2025-07-31 at 12.25.19 AM.jpeg': "In the words of sir DJ Khaled: Another One !!",
    'pictures/Family/WhatsApp Image 2025-07-31 at 12.21.57 AM.jpeg': "Family Time: 🏡 I know how much you miss them on your birthday. Aunty holding two shaitans",
    'pictures/Family/WhatsApp Image 2025-07-31 at 12.21.58 AM.jpeg': "Pragyata Saya: DIDI HAPPY BIRTHDAY, I LOVE YOUU but aapmei dimaag ki kami hai",
    'pictures/Family/WhatsApp Image 2025-07-31 at 12.21.57 AM (1).jpeg': "Such a sweet Family Picture. Uncle looks tired after dealing with two bandars",
    'pictures/Family/WhatsApp Image 2025-07-31 at 12.50.13 AM (2).jpeg': "Pragyata: DIDI I MISS YOU bolna bhul gyi thi 😭",
    'pictures/Family/WhatsApp Image 2025-07-31 at 12.25.19 AM (3).jpeg': "RAKHI TIME: With brothers who'll eventually turn to the dark side **liverpool joke** 😝",
    'pictures/Family/WhatsApp Image 2025-07-31 at 12.21.58 AM (1).jpeg': "Tani: BIG SISTER VIBES",
    'pictures/Family/WhatsApp Image 2025-07-31 at 12.21.58 AM (3).jpeg': "!! Another One !!",
    'pictures/Family/WhatsApp Image 2025-07-31 at 12.21.57 AM (2).jpeg': "hahahahahahaahahahahha 😝 😝 😝 😝 Guess who sent me this",
    'pictures/friends/WhatsApp Image 2025-07-31 at 12.50.13 AM.jpeg': "FRIENDS TIME: ARADHYA GAURI Feature toh must hai 👭❤❤",
    'pictures/friends/WhatsApp Image 2025-07-31 at 12.46.49 AM.jpeg': "SADHVI Feature bhi aagya 👭❤",
    'pictures/friends/WhatsApp Image 2025-07-31 at 12.48.26 AM.jpeg': "Gauri Aradhya ke saath spam hai by god",
    'pictures/friends/WhatsApp Image 2025-07-31 at 12.38.58 AM.jpeg': "I'm out of Captions Now 😰 😰",
    'pictures/friends/WhatsApp Image 2025-07-31 at 12.46.05 AM.jpeg': "Rishikesh Feature: I know how happy you were during this trip ❤❤",
    'pictures/friends/WhatsApp Image 2025-07-31 at 12.50.13 AM (1).jpeg': "RAFTING CHLENGE HUM BHIII 🚤 🚤",
    'pictures/beautiful_tani/WhatsApp Image 2025-07-31 at 12.46.04 AM (1).jpeg': "BEAUTIFUL TANI TIME: I mean i can look at this picture for days 📸",
    'pictures/beautiful_tani/WhatsApp Image 2025-07-31 at 12.46.04 AM.jpeg': "STUNNINGGGGGG ❤❤",
    'pictures/beautiful_tani/WhatsApp Image 2025-07-31 at 12.38.58 AM (3).jpeg': "How did your parents made you this beautiful? 😭 😭 ",
    'pictures/beautiful_tani/WhatsApp Image 2025-07-31 at 12.38.58 AM (1).jpeg': "I'm Lost for Words, No Seriously I am 😭 😭",
    'pictures/beautiful_tani/WhatsApp Image 2025-07-31 at 12.38.58 AM (2).jpeg': "BYE BYE Beautiful 22 year old Tani, Welcome to the 23 year old Club ❤❤"
}

image_paths = list(image_captions.keys())
captions = list(image_captions.values())

# captions = [
#     "Baby Tani 🎂🎈 The most cutest kid i've ever seen",
#     "My favourite Picture of little Tani 📸",
#     "HAHA GuChu PUCHU BACHA ekdum ❤️",
#     "In the words of sir DJ Khaled: Another One !!",
#     "Family Time: 🏡 I know how much you miss them on your birthday. Aunty holding two shaitans",
#     "Pragyata Saya: DIDI HAPPY BIRTHDAY, I LOVE YOUU but aapmei dimaag ki kami hai",
#     "Such a sweet Family Picture. Uncle looks tired after dealing with two bandars",
#     "Pragyata: DIDI I MISS YOU bolna bhul gyi thi 😭",
#     "RAKHI TIME: With brothers who'll eventually turn to the dark side **liverpool joke** 😝",
#     "Tani: BIG SISTER VIBES",
#     "!! Another One !!",
#     "hahahahahahaahahahahha 😝 😝 😝 😝 Guess who sent me this",
#     "FRIENDS TIME: ARADHYA GAURI Feature toh must hai 👭❤❤",
#     "SADHVI Feature bhi aagya 👭❤",
#     "Gauri Aradhya ke saath spam hai by god",
#     "I'm out of Captions Now 😰 😰",
#     "Rishikesh Feature: I know how happy you were during this trip ❤❤",
#     "RAFTING CHLENGE HUM BHIII 🚤 🚤",
#     "BEAUTIFUL TANI TIME: I mean i can look at this picture for days 📸",
#     "STUNNINGGGGGG ❤❤",
#     "How did your parents made you this beautiful? 😭 😭 ",
#     "I'm Lost for Words, No Seriously I am 😭 😭",
#     "BYE BYE Beautiful 22 year old Tani, Welcome to the 23 year old Club"
# ]

if 'image_index' not in st.session_state:
    st.session_state.image_index = 0

def previous_image():
    st.session_state.image_index = (st.session_state.image_index - 1) % len(image_paths)

def next_image():
    st.session_state.image_index = (st.session_state.image_index + 1) % len(image_paths)


st.markdown("""
<style>
.balloons {
  position: fixed;
  width: 100vw;
  height: 100vh;
  pointer-events: none;
  z-index: 0;
}
.balloon {
  position: absolute;
  font-size: 70px;
  animation: floatup 7s linear infinite;
}
.balloon:nth-child(1) { left: 5vw; animation-delay: 0s; }
.balloon:nth-child(2) { left: 15vw; animation-delay: 1s; }
.balloon:nth-child(3) { left: 25vw; animation-delay: 2s; }
.balloon:nth-child(4) { left: 35vw; animation-delay: 3s; }
.balloon:nth-child(5) { left: 50vw; animation-delay: 1.5s; }
.balloon:nth-child(6) { left: 65vw; animation-delay: 2.5s; }
.balloon:nth-child(7) { left: 75vw; animation-delay: 4s; }
.balloon:nth-child(8) { left: 85vw; animation-delay: 3s; }
.balloon:nth-child(9) { left: 95vw; animation-delay: 5s; }
@keyframes floatup {
  0% { bottom: -60px; opacity: 0.7; }
  20% { bottom: 30vh; opacity: 1; }
  80% { opacity: 1; }
  100% { bottom: 100vh; opacity: 0; }
}
</style>
<div class="balloons">
  <span class="balloon">🎈</span>
  <span class="balloon">🎈</span>
  <span class="balloon">🎈</span>
  <span class="balloon">🎈</span>
  <span class="balloon">🎈</span>
  <span class="balloon">🎈</span>
  <span class="balloon">🎈</span>
  <span class="balloon">🎈</span>
  <span class="balloon">🎈</span>
</div>
""", unsafe_allow_html=True)


st.markdown("<h1 style='text-align:center; color:#FFF;'>🎉 HAPPY BIRTHDAY TANISHA 🎉</h1>", unsafe_allow_html=True)
st.columns([1, 6, 1])[1].image(image_paths[st.session_state.image_index], use_container_width=True)


st.markdown(f"""
<p style='text-align:center;
           font-family: "Comic Sans MS", cursive, sans-serif;
           font-size: 22px;
           color: #FFF;
           margin-top: 0px;'>
    {captions[st.session_state.image_index]}
</p>
""", unsafe_allow_html=True)


btn_col1, _, btn_col2 = st.columns([3, 1, 3])
with btn_col1:
    st.button("⟵ Previous", on_click=previous_image, use_container_width=True)
with btn_col2:
    st.button("Next ⟶", on_click=next_image, use_container_width=True)
