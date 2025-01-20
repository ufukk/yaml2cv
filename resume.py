from dataclasses import dataclass, field
from typing import List, Dict
import yaml
from jinja2 import Environment, FileSystemLoader
import sys
from pathlib import Path


@dataclass
class PersonalInformation:
    name: str
    surname: str
    date_of_birth: str
    country: str
    city: str
    address: str
    zip_code: str
    phone_prefix: str
    phone: str
    email: str
    github: str
    linkedin: str
    job_title: str
    professional_summary: str
    code_samples: str

@dataclass
class EducationDetail:
    education_level: str
    institution: str
    field_of_study: str
    final_evaluation_grade: str
    start_date: str
    year_of_completion: str
    exam: Dict[str, str]

@dataclass
class ExperienceDetail:
    position: str
    company: str
    employment_period: str
    location: str
    industry: str
    key_responsibilities: List[Dict[str, str]]
    skills_acquired: List[str]

@dataclass
class Project:
    name: str
    description: str
    link: str
    skills: List[str]

@dataclass
class Achievement:
    name: str
    description: str

@dataclass
class Certification:
    name: str
    description: str

@dataclass
class Language:
    language: str
    proficiency: str

@dataclass
class Availability:
    notice_period: str

@dataclass
class SalaryExpectation:
    salary_range_usd: str

@dataclass
class SelfIdentification:
    gender: str
    pronouns: str
    veteran: str
    disability: str
    ethnicity: str

@dataclass
class LegalAuthorization:
    eu_work_authorization: str
    us_work_authorization: str
    requires_us_visa: str
    requires_us_sponsorship: str
    requires_eu_visa: str
    legally_allowed_to_work_in_eu: str
    legally_allowed_to_work_in_us: str
    requires_eu_sponsorship: str
    canada_work_authorization: str
    requires_canada_visa: str
    legally_allowed_to_work_in_canada: str
    requires_canada_sponsorship: str
    uk_work_authorization: str
    requires_uk_visa: str
    legally_allowed_to_work_in_uk: str
    requires_uk_sponsorship: str

@dataclass
class WorkPreferences:
    remote_work: str
    in_person_work: str
    open_to_relocation: str
    willing_to_complete_assessments: str
    willing_to_undergo_drug_tests: str
    willing_to_undergo_background_checks: str

@dataclass
class Resume:
    personal_information: PersonalInformation
    education_details: List[EducationDetail]
    experience_details: List[ExperienceDetail]
    projects: List[Project]
    achievements: List[Achievement]
    certifications: List[Certification]
    languages: List[Language]
    interests: List[str]
    availability: Availability
    salary_expectations: SalaryExpectation
    self_identification: SelfIdentification
    legal_authorization: LegalAuthorization
    work_preferences: WorkPreferences

def read_yaml(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    return data

def create_resume(data):
    personal_information = PersonalInformation(
        name=data['personal_information'].get('name', ''),
        surname=data['personal_information'].get('surname', ''),
        date_of_birth=data['personal_information'].get('date_of_birth', ''),
        country=data['personal_information'].get('country', ''),
        city=data['personal_information'].get('city', ''),
        address=data['personal_information'].get('address', ''),
        zip_code=data['personal_information'].get('zip_code', ''),
        phone_prefix=data['personal_information'].get('phone_prefix', ''),
        phone=data['personal_information'].get('phone', ''),
        email=data['personal_information'].get('email', ''),
        github=data['personal_information'].get('github', ''),
        linkedin=data['personal_information'].get('linkedin', ''),
        job_title=data['personal_information'].get('job_title', ''),
        professional_summary=data['personal_information'].get('professional_summary', ''),
        code_samples=data['personal_information'].get('code_samples', '')
    )
    
    education_details = [
        EducationDetail(
            education_level=edu.get('education_level', ''),
            institution=edu.get('institution', ''),
            field_of_study=edu.get('field_of_study', ''),
            final_evaluation_grade=edu.get('final_evaluation_grade', ''),
            start_date=edu.get('start_date', ''),
            year_of_completion=edu.get('year_of_completion', ''),
            exam=edu.get('exam', {})
        ) for edu in data.get('education_details', [])
    ]
    
    experience_details = [
        ExperienceDetail(
            position=exp.get('position', ''),
            company=exp.get('company', ''),
            employment_period=exp.get('employment_period', ''),
            location=exp.get('location', ''),
            industry=exp.get('industry', ''),
            key_responsibilities=exp.get('key_responsibilities', []),
            skills_acquired=exp.get('skills_acquired', [])
        ) for exp in data.get('experience_details', [])
    ]
    
    projects = [
        Project(
            name=proj.get('name', ''),
            description=proj.get('description', ''),
            link=proj.get('link', ''),
            skills=proj.get('skills', ''),
        ) for proj in data.get('projects', [])
    ]
    
    achievements = [
        Achievement(
            name=ach.get('name', ''),
            description=ach.get('description', '')
        ) for ach in data.get('achievements', [])
    ]
    
    certifications = [
        Certification(
            name=cert.get('name', ''),
            description=cert.get('description', '')
        ) for cert in data.get('certifications', [])
    ]
    
    languages = [
        Language(
            language=lang.get('language', ''),
            proficiency=lang.get('proficiency', '')
        ) for lang in data.get('languages', [])
    ]
    
    interests = data.get('interests', [])
    
    availability = Availability(
        notice_period=data.get('availability', {}).get('notice_period', '')
    )
    
    salary_expectations = SalaryExpectation(
        salary_range_usd=data.get('salary_expectations', {}).get('salary_range_usd', '')
    )
    
    self_identification = SelfIdentification(
        gender=data.get('self_identification', {}).get('gender', ''),
        pronouns=data.get('self_identification', {}).get('pronouns', ''),
        veteran=data.get('self_identification', {}).get('veteran', ''),
        disability=data.get('self_identification', {}).get('disability', ''),
        ethnicity=data.get('self_identification', {}).get('ethnicity', '')
    )
    
    legal_authorization = LegalAuthorization(
        eu_work_authorization=data.get('legal_authorization', {}).get('eu_work_authorization', ''),
        us_work_authorization=data.get('legal_authorization', {}).get('us_work_authorization', ''),
        requires_us_visa=data.get('legal_authorization', {}).get('requires_us_visa', ''),
        requires_us_sponsorship=data.get('legal_authorization', {}).get('requires_us_sponsorship', ''),
        requires_eu_visa=data.get('legal_authorization', {}).get('requires_eu_visa', ''),
        legally_allowed_to_work_in_eu=data.get('legal_authorization', {}).get('legally_allowed_to_work_in_eu', ''),
        legally_allowed_to_work_in_us=data.get('legal_authorization', {}).get('legally_allowed_to_work_in_us', ''),
        requires_eu_sponsorship=data.get('legal_authorization', {}).get('requires_eu_sponsorship', ''),
        canada_work_authorization=data.get('legal_authorization', {}).get('canada_work_authorization', ''),
        requires_canada_visa=data.get('legal_authorization', {}).get('requires_canada_visa', ''),
        legally_allowed_to_work_in_canada=data.get('legal_authorization', {}).get('legally_allowed_to_work_in_canada', ''),
        requires_canada_sponsorship=data.get('legal_authorization', {}).get('requires_canada_sponsorship', ''),
        uk_work_authorization=data.get('legal_authorization', {}).get('uk_work_authorization', ''),
        requires_uk_visa=data.get('legal_authorization', {}).get('requires_uk_visa', ''),
        legally_allowed_to_work_in_uk=data.get('legal_authorization', {}).get('legally_allowed_to_work_in_uk', ''),
        requires_uk_sponsorship=data.get('legal_authorization', {}).get('requires_uk_sponsorship', '')
    )
    
    work_preferences = WorkPreferences(
        remote_work=data.get('work_preferences', {}).get('remote_work', ''),
        in_person_work=data.get('work_preferences', {}).get('in_person_work', ''),
        open_to_relocation=data.get('work_preferences', {}).get('open_to_relocation', ''),
        willing_to_complete_assessments=data.get('work_preferences', {}).get('willing_to_complete_assessments', ''),
        willing_to_undergo_drug_tests=data.get('work_preferences', {}).get('willing_to_undergo_drug_tests', ''),
        willing_to_undergo_background_checks=data.get('work_preferences', {}).get('willing_to_undergo_background_checks', '')
    )
    
    resume = Resume(
        personal_information=personal_information,
        education_details=education_details,
        experience_details=experience_details,
        projects=projects,
        achievements=achievements,
        certifications=certifications,
        languages=languages,
        interests=interests,
        availability=availability,
        salary_expectations=salary_expectations,
        self_identification=self_identification,
        legal_authorization=legal_authorization,
        work_preferences=work_preferences
    )
    return resume

def merge_dicts(*dicts):
    def merge(d1, d2):
        for key, value in d2.items():
            if not value or value == '':
                continue
            if isinstance(value, dict) and key in d1:
                d1[key] = merge(d1.get(key, {}), value)
            elif value:
                d1[key] = value
        return d1

    result = {}
    for d in dicts:
        result = merge(result, d)
    return result

def generate_html(resume, template_path, output_path):
    env = Environment(loader=FileSystemLoader(template_path))
    template = env.get_template('cv_template.html')
    html_content = template.render(resume=resume)
    
    with open(output_path, 'w') as file:
        file.write(html_content)

def generate_pdf(html_path, pdf_path):
    from weasyprint import HTML
    HTML(html_path).write_pdf(pdf_path)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print('Please provide a yaml path and a key')
        exit(1)
    file_path = sys.argv[1]
    resume_key = sys.argv[2]    
    resume = read_yaml(file_path)[resume_key]
    template_path = './templates'
    target_path = Path(file_path)
    output_path = target_path.parent / f'./cv_{target_path.stem}_{resume_key}.html'
    generate_html(resume, template_path, output_path)
    generate_pdf(output_path, target_path.parent / f'./cv_{target_path.stem}_{resume_key}.pdf')
    print(f'Generated resume for {resume_key} in {target_path.parent / f"cv_{target_path.stem}_{resume_key}.pdf"}')
