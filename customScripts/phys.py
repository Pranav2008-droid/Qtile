import subprocess
from pathlib import Path

def launch_pdf_with_rofi(qtile):
    pdf_dir = Path.home() / "Documents/school/irodov"
    pdf_files = list(pdf_dir.rglob("*.pdf"))

    if not pdf_files:
        return

    pdf_paths = [str(p) for p in pdf_files]

    rofi = subprocess.Popen(
        ['rofi', '-dmenu','-matching','fuzzy', '-p', 'Choose topic:'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        text=True
    )
    stdout, _ = rofi.communicate('\n'.join(pdf_paths))

    selected_pdf = stdout.strip()
    if selected_pdf:
        subprocess.Popen(['zathura', selected_pdf])
