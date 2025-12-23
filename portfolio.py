from fasthtml.common import *
from monsterui.all import *

hyperscript_header = Script(src="https://unpkg.com/hyperscript.org@0.9.14")
hdrs = Theme.blue.headers()
app, rt = fast_app(hdrs=(Theme.blue.headers(highlightjs=True), hyperscript_header))


### Navigation and Scrollspy ###
sections = [
    "welcome",
    "about",
    "skills",
    "experience",
    "projects",
    "certifications",
    "education",
    "contact",
]
skills = [
    "Python",
    "FastHTML",
    "Pandas",
    "SQL",
    "DuckDB",
    "Git",
    "GitHub",
    "REST APIs",
    "HTML",
    "CSS",
    "JavaScript",
    "Pytest",
    "Playwright",
    "Elixir",
    "Power BI",
    "Excel",
    "Power Query",
]

scrollspy_links = (*[A(s.capitalize(), href=f"#{s}-section") for s in sections],)


@rt("/")
def get():
    def _Section(*c, **kwargs):
        return Section(DividerLine(), *c, cls="space-y-3 my-20", **kwargs)

    return Title("Adhil's Portfolio"), Container(
        NavBar(
            *scrollspy_links,
            brand=DivLAligned(
                H3("Adhil's Portfolio"), UkIcon("code-xml", height=30, width=30)
            ),
            sticky=True,
            uk_scrollspy_nav=True,
            scrollspy_cls=ScrollspyT.bold,
        ),
        NavContainer(
            *map(Li, scrollspy_links),
            # ThemePicker(),
            uk_scrollspy_nav=True,
            sticky=True,
            cls=(NavT.primary, "pt-20 px-5 pr-10"),
        ),
        Container(
            Div(
                Div(
                    Img(
                        src="./static/Adhil.jpg",
                        alt="Adhil's Profile Picture",
                        cls="w-44 h-42 mr-4 rounded-full object-cover",
                    ),
                    Div(
                        H1("Hey there, I'm Adhil", cls="text-4xl font-bold"),
                        H6(
                            "Software Engineer @ ",
                            A(
                                "BISquared",
                                href="https://www.getprog.ai/profile/11910293",
                                target="_blank",
                                cls=ButtonT.text,
                            ),
                            cls="mt-2",
                        ),
                        cls="ml-6",
                    ),
                    cls="flex items-center",
                ),
                cls="flex justify-center",
            ),
            _Section(
                Subtitle("Get to know more"),
                H2("About"),
                P(
                    "A passionate Python developer with hands-on experience in data analytics and backend development. I work on ETL pipelines, data validation, and dashboard creation, and build reliable backend features using Python and FastHTML to support real-world applications."
                ),
                id="about-section",
            ),
            _Section(
                H2("Skills"),
                Div(
                    *[P(skill, cls="bg-blue-100 text-blue-800") for skill in skills],
                    cls="flex flex-wrap gap-2",
                ),
                id="skills-section",
            ),
            _Section(
                H2("Experience"),
                Div(
                    H3("BI Squared Consulting Ltd — Chennai"),
                    I(
                        "Software Engineer – Data & Python Development | April 2024 – Present"
                    ),
                    H5("Project: IOM USRAP Dashboard"),
                    Ul(
                        Li(
                            "Developed Power BI dashboards at summary and departmental levels to improve visibility into budget and operational trends."
                        ),
                        Li(
                            "Built Power Query pipelines for data cleaning, merging, and transformation."
                        ),
                        Li(
                            "Performed data validation and quality checks to ensure accurate and reliable reporting."
                        ),
                        Li(
                            "Created clear summary visuals highlighting key trends and progress."
                        ),
                        Li(
                            "Strengthened hands-on experience in Power BI, Power Query, and data modeling."
                        ),
                        cls=ListT.bullet,
                    ),
                    H5("Project: Learning Management System (Internal)"),
                    Ul(
                        Li(
                            "Contributed to a quiz-based LMS enabling teachers to manage questions, quizzes, and student performance."
                        ),
                        Li(
                            "Built student-facing pages for taking quizzes, saving answers, and viewing results."
                        ),
                        Li(
                            "Implemented automated scoring and result summaries to reduce manual review time."
                        ),
                        Li(
                            "Handled Excel imports using Pandas/OpenPyXL, data storage in SQLite, and exports using xlwings."
                        ),
                        Li(
                            "Gained practical experience in Python, FastHTML, and data processing workflows."
                        ),
                        cls=ListT.bullet,
                    ),
                    H5("Project: Quran Memorization SRS"),
                    Ul(
                        Li(
                            "Developed a memorization and revision tracking system used daily by students."
                        ),
                        Li(
                            "Implemented structured workflows across five learning modes including adaptive SRS."
                        ),
                        Li(
                            "Built a multi-role user system for parents and teachers to manage multiple students."
                        ),
                        Li(
                            "Created summary and progress views to track targets and achievements."
                        ),
                        Li(
                            "Enhanced experience with Python, FastHTML, MVC architecture, SQLite, and GitHub."
                        ),
                        cls=ListT.bullet,
                    ),
                ),
                id="experience-section",
            ),
            _Section(
                H2("Certifications"),
                Ul(
                    Li(
                        "Microsoft Power BI Desktop for Business Intelligence – Udemy",
                    ),
                    Li("AI For India 2.0 – GUVI"),
                    Li("Introduction to Python – GUVI"),
                    Li("Build a Face Recognition Application using Python – GUVI"),
                    Li("100 Days of Code: The Complete Python Pro Bootcamp – Udemy"),
                    Li("SQL (Basics & Intermediate) – HackerRank"),
                    cls=ListT.bullet,
                ),
                id="certifications-section",
            ),
            _Section(
                H2("Education"),
                H3("Jamal Mohamed College of Arts and Science"),
                P("Bachelor of Computer Science | 78.76%"),
                P("Tiruchirappalli, Tamil Nadu, India"),
                P("Graduation Date: May 2023"),
                id="education-section",
            ),
            _Section(
                H2("Contact"),
                DivHStacked(
                    A(
                        UkIcon("linkedin", height=30, width=30),
                        href="https://www.linkedin.com/in/adhil03",
                        target="_blank",
                    ),
                    A(
                        UkIcon("github", height=30, width=30),
                        href="https://github.com/adhil03",
                        target="_blank",
                    ),
                    A(
                        UkIcon("phone", height=30, width=30),
                        href="tel:+917339445413",
                        target="_blank",
                    ),
                    A(
                        UkIcon("mail", height=30, width=30),
                        href="mailto:adhilpro253@gamil.com",
                        target="_blank",
                    ),
                ),
                id="contact-section",
            ),
        ),
        cls=(ContainerT.lg, "uk-container-expand"),
    )


serve()
