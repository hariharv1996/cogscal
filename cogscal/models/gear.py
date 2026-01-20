import reflex as rx
from sqlmodel import Field
import math


class Gear(rx.Model, table=True):
    gear_id: int | None = Field(primary_key=True, default=None)
    m_n: float
    z: int
    alpha_n: float
    beta: float
    m_t: float | None = None
    d: float | None = None

    def calculate(self) -> None:
        self.m_t = self.m_n / math.cos(math.radians(self.beta))
        self.d = self.m_t * self.z
