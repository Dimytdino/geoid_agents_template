#!/usr/bin/env python3
"""Generer une documentation HTML autoportante a partir d'une fiche Markdown.

Outillage GeoID : convertit une fiche d'outil redigee en Markdown (modele
`templates/fiche-outil.template.md`) en une page HTML unique, autoportante
(CSS inline), avec navigation laterale (table des matieres auto-generee).

Usage :
    python3 scripts/generer_doc_html.py --source fiche.md --output fiche.html
    python3 scripts/generer_doc_html.py --source fiche.md --output fiche.html \\
        --diagram schema.svg --title "Mon outil"

Arguments :
    --source   (requis) chemin du fichier Markdown source.
    --output   (requis) chemin du fichier HTML a produire.
    --css      feuille de style a inliner (defaut : templates/style-doc-tse.css,
               relatif a la racine du depot).
    --diagram  (optionnel) fichier .svg a injecter a la place du marqueur
               `<!-- WORKFLOW_DIAGRAM -->`. Sans cet argument, le marqueur est
               retire proprement.
    --title    (optionnel) titre de la page ; a defaut, derive du premier
               titre de niveau 1 (H1) du Markdown.

Prerequis : pip install markdown   (seule dependance tierce ; reste = stdlib).

Le script est idempotent : reexecutable sans effet de bord (ecrase le HTML
existant, ne cree aucun fichier intermediaire).
"""

import argparse
import html as _html
import pathlib
import re
import sys

try:
    import markdown
except ImportError:
    print(
        "Erreur : la bibliotheque 'markdown' est introuvable.\n"
        "Installer avec : pip install markdown",
        file=sys.stderr,
    )
    sys.exit(1)

# Racine du depot (ce script vit dans scripts/), pour resoudre le CSS par defaut.
RACINE = pathlib.Path(__file__).resolve().parents[1]
CSS_DEFAUT = RACINE / "templates" / "style-doc-tse.css"

MARQUEUR_DIAGRAMME = "<!-- WORKFLOW_DIAGRAM -->"

# CSS du wrapper de diagramme : injecte par le script, independamment du SVG
# fourni par le projet (le diagramme n'est plus code en dur ici).
DIAGRAM_CSS = """
  <style>
    .diagram-wrapper {
      margin: 1.5rem 0 2rem;
      overflow-x: auto;
    }
    .diagram-wrapper svg {
      max-width: 100%;
      height: auto;
      display: block;
      border-radius: 8px;
    }
  </style>
"""


def deriver_titre(texte_md):
    """Retourne le premier titre H1 du Markdown, ou None s'il n'y en a pas."""
    for ligne in texte_md.splitlines():
        m = re.match(r"^#\s+(.+?)\s*$", ligne)
        if m:
            return m.group(1).strip()
    return None


def construire_arguments(argv=None):
    p = argparse.ArgumentParser(
        description="Genere une doc HTML autoportante depuis une fiche Markdown.",
    )
    p.add_argument("--source", required=True, help="Fichier Markdown source.")
    p.add_argument("--output", required=True, help="Fichier HTML a produire.")
    p.add_argument("--css", default=str(CSS_DEFAUT),
                   help="Feuille de style a inliner (defaut : templates/style-doc-tse.css).")
    p.add_argument("--diagram", default=None,
                   help="Fichier .svg a injecter a la place du marqueur diagramme.")
    p.add_argument("--title", default=None,
                   help="Titre de la page (sinon derive du premier H1).")
    return p.parse_args(argv)


def generer_html(source_text, css_content, diagram_svg=None, titre=None):
    """Convertit le Markdown en page HTML complete (chaine).

    source_text  : contenu Markdown.
    css_content  : contenu de la feuille de style (inline dans <style>).
    diagram_svg  : contenu SVG a injecter, ou None (marqueur retire).
    titre        : titre de page ; derive du premier H1 si None.
    """
    # POLITIQUE DE CONFIANCE : source_text et diagram_svg sont supposés provenir
    # de dépôts contrôlés (fiches internes TSE/GéoID). Le HTML brut Markdown et
    # le SVG sont injectés tels quels — ne pas exposer ce script à du contenu
    # non maîtrisé sans sanitisation préalable (bleach, nh3…).
    md = markdown.Markdown(
        extensions=["tables", "toc", "fenced_code"],
        extension_configs={
            "toc": {
                "title": "Table des matieres",
                "toc_depth": "2-3",
            }
        },
    )
    html_body = md.convert(source_text)
    toc_fragment = md.toc

    if diagram_svg is not None:
        bloc = f'<div class="diagram-wrapper">\n{diagram_svg}\n</div>'
        html_body = html_body.replace(MARQUEUR_DIAGRAMME, bloc)
    else:
        # Pas de diagramme : retirer proprement le marqueur (et le paragraphe
        # vide que markdown peut avoir cree autour).
        html_body = html_body.replace(f"<p>{MARQUEUR_DIAGRAMME}</p>", "")
        html_body = html_body.replace(MARQUEUR_DIAGRAMME, "")

    if titre is None:
        titre = deriver_titre(source_text) or "Documentation GeoID"

    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{_html.escape(titre)}</title>
  <style>{css_content}</style>
{DIAGRAM_CSS}
</head>
<body>
  <div class="page-wrapper">
    <nav id="toc" aria-label="Table des matieres">
      <h2>Table des matieres</h2>
      {toc_fragment}
    </nav>
    <main class="content">
      <div class="content-inner">
        {html_body}
      </div>
    </main>
  </div>
</body>
</html>
"""


def main(argv=None):
    args = construire_arguments(argv)

    source = pathlib.Path(args.source)
    output = pathlib.Path(args.output)
    css = pathlib.Path(args.css)

    if not source.exists():
        print(f"Erreur : fichier source introuvable : {source}", file=sys.stderr)
        return 1
    if not css.exists():
        print(f"Erreur : feuille de style introuvable : {css}", file=sys.stderr)
        return 1

    diagram_svg = None
    if args.diagram is not None:
        diagram_path = pathlib.Path(args.diagram)
        if not diagram_path.exists():
            print(f"Erreur : diagramme introuvable : {diagram_path}", file=sys.stderr)
            return 1
        diagram_svg = diagram_path.read_text(encoding="utf-8")

    source_text = source.read_text(encoding="utf-8")
    css_content = css.read_text(encoding="utf-8")

    html_full = generer_html(
        source_text, css_content, diagram_svg=diagram_svg, titre=args.title
    )

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(html_full, encoding="utf-8")
    print(f"Fichier genere : {output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
