import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="AI Regulation"
)

#### you may edit here onwards ###

st.title("Decoding Public Sentiment:Exploring OpenAI's Regulation Hearing")

#### you may edit here onwards ###


st.write("Sam Altman, CEO of OpenAI, the company who made ChatGPT, testified before the US Senate on May 16, 2023. Altman urged lawmakers to regulate artificial intelligence, arguing that the technology could pose a significant threat to society if it is not properly controlled.")

image1 = Image.open('samaltman.webp') 
st.image(image1, caption='Sam Altman testifying to US Senate about AI Regulation', use_column_width=True)

st.write("With this recent topic, we are aiming to accomplish three things:")

st.markdown("""
- Identify if public is against/pro/neutral to AI Regulation 
- Identify topics discussed about AI regulation
- Provide recommendations for lawmakers 
""")

st.write("These objectives will help us emphasize the importance of public opinion. If we were to somehow regulate AI, the rules, policies and regulations that come with it should not only be coming from one entity, ultimately eliminating bias. ")

st.write('''According to Paul Burstein's work titled "The impact of Public Opinion on Public Policy," it is stated that "Public Opinion holds significant importance." In a democratic nation like ours, expressing our viewpoints can have a pivotal influence on lawmakers.''')

st.write('''Our study will try to uncover the public's opinion on AI Regulation using Data Science methods such as Natural Language Processing. Go through the next pages and explore with us.''')

