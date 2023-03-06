import pandas as pd
import streamlit as st
import pickle
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=81ecbaac78995a1ea7a36fa7082ecfdc&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500"+data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title']==movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[0:7]

    recommended_movies=[]
    recommended_posters=[]
    recommended_movies_tags=[]
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_tags.append(movies.iloc[i[0]].tags[0:100])
        recommended_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_posters,recommended_movies_tags



similarity =pickle.load(open('similarity.pkl','rb'))
movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)


st.title('Witness The Amazing Hollywood Movies')
# st.caption('BY Manvith Kumar')


selected_movies = st.selectbox(
    'Choose Your Movie',
movies['title'].values)

if st.button('Recommend'):
      name,posters,tags = recommend(selected_movies)

      col1,col2,col3,col4,col5,col6,col7 = st.columns(7,gap="medium")
      row1,row2,row3 = st.tabs(['a','b','c'])
      with col1:
          st.subheader(name[0])
          st.image(posters[0])
          st.caption(tags[0])
      with col2:
          st.subheader(name[1])
          st.image(posters[1])
          st.caption(tags[1])
      with col3:
          st.subheader(name[2])
          st.image(posters[2])
          st.caption(tags[2])
      with col4:
          st.subheader(name[3])
          st.image(posters[3])
          st.caption(tags[3])
      with col5:
          st.subheader(name[4])
          st.image(posters[4])
          st.caption(tags[4])
      with col6:
          st.subheader(name[5])
          st.image(posters[5])
          st.caption(tags[5])
      with col7:
          st.subheader(name[6])
          st.image(posters[6])
          st.caption(tags[6])