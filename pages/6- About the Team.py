import streamlit as st
from PIL import Image
st.set_page_config(
    page_title="AI Regulation"
)

#### you may edit here onwards ###

st.title("Meet the Team")

st.write("Our name JAPGJae is an abbreviation of the first letters of the names of the team members, namely, Jamie, Ace, Pau, Gian and Jed. They found a mutual love for the Korean dish _japchae_ (glass noodles) and _jigae_ (hot stew), explaining the remaining two letters _ae_. ")

#1
st.subheader('Jamie Cuadra')

# st.write("Jamie Description ")

# image1 = Image.open('samaltman.webp') 
# st.image(image1, caption='Jamie Cuadra', use_column_width=True)

#2
st.subheader('Ace Canacan')

# st.write("Ace Description ")

# image2 = Image.open('ace.jpg') 
# st.image(image2, caption='Ace Canacan', use_column_width=True)

#3
st.subheader('Pau Sanchez')

# st.write("Pau Description ")

# image3 = Image.open('pau.jpg') 
# st.image(image3, caption='Pau Sanchez', use_column_width=True)

#4
st.subheader('Gian Servanez')

# st.write("Gian Description ")

# image4 = Image.open('samaltman.webp') 
# st.image(image4, caption='Gian Servanez', use_column_width=True)

#5
st.subheader('Jed Soliman')

# st.write("Jed Description ")

# image5 = Image.open('jed.jpg') 
# st.image(image5, caption='Jed Soliman', use_column_width=True)


#try with link

url_jamie = "https://www.linkedin.com/in/austincarvajal/"
url_ace = "https://www.linkedin.com/in/acecanacan/"
url_pau = "https://www.linkedin.com/in/jann-pauline-sanchez/"
url_gian = "https://www.linkedin.com/in/gpservanez/"
url_jed = "https://www.linkedin.com/in/jeremiah-dominic-soliman-59a708155/"
#url_rods = "https://www.linkedin.com/in/ajloconer/"

st.subheader('Jamie')
st.write("Cuadra, Jamie [LinkedIn](%s)" % url_jamie)

st.subheader('Ace')
st.write("Canacan, Ace [LinkedIn](%s)" % url_ace)

st.subheader('Pau')
st.write("Sanchez, Jann Pauline [LinkedIn](%s)" % url_pau)

st.subheader('Gian')
st.write("Servanez, Gian Paolo [LinkedIn](%s)" % url_gian)

st.subheader('Jed')
st.write("Soliman, Jeremiah David [LinkedIn](%s)" % url_jed)


st.markdown('Mentor')
st.subheader('Rods')
st.write("Casera, Rodel")
#st.write("Cuadra, Jamie [LinkedIn](%s)" % url_AJ)


st.write("Feel free to add us on our socials! See you out there!")
