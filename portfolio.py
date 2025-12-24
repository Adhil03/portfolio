from fasthtml.common import *
from monsterui.all import *
from starlette.staticfiles import StaticFiles

# Data Objects
sections = ["about", "skills", "experience", "certifications", "education", "contact"]
skills = [
    ("Python", "code"),
    ("FastHTML", "layout"),
    ("Pandas", "table"),
    ("SQL", "database"),
    ("DuckDB", "zap"),
    ("Power BI", "bar-chart-3"),
]
certs = [
    (
        "Microsoft Power BI Desktop",
        "Udemy",
        "https://www.udemy.com/certificate/UC-c2bd8fc2-2652-4ada-bf7f-c38a13c79b15/",
    ),
    (
        "100 Days of Code: Python Pro",
        "Udemy",
        "https://www.udemy.com/certificate/UC-b4e09f1f-1e91-4fbc-b11c-54ba2c45be54/",
    ),
    (
        "Face Recognition App",
        "GUVI",
        "https://www.guvi.in/verify-certificate?id=161W9Iu2B07e68U9Yv",
    ),
    (
        "AI For India 2.0",
        "GUVI",
        "https://www.guvi.in/verify-certificate?id=61rzp919C0j12P1390",
    ),
    (
        "SQL Intermediate",
        "HackerRank",
        "https://www.hackerrank.com/certificates/d53a7cd388a8",
    ),
]

hdrs = (
    Theme.blue.headers(highlightjs=True),
    Link(rel="stylesheet", href="/static/style.css"),
    Link(
        href="https://fonts.googleapis.com/css2?family=Inter:wght@400;700;800&display=swap",
        rel="stylesheet",
    ),
)

app, rt = fast_app(hdrs=hdrs)
app.mount("/static", StaticFiles(directory="static"), name="static")


def NavBarCustom():
    links = [Li(A(s.capitalize(), href=f"#{s}-section")) for s in sections]
    return NavBar(
        Ul(
            *links,
            cls="uk-navbar-nav",
            uk_scrollspy_nav="closest: li; scroll: true; offset: 100",
        ),
        brand=DivLAligned(
            H4("Adhil's Portfolio", cls="m-0 font-bold tracking-tight"),
            UkIcon("code-xml", height=22, width=22, cls="ml-2 text-blue-500"),
        ),
        sticky=True,
        cls="glass-nav px-8",
    )


def SectionWrapper(*c, id, title):
    return Section(
        Div(
            Div(
                H2(title, cls="font-bold tracking-tight text-3xl"),
                DividerLine(),
                cls="mb-8",
            ),
            *c,
            cls="section-container",
        ),
        id=f"{id}-section",
        cls="py-20",
        uk_scrollspy="cls: uk-animation-slide-bottom-small; delay: 200",
    )


@rt("/")
def get():
    # HERO
    hero = Section(
        Div(
            Div(
                Img(
                    src="/static/adhil.jpg",
                    cls="w-44 h-44 rounded-full object-cover border-4 border-blue-200 shadow-2xl mb-8 mx-auto",
                ),
                Div(
                    H1(
                        "Hey there, I'm Adhil",
                        cls="typing text-4xl md:text-6xl pb-4 font-extrabold tracking-tighter",
                    ),
                    cls="typing-container",
                ),
                H4(
                    "Software Engineer @ ",
                    A(
                        "BISquared",
                        href="https://www.getprog.ai/profile/11910293",
                        target="_blank",
                        cls="text-blue-600",
                    ),
                    cls="text-gray-500 mb-4",
                ),
                I(
                    '"A passionate Python developer with hands-on experience in data analytics and backend development. I build reliable backend features using Python and FastHTML to support real-world applications."',
                    cls="text-gray-500",
                ),
                DivHStacked(
                    A(
                        UkIcon("download-cloud", cls="mr-2"),
                        "Download CV",
                        href="/static/Adhil_M_Resume_Dec2025.pdf",
                        download=True,
                        cls="btn btn-primary",
                    ),
                    A(
                        UkIcon("mail", cls="mr-2"),
                        "Contact Me",
                        href="#contact",
                        cls="btn btn-secondary",
                    ),
                    cls="mt-10 justify-center gap-4",
                ),
                cls="text-center",
            ),
            cls="container py-24 hero-gradient",
        )
    )

    # EXPERIENCE WITH FULL CONTENT
    experience_card = Card(
        Div(
            DivHStacked(
                Div(
                    H3("BI Squared Consulting Ltd", cls="font-bold text-blue-600 m-0"),
                    P(
                        "Software Engineer – Data & Python",
                        cls="text-gray-500 font-medium",
                    ),
                ),
                Span(
                    "April 2024 – Present",
                    cls="px-4 py-1 bg-blue-50 text-blue-700 rounded-full text-xs font-bold",
                ),
                cls="flex justify-between items-start mb-10",
            ),
            Grid(
                # IOM Project
                Div(
                    DivHStacked(
                        UkIcon("presentation", cls="text-blue-500 mr-2"),
                        H4("IOM USRAP Dashboard", cls="m-0 font-bold"),
                    ),
                    Ul(
                        Li(
                            "Developed Power BI dashboards to improve visibility into budget and operational trends."
                        ),
                        Li(
                            "Built Power Query pipelines for data cleaning and transformation."
                        ),
                        Li("Performed data validation to ensure accurate reporting."),
                        cls="list-disc ml-5 mt-4 text-sm text-gray-600 space-y-2",
                    ),
                    cls="p-6 bg-gray-50 rounded-2xl hover:bg-white hover:shadow-xl transition-all h-full border border-transparent hover:border-blue-100",
                ),
                # LMS Project
                Div(
                    DivHStacked(
                        UkIcon("graduation-cap", cls="text-blue-500 mr-2"),
                        H4("Learning Management System", cls="m-0 font-bold"),
                    ),
                    Ul(
                        Li(
                            "Contributed to quiz-based LMS enabling teachers to manage quizzes."
                        ),
                        Li(
                            "Built student pages for taking quizzes and viewing results."
                        ),
                        Li(
                            "Handled Excel imports using Pandas/OpenPyXL and exports via xlwings."
                        ),
                        cls="list-disc ml-5 mt-4 text-sm text-gray-600 space-y-2",
                    ),
                    cls="p-6 bg-gray-50 rounded-2xl hover:bg-white hover:shadow-xl transition-all h-full border border-transparent hover:border-blue-100",
                ),
                # Quran SRS
                Div(
                    DivHStacked(
                        UkIcon("book-open", cls="text-blue-500 mr-2"),
                        H4("Quran Memorization SRS", cls="m-0 font-bold"),
                    ),
                    Ul(
                        Li(
                            "Developed daily revision tracking system with adaptive SRS logic."
                        ),
                        Li(
                            "Built multi-role system for parents, teachers, and students."
                        ),
                        Li("Used FastHTML, MVC architecture, and SQLite."),
                        cls="list-disc ml-5 mt-4 text-sm text-gray-600 space-y-2",
                    ),
                    cls="p-6 bg-gray-50 rounded-2xl hover:bg-white hover:shadow-xl transition-all h-full border border-transparent hover:border-blue-100",
                ),
                cols_md=2,
                gap=6,
            ),
        ),
        cls="p-8 border-0 shadow-2xl ring-1 ring-gray-100",
    )

    return Title("Adhil | Software Engineer"), Main(
        NavBarCustom(),
        hero,
        SectionWrapper(
            P(
                "I have fundamental knowledge and hands-on experience in Data Analytics and Python development. I have worked on ETL and data wrangling pipelines to prepare clean, reliable datasets, developed Power BI dashboards for analysis and reporting, and performed data validation using Excel and Power Query. On the backend side, I have built application features using Python and FastHTML, working with SQLite for data storage. I follow standard development practices, including basic testing and GitHub-based version control, and have applied these skills in real-world projects such as an LMS and a Quran memorization SRS.",
                cls="text-lg leading-relaxed text-gray-600",
            ),
            id="about",
            title="About Me",
        ),
        SectionWrapper(
            Grid(
                *[
                    Card(
                        DivVStacked(
                            UkIcon(i, height=30, width=30, cls="text-blue-500"),
                            H4(n),
                            cls="text-center",
                        ),
                        cls="skill-card border-0 shadow-sm hover:shadow-md transition-all",
                    )
                    for n, i in skills
                ],
                cols_lg=6,
                gap=4,
            ),
            id="skills",
            title="Technical Stack",
        ),
        SectionWrapper(experience_card, id="experience", title="Experience"),
        SectionWrapper(
            Grid(
                *[
                    Card(
                        DivHStacked(
                            Div(
                                H4(name, cls="m-0 font-bold text-sm"),
                                P(f"via {prov}", cls="text-xs text-gray-400"),
                            ),
                            A(
                                UkIcon("external-link", 18, 18),
                                href=link,
                                target="_blank",
                                cls="ml-auto text-blue-500",
                            ),
                        ),
                        cls="p-4 border-0 shadow-sm hover:bg-blue-50/30",
                    )
                    for name, prov, link in certs
                ],
                cols_md=2,
                gap=4,
            ),
            id="certifications",
            title="Certifications",
        ),
        SectionWrapper(
            Card(
                Div(
                    H3("Jamal Mohamed College of Arts and Science", cls="font-bold"),
                    P("Bachelor of Computer Science | 78.76%", cls="text-blue-600"),
                    P("Graduated: May 2023", cls="text-sm text-gray-500"),
                    cls="p-6",
                ),
                cls="border-0 shadow-lg",
            ),
            id="education",
            title="Education",
        ),
        Footer(
            DivCentered(
                DivHStacked(
                    A(
                        UkIcon("linkedin", 30),
                        href="https://linkedin.com/in/adhil03",
                        cls="text-gray-400 hover:text-blue-600 transition",
                    ),
                    A(
                        UkIcon("github", 30),
                        href="https://github.com/adhil03",
                        cls="text-gray-400 hover:text-gray-100 transition",
                    ),
                    A(
                        UkIcon("mail", 30),
                        href="mailto:adlpro253@gmail.com",
                        cls="text-gray-400 hover:text-red-500 transition",
                    ),
                    A(
                        UkIcon("phone", 30),
                        href="tel:+917339445413",
                        cls="text-gray-400 hover:text-green-500 transition",
                    ),
                    A(
                        UkIcon("messages-square", 30),
                        href="https://discordapp.com/users/adhil003",
                        cls="text-gray-400 hover:text-blue-200 transition",
                    ),
                    A(
                        UkIcon("square-activity", 30),
                        href="https://www.hackerrank.com/profile/adlpro253",
                        cls="text-gray-400 hover:text-green-200 transition",
                    ),
                    cls=" space-x-4",
                ),
                I(
                    "© 2025 Adhil. Built with FastHTML & MonsterUI",
                    cls="text-gray-400 text-sm pb-10",
                ),
            ),
            id="contact",
            cls="py-4 bg-gray-900 mt-20",
        ),
    )


serve()
