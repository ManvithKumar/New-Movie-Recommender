import pandas as pd
import streamlit as st
import pickle
import random
import requests

poster_list=[
    'https://static.toiimg.com/photo/msid-71832899/71832899.jpg',
    'https://cinefame.com/wp-content/uploads/2016/03/Myna-Kunja-Kaanom-movie-posters-3.jpg',
    'https://moviegalleri.net/wp-content/gallery/tamil-year-2022/Kombu-Vacha-Singamda-Movie-New-Year-2022-Wishes-Poster.jpg',
    'https://i.pinimg.com/550x/cb/b6/d8/cbb6d8828f9ca4b2c1510999d36547b3.jpg',
    'https://cdn.cinematerial.com/p/297x/oeyq7b59/rudra-thandavam-french-movie-poster-md.jpg?v=1633159263',
    'https://webneel.com/daily/sites/default/files/images/daily/01-2019/7-tamil-movie-poster-design-kollywood-imaika-nodigal-prathoolnt.jpg',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRQ2PrslglfjuTR8H5vzJ-O8oqOVTDmPzIlB3IHHbbGh44zk9KCf_NXOv-fVgSayT7bl-Q&usqp=CAU',
    'https://www.kerala9.com/wp-content/uploads/2022/03/beast-tamil-movie-hd-poster-006-674x1024.jpg',
    'https://www.mixindia.com/wp-content/uploads/2022/01/Beast-Tamil-Movie-Poster.jpg',
    'https://www.plumeriamovies.com/wp-content/uploads/2018/01/PS-Arjuns-Amutha-Sriya-Sree-Ashna.jpg',
    'https://www.mixindia.com/wp-content/uploads/2022/03/Mohandas-Tamil-Movie-Poster.webp',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQGq7GBYCL9D-99vYZy6l_HnZUm07OEUah3UeHwexws7lsgOjSrPlKmzrLFHi291Gbf1zk&usqp=CAU'
]

similarity =pickle.load(open('tamilsimilarity.pkl','rb'))
movies_dict = pickle.load(open('tamilmovie.pkl','rb'))
movies = pd.DataFrame(movies_dict)


def recommend(movie):
    movie_index = movies[movies['Title']==movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:8]

    recommended_movies=[]
    recommended_movies_tags=[]
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].Title)
        recommended_movies_tags.append(movies.iloc[i[0]].tags[0:100])
    return recommended_movies,recommended_movies_tags

st.title('Witness The Spectacular Bollywood Movies')
selected_movies = st.selectbox(
    'Choose Your Movie',
movies['Title'].values)

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