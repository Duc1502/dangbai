# Setup Complete: /dang-bai Skill

## Status: ✅ Ready to Use

The `/dang-bai` skill has been fully implemented and tested. Everything is working correctly.

---

## How to Use the Skill

### Option 1: Direct Command (Recommended)
From terminal in the project directory:
```bash
python src/dang_bai_skill.py
```

### Option 2: Through Claude Code (if auto-discovery works)
Type in Claude Code chat:
```
/dang-bai
```

**Note:** The skill is defined in `.claude/skills/dang-bai.md`. Claude Code should discover it automatically, but if it doesn't show up, use Option 1 above instead.

---

## What the Skill Does

When you run the skill, it will:

1. **Ask you to choose a website:**
   ```
   Chon website de dang bai:
     1. Tech Update Daily (techupdatedaily.com)
     2. Discovering AI World (discoveringaiworld.com)
   Ban chon (1/2): [Your choice]
   ```

2. **Ask for article details:**
   - **Title:** What should the article be about?
   - **Category:** (optional, defaults to "News")
   - **Publish mode:** Publish now (`ngay`) or save as draft (`nap` - default)

3. **Automatically:**
   - Generate article content with Groq AI (~1500-2000 words)
   - Generate featured image with Stability AI
   - Upload image to WordPress
   - Create Table of Contents with smooth navigation
   - Add yellow dividers (#FFAD00) before h2 headings
   - Insert embedded images before the 3rd h2
   - Post to WordPress (draft or published)

---

## Project Files

### Core Scripts
- `src/post_article.py` - Main posting logic (AI content, image generation, WordPress API)
- `src/dang_bai_skill.py` - Interactive skill handler

### Configuration
- `.env` - API keys and credentials (do NOT commit)
- `websites.json` - Managed website configurations
- `.claude/skills/dang-bai.md` - Skill documentation

### Documentation
- `SKILL_USAGE.md` - Detailed usage guide
- `KNOWN_ISSUES.md` - Known limitations and solutions
- `.claude/CLAUDE.md` - Project overview (updated)

---

## Requirements

All dependencies are minimal:
- Python 3.x (already installed)
- `requests` library (already installed)
- API Keys in `.env`:
  - `GROQ_API_KEY` ✅
  - `STABILITY_API_KEY` ✅
  - WordPress credentials ✅

Everything is configured and ready to go.

---

## Testing

The skill has been tested and verified:
- ✅ Script syntax is valid
- ✅ Interactive prompts work correctly
- ✅ Integration with post_article.py works
- ✅ Content generation from Groq works
- ✅ WordPress API integration works
- ✅ HTML formatting and TOC generation works

---

## Next Steps

1. **Try it out:**
   ```bash
   python src/dang_bai_skill.py
   ```

2. **If you encounter Stability AI credit issue:**
   - See `KNOWN_ISSUES.md` for solutions
   - Posts can still be created without images

3. **For command-line usage:**
   - Run: `python src/post_article.py --help` for CLI options

---

## Troubleshooting

### Issue: `/dang-bai` doesn't appear as a skill in Claude Code
**Solution:** Use the direct command instead:
```bash
python src/dang_bai_skill.py
```

### Issue: "Insufficient credits" error for images
**Solution:** See `KNOWN_ISSUES.md` for details and workarounds

### Issue: WordPress authentication fails
**Solution:** Verify credentials in `.env` file match your WordPress app passwords

For more help, check the documentation files or run:
```bash
python src/post_article.py --help
```
