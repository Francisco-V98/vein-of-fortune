#!/usr/bin/env python3
"""Verifica que los mensajes de commit sigan la convención del proyecto.

Formato:  tipo(ámbito): descripción        (ver studio/docs/15-flujo-de-trabajo-y-calidad.md)

Uso:
    python3 tools/ci/check_commits.py origin/main..HEAD
    python3 tools/ci/check_commits.py --subject "feat(market): F2-04 modelo de precio"

El ID de la tarea es obligatorio (ERROR). Los commits de fusión («Merge …») y de reversión
(«Revert "…"») se aceptan tal cual. Solo se revisa el rango del PR, no la historia de main.
"""
import re
import subprocess
import sys

TYPES = ("feat", "fix", "refactor", "perf", "docs", "test", "chore", "ci", "build", "style", "revert", "studio")
SUBJECT_RE = re.compile(r"^(%s)(\([a-z0-9_-]+\))?!?: \S.*$" % "|".join(TYPES))
TASK_RE = re.compile(r"\bF\d-\d{2,3}\b")
MAX_SUBJECT = 100


def check_subject(subject):
    """Devuelve una lista de problemas (vacía si el asunto es válido)."""
    if subject.startswith("Merge ") or subject.startswith('Revert "'):
        return []
    problems = []
    if not SUBJECT_RE.match(subject):
        problems.append("no sigue 'tipo(ámbito): descripción' con tipo en {%s}" % ", ".join(TYPES))
    if len(subject) > MAX_SUBJECT:
        problems.append("el asunto tiene %d caracteres (máximo %d)" % (len(subject), MAX_SUBJECT))
    if subject.endswith("."):
        problems.append("el asunto no debe terminar en punto")
    if not TASK_RE.search(subject):
        problems.append("no menciona una tarea (por ejemplo F2-04)")
    return problems


def commits_in(rev_range):
    out = subprocess.run(["git", "log", "--format=%h%x09%s", rev_range], capture_output=True, text=True, check=True).stdout
    return [line.split("\t", 1) for line in out.splitlines() if line.strip()]


def main(argv):
    if len(argv) == 3 and argv[1] == "--subject":
        problems = check_subject(argv[2])
        for p in problems:
            print("ERROR:", p)
        return 1 if problems else 0
    if len(argv) != 2:
        print(__doc__)
        return 2
    bad = 0
    for sha, subject in commits_in(argv[1]):
        problems = check_subject(subject)
        if problems:
            bad += 1
            print("ERROR %s «%s»" % (sha, subject))
            for p in problems:
                print("   -", p)
    if bad:
        print("\n%d commit(s) no cumplen la convención." % bad)
        return 1
    print("Mensajes de commit OK.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
