# Portfolio site (static)

Plain HTML, CSS and one build script. No framework, no build step needed to host it.

## Edit content
1. Open `content/site.json`. All text lives there.
2. In each case study, replace `"PASTE FINAL TEXT"` with paragraphs (one string per paragraph).
   A string starting with `## ` becomes a subheading (used for Whistleblower).
3. Set `"epigraph"` for the in-game quote, `"video"` for a YouTube ID (e.g. `dQw4w9WgXcQ`), or `"image"` for a path like `images/budget.jpg`.
4. Fill `linkedin` and `bluesky` at the top to show them in the header.
5. Run `python3 build.py` to regenerate the HTML pages. Commit the result.

## Deploy on GitHub Pages
1. Create a repo (e.g. `jt-portfolio`) and upload everything in this folder.
2. Settings > Pages > Deploy from branch > `main` / root.
3. Check the `github.io` address works before touching the domain.
4. When ready: add a file named `CNAME` containing `jtrimmerdesign.uk`, then point the domain's DNS at GitHub Pages (A records for the apex, per GitHub's docs) and remove the Wix redirect.

## Not included yet
Logo, case-study images and videos, ADD//ER and Flailiens pages, final About text.
