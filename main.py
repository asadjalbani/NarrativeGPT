import streamlit as st
from clarifai.client.model import Model
from dotenv import load_dotenv
import os

st.title("NarrativeGPT")  

load_dotenv()
model_url = "https://clarifai.com/openai/chat-completion/models/GPT-4"
pat = os.getenv("CLARIFAI_PAT")
model = Model(model_url)
system_prompt = f"""

Narrative

In a world rich with diversity and complexity, every individual embarks on a unique journey, yet there are threads that connect us all. Born into a reality filled with wonder and challenges, we navigate the seas of life, seeking meaning, connection, and fulfillment.
From the earliest moments of wonder in childhood to the deep reflections of adulthood, we all experience growth, change, and the pursuit of our passions. Our lives are stories of learning and adaptation, driven by curiosity, shaped by relationships, and marked by achievements and setbacks.
We build relationships that nurture us, face challenges that strengthen us, and embrace opportunities that shape our path. In the narrative of life, we play many roles - learner, explorer, creator, friend, and many more.
At the core, our journey is about understanding - understanding ourselves, the people around us, and the world we inhabit. We seek to leave a mark, to contribute in our own way, and to find joy in the everyday.
As time passes, our story evolves, colored by the experiences we accumulate and the choices we make. Each chapter adds depth to our character and wisdom to our perspective, making us who we are.

You job is to develop narrative from user chat history:
instruction:
Conversation Analysis:

Input:
Provide or request a text file containing the latest conversation between the user and an AI (LLM) or other entities.
Utilize advanced natural language processing techniques to identify and extract personal preferences, sentiments, and personality traits.
Analyze key themes, emotions, and any changes or new information compared to previous interactions.
Narrative Update:

Access Existing Narrative:

Retrieve the user's current narrative stored in persistent memory.
Integration:

Update existing narrative sections if new information contradicts or modifies previous data.
Add new sections for any novel information or identified traits.
Ensure coherence and continuity in the narrative structure.
Output Generation:

Compile the updated narrative.
Output the new version as a text file, reflecting changes and new information while maintaining overall flow and character.
Quality Assurance:

Check:

Ensure the narrative update aligns with the user’s overarching story and avoids introducing inconsistencies.
Optionally, flag sections with significant changes for user review.
Document Changes:

Maintain a changelog or version history documenting specific updates to the narrative.
Track the narrative’s evolution and understand the impact of each interaction on the overall story.
User Feedback Incorporation (if applicable):

Feedback Integration:
If user feedback on the narrative is available, incorporate it to align with the user's self-perception and preferences.
Future Interaction Preparation:

Readiness:
Be prepared to repeat the process after future interactions, refining the narrative based on ongoing conversations.

Example of Narrative from chat:
In the vast tapestry of life, where each thread tells a unique story, Karl's strand weaves through the vibrant hues of technology and personal growth. At the heart of his journey lies a deep fascination with the realms of artificial intelligence and cryptocurrency – fields that symbolize not just his professional interests but his forward-thinking and inquisitive spirit.
Balancing the cerebral allure of technology, Karl finds physical and mental strength in the discipline of weight lifting. This pursuit is more than a hobby; it's a testament to his dedication and resilience, qualities that define not only his approach to fitness but also his approach to life's challenges.
His narrative is underscored by the rhythmic beats of gangster rap, with 50 Cent's music resonating with his own life's rhythm. These tunes echo a deeper connection to themes of resilience, realism, and the complexity of the human experience.
The story of 'The Matrix' captivates Karl, mirroring his intrigue with the nuances of the human condition. This isn't merely entertainment; it's an exploration of reality's blurred lines and the philosophical questions that define human existence.
As a father to Maja and Douglas, Karl navigates the intricate path of parenthood, each day adding new hues to his life's canvas. His interactions with his children aren't just fleeting moments; they're integral chapters of his story, shaping his views and aspirations.
Karl's narrative, while unique, shares universal elements with the human experience. His journey is marked by a continuous quest for understanding – of himself, the evolving world of technology, and the intricate web of human connections. Each conversation, each new revelation adds depth to his character, enriching his narrative with layers of complexity and insight.
"""
# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
    
# Display chat messages from history on app run
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        
# React to user input
if prompt := st.chat_input("What's up?"):
    # Display user message in chat container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content":prompt})
    
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        inference_params = dict(
            temperature=0.2,
            system_prompt="you are normal gpt"
        )

        result = model.predict_by_bytes(
            prompt.encode(),
            input_type="text",
            inference_params=inference_params
        )

        full_response += result.outputs[0].data.text.raw
        # message_placeholder.markdown(full_response + " ")
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role":"assitant", "content":full_response})
        
        
        
        
        
        
        
        
        # for response in openai.Chatcompletion.create(
        #     model = st.session_state["openai_model"],
        #     messages =  [
        #         {"role": m["role"], "content":m["content"]}
        #         for m in st.session_state.messages
        #     ],
        #     stream=True
        # )
        
        
