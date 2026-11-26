"""Copy the optional bird add-on into a CAMAT site and load it from its HTML."""

from pathlib import Path
import shutil


MARKER = "<!-- CAMAT_BIRD_EASTER_EGG -->"


def install(source: Path, site: Path) -> None:
    site.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source / "bird.css", site / "bird.css")
    shutil.copy2(source / "bird.js", site / "bird.js")

    stylesheet = '<link rel="stylesheet" href="bird.css">'
    script = '<script src="bird.js" defer></script>'
    for page in site.rglob("*.html"):
        text = page.read_text(encoding="utf-8")
        if MARKER in text:
            continue
        if "</head>" not in text or "</body>" not in text:
            raise RuntimeError(f"Cannot find HTML insertion points in {page}")
        text = text.replace("</head>", f"{MARKER}\n{stylesheet}\n</head>", 1)
        text = text.replace("</body>", f"{script}\n</body>", 1)
        page.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    install(Path(__file__).parent, Path("_site"))
