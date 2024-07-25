import streamlit as st
import json
from backend import holding_advance_degree
from docx import Document
import base64

st.header("Welcome to SAINCUBE EB-2 NIW")

def create_word_doc(text, file_name="generated_document.docx"):
    doc = Document()
    doc.add_paragraph(text)
    doc.save(file_name)
    return file_name

def download_link(file_path, file_label):
    with open(file_path, "rb") as file:
        b64 = base64.b64encode(file.read()).decode()
    href = f'<a href="data:file/docx;base64,{b64}" download="{file_path}">{file_label}</a>'
    return href

st.title("I. Petitioner is a member of the professions holding an advanced degree")

# Create a dictionary to store all input values
input_data = {}

# Function to create an input field with a label and caption
def create_input_with_caption(label, key, caption):
    st.markdown(f"**{label}**")
    input_data[key] = st.text_input("", key=key)
    st.caption(caption)

# Basic Information
st.header("Basic Information")
create_input_with_caption("Petitioner/Beneficiary Name", "name", "e.g., John Doe")
create_input_with_caption("Petitioner/Beneficiary Title", "title", "e.g., Research Scientist")
create_input_with_caption("Pronouns (He/She/They)", "pronouns", "e.g., He/She/They")

# Education
st.header("Education")
create_input_with_caption("Degree", "degree", "e.g., Ph.D.")
create_input_with_caption("Field", "field", "e.g., Computer Science")
create_input_with_caption("University", "university", "e.g., Stanford University")
create_input_with_caption("Year", "year", "e.g., 2020")
create_input_with_caption("Exhibit Number for Diploma and Transcripts", "exhibit_diploma", "e.g., Exhibit A")
create_input_with_caption("Exhibit Number for Advisory Evaluation", "exhibit_evaluation", "e.g., Exhibit B")

# Current Research
st.header("Current Research")
create_input_with_caption("Brief Description of Proposed Endeavor", "brief_description", "e.g., Developing novel machine learning algorithms")
create_input_with_caption("Detailed Description of Research", "detailed_description", "e.g., Our research focuses on...")
create_input_with_caption("Exhibit Number for Research", "exhibit_research", "e.g., Exhibit C")

# Employment
st.header("Employment")
create_input_with_caption("Position", "position", "e.g., Assistant Professor")
create_input_with_caption("Institution", "institution", "e.g., MIT")
create_input_with_caption("Exhibit Number for Employment Plans", "exhibit_employment", "e.g., Exhibit D")

# Future Research
st.header("Future Research")
create_input_with_caption("Detailed Description of Future Research", "future_research", "e.g., In the next phase of our research...")
create_input_with_caption("Exhibit Number for Future Research", "exhibit_future_research", "e.g., Exhibit E")

# Expert Quotes
st.header("Expert Quotes")
for i in range(1, 5):
    st.subheader(f"Expert {i}")
    create_input_with_caption("Name", f"expert_{i}_name", f"e.g., Dr. Jane Smith")
    create_input_with_caption("Position", f"expert_{i}_position", f"e.g., Professor of Physics")
    create_input_with_caption("Institution", f"expert_{i}_institution", f"e.g., Harvard University")
    create_input_with_caption("Exhibit Number", f"expert_{i}_exhibit", f"e.g., Exhibit F{i}")
    create_input_with_caption("Quote", f"expert_{i}_quote", f"e.g., The research conducted by...")

# Additional Information
st.header("Additional Information")
create_input_with_caption("Degree(s)", "degrees", "e.g., Ph.D., M.S.")
create_input_with_caption("Field(s)", "fields", "e.g., Computer Science, Data Science")
create_input_with_caption("University/Universities", "universities", "e.g., Stanford University, MIT")
create_input_with_caption("Current Position", "current_position", "e.g., Postdoctoral Researcher")
create_input_with_caption("Current Institution", "current_institution", "e.g., Google Research")
create_input_with_caption("Brief Description of Research Topics", "research_topics", "e.g., Machine learning, Natural language processing")
create_input_with_caption("Exhibit Numbers for Research Topics", "exhibit_topics", "e.g., Exhibit G, H")
create_input_with_caption("Future Institution", "future_institution", "e.g., Apple AI Research")

# Publications and Citations
st.header("Publications and Citations")
create_input_with_caption("Number of Peer-Reviewed Journal Articles", "num_articles", "e.g., 15")
create_input_with_caption("Number of First-Authored Articles", "num_first_author", "e.g., 8")
create_input_with_caption("Exhibit Numbers for Publications", "exhibit_publications", "e.g., Exhibit I")
create_input_with_caption("Citation Source", "citation_source", "e.g., Google Scholar")
create_input_with_caption("Number of Citations", "num_citations", "e.g., 500")
create_input_with_caption("Exhibit Number for Citations", "exhibit_citations", "e.g., Exhibit J")

# Research Impact
st.header("Research Impact")
for i in range(1, 4):
    create_input_with_caption(f"Example {i} of How Other Researchers Benefited from Your Research", f"impact_example_{i}", f"e.g., Dr. Smith's team utilized our algorithm to...")
create_input_with_caption("Exhibit Numbers for Examples", "exhibit_impact", "e.g., Exhibit K, L, M")

# Future Plans
st.header("Future Plans")
create_input_with_caption("Future Position", "future_position", "e.g., Senior AI Researcher")
create_input_with_caption("Relevant Skills/Technologies", "skills", "e.g., Deep learning, TensorFlow, PyTorch")
create_input_with_caption("Field of Advanced Degree", "advanced_degree_field", "e.g., Artificial Intelligence")
create_input_with_caption("Specific Objectives", "objectives", "e.g., Develop more efficient neural network architectures")
create_input_with_caption("Exhibit Numbers for Proposed Endeavor", "exhibit_endeavor", "e.g., Exhibit N, O")
create_input_with_caption("Industry/Sector", "industry", "e.g., Technology")
create_input_with_caption("Exhibit Numbers for Industry/Sector Value", "exhibit_industry", "e.g., Exhibit P")
create_input_with_caption("Relevant Issues", "issues", "e.g., Ethical AI, Data privacy")
create_input_with_caption("Relevant Sector", "relevant_sector", "e.g., Healthcare")
create_input_with_caption("Relevant Approaches", "approaches", "e.g., Federated learning, Differential privacy")
create_input_with_caption("Brief Description of Key Research Contributions", "key_contributions", "e.g., Developed a novel approach to...")
create_input_with_caption("Exhibit Numbers for Key Research Contributions", "exhibit_contributions", "e.g., Exhibit Q, R")
create_input_with_caption("Exhibit Numbers for Experience, Leadership, Expertise", "exhibit_experience", "e.g., Exhibit S, T, U")

# Generate text when button is clicked
if st.button("Generate Member Holding Advance Degree"):
    with st.spinner("Generating text..."):
        try:
            # Convert input_data to JSON
            json_data = json.dumps(input_data, indent=2)
            
            # Here you would typically send json_data to your backend
            # For now, we'll just use it as the user prompt
            response = holding_advance_degree(json_data)
            response_text = response['choices'][0]['message']['content']
            st.text_area("Generated Text:", value=response_text, height=200)

            # Create and provide a download link for the Word document
            file_name = create_word_doc(response_text)
            st.markdown(download_link(file_name, 'Download Generated Document'), unsafe_allow_html=True)

            # Provide a download link for the JSON data
            st.download_button(
                label="Download Input Data as JSON",
                data=json_data,
                file_name="input_data.json",
                mime="application/json"
            )
        except Exception as e:
            st.error(f"Error: {e}")