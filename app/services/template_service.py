from pathlib import Path

from jinja2 import (
    Environment,
    FileSystemLoader,
    select_autoescape
)


BASE_DIR = Path(__file__).resolve().parent.parent

templates = Environment(
    loader=FileSystemLoader(
        BASE_DIR / "templates"
    ),
    autoescape=select_autoescape(
        ["html", "xml"]
    ),
)


class TemplateService:

    @staticmethod
    def render(
        template_name: str,
        context: dict | None = None,
    ) -> str:
        template = templates.get_template(
            template_name
        )

        return template.render(
            **(context or {})
        )
