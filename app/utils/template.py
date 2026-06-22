from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def render_template(
    template_name: str,
    **kwargs
):

    template_path = (
        BASE_DIR
        / "templates"
        / "emails"
        / template_name
    )

    html = template_path.read_text(
        encoding="utf-8"
    )

    for key, value in kwargs.items():

        html = html.replace(
            f"{{{{{key}}}}}",
            str(value)
        )

    return html