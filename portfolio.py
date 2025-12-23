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
    "blog",
    "contact",
]
scrollspy_links = (*[A(s.capitalize(), href=f"#{s}-section") for s in sections],)


@rt("/")
def get():
    def _Section(*c, **kwargs):
        return Section(*c, cls="space-y-3 my-48", **kwargs)

    return Container(
        NavBar(
            *scrollspy_links,
            brand=DivLAligned(
                H3("Adhil's Portfolio"), UkIcon("rocket", height=30, width=30)
            ),
            sticky=True,
            uk_scrollspy_nav=True,
            scrollspy_cls=ScrollspyT.bold,
        ),
        NavContainer(
            *map(Li, scrollspy_links),
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
                H2("About Me"),
                P(
                    "A passionate Python developer with hands-on experience in data analytics and backend development. I work on ETL pipelines, data validation, and dashboard creation, and build reliable backend features using Python and FastHTML to support real-world applications."
                ),
                id="about-section",
            ),
        ),
        cls=(ContainerT.lg, "uk-container-expand"),
    )


serve()
