# Movie Recommender System

This project is a movie recommender system that suggests similar movies based on a selected movie. It uses the TMDB dataset and the TMDB API to fetch movie posters.

## Project Structure

The project consists of the following components:

1. **Data Preprocessing and Feature Extraction:**
   - Load and preprocess the movie dataset.
   - Combine genres and overview into a single feature for each movie.
   - Use CountVectorizer to convert text data into numerical features.
   - Calculate cosine similarity between movie features.

2. **Movie Recommendation Functionality:**
   - Define a function to recommend movies based on cosine similarity.
   - Fetch movie posters using the TMDB API.

3. **Web Interface with Streamlit:**
   - Create a simple web interface using Streamlit.
   - Display movie recommendations and their posters.

## Files

- `tmdb_movies_data.csv`: CSV file containing the movie dataset.
- `movies_list.pkl`: Pickle file containing preprocessed movie features.
- `similarity.pkl`: Pickle file containing cosine similarity matrix.
- `app.py`: Streamlit app script for the movie recommender system.

## Setup Instructions

### Prerequisites

- Python 3.7 or above
- Required Python libraries:
  - pandas
  - sklearn
  - streamlit
  - requests
  - pickle

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/movie-recommender-system.git
    cd movie-recommender-system
    ```

2. Install the required libraries:

    ```bash
    pip install -r requirements.txt
    ```

3. Download the TMDB dataset and place it in the project directory as `tmdb_movies_data.csv`.

### Running the Project

1. Preprocess the data and save the necessary files:

    ```python
    # Run the following script in a Python environment

    import pandas as pd
    import pickle
    from sklearn.feature_extraction.text import CountVectorizer
    from sklearn.metrics.pairwise import cosine_similarity

    # Load the data
    movies = pd.read_csv("tmdb_movies_data.csv")

    # Preprocess the data
    features = movies[["id", "original_title", "genres", "overview"]]
    features["tags"] = features["genres"] + " " + features["overview"]
    features = features.drop(columns=["genres", "overview"], axis=1)

    # Vectorize the data
    cv = CountVectorizer(max_features=10866, stop_words="english")
    vector = cv.fit_transform(features["tags"].values.astype("U")).toarray()

    # Calculate cosine similarity
    similarity = cosine_similarity(vector)

    # Save the processed data
    pickle.dump(features, open("movies_list.pkl", "wb"))
    pickle.dump(similarity, open("similarity.pkl", "wb"))
    ```

2. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

### Usage

- Open the Streamlit app in your web browser.
- Select a movie from the dropdown list.
- Click the "Show Recommend" button to display recommended movies and their posters.

### API Key

To fetch movie posters, the app uses the TMDB API. Replace the `ACCESS_TOKEN` in `app.py` with your own TMDB API access token.

```python
ACCESS_TOKEN = "your_tmdb_api_access_token"
