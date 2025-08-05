# Autonom Kodgranskare & Refaktor-Bot för GitHub Repo

## Översikt
Detta projekt är en autonom bot som triggas vid nya Pull Requests i ett GitHub-repo. Botens huvuduppgifter är att:

- Klona PR-branchen automatiskt
- Analysera koden för stil, komplexitet och säkerhetsproblem
- Lämna inline-kommentarer med konkreta förslag och förändrings-patchar
- Utföra automatiska refaktoreringar när författaren godkänner via en `/refactor sign-off`-kommentar

Projektet använder OpenAI:s nya Responses API för att orkestrera flera agenter som hanterar statisk analys, diff-generering och commit-logik.

## Funktioner
- Automatisk kloning och hantering av PR-branchar
- Stilstils- och säkerhetsanalys med hjälp av Python-bibliotek (t.ex. `radon`, `bandit`)
- Kommentarer i GitHub-PR via GitHub API med patchar i Unified Diff-format
- Automatisk fixup-commit och push vid godkännande från PR-författaren

## Teknologier
- Python 3.12+
- GitPython för hantering av Git-repositorier
- OpenAI Responses API för AI-driven kodanalys
- `python-dotenv` för hantering av miljövariabler
- `requests` och `httpx` för HTTP-anrop till GitHub och OpenAI
- Säkerhets- och kodkomplexitetsverktyg: `bandit`, `radon`

## Kom igång

### Förutsättningar
- GitHub Personal Access Token med repo-access
- OpenAI API-nyckel
- Python 3.12+ och virtuellt miljö (venv)

### Installera beroenden
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Miljövariabler i .env
```bash
OPENAI_API_KEY=din_openai_nyckel
GITHUB_TOKEN=din_github_token
```

Projektet är under aktiv utveckling. Feedback och bidrag är varmt välkomna!
© 2025 Gulbaran
