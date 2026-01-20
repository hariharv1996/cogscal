import reflex as rx


style = {
    "width": "20%",
    "bg_color": "slate",
    "height": "100vh",
    "border_right": "1px solid white",
}


def nav() -> rx.Component:
    return rx.vstack(
        rx.heading("Cogscal", color=rx.color("accent", 10), margin_bottom="1rem"),
        rx.link("Home", href="/"),
        rx.link("Gears", href="/gears"),
        rx.link("Bearings", href="/bearings"),
        style=style,
    )
