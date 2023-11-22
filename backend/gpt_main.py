import openai
from gpt_config import config_gpt


class ChatGpt(config_gpt):
    
    def __init__(self) -> None:
        super().__init__()
    
    def generate_petition(self, _input):

        prompt = f"""
        Create a detailed and comprehensive petition cover letter for an EB-2 National Interest Waiver (NIW) petition on behalf of a Ph.D. holder and researcher, based on the provided information using the instructions given below use up 5000 words:

[Start of Infromation]
petitioners_name = {_input['full_name']}
highest_qualification = {_input['highest_qualification']}
year_of_qualification = {_input['year_of_qualification']}
main_field_industry = {_input['main_field_industry']}
subfields_specializations = {_input['subfields_specializations']}
top_skills = {_input['top_skills']}
place_in_the_field = {_input['place_in_the_field']}
achievements_summary = {_input['achievements_summary']}
plans_for_engagement = {_input['plans_for_engagement']}
merit_and_national_importance = {_input['merit_and_national_importance']}
contributions_to_field = {_input['contributions_to_field']}
media_coverage = {_input['media_coverage']}
occasions_as_judge = {_input['occasions_as_judge']}
publications = {_input['publications']}
[End of Information]


An individual having Ph.D. research in Science Technology Engineering and Mathematics (STEM) fields or in Emerging Technologies have higher chances of EB2- NIW due to US national importance

[Start of Format]
Your task is to construct a professional, detailed, and legally justified EB2 NIW Petition cover letter with professional and legal tone.
The Petition letter must always include the sections: Introduction to Standard of Proof, Highlighting Advanced Degree, Detailing Proposed Endeavor, Emphasizing Merit and National Importance, Addressing the Multifaceted Assessment, Highlighting Education and Record of Success, Leveraging Testimonials and External Recognition,Connecting Research to National Importance, Addressing Potential Concerns, Creating a Cohesive Narrative, Conclusion .

[End of Format]

[Start of Instruction]
Instructions for these sections are given below:
-Introduction to Standard of Proof,
Generate an introduction of up to 300 words that elaborates on the 'preponderance of the evidence' standard and how it applies to EB2 NIW petitions, drawing insights from Matter of Dhanasar, Matter of E-M-, and U.S. v. Cardoza-Fonseca.

For example:
Note that the standard of proof for petitions filed for National Interest Waiver cases is the “preponderance of the evidence” standard. See Matter of Dhanasar, 26 I&N Dec. 884, 889 (AAO 2016). Thus, if the petitioner submits relevant, probative, and credible evidence that leads USCIS to believe that the claim is “more likely than not” or “probably true,” the petitioner has satisfied the standard of proof. Matter of E-M-, 20 I&N Dec. 77, 79-80 (Comm’r 1989); see also U.S. v. Cardoza-Fonseca, 480 U.S. 421 (1987) (discussing “more likely than not” as a greater than 50% chance of an occurrence taking place). 

-Individual is a member of the professions holding an advanced degree
Compose a narrative of up to 500 words underscoring the significance of the individual's Ph.D. in Degree Field from Degree University and Degree Completion year. 
Emphasize the advanced education's impact on their qualifications,
Position them as a highly skilled and accomplished professional, persuasive, and succinct, 
Aiming to portray the individual as an exceptionally qualified professional in their field
For example:
[Individual's Name]'s proposed endeavor is to advance the field of [Individual's Expertise] by conducting cutting-edge research in [Specify Research Focus]. As a seasoned professional in [Individual's Field], [Individual's Last Name]'s goal is to contribute to the development of [Specify Field Advancements] and innovative solutions. The proposed endeavor entails [Brief Description of Endeavor], focusing on [Specific Goals or Objectives].
This petition seeks to waive the job offer requirement, emphasizing that [Individual's Last Name]'s proposed endeavor is distinct from their prospective employment. Nevertheless, we are including [Individual's Last Name]'s employment plans to demonstrate their commitment and capability to further their proposed endeavor. Drawing from [Individual's Educational and Research Background], [Individual's Last Name] intends to pursue employment as [Specify Position] at [Prospective Employer] or a similar institution (Exhibit [Reference]). This employment aligns with [Individual's Last Name]'s overarching goal of [Brief Description of Career Aspirations].
[Individual's Last Name] envisions leveraging their expertise in [Key Skills or Areas of Expertise], including [Specify Skills], to spearhead research and development initiatives. The primary focus remains on [Specify Main Goals], wherein [Individual's Last Name] aims to [Detailed Description of Goals]. This paragraph underscores the significance of the proposed endeavor itself, with an emphasis on [Individual's Last Name]'s potential contributions to the field.


-Individual’s proposed endeavor is to [research area] to create [research impact] 
Compose a detailed description of up to 800 words enhancing the portrayal of the proposed endeavor of developing state-of-the-art field_of_expertise in the field of research area. All aspects should be emphasized to make it stand out.

1. Describe the innovative aspects of the proposed endeavor that set it apart from existing initiatives.
2. Highlight any unique methodologies, technologies, or approaches that will be employed.
3. Clearly state how the development of the Field of Expertise aligns with United States national importance and global priorities.

For example:
[Individual's Name]'s proposed endeavor in the field of [Specify Expertise or Field] holds significant merit and national importance. [Individual's Last Name]'s research focuses on [Specify Research Focus], aiming to contribute to [Specify Field Advancements] and address critical challenges in [Specify Relevant Area].

-Individual’s proposed endeavor has both substantial merit and national importance, 
Given the extensive research applications and provided for Individual's Name and accomplishments, your task is to bolster the argument for the substantial merit and national importance of his proposed endeavor. Craft a detailed narrative, up to 800 words, highlighting specific examples and key points that underscore the significance of  Individual's Name work in the context of national interest. Maintain a persuasive and professional tone, stressing the urgency and importance of individual's work for the nation.

1. Articulate how an individual’s research directly addresses critical national challenges or priorities.
2. Connect the proposed endeavor to broader U.S. national goals and underscore its potential to contribute to solutions for pressing issues
3. Generate and Integrate quantifiable metrics or potential impact indicators related to the proposed endeavor.
4. Generate, project and emphasize the scale of the positive effects the individual’s research that could have at the national level given the provided data of the individual
5. Demonstrate how an individual's work aligns with and supports current national policies of U.S.
6. Illustrate the relevance of the proposed endeavor in the context of US governmental priorities and initiatives.
7. Discuss how the outcomes of the proposed endeavor extend beyond the academic realm to positively impact society.
8. Highlight potential benefits for communities, industries, or public health.

For Example:
The substantial merit of [Individual's Last Name]'s proposed endeavor is evident in [his/her] dedication to improving [Specify Global Issue or Challenge]. For instance, [Provide Statistics or Context] highlights the urgency and scale of the issue [Individual's Last Name] aims to address. [Describe Current Limitations or Challenges in the Field] emphasize the need for innovative solutions.
[Individual's Last Name]'s development of [Specify Project or System] is a testament to [his/her] commitment to overcoming these challenges. The application of [Specify Innovative Methods or Technologies] demonstrates not only an understanding of the issues at hand but also a unique approach to solving them. This research is poised to benefit [Specify Target Population or Industry], making a positive impact on a national and potentially global scale.
The national importance of [Individual's Last Name]'s proposed endeavor is underscored by its alignment with [Specify Relevant National Initiatives or Strategies]. As recognized by [Reference to Relevant Report or Analysis], [Specify Importance of Field or Technology] is crucial in [National Context or Strategy]. [Highlight Constraints or Challenges in the National Context] further accentuates the significance of [Individual's Last Name]'s research in overcoming these obstacles.
In summary, [Individual's Last Name]'s proposed research on [Specify Project or System] is both meritorious and nationally significant. It addresses pressing challenges in [Specify Field], aligns with [National Initiatives or Strategies], and showcases [Individual's Last Name]'s commitment to advancing knowledge and making a meaningful impact in [Specify Area]. (Exhibits [Reference to Supporting Documents or Publications]).
-Individual is well positioned to advance the proposed endeavor,
In accordance with the Dhanasar framework, provide a detailed assessment of how individual is exceptionally well positioned to advance his proposed endeavor. Address each facet of the multifaceted assessment, focusing on the key aspects that underscore his capability and potential for success. Generate a comprehensive response, up to 400  words.

i. Education, Skills, and Knowledge :

Illuminate individual's educational background, emphasizing how his qualifications uniquely position him for success up to 80 words.
Showcase specific instances of his record of success, detailing achievements, publications, or impactful projects relevant to the proposed endeavor up to 100 words.

ii. Record of Success in Related or Similar Efforts and Interest of Relevant Individuals :

compose testimonials and external recognitions received by individual, showcasing the credibility and support he has garnered up to 80 words.
Discuss how these testimonials affirm his capabilities and bolster the merit of the proposed endeavor up to 70 words.
1. Individual’s research is highly novel and influential in his field:
Articulate the connection between individual's research and its broader implications for national importance up to 100 words.
Highlight how his work aligns with key national priorities, emphasizing its potential impact on societal, economic, or strategic levels up to 100 words.

2. Progress Toward Achieving the Proposed Endeavor & Plan for Future Activity in the Field:
Proactively address potential concerns related to the proposed endeavor, providing strategies or evidence that mitigates uncertainties up to 120 words.
Emphasize individual's preparedness, resilience, and adaptability in navigating challenges up to 150 words.



-On balance, it would be beneficial to the United States to waive the requirements of a job offer and thus of a labor certification, 

Compose “Creating a Cohesive Narrative" that seamlessly ties together the key elements of individual's education, proposed endeavor, merit, national importance, and his ability to advance the endeavor. Draft a narrative of up to 500 words that ensures a smooth and interconnected flow, emphasizing the elements that should be woven seamlessly throughout the letter, Maintain a coherent and professional tone, ensuring a seamless transition between each element. Use transitions and linking sentences to create a fluid narrative.

Begin by succinctly highlighting [Petitioner's Name]'s educational achievements, showcasing how his academic journey has equipped him with the necessary knowledge and skills for the proposed endeavor.

Introduce the proposed endeavor, providing a clear and compelling overview of its objectives, significance, and potential impact. Connect it to individual's education and expertise.

Weave in elements of individual's merit and track record of success, drawing attention to specific achievements, publications, or contributions that underline his capability and qualifications.

Articulate how the proposed endeavor aligns with national priorities and underscore its potential significance on a broader scale. Emphasize the national importance of individual's work.

Discuss individual's unique abilities and skills that position him to successfully advance the proposed endeavor. Provide concrete examples or instances where his expertise has been pivotal.

-Conclusion 
Compose the "conclusion" for the EB2 NIW Petition cover letter that justifies that the individual is a member of the professions holding an advanced degree;
the individual's proposed endeavor has both substantial merit and national importance;
the individual is well-positioned to advance the proposed endeavor; and
On balance, it would be beneficial to the United States to waive the requirements of a job offer and thus of a labor certification.


Compose a conclusion that encapsulates the four crucial elements of the Dhanasar framework, Maintain a persuasive and professional tone throughout the conclusion, ensuring coherence and clarity length of 200 words:

Member of the Professions with an Advanced Degree:

Discuss how the individual is a member of the professions holding an advanced degree. Highlight the significance of their educational background in positioning them as an expert in their field.
Proposed Endeavor with Substantial Merit and National Importance:

Emphasize the substantial merit and national importance of the individual's proposed endeavor. Provide insights into how the project addresses critical issues and aligns with national priorities.
Well Positioned to Advance the Proposed Endeavor:

Detail how the individual is well-positioned to advance the proposed endeavor. Showcase their unique qualifications, skills, and track record that make them a credible and capable leader in their field.

Beneficial to the United States to Waive Job Offer Requirements:

Conclude by summarizing why, on balance, it would be beneficial to the United States to waive the requirements of a job offer and a labor certification. Connect this decision to the overall merit, importance, and the individual's capacity to contribute significantly.
[End of Instruction]
        """
        messages = [{"role": "system", "content":self.system},
                    {"role": "user", "content":prompt}]
        openai.api_key = "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"
        
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo-16k", messages=messages,
                                                    temperature=0.1)
        
        reply = response.choices[0].message.content
        
        return reply