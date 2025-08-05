import os
from dotenv import load_dotenv
from utils.git_utils import clone_repo_branch
from agents.analyzer_agent import analyze_codebase
from agents.diff_agent import generate_diffs_for_repo, apply_patch
from pathlib import Path
from agents.commit_agent import check_refactor_signoff, commit_and_push_changes

# Ladda miljövariabler från .env-filen
load_dotenv()

# Hämta nycklar
openai_api_key = os.getenv("OPENAI_API_KEY")
github_token = os.getenv("GITHUB_TOKEN")

# Validera OpenAI-nyckeln
if not openai_api_key:
    print("❌ OPENAI_API_KEY saknas i .env-filen.")
    exit(1)

# Validera GitHub-token
if not github_token:
    print("❌ GITHUB_TOKEN saknas i .env-filen.")
    exit(1)

print("✅ Alla nycklar är korrekt laddade!")

# Testvärden (byt ut mot verkliga PR-data)
REPO_URL = "https://github.com/gulcoder/code-review-bot.git"
PR_BRANCH = "test-pr2"  # eller t.ex. "feature/ny-funktion"
CLONE_DIR = "cloned_repo"

# Klona PR-branchen
print(f"🔁 Klonar {PR_BRANCH} från {REPO_URL} ...")
clone_repo_branch(REPO_URL, PR_BRANCH)
print("✅ Kloning klar.")

# Kör analys på klonad repo
print("🔍 Kör kodanalys...")
analysis_results = analyze_codebase(CLONE_DIR)

# Visa en enkel summering av resultaten
print("\n=== Kodkomplexitet per fil ===")
for file_result in analysis_results["complexity"]:
    print(f"{file_result['file']}: {len(file_result['complexity'])} block analyserade")

print(f"\nMaintanability Index för hela kodbasen: {analysis_results['maintainability']:.2f}")

print("\nSäkerhetsproblem från Bandit:")
if analysis_results["security_issues"]:
    for issue in analysis_results["security_issues"]:
        print(f"- {issue['filename']} [{issue['severity']}] - {issue['issue_text']}")
else:
    print("Inga säkerhetsproblem hittades.")

print("🔁Genererar refaktoreringar och diffs...")
diffs = generate_diffs_for_repo(Path(CLONE_DIR))

if diffs:
    for file, diff_text in diffs.items():
        print(f"\n 📝Diff för {file}: \n{diff_text}\n")
        apply_patch(CLONE_DIR, file, diff_text)
else:
    print("✅Inga refaktoreringar föreslagna")


# Hårdkodade testvärden
REPO_OWNER = "gulcoder"
REPO_NAME = "code-review-bot"
PR_BRANCH ="test-pr2"
PR_NUMBER = 2  # <-- ändra vid riktig test!

if check_refactor_signoff(REPO_OWNER, REPO_NAME, PR_NUMBER, github_token):
    commit_and_push_changes(CLONE_DIR, PR_BRANCH)
else:
    print("🚫 Inget att committa.")


