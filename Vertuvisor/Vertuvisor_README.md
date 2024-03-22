# Vertuvisor

## Overview

This project aims to scrape course information from two UNC websites to gather data on classes and departments. The script scrapes HTML content from the websites, parses it, and generates CSV files containing information about classes and their prerequisites.

## Requirements

- Python 3.x
- Libraries: requests, BeautifulSoup, pandas

## Installation

1. Clone the repository:

```bash
git clone https://github.com/ConorJones05/ConorJonesProjects.git
```

2. Install the required libraries:

```bash
pip install requests
pip install beautifulsoup4
pip install pandas
```

## Usage

1. Run the Python script `classes_site_scraper.py`.
2. The script will scrape the specified UNC websites for course information.
3. CSV files containing class details and prerequisites will be generated in the specified output directory.

## Configuration

- Modify the `url_list` and `output_directory` variables in the script to scrape different UNC websites and specify the output directory for CSV files.
- Customize the script as needed to extract additional information from the websites.

## Example

```python
python scraper.py
```

## Contributors

- [Conor Jones](https://github.com/COnorJones05)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to adjust it according to your project's specific details and requirements!
