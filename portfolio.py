from fasthtml.common import *
from monsterui.all import *
from starlette.staticfiles import StaticFiles
import urllib.parse

# Data Objects
skill_categories = {
    "Data Analytics": [
        ("Pandas", "table"),
        ("SQL", "database"),
        ("DuckDB", "zap"),
        ("Power BI", "bar-chart-3"),
        ("Rill Data", "chart-line"),
        ("Matplotlib", "chart-spline"),
        ("Excel", "file-spreadsheet"),
        ("Power Query", "filter"),
    ],
    "Development": [
        ("Python", "code"),
        ("FastHTML", "rocket"),
        ("REST APIs", "globe"),
        ("Git", "git-branch"),
        ("GitHub", "github"),
        ("Pytest", "check-circle"),
        ("SQL", "database"),
        ("SQLite", "database"),
        ("SQLAlchemy", "database-zap"),
        ("FastAPI", "rocket"),
    ],
}
# Data Analytics Focus
da_expertise = [
    "Data Cleaning",
    "Data Visualization",
    "Data Manipulation",
    "Data Aggregation",
    "Exploratory Data Analysis",
    "Performance Metrics",
    "ETL Pipelines",
    "Dashboard Design",
    "SQLite",
]

# Software Development Focus
dev_expertise = [
    "FastHTML",
    "SQLAlchemy",
    "Git",
    "GitHub",
    "Backend Logic",
    "MVC Architecture",
    "Automated Testing",
    "Authentication",
    "Authorization",
    "Version Control",
    "Testing",
    "TDD",
    "BDD",
]
expertise_areas = da_expertise + dev_expertise
contact_links = [
    A(
        UkIcon("linkedin", 30),
        href="https://linkedin.com/in/adhil03",
        cls="text-gray-400 hover:text-blue-600 transition",
    ),
    A(
        UkIcon("github", 30),
        href="https://github.com/adhil03",
        cls="text-gray-400 hover:text-gray-200 transition",
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
]
sections = [
    "home",
    "about",
    "skills",
    "experience",
    "certifications",
    "education",
    "contact",
]
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
        "Data Analysis using Microsoft Excel",
        "Coursera",
        "https://www.coursera.org/account/accomplishments/verify/BH80B53FE41E/",
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
        cls="py-12",
        uk_scrollspy="cls: uk-animation-slide-bottom-small; delay: 200",
    )


def SkillsSection():
    # Helper to build a category grid
    def CategoryGrid(title, skill_list):
        return Div(
            H3(title, cls="text-xl font-bold mb-6 text-blue-600"),
            Grid(
                *[
                    Card(
                        DivVStacked(
                            Div(
                                UkIcon(icon, height=30, width=30, cls="text-blue-500"),
                                cls="skill-icon-container mb-3",
                            ),
                            H4(name, cls="font-bold text-sm m-0"),
                            cls="text-center p-4",
                        ),
                        cls="skill-card border-0 shadow-sm",
                    )
                    for name, icon in skill_list
                ],
                cols_min=2,
                cols_md=3,
                cols_lg=6,
                gap=4,
            ),
            cls="mb-12",
        )

    return SectionWrapper(
        Div(
            # 1. Main Tools Categories
            *[CategoryGrid(cat, items) for cat, items in skill_categories.items()],
            # 2. Concepts & Expertise (Floating Badges Style)
            Div(
                H3("Concepts & Expertise", cls="text-xl font-bold mb-6 text-blue-600"),
                Div(
                    *[
                        Span(
                            exp,
                            cls="px-6 py-3 bg-gray-50 border border-gray-100 rounded-xl text-sm font-semibold text-gray-700 m-2 inline-block hover:border-blue-400 hover:text-blue-600 transition-all",
                        )
                        for exp in expertise_areas
                    ],
                    cls="flex flex-wrap justify-start",
                ),
                cls="mt-16 p-8 bg-blue-50/30 rounded-3xl border border-blue-100/50",
            ),
        ),
        id="skills",
        title="Technical Stack",
    )


def ContactSection():
    return SectionWrapper(
        Div(
            H3("Get In Touch"),
            Grid(
                # Left side: Text info
                Div(
                    H3("Let's work together", cls="font-bold text-2xl mb-4"),
                    I(
                        "I'm currently looking for new opportunities. Whether you have a question or just want to say hi, I'll try my best to get back to you!",
                        cls="text-grey-600 justify mb-6",
                    ),
                    DivVStacked(
                        DivHStacked(
                            UkIcon("mail", cls="text-blue-500 mr-3"),
                            P("adlpro253@gmail.com", cls="m-0"),
                        ),
                        DivHStacked(
                            UkIcon("phone", cls="text-blue-500 mr-3"),
                            P("+91 7339445413", cls="m-0"),
                        ),
                        gap=4,
                    ),
                    cls="pr-8",
                ),
                # Right side: The Form
                # Inside ContactSection()
                Form(
                    DivVStacked(
                        Input(
                            placeholder="Your Name",
                            name="name",
                            cls="contact-input rounded-xl p-4",
                            required=True,
                        ),
                        Input(
                            placeholder="Your Email",
                            name="email",
                            type="email",
                            cls="contact-input rounded-xl p-4",
                            required=True,
                        ),
                        TextArea(
                            placeholder="How can I help you?",
                            name="message",
                            rows=4,
                            cls="contact-input rounded-xl p-4",
                            required=True,
                        ),
                        Button(
                            "Send Message",
                            type="submit",
                            cls=ButtonT.primary + " py-4 rounded-xl font-bold",
                        ),
                        gap=4,
                    ),
                    action="/send-message",
                    method="post",
                ),
                cols_md=2,
                gap=12,
                cls="items-center",
            ),
            cls="form-container border border-gray-100",
        ),
        id="contact",
        title="Get In Touch",
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
                Div(
                    I(
                        '"A passionate Python developer with hands-on experience in data analytics and backend development. I build reliable backend features using Python and FastHTML to support real-world applications."',
                        cls="text-gray-500",
                    ),
                    cls="max-w-lg mx-auto mb-6 px-4",
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
                        href="#contact-section",
                        cls="btn btn-secondary",
                    ),
                    cls="mt-10 justify-center gap-4",
                ),
                cls="text-center",
            ),
            DivCentered(
                DivHStacked(
                    *(contact_links),
                    id="contact_links",
                    cls="space-x-10 mt-4",
                ),
            ),
            cls="container py-12 hero-gradient",
        ),
        id="home-section",
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
        #
        SkillsSection(),
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
        ContactSection(),
        Footer(
            DivCentered(
                DivHStacked(
                    *(contact_links),
                    cls=" space-x-4",
                ),
                I(
                    "© 2025 Adhil. Built with FastHTML & MonsterUI",
                    cls="text-gray-400 text-sm pb-10",
                ),
            ),
            cls="py-4 bg-gray-900 mt-20",
        ),
    )


@rt("/send-message", methods=["POST"])
async def post(request):
    form = await request.form()
    name = form.get("name")
    email_addr = form.get("email")
    message = form.get("message")

    subject = f"Portfolio Message from {name}"
    body = f"From: {name} ({email_addr})\n\nMessage:\n{message}"

    mailto_link = f"mailto:adlpro253@gmail.com?subject={urllib.parse.quote(subject)}&body={urllib.parse.quote(body)}"
    return RedirectResponse(url=mailto_link)


serve()
