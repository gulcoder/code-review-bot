import os
from radon.complexity import cc_visit
from radon.metrics import mi_visit
import bandit
from bandit.core.manager import BanditManager
from bandit.core import config as bandit_config

def analyze_codebase(repo_path):
    results = {
        "complexity": [],
        "maintainability": None,
        "security_issues": []
    }

    # Analysera komplexitet per fil
    for root, _, files in os.walk(repo_path):
        for file in files:
            if file.endswith(".py"):
                filepath = os.path.join(root, file)
                with open(filepath, "r") as f:
                    code = f.read()
                complexity = cc_visit(code)
                results["complexity"].append({
                    "file": filepath,
                    "complexity": complexity
                })

    # Maintainability index på hela kodbasen
    all_code = ""
    for root, _, files in os.walk(repo_path):
        for file in files:
            if file.endswith(".py"):
                with open(os.path.join(root, file), "r") as f:
                    all_code += f.read() + "\n"

    results["maintainability"] = mi_visit(all_code, True)


    # Bandit säkerhetsanalys
    conf = bandit_config.BanditConfig()
    manager = BanditManager(conf, "file")
    manager.discover_files([repo_path], True)
    manager.run_tests()
    results["security_issues"] = [
        {
            "filename": issue.fname,
            "issue_text": issue.text,
            "severity": issue.severity,
            "confidence": issue.confidence
        }
        for issue in manager.results
    ]

    return results
