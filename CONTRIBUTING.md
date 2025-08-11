# Contributing to Loadouts for Genshin Impact

Thank you for your interest in contributing to **Loadouts for Genshin Impact**! This project helps travelers manage their custom equipment loadouts and calculate statistics for characters, artifacts, and weapons.

## 🚀 Getting Started

### Prerequisites

Before contributing, ensure you have:
- **Python 3.12+**
- **Poetry** for dependency management
- **Git** for version control
- **Tesseract OCR** for screenshot processing functionality

### Development Setup

Follow the installation steps from the **"Installation > From Source"** section in README.md

## 📋 Development Guidelines

### Code Style Guidelines

- **Line length**: Maximum 100 characters
- **Type hints**: Required for all function signatures
- **Docstrings**: Use Google-style docstrings for public functions
- **Import organization**: Handled automatically by `ruff`
- **Naming conventions**: Follow Python PEP 8 standards

### Code Quality Standards

Before submitting any changes, ensure your code passes all quality checks:

```bash
tox -e cleaning
```

## 🔧 Project Structure

Understanding the codebase organization:

### Overview

```
gi-loadouts/
├── 📁 assets/          # Static assets and UI resources
├── 📁 gi_loadouts/     # Main application source code
└── 📁 test/            # Comprehensive test suite
```

### 📂 Assets Directory (`assets/`)

Contains all static resources including in-game assets, fonts, and UI assets:

```
assets/
├── 📁 data/            # OCR training data files
├── 📁 docs/            # Documentation images and screenshots
├── 📁 font/            # Font assets for UI
│   ├── 📁 icon/        # Font Icons
│   └── 📁 text/        # Font texts
├── 📁 icon/            # Application icons
└── 📁 imgs/            # In-game asset images
    ├── 📁 arti/        # Artifact set images
    ├── 📁 char/        # Character images
    ├── 📁 pmon/        # Chibi Paimon images
    ├── 📁 rare/        # Rarity background images
    ├── 📁 vson/        # Vision type images
    └── 📁 weap/        # Weapon images
```

### 📂 Source Code Directory (`gi_loadouts/`)

The main application source code organized into three core layers:

```
gi_loadouts/
├── 📁 data/            # Game data models and definitions
├── 📁 face/            # User interface components and their integration logic
└── 📁 type/            # Type definitions and data models
```

#### Game Data Layer (`gi_loadouts/data/`)

Contains all Genshin Impact game data definitions:

```
data/
├── 📁 arti/            # Artifact set models and definitions
├── 📁 char/            # Character models and definitions
└── 📁 weap/            # Weapon models and definitions by type
    ├── 📁 bows/        # Bow models and definitions
    ├── 📁 catalysts/   # Catalyst models and definitions
    ├── 📁 claymores/   # Claymore models and definitions
    ├── 📁 polearms/    # Polearm models and definitions
    └── 📁 swords/      # Sword models and definitions
```

#### User Interface Layer (`gi_loadouts/face/`)

Qt-based GUI components, dialogs and their integration logic:

```
face/
├── 📁 info/            # Information dialog components and integration logic
├── 📁 lcns/            # License dialog components and integration logic
├── 📁 otpt/            # Overall stats dialog components and integration logic
├── 📁 rsrc/            # Qt resource files (generated)
├── 📁 scan/            # OCR scanning interface and integration logic
└── 📁 wind/            # Main window interface and integration logic
```

#### Type System Layer (`gi_loadouts/type/`)

Pydantic models and type definitions:

```
type/
├── 📁 arti/            # Artifact type definitions
├── 📁 calc/            # Calculation type definitions
├── 📁 char/            # Character type definitions
├── 📁 file/            # File format type definitions
├── 📁 levl/            # Level type definitions
├── 📁 rank/            # Rank type definitions
├── 📁 rare/            # Rarity type definitions
├── 📁 stat/            # Statistics type definitions
├── 📁 vson/            # Vision type definitions
└── 📁 weap/            # Weapon type definitions
```

### 📂 Test Suite Directory (`test/`)

Comprehensive testing framework with 1420+ tests:

```
test/
├── 📁 data/            # Data layer tests
├── 📁 face/            # UI component tests
├── 📁 static/          # Test assets and mock data
└── 📁 type/            # Type definition tests
```

## 🎯 Types of Contributions

### 📊 Regular Game Content Updates

These contributions involve adding new game content when Genshin Impact releases new characters, weapons, and artifact sets

#### 1. Adding New Characters

1. **Download character assets** from Genshin Impact wiki `https://genshin-impact.fandom.com/wiki/<character_name>/Gallery` in `webp` format  
   Use lowercase letters for naming files and underscores for special characters
   - Character Icon → `assets/imgs/char/face/<character_name>.webp`
   - Multi-Wish → `assets/imgs/char/wish/<character_name>.webp`
   - Background → `assets/imgs/char/back/<character_name>.webp`
   - Banner → `assets/imgs/char/name/<character_name>.webp`

2. **Update resource files**
   - Add records in `.qrc` files
   - Generate Qt resource files:
     ```bash
     pyside6-rcc assets/back.qrc -o gi_loadouts/face/rsrc/char/back.py
     pyside6-rcc assets/face.qrc -o gi_loadouts/face/rsrc/char/face.py
     pyside6-rcc assets/name.qrc -o gi_loadouts/face/rsrc/char/name.py
     pyside6-rcc assets/wish.qrc -o gi_loadouts/face/rsrc/char/wish.py
     ```

3. **Add character data**
   - Add character name in ENUM `CharName` in `gi_loadouts/type/char/__init__.py`
   - Create character data file in `gi_loadouts/data/char/<character_name>.py`
   - Fetch character related details from Genshin Impact wiki page `https://genshin-impact.fandom.com/wiki/<character_name>`
   - Fetch character related base and ascension details from Genshin Impact wiki page [Level Scaling](https://genshin-impact.fandom.com/wiki/Character/Level_Scaling)
   - Add character class in `__charmaps__` in `gi_loadouts/data/char/__init__.py`
   - Add tests in `test/data/test_char.py`

#### 2. Adding New Weapons

1. **Download weapon assets** from Genshin Impact wiki `https://genshin-impact.fandom.com/wiki/<weapon_name>` in `webp` format  
Use mnemonic codes (4-letter abbreviations) for naming files:
   - Base version → `assets/imgs/weap/<weapon_type>/<mnemonic_code>_a.webp`
   - 2nd Ascension → `assets/imgs/weap/<weapon_type>/<mnemonic_code>_b.webp`

2. **Update resource files**
   - Add records in `.qrc` files
   - Generate Qt resource files:
     ```bash
     pyside6-rcc assets/weap.qrc -o gi_loadouts/face/rsrc/weap/__init__.py
     ```

3. **Add weapon data**
   - Create weapon data file in `gi_loadouts/data/weap/<weapon_type>/<mnemonic_code>.py`  
   **Note**: `refi_stat` only needs to be added for weapons that directly apply measurable buffs without conditions  
   **Examples**:
     - Aqua Simulacra: Increases HP of the character equipping the weapon
     - Cashflow Supervision: Increased ATK of the character equipping the weapon
     - Redhorn Stonethresher: Increases DEF of the character equipping the weapon
     - Skyward Spine: Increase CRIT Rate of the character equipping the weapon
     - Absolution: Increases CRIT Damage of the character equipping the weapon
   - Fetch weapon details from Genshin Impact wiki page `https://genshin-impact.fandom.com/wiki/<weapon_name>`
   - Deduce the `tier` of the weapon by comparing the `Quality` of the weapon and `Value` of `Base ATK` at `Level 1/20` from Genshin Impact wiki page `https://genshin-impact.fandom.com/wiki/<weapon_name>` with [Rarity and Value](https://genshin-impact.fandom.com/wiki/Weapon/Level_Scaling)
   - Add weapon class in `<weapon_type>Dict` in `gi_loadouts/data/weap/<weapon_type>/__init__.py`
   - Add tests in `test/data/weap/test_<weapon_type>.py` and `test/face/wind/weap/kind/test_<weapon_type>.py`

#### 3. Adding New Artifact Sets

1. **Download artifact assets** from Genshin Impact wiki `https://genshin-impact.fandom.com/wiki/<artifact_set_name>` in `webp` format  
Use mnemonic codes (4-letter abbreviations) for naming files:
    - Flower of Life → `assets/imgs/arti/<mnemonic_code>/fwol.webp`
    - Plume of Death → `assets/imgs/arti/<mnemonic_code>/pmod.webp`
    - Sands of Eon → `assets/imgs/arti/<mnemonic_code>/sdoe.webp`
    - Goblet of Eonothem → `assets/imgs/arti/<mnemonic_code>/gboe.webp`
    - Circlet of Logos → `assets/imgs/arti/<mnemonic_code>/ccol.webp`
2. **Update resource files**
   - Add records in `.qrc` files
   - Generate Qt resource files:
     ```bash
     pyside6-rcc assets/arti.qrc -o gi_loadouts/face/rsrc/arti/__init__.py
     ```
3. **Add artifact set data**
   - Create artifact set data file in `gi_loadouts/data/arti/<mnemonic_code>.py`  
   **Note**: `__pairdata__` and `__quaddata__` only need to be added for artifact sets that directly apply measurable buffs without conditions. (To date, no artifact has such buffs, so `__quaddata__` has not been used.)  
   **Examples**:
     - Tiny Miracle: All Elemental RES increased by 20%
   - Fetch artifact set related details from Genshin Impact wiki page `https://genshin-impact.fandom.com/wiki/<artifact_set_name>`
   - Add artifact set information in `__artilist__` in `gi_loadouts/data/arti/__init__.py`
   - Add tests in `test/data/test_arti.py`

### 🛠️ Application Improvements

These contributions involve enhancing the application's functionality and user experience:

#### 1. UI/UX Enhancements

1. **Use Qt6 Designer** when making any change in UI/UX to generate `.ui` files following the existing patterns
2. **Convert `.ui` files into `.py` files** with the objective of using application designs as Python classes:
    ```bash
    pyside6-uic assets/<file_name>.ui -o gi_loadouts/face/<file_name>/<file_name>.py
    ```
3. **Add necessary changes in the codebase** for integrating the UI/UX changes
4. **Add comprehensive tests** for `100%` code coverage

#### 2. OCR and Image Processing

1. **Add necessary changes in the codebase** for improving text recognition accuracy
2. **Test with various screenshot formats** and qualities
3. **Handle edge cases and error conditions**
4. **Add comprehensive tests** for `100%` code coverage

#### 3. Performance and Logic Improvements

1. **Optimize calculation algorithms**
2. **Improve data loading and caching**
3. **Enhance error handling and validation**
4. **Refactor code for better maintainability**
5. **Add comprehensive tests for new logic**

#### 4. Feature Development

1. **Research existing codebase** patterns
2. **Design feature architecture** following project conventions
3. **Implement with proper type hints** and documentation
4. **Add comprehensive tests**
5. **Update user documentation** if needed

## 🐛 Bug Reports and Feature Requests

### Reporting Bugs

- **Environment**: OS, Python version, Poetry version, Tesseract version
- **Steps to reproduce**: Detailed reproduction steps
- **Expected behavior**: What should happen
- **Actual behavior**: What actually happens
- **Screenshots or logs**: Visual evidence or error logs
- **Additional context**: Any other context about the problem

### Feature Requests

- **Current problem**: Describe the problem you're trying to solve
- **Proposed feature**: Describe the feature or improvement you would like to see added
- **Benefits of this feature**: Explain why this feature would be beneficial for users or developers
- **Usage examples**: Provide examples or use cases to show how this feature might be used
- **Screenshots or mockups (optional)**: Add any images or mockups to explain your idea
- **Additional context**: Add any other context or information that may be relevant for the feature request

## 🧪 Testing

### Running Tests

```bash
tox
```

### Writing Tests

- Write tests for all new functionality
- Include edge cases and error conditions
- Use proper mocking for external dependencies
- Follow existing test patterns and structures
- Ensure tests are deterministic and isolated

## 📝 Commit Guidelines

We follow conventional commit standards:

- `feat:` New features
- `fix:` Bug fixes
- `docs:` Documentation changes
- `style:` Code style/formatting changes
- `refactor:` Code refactoring without functional changes
- `test:` Adding or modifying tests
- `chore:` Maintenance tasks (dependencies, build, etc.)
- `perf:` Performance improvements

### Example Commits

```bash
feat: add Nahida character data and assets
fix: improve artifact stat recognition accuracy
docs: update installation instructions for Windows
test: add comprehensive tests for catalyst weapons
```

## 🚀 Pull Request Process

### Before Submitting

1. **Create a new branch** with standard naming convention:
   ```bash
   git checkout -b feat/your-feature-name
   git checkout -b fix/your-fix-name
   git checkout -b docs/your-docs-name
   git checkout -b test/your-test-name
   ```

2. **Make your changes** as per requirements
3. **Add or update tests** for your changes ensuring 100% code coverage
4. **Update documentation** if needed

### Submitting Your Pull Request

1. **Push your branch**:
   ```bash
   git push origin feat/your-feature-name
   git push origin fix/your-fix-name
   git push origin docs/your-docs-name
   git push origin test/your-test-name
   ```

2. **Create Pull Request** on GitHub with:
   - Clear, descriptive title
   - Detailed description of changes
   - Reference to related issues
   - Screenshots (if applicable)
   - Testing instructions

3. **Address review feedback** promptly
4. **Ensure CI checks pass** before requesting final review

### Pull Request Template

```markdown
## Summary
Brief description of what this PR does.

## Changes Made
- List of specific changes
- Include both code and asset changes

## Testing
- [ ] New tests added for new functionality
- [ ] Manual testing completed

## Screenshots (if applicable)
Include screenshots

## Related Issues
Fixes #123, Closes #456
```

## 🤝 Community Guidelines

- **Be respectful** and inclusive in all interactions
- **Help newcomers** get started with contributing
- **Share knowledge** and best practices
- **Provide and receive constructive feedback** during code reviews

## 🏆 Recognition

Contributors are recognized in:
- Release notes
- GitHub contributor graphs
- Special mentions for outstanding contributions

## 📞 Getting Help

- **Documentation**: Check README.md, CONTRIBUTING.md and existing code
- **Issues**: Search existing issues before creating new ones
- **Maintainers**: Contact project maintainers for complex questions

## 🙏 Thank you for contributing to Loadouts for Genshin Impact!

Your contributions help travelers worldwide optimize their character builds and enhance their gaming experience. Every contribution, whether it's a bug fix, new feature, or documentation improvement, makes a meaningful difference to the community.

## 📄 License

By contributing to GI Loadouts, you agree that your contributions will be licensed under the **GPL-3.0-or-later** license.

## 📄 Disclaimer

All rights to Genshin Impact assets used in this project are reserved by miHoYo Ltd. and Cognosphere Pte., Ltd.

Other properties belong to their respective owners.
