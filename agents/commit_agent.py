import os
import subprocess
import requests

def check_refactor_signoff(repo_owner, repo_name, pr_number, github_token):
    """Kollar om /refactor sign-off finns i PR-kommentarerna på GitHub."""
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/issues/{pr_number}/comments"
    headers = {
        "Authorization": f"token {github_token}",
        "Accept": "application/vnd.github+json"
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"❌ Misslyckades att hämta kommentarer: {response.status_code}")
        return False

    comments = response.json()
    for comment in comments:
        if "/refactor sign-off" in comment["body"].lower():
            print("✅ Refactor sign-off hittades i kommentarerna.")
            return True

    print("ℹ️ Ingen refactor sign-off hittades.")
    return False

def git_has_changes():
    """Kollar om det finns ändringar att committa."""
    result = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
    return bool(result.stdout.strip())

def commit_fixup(target_commit_hash):
    """Gör en fixup-commit mot angiven commit hash."""
    if not git_has_changes():
        print("🚫 Inget att committa, hoppar över fixup-commit.")
        return False
    try:
        subprocess.run(["git", "commit", "--fixup", target_commit_hash], check=True)
        print("✅ Fixup-commit skapad.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Fel vid git commit --fixup: {e}")
        return False

def push_branch(branch):
    """Pushar den aktuella branchen till origin."""
    try:
        subprocess.run(["git", "push", "origin", branch], check=True)
        print("✅ Push lyckades.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Fel vid git push: {e}")

def handle_refactor_signoff(clone_dir, pr_branch, target_commit_hash):
    """Samordnar fixup-commit och push om det finns ändringar."""
    os.chdir(clone_dir)
    added_files = subprocess.run(["git", "add", "."], check=True)

    committed = commit_fixup(target_commit_hash)
    if committed:
        push_branch(pr_branch)
    else:
        print("🚫 Hoppar push eftersom inga ändringar fanns.")

def commit_and_push_changes(clone_dir, target_branch):
    """Samordnar fixup-commit och push om det finns ändringar.

    Hittar senaste commit, gör fixup och pushar."""
    os.chdir(clone_dir)

    # Hitta senaste commit att göra fixup mot
    last_commit = subprocess.check_output(["git", "rev-parse", "HEAD"]).decode().strip()

    # Lägg till ändringar
    subprocess.run(["git", "add", "."], check=True)

    # Skapa fixup commit
    try:
        subprocess.run(["git", "commit", "--fixup", last_commit], check=True)
        print("✅ Fixup commit skapad.")
    except subprocess.CalledProcessError as e:
        print(f"🚫 Inget att committa, hoppade fixup: {e}")
        return

    # Push till origin
    try:
        subprocess.run(["git", "push", "origin", target_branch], check=True)
        print("✅ Push lyckades.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Fel vid git push: {e}")

