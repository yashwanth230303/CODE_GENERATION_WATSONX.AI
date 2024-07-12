import streamlit as st
import getpass
from ibm_watsonx_ai.foundation_models import Model

def get_credentials():
    # Simulating the input of API key 'abc123456'
    apikey = 'O0g17oATnv3hpejzM9svvjaNQc7LX7xV2qH5418saEXD'
    return {
        "url": "https://us-south.ml.cloud.ibm.com",
        "apikey": apikey
    }


# Parameters and model initialization
model_id = "codellama/codellama-34b-instruct-hf"
parameters = {
    "decoding_method": "greedy",
    "max_new_tokens": 1000,
    "min_new_tokens": 1,
    "stop_sequences": ["<end of code>"],
    "repetition_penalty": 1
}

# Streamlit app begins
st.title('Code Generation with IBM WATSONX AI')

# Input prompt text area
prompt_input = st.text_area('Enter your prompt (instructions):', height=250)

# Button to generate code
if st.button('Generate Code'):
    st.text("Generating code...")

    # Initialize the model with credentials
    credentials = get_credentials()
    model = Model(
        model_id=model_id,
        params=parameters,
        credentials=credentials,
        project_id="78275590-aa27-4c1e-a426-f39640aa0003",
    )

    # Generate response based on the prompt
    generated_response = model.generate_text(prompt=prompt_input, guardrails=False)

    # Display the generated response
    st.subheader('Generated Code:')
    st.code(generated_response)

# Instructions or info section
st.markdown('''
### Instructions:
- Enter the instructions for code generation in the text area.
- Click on **Generate Code** to generate Python code based on the instructions.
''')