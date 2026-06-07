import re

file_path = 'Projektseminar_Infomanagement/Abschlusspresentation.md'
with open(file_path, 'r') as f:
    text = f.read()

# Fix the 5 slides already updated:
old_style = """<style scoped>
section {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  padding: 0 40px;
}
.ujm-img { max-width: 100% !important; max-height: 70vh !important; width: auto !important; height: auto !important; }
.ujm-label { font-weight: bold; font-size: 1.2em; color: #295A97; width: 33%; text-align: center; }
.ujm-container { width: 67%; text-align: center; }
</style>"""

new_style = """<style scoped>
section {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  padding: 0 40px;
}
.ujm-img { max-width: 100% !important; max-height: 70vh !important; width: auto !important; height: auto !important; }
.ujm-label { font-weight: bold; font-size: 0.9em; color: #295A97; width: 22%; text-align: left; }
.ujm-container { width: 78%; text-align: center; }
</style>"""

text = text.replace(old_style, new_style)

# Fix the 6th slide:
old_6th = """<style scoped>
section {
  justify-content: flex-start;
  align-items: stretch;
  padding: 5px;
}
table, th, td { border: none !important; }
.ujm-img { max-width: 100% !important; max-height: 55vh !important; width: auto !important; height: auto !important; }
.ujm-label { font-weight: bold; font-size: 0.7em; color: #295A97; }
</style>

<div style="display: flex; align-items: center; gap: 10px; width: 100%; height: 100%;">
  <div class="ujm-label" style="width: 33%; text-align: center; flex-shrink: 0;">Sachbearbeiter ULB</div>
  <div style="width: 67%; text-align: center;">
    <img src="Artefakte/Final/1_Ist_Prozess/1_b_User-Journey-Maps/UJM-Internationaler-Gast.png" class="ujm-img" />
  </div>
</div>
</div>"""

new_6th = new_style + """

<div class="ujm-label">Sachbearbeiter ULB</div>
<div class="ujm-container">
  <img src="Artefakte/Final/1_Ist_Prozess/1_b_User-Journey-Maps/UJM-Internationaler-Gast.png" class="ujm-img" />
</div>"""

text = text.replace(old_6th, new_6th)

with open(file_path, 'w') as f:
    f.write(text)

print("Done replacing.")
