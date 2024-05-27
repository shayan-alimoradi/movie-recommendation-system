import streamlit as st
import requests
import pickle

ACCESS_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwZDQyZDI5NTljYzY4NWI2ZWZmNmJiZWRjYTdjMzViOCIsInN1YiI6IjY2NTQ2MjhiMzM3Zjk5ZmRiYTkxMWJjZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.B9BI1t2YpwEvKSNANWTDOSlpfM4J8w9kARkWPbGFJxU"


movies_list = pickle.load(open("movies_list.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

st.header("Movie Recommender System")
select_value = st.selectbox("Select movie from dropdown", movies_list["original_title"])

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    res = requests.get(url, headers={"Authorization": f"Bearer {ACCESS_TOKEN}"}).json()
    poster_path = res["poster_path"]
    full_path = f"https://image.tmdb.org/t/p/w500/{poster_path}"
    return full_path


def recommend(movies):
    index = movies_list[movies_list["original_title"] == movies].index[0]
    similar_movies = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])

    recommend_movies = []
    recommend_poster = []
    for similar_movie in similar_movies[1:6]:
        movies_id = movies_list.iloc[similar_movie[0]].id
        recommend_movies.append(movies_list.iloc[similar_movie[0]].original_title)
        recommend_poster.append(fetch_poster(movies_id))
    
    return recommend_movies, recommend_poster


if st.button("Show Recommend"):
    movie_name, movie_poster = recommend(select_value)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(movie_name[0])
        st.image(movie_poster[0])
    with col2:
        st.text(movie_name[1])
        st.image(movie_poster[1])
    with col3:
        st.text(movie_name[2])
        st.image(movie_poster[2])
    with col4:
        st.text(movie_name[3])
        st.image(movie_poster[3])
    with col5:
        st.text(movie_name[4])
        st.image(movie_poster[4])

