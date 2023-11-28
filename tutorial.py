import streamlit as st
st.set_page_config(page_title='MyFirstLit',page_icon='random')
st.image('https://media.istockphoto.com/id/1382384282/photo/bangalore-or-bengaluru.webp?b=1&s=170667a&w=0&k=20&c=qxO3Yl7LBs5jewoI5eAWsLrVtEw0QyH4RdKwyZrALCg=')
mymenu=st.sidebar.selectbox('My Menu',('home','fillform','download'))
st.title('technology')
st.header('garima')
st.text('this is tutorial in streamlit library')
st.image('https://media.istockphoto.com/id/1382384282/photo/bangalore-or-bengaluru.webp?b=1&s=170667a&w=0&k=20&c=qxO3Yl7LBs5jewoI5eAWsLrVtEw0QyH4RdKwyZrALCg=')
if(mymenu=='home'):
 st.markdown('<centre><h1>WELCOME</h1></centre>',unsafe_allow_html=True)
 st.video('https://www.youtube.com/watch?v=jADTdg-o8i0')
elif(mymenu=='fillform'):
 with st.form('my form'):
  name=st.text_input('enter name')
  dob=st.date_input("choose dob ")
  marks=st.slider('choose marks')
  k=st.form_submit_button('submit form')
  if k:
   st.write('Name : ',name,'DOB : ',dob,'Marks : ',marks)
elif(mymenu=='download'):
 st.header('downloads')
 st.download_button('download now','hello this is the download data','gt.txt')