import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Perplexity API endpoint
API_URL = "https://api.perplexity.ai/chat/completions"

# Get API key from environment variable
api_key = os.getenv("PERPLEXITY_API_KEY")

st.set_page_config(page_title="Perplexity AI Search", layout="wide")
st.title("Perplexity AI Search")

if not api_key:
    st.error("Please set the PERPLEXITY_API_KEY environment variable.")
    st.stop()

# Input for user query
user_query = st.text_input("Enter your question:")

# Create two columns for the main layout
col1, col2 = st.columns([2, 1])

with col1:
    with st.expander("Basic Settings", expanded=True):
        use_max_tokens = st.checkbox("Specify max tokens", value=False)
        if use_max_tokens:
            max_tokens = st.number_input("Max Tokens", min_value=1, value=100)
        else:
            st.info("Max tokens will be determined by the API")
        temperature = st.slider("Temperature", min_value=0.0, max_value=2.0, value=0.2, step=0.1)
        top_p = st.slider("Top P", min_value=0.0, max_value=1.0, value=0.9, step=0.1)

with col2:
    with st.expander("Advanced Settings", expanded=False):
        return_citations = st.checkbox("Return Citations", value=True)
        return_images = st.checkbox("Return Images", value=False)
        return_related_questions = st.checkbox("Return Related Questions", value=False)
        search_recency_filter = st.selectbox("Search Recency Filter", ["month", "week", "day", "hour"])
        top_k = st.number_input("Top K", min_value=0, max_value=2048, value=0)
        frequency_penalty = st.slider("Frequency Penalty", min_value=0.0, max_value=2.0, value=1.0, step=0.1)
        search_domain_filter = st.text_input("Search Domain Filter (comma-separated, max 3)", value="perplexity.ai")

if st.button("Search", disabled=not user_query):
    # Prepare the payload
    payload = {
        "model": "llama-3.1-sonar-small-128k-online",
        "messages": [
            {
                "role": "system",
                "content": "Be precise and concise."
            },
            {
                "role": "user",
                "content": user_query
            }
        ],
        "temperature": temperature,
        "top_p": top_p,
        "return_citations": return_citations,
        "search_domain_filter": [domain.strip() for domain in search_domain_filter.split(',')][:3],
        "return_images": return_images,
        "return_related_questions": return_related_questions,
        "search_recency_filter": search_recency_filter,
        "top_k": top_k,
        "frequency_penalty": frequency_penalty
    }

    # Only include max_tokens if the user has specified it
    if use_max_tokens:
        payload["max_tokens"] = max_tokens

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    with st.spinner('Searching...'):
        try:
            response = requests.post(API_URL, json=payload, headers=headers)
            response.raise_for_status()
            result = response.json()
            
            # Display the response
            st.subheader("Response:")
            st.markdown(result['choices'][0]['message']['content'])
            
            # Display citations if available
            if 'citations' in result and result['citations']:
                st.subheader("Citations:")
                for citation in result['citations']:
                    st.markdown(f"- [{citation['title']}]({citation['url']})")
            
            # Display related questions if available
            if 'related_questions' in result and result['related_questions']:
                st.subheader("Related Questions:")
                for question in result['related_questions']:
                    st.markdown(f"- {question}")

        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 429:
                st.error("Rate limit exceeded. Please wait a moment before trying again.")
            else:
                st.error(f"An HTTP error occurred: {e}")
        except requests.exceptions.RequestException as e:
            st.error(f"An error occurred: {e}")

st.markdown("---")
st.markdown("Made by [Kausshik](https://x.com/kausshik_m) using Claude, Curson, and Perplexity AI")