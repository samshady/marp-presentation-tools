# Skill Deployment

After updating any skill in `skills/`, re-sync to global:

```bash
cp skills/marp-presentation-pipeline/SKILL.md ~/.kilo/skills/marp-presentation-pipeline/SKILL.md
cp skills/marp-presentation-creator/SKILL.md ~/.kilo/skills/marp-presentation-creator/SKILL.md
cp skills/marp-presentation-quality/SKILL.md ~/.kilo/skills/marp-presentation-quality/SKILL.md
cp skills/marp-presentation-designer/SKILL.md ~/.kilo/skills/marp-presentation-designer/SKILL.md
```

All 4 skills must be present in `~/.kilo/skills/` for Kilo to discover them from any directory.
