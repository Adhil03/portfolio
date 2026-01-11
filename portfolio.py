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
    "experience",
    "projects",
    "skills",
    "certifications",
    "education",
    "contact",
]

skill_categories = {
    "Backend & App Dev": [
        ("Python", "code"),
        ("Django (MVT)", "layers"),
        ("FastHTML", "rocket"),
        ("HTMX", "zap"),
        ("RESTful APIs", "globe"),
    ],
    "Databases & ORM": [
        ("SQL", "database"),
        ("SQLite", "database-zap"),
        ("DuckDB", "box"),
        ("SQLAlchemy", "link"),
    ],
    "Data Analytics": [
        ("Pandas", "table"),
        ("Power BI", "bar-chart-3"),
        ("Power Query", "filter"),
        ("Excel", "file-spreadsheet"),
    ],
    "Tools & Deployment": [
        ("Git", "git-branch"),
        ("GitHub", "github"),
        ("Railway", "train-front"),
        ("Render", "cloud"),
        ("VS Code", "terminal-square"),
    ],
}

expertise_areas = [
    "Backend Logic",
    "MVC/MVT Architecture",
    "Unit Testing",
    "API Integration",
    "Version Control",
    "TDD",
    "BDD",
    "CI/CD Concepts",
    "Data Modelling",
    "Data Validation",
    "ETL Pipelines",
    "Dashboard Design",
]

provider_logos = {
    "Udemy": "/static/udemy.png",
    "Coursera": "/static/coursera.png",
    "GUVI": "/static/guvi.jpeg",
    "HackerRank": "/static/hackerrank.png",
}

certs = [
    (
        "100 Days of Code: Python Pro",
        "Udemy",
        "https://www.udemy.com/certificate/UC-b4e09f1f-1e91-4fbc-b11c-54ba2c45be54/",
    ),
    (
        "Microsoft Power BI Desktop",
        "Udemy",
        "https://www.udemy.com/certificate/UC-c2bd8fc2-2652-4ada-bf7f-c38a13c79b15/",
    ),
    (
        "SQL (Basic & Intermediate)",
        "HackerRank",
        "https://www.hackerrank.com/certificates/d53a7cd388a8",
    ),
    (
        "Data Analysis using Microsoft Excel",
        "Coursera",
        "https://www.coursera.org/account/accomplishments/verify/BH80B53FE41E/",
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
    nav_links = [Li(A(s.capitalize(), href=f"#{s}-section")) for s in sections]
    return NavBar(
        Ul(
            *nav_links,
            cls="uk-navbar-nav desktop-nav",
            uk_scrollspy_nav="closest: li; scroll: true; offset: 100",
        ),
        brand=DivLAligned(
            H4(A("Adhil's Portfolio", href="/", cls="m-0 font-bold")),
            A(UkIcon("badge-check", cls="p-2"), href="/"),
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
    subject = urllib.parse.quote(f"Portfolio Message from {form.get('name')}")
    body = urllib.parse.quote(
        f"From: {form.get('name')} ({form.get('email')})\n\n{form.get('message')}"
    )
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
                    I("Chennai, India"),
                    cls="justify-center mb-4",
                ),
                Div(
                    I(
                        '"Software Engineer with 1+ years of experience in Python application development. Built LMS and SRS applications using FastHTML, and currently strengthening backend skills with Django (MVT)."'
                    ),
                    cls="max-w-lg mx-auto mb-6 px-4 text-muted-foreground",
                ),
                DivHStacked(
                    A(
                        UkIcon("download-cloud", cls="mr-2"),
                        "Download CV",
                        href="/static/Adhil_M_Resume_Jan2026.pdf",
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

    # Professional Experience Section
    experience_card = Card(
        Div(
            DivHStacked(
                Div(
                    H3("BI Squared Consulting Ltd", cls="font-bold text-primary m-0"),
                    P(
                        "Associate Software Engineer – Data & Python",
                        cls="text-muted-foreground",
                    ),
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
                        Div(
                            *[
                                Span(
                                    tag,
                                    cls="text-[10px] border border-primary/20 bg-primary/5 px-2 py-0.5 rounded-md text-muted-foreground",
                                )
                                for tag in tags
                            ],
                            cls="flex flex-wrap gap-2 mt-3 mb-2",
                        ),
                        Div(
                            (
                                Span(
                                    "Confidential 🔒",
                                    cls="text-[10px] bg-blue-50 text-blue-600 px-2 py-0.5 rounded",
                                )
                                if confidential
                                else ""
                            ),
                            cls="mt-1",
                        ),
                        Ul(
                            *[Li(b) for b in bullets],
                            cls="list-disc ml-5 mt-2 text-sm text-muted-foreground space-y-1",
                        ),
                        Details(
                            Summary(
                                "View Details",
                                cls="text-xs text-primary cursor-pointer mt-4 hover:underline",
                            ),
                            Div(
                                Hr(cls="my-2"),
                                P(
                                    proof_desc,
                                    cls="text-xs italic text-muted-foreground m-6",
                                ),
                                (
                                    DivHStacked(
                                        A(
                                            Button(
                                                "Code",
                                                cls="uk-button-xsmall uk-button-default text-[10px]",
                                            ),
                                            href=repo_url,
                                            target="_blank",
                                        ),
                                        cls="gap-2",
                                    )
                                    if repo_url
                                    else P(
                                        "Codebase is private per client agreement.",
                                        cls="text-[10px] text-muted-foreground m-6",
                                    )
                                ),
                            ),
                            cls="mt-auto",
                        ),
                        cls="p-6 project-subcard rounded-2xl h-full shadow-sm flex flex-col",
                    )
                    for title, icon, bullets, tags, confidential, repo_url, proof_desc in [
                        (
                            "IOM USRAP Dashboard",
                            "presentation",
                            [
                                "Developed multi-departmental Power BI dashboards to improve visibility into budget trends.",
                                "Engineered automated Power Query pipelines for ETL and data transformation.",
                                "Performed thorough data validation to ensure 100% reporting accuracy.",
                            ],
                            ["Power BI", "Power Query", "Excel", "Data Modeling"],
                            True,
                            None,
                            "Confidential financial reporting project.",
                        ),
                        (
                            "Learning Management System",
                            "graduation-cap",
                            [
                                "Built a quiz-based internal LMS using Python and FastHTML, automating scoring logic.",
                                "Contributed to student-facing features for quiz attempts and result tracking.",
                                "Optimized data operations by importing questions via Pandas/Openpyxl.",
                            ],
                            ["Python", "FastHTML", "SQLite", "Pandas"],
                            False,
                            "https://github.com/BIsquared/lms",
                            "Collaborated in a Driver-Navigator setup.",
                        ),
                        (
                            "Quran Memorization SRS",
                            "book-open",
                            [
                                "Architected a tracking system with adaptive Spaced Repetition logic and MVC architecture.",
                                "Implemented multi-role user management for parents, teachers, and students.",
                                "Enhanced system performance using Python and SQLite.",
                            ],
                            ["Python", "FastHTML", "MVC", "Algorithms"],
                            False,
                            "https://github.com/siraj-samsudeen/quran-srs",
                            "Developed core revision logic.",
                        ),
                    ]
                ],
                cols_md=2,
                gap=6,
            ),
        ),
        cls="p-8 border-0 shadow-2xl",
    )

    # Personal Projects Grid
    personal_projects = Grid(
        Card(
            Div(
                H4("Own Space – Django Task Manager", cls="font-bold text-primary"),
                Div(
                    *[
                        Span(
                            tag,
                            cls="text-[10px] border border-primary/20 bg-primary/5 px-2 py-0.5 rounded-md text-muted-foreground",
                        )
                        for tag in ["Django", "SQLite", "MVT"]
                    ],
                    cls="flex flex-wrap gap-2 mt-2 mb-2",
                ),
                P(
                    "Mastered Django MVT and ORM through a full-featured CRUD application.",
                    cls="text-sm text-muted-foreground",
                ),
                Ul(
                    Li("Django MVT Architecture"),
                    Li("PRG Design Pattern"),
                    Li("Database Migrations"),
                    cls="text-xs mt-4 list-disc ml-4",
                ),
                cls="p-6 h-full shadow-sm flex flex-col",
            ),
            cls="project-subcard",
        ),
        Card(
            Div(
                H4("Developer Portfolio (FastHTML)", cls="font-bold text-primary"),
                Div(
                    *[
                        Span(
                            tag,
                            cls="text-[10px] border border-primary/20 bg-primary/5 px-2 py-0.5 rounded-md text-muted-foreground",
                        )
                        for tag in ["Python", "FastHTML", "Railway", "Render"]
                    ],
                    cls="flex flex-wrap gap-2 mt-2 mb-2",
                ),
                P(
                    "A high-performance site deployed on Railway using modern Python web tools.",
                    cls="text-sm text-muted-foreground",
                ),
                Ul(
                    Li("FastHTML & HTMX"),
                    Li("AI-Assisted UI Rapid Prototyping"),
                    Li("Cloud Deployment"),
                    cls="text-xs mt-4 list-disc ml-4",
                ),
                cls="p-6 h-full shadow-sm flex flex-col",
            ),
            cls="project-subcard",
        ),
        cols_md=2,
        gap=6,
    )

    return Title("Adhil | Software Engineer"), Main(
        NavBarCustom(),
        hero,
        SectionWrapper(
            P(
                "Software Engineer with 1+ years of experience in Python application development and data-supported systems. I enjoy working across backend logic and data processing to build practical solutions for real-world use cases.",
                cls="text-lg text-muted-foreground leading-relaxed",
            ),
            id="about",
            title="About Me",
        ),
        SectionWrapper(
            experience_card, id="experience", title="Professional Experience"
        ),
        SectionWrapper(personal_projects, id="projects", title="Personal Projects"),
        SectionWrapper(
            Div(
                *[
                    Div(
                        H3(cat, cls="text-xl font-bold mb-4 text-primary"),
                        Div(
                            *[
                                Card(
                                    DivVStacked(
                                        # Icon stays a good visible size
                                        UkIcon(
                                            i, height=28, width=28, cls="text-primary"
                                        ),
                                        # Text wraps if needed, small font
                                        H4(
                                            n,
                                            cls="text-xs m-0 mt-2 font-medium leading-tight",
                                        ),
                                        cls="text-center items-center justify-center h-full",
                                    ),
                                    # FIXED WIDTHS: w-24 on mobile, w-32 on desktop
                                    # This prevents them from becoming huge on laptops
                                    cls="w-24 md:w-32 p-3 hover:border-primary/50 transition-colors shadow-sm bg-card",
                                )
                                for n, i in items
                            ],
                            # Flex wrap allows them to pack tightly
                            cls="flex flex-wrap gap-3",
                        ),
                        cls="mb-8",
                    )
                    for cat, items in skill_categories.items()
                ],
                # Expertise Section (Concepts)
                Div(
                    H3("Expertise", cls="text-xl font-bold mb-4 text-primary"),
                    Div(
                        *[
                            Span(
                                exp,
                                cls="px-4 py-2 bg-muted rounded-xl text-sm m-1 inline-block border border-border skill-card",
                            )
                            for exp in expertise_areas
                        ],
                        cls="flex flex-wrap gap-2",
                    ),
                    cls="mt-6 p-6 rounded-2xl border border-dashed border-primary/20",
                ),
            ),
            id="skills",
            title="Technical Stack",
        ),
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
        SectionWrapper(
            Div(
                UkIcon("heart-handshake", height=80, width=80, cls="text-primary mb-6"),
                Grid(
                    Div(
                        H3("Let's work together", cls="font-bold text-2xl mb-4"),
                        P(
                            "I'm currently looking for new opportunities in Python development.",
                            cls="text-muted-foreground m-4",
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
                    "© 2026 Adhil. Built with FastHTML & MonsterUI",
                    cls="text-muted-foreground text-sm p-10",
                )
            ),
            cls="mt-12",
        ),
    )


if __name__ == "__main__":
    serve()
