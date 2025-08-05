import subprocess
import os
import shutil

def clone_repo_branch(repo_url, branch, clone_dir="cloned_repo"):
    """
    Klonar en specifik branch från ett repo med säker checkout.
    Om mappen clone_dir redan finns tas den bort först.
    """
    # Rensa gammal klon om den finns
    if os.path.exists(clone_dir):
        shutil.rmtree(clone_dir)

    print(f"🔁 Klonar branch '{branch}' från {repo_url} till {clone_dir} ...")
    subprocess.run(["git", "clone", "--branch", branch, repo_url, clone_dir], check=True)
    print("✅ Kloning klar.")
