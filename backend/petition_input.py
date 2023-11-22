from pydantic import BaseModel

class PetitionInput(BaseModel):
    full_name: str
    highest_qualification: str
    year_of_qualification: int
    main_field_industry: str
    subfields_specializations: str
    top_skills: str
    place_in_the_field: str
    achievements_summary: str
    plans_for_engagement: str
    merit_and_national_importance: str
    contributions_to_field: str
    media_coverage: str
    occasions_as_judge: str
    publications: str
