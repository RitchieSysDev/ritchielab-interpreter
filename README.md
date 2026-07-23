# RitchieLab Interpreter

This repository contains an interactive medical interpretation web app.

## Deployment targets

The site is designed to work as a static site on both GitHub Pages and Cloudflare Pages.

### GitHub Pages
1. Push this repository to GitHub.
2. Open the repository Settings > Pages.
3. Choose GitHub Actions as the source.
4. The workflow in [.github/workflows/deploy-pages.yml](.github/workflows/deploy-pages.yml) will publish the site automatically.

### Cloudflare Pages
1. Create a new Cloudflare Pages project.
2. Connect this GitHub repository.
3. Set the build command to empty or leave it blank.
4. Set the output directory to the repository root.
5. Deploy.

## Files
- [index.html](index.html) - Main website entry point
- [.github/workflows/deploy-pages.yml](.github/workflows/deploy-pages.yml) - GitHub Pages deployment workflow

## Notes
- The app uses inline CSS and JavaScript, so no build step is required.
- If you want a custom domain later, add it in GitHub Pages or Cloudflare Pages settings.
