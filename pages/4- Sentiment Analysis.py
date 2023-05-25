import streamlit as st

st.set_page_config(
    page_title="AI Regulation"
)

#### you may edit here onwards ###

st.title("Sentiment analysis of Twitter and Reddit Data")



st.markdown("""
After computing the similarity scores of the posts to the five topics, it was observed that most or 40.7% of the posts were classified under AI & Systems, followed by People and Technology. Notice that most of the posts were classified in Systems, and that is mainly because discussions of governance fall under this topic.
""")
            
st.image('label.jpg')

st.markdown("""
The sentiments are mainly positive on the sectors of people and systems. in the industry and innovation sectors the opinions are mostly neutral. And for the sentiments about technology they are mostly positive which are closely followed by neutral sentiments. Let's take a closer look at the sentiments on these different topics.

""")
            
st.image("SA.jpg")


st.header("AI & Systems")

st.image('01 systems.jpg')

st.markdown("""

For the topic of AI and systems here and positive sentiments it discusses AI’s role in affectively optimizing systems and improving governance processes. it says here in the sample text that AI can improve the operations within a hospital or medical facility.
In neutral sentiments are they detailed how AI is utilized in system optimization and governance without passing any judgment such as hear the text Stating the Senate hearing of sam altman.
For the negative sentiments, they also expressed ethical concerns of tech dominance where in this text it states that It is an unfortunate case that AI will inevitably replace thousands and thousands of jobs.

""")
            

st.header("AI & People")

st.image('02 people.jpg')

st.markdown("""

In the topic of AI and people the positive sentiments acknowledges and applauds the positive impact of AI into the every day human activities here in the sample text, the user mentions the potential of AI for the benefit neurodivergent individuals.
For the neutral sentiments, AI was discussed about its integration into human activities without any clear positive or negative opinion and in this text the user is asking when Is the chat GPT app coming to Singapore. 
now for the negative sentiments. they also expressed concerns about The uncertainties on whether humans can properly adapt to aI and the sample text says that they are concerned about not knowing how to align our human activities with AI development

""")
            
st.header("AI & Technology")

st.image('03 technology.jpg')

st.markdown("""

In the topic of AI artificial intelligence as it technology the positive sentiments Celebrate aI like chat GPT for it's beneficial influence and role in the advancement of society and the industry. Here in the sample Text it emphasizes how AI machine learning algorithms have improved colonoscopies.
For neutral sentiments they discuss the role of AI in society and industry but without any positive or negative bias here in this sample text it talks about how chat GPT and me Journey are used for Imagineering.
For negative sentiments they voiced concerns about the potential negative impacts of AI in the society and the industry such as overregulation. Here in this  sample text The user mentioned a vulgar word about some Altman's Initiative in the regulation of ai.

""")
            
st.header("AI & Innovation")
st.image('04 innovation.jpg')
st.markdown("""
For AI and innovation the positive sentiments praises how they can take part in Augmentin human creativity for example the text here below says How game development can be revolutionized with artificial intelligence.
The neutral sentiments talks about a certain type platforms such as chat GPT just like what was stated here in the text below.
For the negative sentiments it highlights how Hey I can be exploited for personal gain

""")
            

st.header("AI & Industry")
st.image('05 industry.jpg')
st.markdown("""
For AI and the industry the positive sentiments and commends the role of AI and enhancing businesses such as this sample texted and said that Chachi beauty is being used by their business.
For the neutral statements they provide Context about how AIS used in the business sector such as the street that says The presence of business owners using AI tools.
The negative sentiments highlighted the concerns of AI Being smarter and more capable than humans such as this sample text Talks about ai and enslaving mankind.

""")
            
st.header("Sample Tweets")

st.image("people twt.jpg")
st.image("tech twt.jpg")
st.image("industry twt.jpg")
            



            









