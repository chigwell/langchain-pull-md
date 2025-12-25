[![PyPI version](https://badge.fury.io/py/langchain-pull-md.svg?1)](https://badge.fury.io/py/langchain-pull-md)
[![License: Apache 2.0](https://img.shields.io/badge/license-Apache%202.0-green?style=flat-square)](https://opensource.org/licenses/Apache-2.0)
[![Downloads](https://static.pepy.tech/badge/langchain-pull-md?1)](https://pepy.tech/project/langchain-pull-md)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-blue)](https://www.linkedin.com/in/eugene-evstafev-716669181/)

# langchain-pull-md

> **Deprecated:** This package is deprecated because the `pull.md` service was switched off on 25/12/2025.

**`langchain-pull-md`** is a Python package that extends [LangChain](https://github.com/langchain/langchain) by providing a markdown loader from URLs using the `pull.md` service. This package enables the fetching of fully rendered Markdown content, which is especially useful for web pages that utilize JavaScript frameworks such as React, Angular, and Vue.js.

---

## Key Features

- Convert URLs to Markdown directly, supporting pages rendered with JavaScript frameworks.
- Efficiently fetch markdown without local server resource consumption using the external `pull.md` service.

---

## Installation

To install the package, use:

```bash
pip install langchain-pull-md
```

---

## Usage

Here’s how you can use the `PullMdLoader` from `langchain-pull-md`:

### **Basic Example**

```python
from langchain_pull_md import PullMdLoader

# Initialize using a URL
loader = PullMdLoader(url="http://example.com")

documents = loader.load()
print(documents)
```

---

## Parameters

### `PullMdLoader` Constructor

| Parameter | Type  | Default | Description                            |
|-----------|-------|---------|----------------------------------------|
| `url`     | `str` | None    | The URL to fetch and convert to Markdown. |

---

## Testing

To run the tests:

1. Clone the repository:
   ```bash
   git clone https://github.com/chigwell/langchain-pull-md
   cd langchain-pull-md
   ```

2. Install development dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the tests:
   ```bash
   pytest tests/test_markdown_loader.py
   ```

---

## Contributing

Contributions are welcome! If you have ideas for new features or spot a bug, feel free to:
- Open an issue on [GitHub](https://github.com/chigwell/langchain-pull-md/issues).
- Submit a pull request.

---

## License

This project is licensed under the Apache 2.0 License. See the [LICENSE](https://github.com/chigwell/langchain-pull-md/blob/main/LICENSE) file for details.

---

## Acknowledgements

- [LangChain](https://github.com/langchain/langchain) for providing the base integration framework.
- [pull.md](https://pull.md/) for enabling efficient Markdown extraction from dynamic web pages.
