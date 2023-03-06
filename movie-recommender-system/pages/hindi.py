import pandas as pd
import streamlit as st
import pickle
from PIL import Image
import random
import requests

poster_list=[
    'https://1.bp.blogspot.com/-79vmCCwoZ_E/X4_artAUp7I/AAAAAAAAaO4/qsr-ZiGmgwcmsP72F_NAyWamwA2rsLhTwCLcBGAsYHQ/s595/Suraj-Pe-Mangal-Bhari-movie-poster-release-date.jpg',
    'https://webneel.com/daily/sites/default/files/images/daily/08-2018/4-india-movie-poster-design-idea-bahubali.jpg',
    'https://mir-s3-cdn-cf.behance.net/project_modules/disp/eb2be551087591.58e274bfab3d3.jpg',
    'https://movieposters2.com/images/1540460-b.jpg',
    'https://www.bollywoodhungama.com/wp-content/uploads/2022/12/Shah-Rukh-Khan-gears-up-for-Pathaan-with-new-thrilling-poster-featuring-Deepika-Padukone-and-John-Abraham-asks-fans-%E2%80%98Peti-baandh-li-hai.jpg',
    'https://moviegalleri.net/wp-content/gallery/allu-arjun-pushpa-first-look-posters-hd/actor-allu-arjun-pushpa-hindi-movie-first-look-posters-hd.jpg',
    'https://www.mixindia.com/wp-content/uploads/2022/05/Doctor-G-Hindi-Movie-Poster-2-scaled.jpg',
    'https://i.pinimg.com/236x/ab/70/9b/ab709b432e40b76a05ed57daf227790b--hindi-movies-online-bollywood-posters.jpg',
    'https://upload.wikimedia.org/wikipedia/en/6/69/83_film_poster.jpg',
    'https://static.toiimg.com/photo/msid-68936282/68936282.jpg',
    'https://www.mixindia.com/wp-content/uploads/2022/05/Yodha-Hindi-Movie-Poster-2.jpg',
    'https://www.mixindia.com/wp-content/uploads/2022/02/Prithviraj-Hindi-Movie-Poster-1.jpg',
    'https://media-cache.cinematerial.com/p/500x/nnujfom5/sanju-indian-movie-poster.jpg?v=1525428167',
    'https://cdn.cinematerial.com/p/297x/0qq6vcys/super-hero-indian-movie-poster-md.jpg?v=1526979502',
    'https://media-cache.cinematerial.com/p/500x/wryuyls6/kaappaan-indian-movie-poster.jpg?v=1569394716',
    'https://media-cache.cinematerial.com/p/500x/fva3vb9r/arundhati-indian-movie-poster.jpg?v=1456438634',
    'https://e1.pxfuel.com/desktop-wallpaper/998/938/desktop-wallpaper-brahmastra-bollywood-2022-movie-poster-thumbnail.jpg',
    'https://pbs.twimg.com/media/FnN15SvaYAE2Qcf?format=jpg&name=large' 
]

similarity =pickle.load(open('hindisimilarity.pkl','rb'))
movies_dict = pickle.load(open('hindimovie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

poster = Image.open('images.jpg')


def recommend(movie):
    movie_index = movies[movies['title']==movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:8]

    recommended_movies=[]
    recommended_movies_tags=[]
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_tags.append(movies.iloc[i[0]].tags[0:100])
    return recommended_movies,recommended_movies_tags

st.title('Witness The Spectacular Bollywood Movies')
selected_movies = st.selectbox(
    'Choose Your Movie',
movies['title'].values)

if st.button('Recommend'):
      name,tags = recommend(selected_movies)

      col1,col2,col3,col4,col5,col6,col7 = st.columns(7,gap='medium')
      with col1:
          st.subheader(name[0])
          st.image(random.choice(poster_list))
          st.caption(tags[0])
      with col2:
          st.subheader(name[1])
          st.image(random.choice(poster_list))
          st.caption(tags[1])
      with col3:
          st.subheader(name[2])
          st.image(random.choice(poster_list))
          st.caption(tags[2])
      with col4:
          st.subheader(name[3])
          st.image(random.choice(poster_list))
          st.caption(tags[3])
      with col5:
          st.subheader(name[4])
          st.image(random.choice(poster_list))
          st.caption(tags[4])
      with col6:
          st.subheader(name[5])
          st.image(random.choice(poster_list))
          st.caption(tags[5])