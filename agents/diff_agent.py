import difflib
from pathlib import Path
import subprocess

def generate_diff(original_code: str, refactored_code: str, filename: str) -> str:
    original_lines = original_code.splitlines(keepends=True)
    refactored_lines = refactored_code.splitlines(keepends=True)
    diff = difflib.unified_diff(
        original_lines,
        refactored_lines,
        fromfile=f"a/{filename}",
        tofile=f"b/{filename}",
        lineterm=""
    )
    return "".join(diff)

def simple_refactor(code: str) -> str:
    # Här kan du lägga in enkel refaktorering, t.ex. ta bort extra whitespace
    # eller fixa importordning etc.
    # För demo, vi bara strippar trailing whitespace
    lines = [line.rstrip() + "\n" for line in code.splitlines()]
    return "".join(lines)

def generate_refactor_diff_for_file(filepath: Path) -> str:
    original_code = filepath.read_text()
    refactored_code = simple_refactor(original_code)
    if original_code == refactored_code:
        return ""  # Ingen förändring
    return generate_diff(original_code, refactored_code, filepath.name)

def generate_diffs_for_repo(repo_path: Path) -> dict:
    diffs = {}
    for filepath in repo_path.rglob("*.py"):
        diff = generate_refactor_diff_for_file(filepath)
        if diff:
            diffs[str(filepath.relative_to(repo_path))] = diff
    return diffs

def apply_patch(clone_dir: str, file_path: str, diff_text: str):
    """
    Applicera en unified diff till en fil i clone_dir.
    """
    full_path = Path(clone_dir) / file_path

    # Skriv diff-texten till en temporär patchfil
    patch_file = Path(clone_dir) / "temp.patch"
    with open(patch_file, "w") as f:
        f.write(diff_text)

    try:
        # Kör git apply för att applicera patchen i clone_dir
        subprocess.run(
            ["git", "apply", "--whitespace=fix", str(patch_file)],
            cwd=clone_dir,
            check=True,
            capture_output=True,
            text=True,
        )
        print(f"✅ Patch applicerad på {file_path}")
    except subprocess.CalledProcessError as e:
        print(f"❌ Misslyckades applicera patch på {file_path}: {e.stderr}")

    # Ta bort temporär patchfil
    patch_file.unlink()