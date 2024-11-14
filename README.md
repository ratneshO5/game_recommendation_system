# GameRack - Game Recommendation System

GameRack is a **game recommendation system** that provides users with personalized game suggestions based on a large dataset of Steam games. The web application features a sleek UI, real-time search predictions, and detailed game info, all built using **Python**, **Streamlit**, and deployed on **Streamlit Cloud**.

## 🌐 Live Demo

Try the application here: [GameRack on Streamlit](https://gamerack.streamlit.app/)

## 🔥 Features

- **Real-Time Search and Autocomplete**: Type in a game name and get instant search predictions.
- **Game Recommendations**: Personalized game suggestions based on user input using TF-IDF.
- **Related Games Section**: Discover similar games on the game info page, enhanced with association rule mining.
- **User-Friendly Interface**: Modern and responsive UI for a great user experience.

## 🗂️ Dataset Information

The dataset includes information about games such as:
- **Attributes**: appid, name, release_date, developer, publisher, platforms, categories, genres, achievements, ratings, playtime, and price.
- **Source**: Steam dataset with a diverse collection of attributes for accurate recommendations.

## 🛠️ Technologies Used

- **Python**: Core programming language
- **Pandas, NumPy**: Data analysis
- **Scikit-learn**: Machine learning model (TF-IDF)
- **Streamlit**: Web framework for the application
- **Streamlit Cloud**: Hosting platform

## 📦 Installation

1. Clone the repository:
  
   git clone https://github.com/your-username/game_recommendation_system.git
   cd game_recommendation_system
   

2. Install the required packages:
  
   pip install -r requirements.txt
   

3. Run the app.py application:
   
   streamlit run app.py
   

## 🚀 Usage

- Open the application in your web browser using the provided URL.
- Select a game from the dropdown to get recommendations.
- Explore related games and discover new titles based on your interests.

## 📊 Screenshots
![image](https://github.com/user-attachments/assets/94536751-af4e-4c4c-9e3a-41c649272d70)
![image](https://github.com/user-attachments/assets/80427e04-f02b-481b-8c2a-6e1941879239)



## 🤝 Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests.
