from fastapi import FastAPI
from petition_input import PetitionInput
from gpt_main import ChatGpt

app = FastAPI()
gpt_model = ChatGpt()
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/generate_petition")
def generate_petition_(request: PetitionInput):
    full_name = request.full_name
    highest_qualification = request.highest_qualification
    year_of_qualification = request.year_of_qualification
    main_field_industry = request.main_field_industry
    subfields_specializations = request.subfields_specializations
    top_skills = request.top_skills
    place_in_the_field = request.place_in_the_field
    achievements_summary = request.achievements_summary
    plans_for_engagement =  request.plans_for_engagement
    merit_and_national_importance = request.merit_and_national_importance
    contributions_to_field = request.contributions_to_field
    media_coverage = request.media_coverage
    occasions_as_judge = request.occasions_as_judge
    publications = request.publications
    request = {
        "full_name": full_name,
        "highest_qualification": highest_qualification,
        "year_of_qualification": year_of_qualification,
        "main_field_industry": main_field_industry,
        "subfields_specializations": subfields_specializations,
        "top_skills": top_skills,
        "place_in_the_field": place_in_the_field,
        "achievements_summary": achievements_summary,
        "plans_for_engagement": plans_for_engagement,
        "merit_and_national_importance": merit_and_national_importance,
        "contributions_to_field": contributions_to_field,
        "media_coverage": media_coverage,
        "occasions_as_judge": occasions_as_judge,
        "publications": publications,
    }
    response = gpt_model.generate_petition(request)
    return response
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
