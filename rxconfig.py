import reflex as rx
import os

config = rx.Config(
    app_name="cogscal",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
    db_url=os.getenv("DATABASE_URL", "sqlite:///reflex.db"),
)
