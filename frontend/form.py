import streamlit as st
import requests

def main():
    st.title("Petitioner Information Form")

    # Form inputs
    full_name = st.text_input("Full Name of the Petitioner:")
    highest_qualification = st.text_input("Highest Qualification:")
    year_of_qualification = st.text_input("Year of Qualification:")
    main_field = st.text_input("Main Field/Industry:")
    subfields = st.text_input("Subfields/Specializations:")
    top_skills = st.text_input("Top Skills:")
    place_in_field = st.text_input("Place in the Field (Areas of Expertise):")
    achievements = st.text_area("Summary of Top Achievements in the Field/Industry:")
    engagement_plans = st.text_area("Plans for Continued Engagement in the Field:")
    merit_and_importance = st.text_area("Substantial Merit and National Importance of the Proposed Endeavor:")
    contributions = st.text_area("Contributions to the Field or Industry:")
    media_coverage = st.text_area("Major Media Coverage Related to the Research Project:")
    judge_occasions = st.text_area("Occasions where the Petitioner has Served as a Judge in the Field/Industry:")
    publications = st.text_area("List of Full-length Journal Articles, Books, Chapters, or Articles in Conference Proceedings:")

    # Submit button
    if st.button("Submit"):
        # Create a dictionary with the form data
        form_data = {
            "full_name": full_name,
            "highest_qualification": highest_qualification,
            "year_of_qualification": year_of_qualification,
            "main_field_industry": main_field,
            "subfields_specializations": subfields,
            "top_skills": top_skills,
            "place_in_the_field": place_in_field,
            "achievements_summary": achievements,
            "plans_for_engagement": engagement_plans,
            "merit_and_national_importance": merit_and_importance,
            "contributions_to_field": contributions,
            "media_coverage": media_coverage,
            "occasions_as_judge": judge_occasions,
            "publications": publications,
        }

        # st.write(form_data)
        with st.spinner("Generating..."):
            # Send a POST request to the FastAPI server
            response = requests.post("http://127.0.0.1:8000/generate_petition", json=form_data)

        if response.status_code == 200:
            st.success("Form submitted successfully!")
            st.markdown(f"### Response from the FastAPI server:\n\n{response.json()}")
        else:
            st.error(f"Failed to submit the form. Server returned {response.status_code} status code.")

if __name__ == "__main__":
    main()