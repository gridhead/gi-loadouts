# Contributing to GI Loadouts

Thank you for your interest in contributing to GI Loadouts! This guide will help you get started with the development process.

## Table of Contents

- [Development Setup](#development-setup)
- [Code Quality](#code-quality)
- [Testing](#testing)
- [Submitting Changes](#submitting-changes)
- [Code Style](#code-style)
- [Issue Reporting](#issue-reporting)

## Development Setup

### Prerequisites

- Python 3.12 or 3.13
- Poetry (for dependency management)
- Git

### Setting up the Development Environment

1. **Clone the repository:**
   ```bash
   git clone https://github.com/gridhead/gi-loadouts.git
   cd gi-loadouts
   ```

2. **Install Poetry (if not already installed):**
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

3. **Install dependencies:**
   ```bash
   poetry install
   ```

4. **Install pre-commit hooks (recommended):**
   ```bash
   poetry run pre-commit install
   ```

### Running the Application

```bash
poetry run gi-loadouts
```

## Code Quality

We use several tools to maintain code quality:

### Pre-commit Hooks

Pre-commit hooks are automatically installed and will run on every commit:

- **Ruff**: Linting and code formatting
- **MyPy**: Static type checking
- **Bandit**: Security scanning
- **Various checks**: Trailing whitespace, file formatting, etc.

To run pre-commit hooks manually:
```bash
poetry run pre-commit run --all-files
```

### Manual Quality Checks

```bash
# Run linting
poetry run ruff check gi_loadouts/

# Run formatting
poetry run ruff format gi_loadouts/

# Run type checking
poetry run mypy gi_loadouts/

# Run security scanning
poetry run bandit -r gi_loadouts/
```

## Testing

### Running Tests

```bash
# Run all tests
poetry run pytest

# Run tests with coverage
poetry run pytest --cov=gi_loadouts --cov-report=html

# Run tests in parallel
poetry run pytest -n auto

# Run specific test file
poetry run pytest test/test_main.py
```

### Using Tox

For comprehensive testing across different Python versions:

```bash
# Install tox
poetry run pip install tox

# Run tests for all environments
tox

# Run tests for specific environment
tox -e py312
```

## Submitting Changes

### Before Submitting

1. **Check that your code passes all quality checks:**
   ```bash
   poetry run ruff check gi_loadouts/
   poetry run mypy gi_loadouts/
   poetry run pytest
   ```

2. **Update tests if needed**
3. **Update documentation if needed**

### Pull Request Process

1. **Create a feature branch:**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes and commit:**
   ```bash
   git add .
   git commit -m "feat: add your feature description"
   ```

3. **Push your branch:**
   ```bash
   git push origin feature/your-feature-name
   ```

4. **Create a Pull Request** on GitHub

### Commit Message Convention

We follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

- `feat:` for new features
- `fix:` for bug fixes
- `docs:` for documentation changes
- `style:` for formatting changes
- `refactor:` for code refactoring
- `test:` for adding or modifying tests
- `chore:` for maintenance tasks

## Code Style

### Python Code Style

- **Line length**: Maximum 100 characters
- **Type hints**: Required for all function signatures
- **Docstrings**: Use Google-style docstrings for all public functions
- **Import organization**: Use `ruff` for automatic import sorting

### Example Function

```python
def process_artifact_data(artifact_name: str, stats: dict[str, float]) -> ArtifactData:
    """
    Process artifact data and return structured artifact object.

    Args:
        artifact_name: The name of the artifact
        stats: Dictionary mapping stat names to values

    Returns:
        Processed artifact data object

    Raises:
        ValueError: If artifact_name is empty or stats are invalid
    """
    if not artifact_name.strip():
        raise ValueError("Artifact name cannot be empty")
    
    return ArtifactData(name=artifact_name, stats=stats)
```

## Issue Reporting

### Bug Reports

When reporting bugs, please include:

- **Environment details**: OS, Python version, Poetry version
- **Steps to reproduce**: Detailed steps to reproduce the issue
- **Expected behavior**: What you expected to happen
- **Actual behavior**: What actually happened
- **Screenshots/logs**: If applicable

### Feature Requests

When requesting features, please include:

- **Use case**: Why this feature would be useful
- **Proposed solution**: How you think it should work
- **Alternatives**: Other solutions you've considered

## Development Guidelines

### Adding New Characters

1. Create character data file in `gi_loadouts/data/char/`
2. Follow existing character file patterns
3. Add appropriate type hints
4. Update any related enums or constants

### Adding New Weapons

1. Create weapon data file in appropriate category
2. Follow existing weapon file patterns
3. Ensure all stats are properly typed
4. Add tests for new weapon data

### UI Changes

1. Use Qt Designer files when possible
2. Follow existing UI patterns and styles
3. Ensure accessibility considerations
4. Test on different screen sizes

## Getting Help

- **Documentation**: Check the README.md and existing code
- **Issues**: Search existing issues before creating new ones
- **Discussions**: Use GitHub Discussions for questions
- **Contact**: Reach out to maintainers for complex questions

## License

By contributing to GI Loadouts, you agree that your contributions will be licensed under the GPL-3.0-or-later license.

---

Thank you for contributing to GI Loadouts! 🎮