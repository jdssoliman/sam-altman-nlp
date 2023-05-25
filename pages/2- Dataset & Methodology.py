import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="AI Regulation"
)

#### you may edit here onwards ###

st.title("The Dataset & Methodology")

st.markdown("""

The data of this study were obtained from three sources:  
    1. Open AI Senate Hearing Transcript from Tech Policy Press  
    2. Twitter  
    3. Reddit 
            """)


##add image here of dataset dashboard when finalizes

st.markdown("The topics from the senate hearing will be identified using topic modeling; and the public posts will be categorized and analyzed via sentiment analysis for each of these identified topics.")

st.image('methodology.png')






