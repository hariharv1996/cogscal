import reflex as rx
from cogscal.components.nav import nav
from cogscal.models.gear import Gear

style = {"margin_x": "1rem"}


class State(rx.State):
    gear: Gear

    @rx.event
    def set_gear_data(self, gear_data: dict):
        if gear_data["gear_id"]:
            gear_id = int(gear_data["gear_id"])
        else:
            gear_id = None
        self.gear = Gear(
            gear_id=gear_id,
            m_n=float(gear_data["m_n"]),
            z=int(gear_data["z"]),
            alpha_n=float(gear_data["alpha_n"]),
            beta=float(gear_data["beta"]),
        )
        with rx.session() as session:
            session.add(self.gear)
            session.commit()

    @rx.event
    def get_gear_data(self, form_data: dict):
        with rx.session() as session:
            self.gear = session.get(Gear, int(form_data["gear_id"]))
            self.gear.calculate()


def gears() -> rx.Component:
    return rx.hstack(
        nav(),
        rx.vstack(
            rx.heading("Gears"),
            rx.form(
                rx.vstack(
                    rx.input(placeholder="Gear ID", name="gear_id"),
                    rx.input(placeholder="Normal module", name="m_n"),
                    rx.input(placeholder="Number of teeth", name="z"),
                    rx.input(placeholder="Pressure angle", name="alpha_n"),
                    rx.input(placeholder="Helix angle", name="beta"),
                    rx.button("Add to database", type="submit"),
                    gap="1rem",
                ),
                on_submit=State.set_gear_data,
            ),
            rx.form(
                rx.vstack(
                    rx.input(placeholder="Gear ID", name="gear_id"),
                    rx.button("Search", type="submit"),
                ),
                on_submit=State.get_gear_data,
            ),
            rx.text(
                f"id: {State.gear.gear_id}, m_n: {State.gear.m_n}, z: {State.gear.z}, alpha_n: {State.gear.alpha_n}, beta: {State.gear.beta}, d: {State.gear.d}, m_t: {State.gear.m_t}"
            ),
            style=style,
        ),
    )
