import re

file_path = 'Projektseminar_Infomanagement/Abschlusspresentation.md'
with open(file_path, 'r') as f:
    text = f.read()

old_style = """<style scoped>
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

new_style = """<style scoped>
section {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  padding: 0 40px;
}
.ujm-img { max-width: 100% !important; max-height: 85vh !important; width: auto !important; height: auto !important; }
.ujm-label { font-weight: bold; font-size: 0.9em; color: #295A97; min-width: 25%; width: 25%; text-align: left; white-space: nowrap; }
.ujm-container { width: 75%; text-align: center; }
</style>"""

text = text.replace(old_style, new_style)

with open(file_path, 'w') as f:
    f.write(text)

print("Done replacing.")
