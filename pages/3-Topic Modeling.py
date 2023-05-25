import streamlit as st

st.set_page_config(
    page_title="AI Regulation"
)

#### you may edit here onwards ###


st.title("Topics of the Senate Hearing")

st.markdown("""

Starting with the Open AI Hearing transcript scraped from the Tech Policy Press website, the data was scraped and cleaned as detailed in the following steps

""")
            
st.image('cleaning.jpg')

st.markdown("""

The cleaning and preparation steps were done to improve the keywords for the topic identification.

Gensim LDA (Latent Dirichlet Allocation) was used to identify the topics discussed during the hearing, which we will be using to classify the social media posts in the following steps. During the hyperparameter tuning process, it was identified that the ideal number is 5 topics, with 67% coherence score. 

""")


st.image('hypertuning.jpg')

st.markdown('Shown below is the visualization of the topic modeling. The keywords in each topic were used to identify the subjects of the US senate hearing which are technology, people, systems, industry/businesses, innovation')

st.image('topic modeling.png')

st.header('The Topics')

st.image('topics.jpg')

st.markdown("On the next pages, we will identify the public's sentiments in each of these topics.")