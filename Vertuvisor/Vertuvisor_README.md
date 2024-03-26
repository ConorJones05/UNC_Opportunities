# Vertuvisor

Vertuvisor is a tool designed to assist students at UNC (University of North Carolina) in planning their coursework effectively. By analyzing students' majors and strengths, Vertuvisor generates personalized four-year plans that align with their academic goals and interests.

## Features

- **Major Scraping**: Vertuvisor scrapes major and minor information from the UNC catalog website, categorizing majors into Arts and Sciences based on degree type (B.A. or B.S.).
  
- **Course Scraping**: The tool extracts course details, including course codes and prerequisites, from the UNC catalog.

- **Data Organization**: Vertuvisor organizes course information into CSV files, with each file containing courses for a specific major. This facilitates easy access and analysis of course data.

- **PDF Text Extraction**: Additionally, Vertuvisor includes a function to extract text from PDF files, which can be useful for gathering additional information related to courses or majors.

- **CSV File Combination**: Vertuvisor provides a function to combine multiple CSV files into a single DataFrame. This is useful for aggregating data from different sources or organizing data for analysis.

## Usage

To use Vertuvisor, follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Run the provided Python scripts to scrape major and course information, organize the data, and generate four-year plans.

Example usage:

```bash
python scrape_majors.py
python scrape_courses.py
python organize_data.py
python combine_csv_files.py
```

## Dependencies

Vertuvisor relies on the following Python libraries:

- requests
- BeautifulSoup
- pandas
- PyPDF2

Ensure these dependencies are installed before running the scripts.

## Contributing

Contributions to Vertuvisor are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and ensure the code passes any existing tests.
4. Submit a pull request with a clear description of your changes.

## License

[MIT License](LICENSE)
```

Feel free to adjust the content as needed to fit your project's specific requirements. Let me know if you need further assistance!
