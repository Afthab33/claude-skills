# Claude Skills

A collection of [Claude Code](https://claude.com/claude-code) skills for everyday productivity — writing, planning, research, and workflow automation. Drop them into `~/.claude/skills/` and Claude will pick them up automatically when a task matches.

## What's a Skill?

A skill is a folder containing a `SKILL.md` file (plus optional scripts, templates, or reference docs) that teaches Claude a specific workflow. Once installed, Claude invokes the skill on its own when your request matches its description — no slash command needed.

```
skill-name/
├── SKILL.md          # required — instructions + YAML frontmatter
├── scripts/           # optional — executable helpers
└── references/         # optional — docs loaded on demand
```

## Installation

Clone the repo and symlink the skills you want into your personal Claude directory:

```bash
git clone https://github.com/Afthab33/claude-skills.git
cd claude-skills

# Symlink a single skill
ln -s "$(pwd)/skill-name" ~/.claude/skills/skill-name

# Or symlink everything
for dir in */; do
  name="${dir%/}"
  ln -s "$(pwd)/$name" ~/.claude/skills/"$name"
done
```

Symlinking (rather than copying) means `git pull` keeps your local skills up to date automatically.

## Skills

| Skill | Description |
|---|---|
| _add rows as you add skills_ | |

## Contributing

PRs are welcome — new skills, fixes, or improvements to existing ones.

1. Fork the repo and create a branch: `git checkout -b add-skill-name`
2. Add your skill under a new folder with a `SKILL.md` inside (see [Anthropic's skill authoring guidance](https://docs.claude.com) for format details)
3. Keep descriptions specific — a clear, narrow description helps Claude trigger the skill only when it's actually relevant
4. Test the skill locally before opening a PR
5. Open a PR with a short explanation of what the skill does and when it should trigger

### Guidelines for new skills

- One skill, one clear purpose — avoid bundling unrelated workflows into a single skill
- Keep `SKILL.md` instructions direct and specific; examples work better than abstract rules
- If the skill needs scripts or reference files, keep them in subfolders (`scripts/`, `references/`) rather than inline in `SKILL.md`
- No secrets, API keys, or credentials in any skill file

## License

[MIT](LICENSE) — use, modify, and share freely.
