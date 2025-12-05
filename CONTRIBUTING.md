# Contributing to Loadouts for Genshin Impact

Thank you for your interest in contributing to **Loadouts for Genshin 
Impact**! This project helps travelers manage their custom equipment and 
calculate statistics for characters, artifacts, and weapons.

## 🚀 Getting started

### Prerequisites

Before contributing, ensure you have:

- **Python 3.12** or greater version

- **UV** for dependency management

- **Git** for version control

- **Tesseract OCR** for screenshot processing

### Development setup

Follow the installation steps from the **"Installation > From Source"**
section in
[README.md](https://github.com/gridhead/gi-loadouts/blob/main/README.md)
file.

## 📋 Development guidelines

### Code Styles

- **Line length**: Maximum 100 characters per line

- **Type hints**: Required for all function signatures

- **Inline documentation**: Use Google-style docstrings for public functions

- **Import organization**: Handled automatically by `ruff`

- **Naming conventions**: Follow Python PEP 8 standards

- **Code formatting**: Use `ruff format` for consistent style

### Code quality

Before submitting any changes, ensure your code passes all quality checks:

```bash
tox -e cleaning
```

## 🔧 Project structure

Understanding the codebase organization:

### Overview

```bash
gi-loadouts/
├── 📁 assets/          # Static assets
├── 📁 gi_loadouts/     # Source code
└── 📁 test/            # Test suite
```

### Static assets (`assets/`)

Contains resources including static assets like images and icons and UI 
resources like fonts and specifications:

```bash
assets/
├── 📁 data/            # OCR model
├── 📁 docs/            # Documentation screenshots
├── 📁 font/            # Font resources
│   ├── 📁 icon/        # Icon fonts
│   └── 📁 text/        # Text fonts
├── 📁 icon/            # Application icon
└── 📁 imgs/            # In-game resources
    ├── 📁 arti/        # Artifact resources
    ├── 📁 char/        # Character resources
    ├── 📁 pmon/        # Paimon resources
    ├── 📁 rare/        # Rarity resources
    ├── 📁 vson/        # Vision resources
    └── 📁 weap/        # Weapon resources
```

### Source code (`gi_loadouts/`)

The source code is organized into three layers:

```bash
gi_loadouts/
├── 📁 data/            # Data definitions
├── 📁 face/            # Application logic
└── 📁 type/            # Type definitions
```

#### Data definitions (`gi_loadouts/data/`)

Contains all game data definitions:

```bash
data/
├── 📁 arti/            # Artifact definitions
├── 📁 char/            # Character definitions
└── 📁 weap/            # Weapon types
    ├── 📁 bows/        # Bow definitions
    ├── 📁 catalysts/   # Catalyst definitions
    ├── 📁 claymores/   # Claymore definitions
    ├── 📁 polearms/    # Polearm definitions
    └── 📁 swords/      # Sword definitions
```

#### Application logic (`gi_loadouts/face/`)

Contains GUI components and integration logic:

```bash
face/
├── 📁 info/            # Information resources
├── 📁 lcns/            # License resources
├── 📁 otpt/            # Overall resources
├── 📁 rsrc/            # Generated resources
├── 📁 scan/            # Scanning resources
└── 📁 wind/            # Primary resources
```

#### Type definitions (`gi_loadouts/type/`)

Contains Pydantic type models:

```bash
type/
├── 📁 arti/            # Artifact definitions
├── 📁 calc/            # Calculation definitions
├── 📁 char/            # Character definitions
├── 📁 file/            # Specification definitions
├── 📁 levl/            # Level definitions
├── 📁 rank/            # Rank definitions
├── 📁 rare/            # Rarity definitions
├── 📁 stat/            # Statistics definitions
├── 📁 vson/            # Vision definitions
└── 📁 weap/            # Weapon definitions
```

### Test suite (`test/`)

Contains comprehensive test suite:

```bash
test/
 ├── 📁 data/            # Data tests
 ├── 📁 face/            # Component tests
 ├── 📁 static/          # Required assets
 └── 📁 type/            # Type tests
```

## 📦 Content updates

Involves providing content updates while keeping up with the Genshin Impact 
releases of characters, weapons and artifacts

### Adding characters

1. Download static assets from
   [Genshin Impact Wiki](https://genshin-impact.fandom.com/wiki/Genshin_Impact_Wiki) 
   in the `WEBP` format and place them in the appropriate directories
   - Icon → `assets/imgs/char/face/<char_name>.webp`
   - Multi-Wish → `assets/imgs/char/wish/<char_name>.webp`
   - Background → `assets/imgs/char/back/<char_name>.webp`
   - Banner → `assets/imgs/char/name/<char_name>.webp`

2. Ensure lowercase for alphabetical characters and underscores for special 
   characters while naming the static assets

3. Update resource binaries in accordance with the newly added static resources
   and generate them in the `QRC` format
   ```bash
   (venv) $ nano assets/back.qrc
   (venv) $ nano assets/face.qrc
   (venv) $ nano assets/name.qrc
   (venv) $ nano assets/wish.qrc
   (venv) $ pyside6-rcc assets/back.qrc -o gi_loadouts/face/rsrc/char/back.py
   (venv) $ pyside6-rcc assets/face.qrc -o gi_loadouts/face/rsrc/char/face.py
   (venv) $ pyside6-rcc assets/name.qrc -o gi_loadouts/face/rsrc/char/name.py
   (venv) $ pyside6-rcc assets/wish.qrc -o gi_loadouts/face/rsrc/char/wish.py
   ```

4. Include statistical information using the following steps
   - Add character name in ENUM `CharName` in 
     `gi_loadouts/type/char/__init__.py`
   - Create character data in the
     `gi_loadouts/data/char/<char_name>.py` file
   - Fetch character related statistical details from the corresponding
     [Genshin Impact Wiki](https://genshin-impact.fandom.com/wiki/Genshin_Impact_Wiki)
     statistical page
   - Include the fetched statistical details in the
     `gi_loadouts/data/char/<char_name>.py` file
   - Fetch character related ascension details from the corresponding
     [Genshin Impact Wiki](https://genshin-impact.fandom.com/wiki/Genshin_Impact_Wiki)
     ascension page
   - Include the fetched ascension details in the
     `gi_loadouts/data/char/<char_name>.py` file
   - Include the character class in the `__charmaps__` in the
     `gi_loadouts/data/char/__init__.py` file
   - Introduce the character tests in the
     `test/data/test_<char_name>.py` file

### Adding weapons

1. Download static assets from
   [Genshin Impact Wiki](https://genshin-impact.fandom.com/wiki/Genshin_Impact_Wiki)
   in the `WEBP` format and place them in the appropriate directories
   - Base → `assets/imgs/weap/<type>/<weap_code>_a.webp`
   - Ascended → `assets/imgs/weap/<type>/<weap_code>_b.webp`

2. Ensure lowercase for alphabetical characters and underscores for special
   characters while naming the static assets

3. Update resource binaries in accordance with the newly added static resources
   and generate them in the `QRC` format
   ```bash
   (venv) $ nano assets/weap.qrc
   (venv) $ pyside6-rcc assets/weap.qrc -o gi_loadouts/face/rsrc/weap/__init__.py
   ```

4. Include statistical information using the following steps
   - Create weapon data in the
     `gi_loadouts/data/<type>/<weap_name>.py` file
   - In `refi_stat`, include statistical changes from weapon refinements that
     are applicable without external conditions
   - In `refi_list`, include information changes from weapon refinements that
     are applicable or not applicable
   - Fetch weapon related statistical details from the corresponding
     [Genshin Impact Wiki](https://genshin-impact.fandom.com/wiki/Genshin_Impact_Wiki)
     statistical page
   - Include the fetched statistical details in the
     `gi_loadouts/data/<type>/<weap_name>.py`
   - Deduce the `tier` of the weapon by comparing the `Quality` of the weapon
     and `Value` of `Base ATK` at `Level 1/20` from the corresponding
     [Genshin Impact Wiki](https://genshin-impact.fandom.com/wiki/Weapon/Level_Scaling)
     ascension page
   - Include the weapon class in the `<type>Dict` in the
     `gi_loadouts/data/weap/<type>/__init__.py` file
   - Introduce the weapon tests in the
     `test/face/wind/weap/kind/test_<type>.py` file

### Adding artifacts

1. Download static assets from
   [Genshin Impact Wiki](https://genshin-impact.fandom.com/wiki/Genshin_Impact_Wiki)
   in the `WEBP` format and place them in the appropriate directories
   - Flower of Life → `assets/imgs/arti/<arti_code>/fwol.webp`
   - Plume of Death → `assets/imgs/arti/<arti_code>/pmod.webp`
   - Sands of Eon → `assets/imgs/arti/<arti_code>/sdoe.webp`
   - Goblet of Eonothem → `assets/imgs/arti/<arti_code>/gboe.webp`
   - Circlet of Logos → `assets/imgs/arti/<arti_code>/ccol.webp`

2. Ensure lowercase for alphabetical characters and underscores for special
   characters while naming the static assets

3. Update resource binaries in accordance with the newly added static resources
   and generate them in the `QRC` format
   ```bash
   (venv) $ nano assets/arti.qrc
   (venv) $ pyside6-rcc assets/arti.qrc -o gi_loadouts/face/rsrc/arti/__init__.py
   ```

4. Include statistical information using the following steps.
   - Create artifact data in the
     `gi_loadouts/data/arti/<arti_code>.py` file
   - In `__pairdata__` and `__quaddata__`, include statistical changes from
     artifact sets that are applicable without external conditions
   - In `__pairtext__` and `__quadtext__`, include information changes from
     artifact sets that are applicable or not applicable
   - Fetch artifact related statistical details from the corresponding
     [Genshin Impact Wiki](https://genshin-impact.fandom.com/wiki/Genshin_Impact_Wiki)
     statistical page
   - Include the fetched statistical details in the
     `gi_loadouts/data/arti/<arti_code>.py` file
   - Include the artifact class in the `__artilist__` variable in the
     `gi_loadouts/data/arti/__init__.py` file
   - Ensure that the information associated to the pieces, rarities,
     configurations and filenames are properly populated
   - Introduce the artifact tests in the
     `test/data/test_arti.py` file

## 🛠️ Application improvements

These contributions involve enhancing the application's functionality and 
user experience.

### 1. UI/UX enhancements

1. Use Qt6 Designer to make changes to the `UI` files while following the 
   existing patterns

2. Convert the `UI` files into Python files to include the updated changes in
   the application
   ```bash
   (venv) $ pyside6-uic assets/<filename>.ui -o gi_loadouts/face/<module>/<filename>.py
   ```

3. Change the application logic accordingly to play well with the updated 
   component changes

4. Ensure that the updated changes come with updated tests to maintain the
   100% coverage

### 2. Image processing

1. Add necessary changes in the codebase for improving the accuracy of the 
   recognition operations

2. Check with various screenshots of different types and different qualities
   before progressing

3. Handle potentially appearing edge cases and error conditions to the best of
   your capabilities

4. Ensure that the updated changes come with updated tests to maintain the
   100% coverage

### 3. Performance improvements

1. Find means to introduce calculation optimizations or logic changes in the
   application codebase

2. Check with various conditions to understand if the meaningful improvements
   are introduced

3. Handle potentially appearing edge cases and error conditions to the best of
   your capabilities

4. Ensure that the updated changes come with updated tests to maintain the
   100% coverage

### 4. Feature development

1. Design meaningful advancements and feature architecture in accordance to the
   existing patterns

2. Ensure that the introduced changes are accompanied by the associated typing
   and documentation

3. Handle potentially appearing edge cases and error conditions to the best of
   your capabilities

4. Ensure that the updated changes come with updated tests to maintain the
   100% coverage

## 🐛 Reporting bugs

While informing the maintainers of unintended observations, please include the 
following information

- **Environment information** like the operating system, Python version, UV
  version, Tesseract version etc

- **Reproducible steps** to help the maintainers encounter the same unintended
  observations that you made

- **Expected behaviour** to help the maintainers understand the intended
  outcome from the actions

- **Encountered behaviour** to help the maintainers understand the unintended
  outcome from the actions

- **Contextual information** like screenshots and tracebacks can immensely help
  accelerate the debugging process

- **Additional information** that you might be able to share can help further
  improve the application codebase

## 🚀 Requesting features

While asking the maintainers of required advancements, please include the 
following information

- Describe the current problem that you are intending to solve with the
  advancement introduction

- Describe the proposed feature that would help address the aforementioned 
  problem statement

- Explain the potential benefits of the features towards experienced by users 
  and/or maintainers

- Provide the usage examples to further elucidate on the usecases of the said
  feature addition.

## 🧪 Testing codebase

### Execution

The project incorporates an extensive codebase test suite managing both quality
and functionality

- Use the following command the run the test suite.
  ```bash
  (venv) $ tox
  ```

- The quality checks can be executed using the following command.
  ```bash
  (venv) $ tox -e cleaning
  ```

- The functionality tests can be executed using the following command.
  ```bash
  (venv) $ tox -e py<python-vers>
  ```

- The functionality tests can be sped up using multiple processors.
  ```bash
  (venv) $ tox -e py<python-vers>-dist
  ```

### Writing

While maintaining the test suite, please consider the following points for 
uniform experience

- Ensure that introduced functionalities are accompanied by the tests covering
  various conditions

- Make best efforts possible to cater to as many edge cases and error states 
  as possible

- Utilize proper mocking to ensure deterministic behaviour from tests using
  external dependencies

- Follow existing testing structures to conveniently write tests that are 
  functionally isolated

## 🤝 Contributing guidelines

While contributing to the project, please observe the following guidelines for
friendly community

- Be respectful and inclusive to contributors regardless of their background
  and/or experience

- Assist newcomers as and when possible to get started with contributing to the
  project community

- Share problem learnings and best practices to encourage upskilling inside the
  project community

- Provide constructive feedback in issue tickets and pull requests and in turn,
  receive them

## 📄 Contribution license

By contributing to Loadouts for Genshin Impact, you agree that your
contributions will be licensed under the **GPL-3.0-or-later** license.

## 📄 Community disclaimer

All rights to Genshin Impact assets used in this project are reserved by 
miHoYo Ltd. and Cognosphere Pte., Ltd.

Other properties belong to their respective owners.
