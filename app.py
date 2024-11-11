import streamlit as st
import pickle
import pandas as pd
import requests


# Custom CSS to adjust the margin and padding
st.markdown("""
    <style>
        .main {
            margin:20;
            width: 100%;
        }
        .block-container {
            max-width: 80% !important;  
        }
    </style>
""", unsafe_allow_html=True)

# Your Streamlit app code follows

# Function to fetch poster using Steam API
@st.cache_data
def fetch_poster(game_id):
    url = f"https://store.steampowered.com/api/appdetails?appids={game_id}"
    response = requests.get(url)
    data = response.json()

    # Access the JSON response using game_id as the key
    if str(game_id) in data and data[str(game_id)]['success']:
        poster_path = data[str(game_id)]['data'].get('header_image')
        return poster_path
    else:
        return None

# Load similarity matrix and game data
cosine_sim = pickle.load(open('similarity.pkl', 'rb'))
Games_dict = pickle.load(open('game_dict.pkl', 'rb'))
steam_data = pd.DataFrame(Games_dict)

# Recommendation function
def recommend(game_title):
    if game_title not in steam_data['name'].values:
        st.error(f"Game title '{game_title}' not found in the dataset.")
        return [], []

    # Get the index of the game
    idx = steam_data[steam_data['name'] == game_title].index[0]

    if idx >= len(cosine_sim):
        st.error("Selected game index is out of bounds.")
        return [], []

    # Get similarity scores and sort them
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:11]

    # Prepare recommendations
    recommended_game_names = []
    recommended_game_posters = []

    for i in sim_scores:
        game_index = i[0]
        game_id = steam_data.iloc[game_index]['appid']
        game_name = steam_data.iloc[game_index]['name']

        # Fetch poster and append data
        poster = fetch_poster(game_id)
        recommended_game_names.append(game_name)
        recommended_game_posters.append(poster)

    return recommended_game_names, recommended_game_posters

# Streamlit UI
st.title('GameRack')

selected_game_name = st.selectbox("Select a game:", steam_data['name'].values)

if st.button("Recommend"):
    recommendations, posters = recommend(selected_game_name)

    # Display the recommendations
    if recommendations:
        cols = st.columns(5)  # Create three columns

        for idx, (name, poster) in enumerate(zip(recommendations, posters)):
            col = cols[idx % 5]  # Distribute items across the columns
            with col:
                st.text(name)
                if poster:
                    st.image(poster)
                else:
                    st.write("Poster not available.")
    else:
        st.write("No recommendations found.")

