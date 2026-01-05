from fasthtml.common import *
from monsterui.all import *
from starlette.staticfiles import StaticFiles
from starlette.responses import RedirectResponse, FileResponse
import urllib.parse

# 1. APP & DATA SETUP
hdrs = (
    Theme.blue.headers(highlightjs=True),
    Link(rel="stylesheet", href="/static/style.css"),
    Link(rel="icon", href="/static/favicon.ico", type="image/x-icon"),
)

app, rt = fast_app(hdrs=hdrs, bodykw={"class": "bg-background text-foreground"})
app.mount("/static", StaticFiles(directory="static"), name="static")

sections = [
    "home",
    "about",
    "skills",
    "experience",
    "certifications",
    "education",
    "contact",
]

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
    ],
}

expertise_areas = [
    "Data Cleaning",
    "Data Visualization",
    "Data Manipulation",
    "Data Aggregation",
    "Exploratory Data Analysis",
    "Performance Metrics",
    "ETL Pipelines",
    "Dashboard Design",
    "SQLite",
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

provider_logos = {
    "Udemy": "/static/udemy.png",
    "Coursera": "/static/coursera.png",
    "GUVI": "/static/guvi.jpeg",
    "HackerRank": "/static/hackerrank.png",
}

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

contact_links = [
    A(
        UkIcon("linkedin", 30),
        href="https://linkedin.com/in/adhil03",
        cls="text-muted-foreground hover:text-primary transition",
    ),
    A(
        UkIcon("github", 30),
        href="https://github.com/adhil03",
        cls="text-muted-foreground hover:text-foreground transition",
    ),
    A(
        UkIcon("mail", 30),
        href="mailto:adlpro253@gmail.com",
        cls="text-muted-foreground hover:text-destructive transition",
    ),
    A(
        UkIcon("phone", 30),
        href="tel:+917339445413",
        cls="text-muted-foreground hover:text-success transition",
    ),
]


# 2. COMPONENTS
def NavBarCustom():
    tp_dropdown = Div(
        ThemePicker(mode=True, color=True, radii=True),
        uk_dropdown="mode: click; pos: bottom-right",
    )

    # Desktop Links
    nav_links = [Li(A(s.capitalize(), href=f"#{s}-section")) for s in sections]

    return NavBar(
        # Horizontal Desktop Nav
        Ul(
            *nav_links,
            cls="uk-navbar-nav desktop-nav",
            uk_scrollspy_nav="closest: li; scroll: true; offset: 100",
        ),
        brand=DivLAligned(
            H4("Adhil's Portfolio", cls="m-0 font-bold"),
            UkIcon("badge-check", cls="ml-2"),
            Button(UkIcon("palette"), cls="ml-4 btn-ghost"),
            tp_dropdown,
        ),
        sticky=True,
        cls="glass-nav px-8",
    )


def SectionWrapper(*c, id, title):
    return Section(
        Div(
            Div(H2(title, cls="font-bold text-3xl"), DividerLine(), cls="mb-8"),
            *c,
            cls="section-container",
        ),
        id=f"{id}-section",
        cls="py-16",
        uk_scrollspy="cls: uk-animation-slide-bottom-small; delay: 200",
    )


# 3. ROUTES
@rt("/favicon.ico")
def get():
    return FileResponse("static/favicon.ico")


@rt("/send-message", methods=["POST"])
async def post(request):
    form = await request.form()
    name, email, msg = form.get("name"), form.get("email"), form.get("message")
    subject = urllib.parse.quote(f"Portfolio Message from {name}")
    body = urllib.parse.quote(f"From: {name} ({email})\n\n{msg}")
    return RedirectResponse(
        url=f"mailto:adlpro253@gmail.com?subject={subject}&body={body}"
    )


@rt("/")
def get():
    # Hero Section
    hero = Section(
        Div(
            Div(
                Img(
                    src="/static/adhil.jpg",
                    cls="w-44 h-44 rounded-full object-cover border-4 border-primary shadow-2xl mb-8 mx-auto",
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
                        cls=("text-primary font-bold", ButtonT.text),
                    ),
                    cls="mb-4",
                ),
                DivHStacked(
                    UkIcon("map-pin", cls="mr-2"),
                    A(
                        I("Chennai, India", cls=("text-grey-300", ButtonT.text)),
                        href="https://maps.app.goo.gl/Mo764VWQ21JRVR8v7",
                        target="_blank",
                    ),
                    cls="justify-center mb-4",
                ),
                Div(
                    I(
                        '"A passionate Python developer with hands-on experience in data analytics and backend development. I build reliable backend features using Python and FastHTML to support real-world applications."',
                        cls="text-gray-500",
                    ),
                    cls="max-w-lg mx-auto mb-6 px-4 text-muted-foreground",
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
                DivCentered(DivHStacked(*contact_links, cls="space-x-8 mt-10")),
                cls="text-center",
            ),
            cls="container py-12 hero-gradient",
        ),
        id="home-section",
    )

    # Full Experience Section
    experience_card = Card(
        Div(
            DivHStacked(
                Div(
                    H3("BI Squared Consulting Ltd", cls="font-bold text-primary m-0"),
                    P("Software Engineer – Data & Python", cls="text-muted-foreground"),
                ),
                Span(
                    "April 2024 – Present",
                    cls="px-4 py-1 bg-primary/10 text-primary rounded-full text-xs font-bold ml-auto",
                ),
                cls="flex justify-between items-start mb-10",
            ),
            Grid(
                *[
                    Div(
                        DivHStacked(
                            UkIcon(icon, cls="text-primary mr-2"),
                            H4(title, cls="m-0 font-bold"),
                        ),
                        # Label Row (Confidential / Pair Programming)
                        Div(
                            (
                                Span(
                                    "Confidential 🔒",
                                    cls="text-[10px] bg-blue-50 text-blue-600 px-2 py-0.5 rounded",
                                )
                                if confidential
                                else ""
                            ),
                            # (
                            #     Span(
                            #         # "Pair Programmed",
                            #         cls="text-[10px] bg-blue-50 text-blue-600 px-2 py-0.5 rounded",
                            #     )
                            #     if pair_programmed
                            #     else ""
                            # ),
                            # (
                            #     Span(
                            #         # "Collabration",
                            #         cls="text-[10px] bg-blue-50 text-blue-600 px-2 py-0.5 rounded",
                            #     )
                            #     if collabrative
                            #     else ""
                            # ),
                            cls="mt-2",
                        ),
                        Ul(
                            *[Li(b) for b in bullets],
                            cls="list-disc ml-5 mt-4 text-sm text-muted-foreground space-y-2",
                        ),
                        # Expandable Proof Section
                        Details(
                            Summary(
                                "View Proof & Links",
                                cls="text-xs text-primary cursor-pointer mt-4 hover:underline",
                            ),
                            Div(
                                Hr(cls="my-2"),
                                P(
                                    proof_desc,
                                    cls="text-xs italic text-muted-foreground m-6",
                                ),
                                (
                                    (
                                        DivHStacked(
                                            (
                                                A(
                                                    Button(
                                                        "Code",
                                                        cls="uk-button-xsmall uk-button-default text-[10px]",
                                                    ),
                                                    href=repo_url,
                                                    target="_blank",
                                                )
                                                if repo_url
                                                else ""
                                            ),
                                            (
                                                A(
                                                    Button(
                                                        "Verify",
                                                        cls="uk-button-xsmall uk-button-primary text-[10px]",
                                                    ),
                                                    href=f"{repo_url}/graphs/contributors",
                                                    target="_blank",
                                                )
                                                if repo_url
                                                else ""
                                            ),
                                            cls="gap-2",
                                        )
                                        if not confidential
                                        else P(
                                            "Codebase is private per client agreement.",
                                            cls="text-[10px] text-muted-foreground m-6",
                                        )
                                    ),
                                ),
                            ),
                            cls="mt-auto",
                        ),
                        cls="p-6 project-subcard rounded-2xl h-full shadow-sm flex flex-col",
                    )
                    for title, icon, bullets, confidential, repo_url, proof_desc in [
                        (
                            "IOM USRAP Dashboard",
                            "presentation",
                            [
                                "Developed Power BI dashboards at summary and departmental levels to improve visibility into budget and operational trends.",
                                "Built Power Query pipelines for data cleaning, merging, and transformation.",
                                "Performed data validation and quality checks to ensure accurate reporting.",
                            ],
                            True,  # Confidential
                            # False,  # Pair Programmed
                            # False,
                            None,
                            "Client Confidentiality Agreement in place.",
                        ),
                        (
                            "Learning Management System",
                            "graduation-cap",
                            [
                                "Contributed to a quiz-based LMS enabling teachers to manage questions, quizzes, and student performance.",
                                "Built student-facing pages for taking quizzes, saving answers, and viewing results.",
                                "Handled Excel imports using Pandas/OpenPyXL and exports via xlwings.",
                            ],
                            False,
                            # True,  # Pair Programmed
                            # False,
                            "https://github.com/BIsquared/lms",
                            "Collaborated in a Driver-Navigator setup to ensure high code quality.",
                        ),
                        (
                            "Quran Memorization SRS",
                            "book-open",
                            [
                                "Developed daily revision tracking system with adaptive SRS logic.",
                                "Built multi-role user system for parents, teachers, and students.",
                                "Enhanced experience with Python, FastHTML, MVC, and SQLite.",
                            ],
                            False,
                            # False,
                            # True,
                            "https://github.com/siraj-samsudeen/quran-srs",
                            "Collaborated on feature implementation and logic refinement for the Spaced Repetition engine.",
                        ),
                    ]
                ],
                cols_md=2,
                gap=6,
            ),
        ),
        cls="p-8 border-0 shadow-2xl",
    )
    return Title("Adhil | Software Engineer"), Main(
        NavBarCustom(),
        hero,
        SectionWrapper(
            P(
                "I have fundamental knowledge and hands-on experience in Data Analytics and Python development. I have worked on ETL and data wrangling pipelines to prepare clean, reliable datasets, developed Power BI dashboards for analysis and reporting, and performed data validation using Excel and Power Query. On the backend side, I have built application features using Python and FastHTML, working with SQLite for data storage. I follow standard development practices, including basic testing and GitHub-based version control, and have applied these skills in real-world projects such as an LMS and a Quran memorization SRS.",
                cls="text-lg text-muted-foreground leading-relaxed",
            ),
            id="about",
            title="About Me",
        ),
        # Tech Stack with Categories
        SectionWrapper(
            Div(
                *[
                    Div(
                        H3(cat, cls="text-xl font-bold mb-6 text-primary"),
                        Grid(
                            *[
                                Card(
                                    DivVStacked(
                                        UkIcon(
                                            i, height=30, width=30, cls="text-primary"
                                        ),
                                        H4(n, cls="text-sm m-0"),
                                        cls="text-center p-4",
                                    ),
                                    cls="skill-card",
                                )
                                for n, i in items
                            ],
                            cols_lg=6,
                            gap=4,
                        ),
                        cls="mb-12",
                    )
                    for cat, items in skill_categories.items()
                ],
                Div(
                    H3(
                        "Concepts & Expertise",
                        cls="text-xl font-bold mb-6 text-primary",
                    ),
                    Div(
                        *[
                            Span(
                                exp,
                                cls="px-4 py-2 bg-muted rounded-xl text-sm m-1 inline-block border border-border skill-card",
                            )
                            for exp in expertise_areas
                        ],
                        cls="flex flex-wrap",
                    ),
                    cls="mt-10 p-8 rounded-3xl border border-primary/10",
                ),
            ),
            id="skills",
            title="Technical Stack",
        ),
        SectionWrapper(experience_card, id="experience", title="Experience"),
        # Certifications with Provider Logos
        SectionWrapper(
            Grid(
                *[
                    Card(
                        DivHStacked(
                            Img(src=provider_logos.get(prov, ""), cls="w-10 h-10 mr-4"),
                            Div(
                                H4(name, cls="m-0 text-sm font-bold"),
                                P(prov, cls="text-xs text-muted-foreground"),
                            ),
                            A(
                                UkIcon("external-link", 18),
                                href=link,
                                target="_blank",
                                cls="ml-auto text-primary",
                            ),
                        ),
                        cls="p-5 project-subcard shadow-sm",
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
                    P("Bachelor of Computer Science | 78.76%", cls="text-primary"),
                    P("Graduated: May 2023", cls="text-sm text-muted-foreground"),
                    cls="p-6",
                )
            ),
            id="education",
            title="Education",
        ),
        # Contact Form
        SectionWrapper(
            Div(
                UkIcon("heart-handshake", height=80, width=80, cls="text-primary mb-6"),
                Grid(
                    Div(
                        H3("Let's work together", cls="font-bold text-2xl mb-4"),
                        P(
                            "I'm currently looking for new opportunities. Whether you have a question or just want to say hi, I'll try my best to get back to you!",
                            cls="text-muted-foreground m-4 justify-center",
                        ),
                        DivVStacked(
                            DivHStacked(
                                UkIcon("mail", cls="text-primary mr-3"),
                                P("adlpro253@gmail.com"),
                            ),
                            DivHStacked(
                                UkIcon("phone", cls="text-primary mr-3"),
                                P("+91 7339445413"),
                            ),
                            cls="mb-2",
                            gap=4,
                        ),
                    ),
                    Form(
                        DivVStacked(
                            Input(
                                placeholder="Name",
                                name="name",
                                cls="contact-input",
                                required=True,
                            ),
                            Input(
                                placeholder="Email",
                                name="email",
                                type="email",
                                cls="contact-input",
                                required=True,
                            ),
                            TextArea(
                                placeholder="Message",
                                name="message",
                                rows=4,
                                cls="contact-input",
                                required=True,
                            ),
                            Button(
                                "Send Message",
                                type="submit",
                                cls="btn btn-primary py-4",
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
                cls="form-container shadow-xl",
            ),
            id="contact",
            title="Get In Touch",
        ),
        Footer(
            DivCentered(
                P(
                    "© 2025 Adhil. Built with FastHTML & MonsterUI",
                    cls="text-muted-foreground text-sm p-10",
                )
            ),
            cls="mt-12",
        ),
    )


if __name__ == "__main__":
    serve()
