import reflex as rx
from cogscal.components.nav import nav

style = {"margin_x": "1rem"}


def bearings() -> rx.Component:
    return rx.hstack(
        nav(),
        rx.vstack(rx.heading("Bearings"), style=style),
    )
