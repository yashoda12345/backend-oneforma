from fastapi import APIRouter
from app.api.api_v1.endpoints import user, authentication, job, personal_information, expertise_mapper, intrest_mapper, \
    skill_mapper, gender, nationality, ethnicity, state, country, country_code, expertise, skill, intrest, \
    industry_mapper, industry, degree, education_mapper, experience, language_mapper, language, proficiency

api_router = APIRouter()

api_router.include_router(authentication.router, tags=["Authentication"])
api_router.include_router(country.router, prefix="/country", tags=["Country"])
api_router.include_router(country_code.router, prefix="/country-code", tags=["Country Code"])
api_router.include_router(degree.router, prefix="/degree", tags=["Degree"])
api_router.include_router(education_mapper.router, prefix="/user-education", tags=["Education"])
api_router.include_router(ethnicity.router, prefix="/ethnicity", tags=["Ethnicity"])
api_router.include_router(expertise_mapper.router, prefix="/user-expertise", tags=["Expertise"])
api_router.include_router(expertise.router, prefix="/expertise", tags=["Expertise Options"])
api_router.include_router(experience.router, prefix="/experience", tags=["Experience"])
api_router.include_router(gender.router, prefix="/gender", tags=["Gender"])
api_router.include_router(industry_mapper.router, prefix="/user-industry", tags=["Industry"])
api_router.include_router(industry.router, prefix="/industry", tags=["Industry Options"])
api_router.include_router(intrest_mapper.router, prefix="/user-intrest", tags=["Intrest"])
api_router.include_router(intrest.router, prefix="/intrest", tags=["Intrest Options"])
api_router.include_router(job.router, prefix="/job", tags=["Job"])
api_router.include_router(language_mapper.router, prefix="/user-language", tags=["Language"])
api_router.include_router(language.router, prefix="/language", tags=["Language Options"])
api_router.include_router(nationality.router, prefix="/nationality", tags=["Nationality"])
api_router.include_router(proficiency.router, prefix="/proficiency", tags=["Proficiency"])
api_router.include_router(personal_information.router, prefix="/personal-information", tags=["Personal Information"])
api_router.include_router(skill_mapper.router, prefix="/user-skill", tags=["Skill"])
api_router.include_router(skill.router, prefix="/skill", tags=["Skill Options"])
api_router.include_router(state.router, prefix="/state", tags=["State"])
api_router.include_router(user.router, prefix="/user", tags=["User"])
