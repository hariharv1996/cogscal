import reflex as rx
from cogscal.components.nav import nav
from cogscal.pages.gears import gears
from cogscal.pages.bearings import bearings

style = {
    "font_family": "Verdana",
    "padding": "1rem",
}


def index() -> rx.Component:
    return rx.hstack(
        nav(),
        rx.vstack(
            rx.heading(
                "Welcome to ",
                rx.text("Cogscal", as_="span", color=rx.color("accent", 10)),
            ),
            rx.text(
                "A full stack gearbox machine element calculation and database maintenance web application built with ",
                rx.link("Reflex", href="https://reflex.dev"),
            ),
            margin_x="1rem",
        ),
    )


app = rx.App(
    theme=rx.theme(has_background=True, accent_color="teal", appearance="dark"),
    style=style,
)
app.add_page(index)
app.add_page(gears, route="/gears")
app.add_page(bearings, route="/bearings")
