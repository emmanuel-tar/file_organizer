# File Organizer by Usage Frequency

**File Organizer** is a Python-based utility designed to help users organize files and folders on their Windows systems based on access frequency. The tool categorizes files into "Frequently Used" and "Least Used" folders based on the last access time, making it easier to declutter directories and access frequently used files quickly.

## Features

- **Access-Based Organization**: Automatically organizes files based on their last access time.
- **Custom Threshold Days**: Users can specify the number of days to determine frequency.
- **Graphical User Interface (GUI)**: Simple and intuitive interface built with `tkinter`.
- **Logging**: Logs all activities and errors to a file for easy tracking and debugging.
- **Undo-Friendly**: Keeps the folder structure intact for manual corrections if needed.

## Technologies Used

- **Python**: Core logic and functionality.
- **tkinter**: For the graphical user interface.
- **os** and **shutil**: For file system operations.
- **logging**: To track operations and errors.

## Installation

Follow these steps to set up and use the project:

### Prerequisites
- Python 3.7 or higher installed on your system.
- Basic understanding of running Python scripts.

### Clone the Repository
```bash
git clone https://github.com/emmanuel-tar/file_organizer.git
cd file_organizer
```

### Install Dependencies
No additional dependencies are required since the project uses standard Python libraries. However, you can create a virtual environment for better isolation:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Run the Application
```bash
python file_organizer.py
```

This will launch the GUI, allowing you to organize your files easily.

## How to Use

1. **Launch the GUI**: Run the `file_organizer.py` script.
2. **Select Directory**: Use the "Browse" button to choose the folder you want to organize.
3. **Set Threshold Days**: Enter the number of days to define frequently used files (default is 30).
4. **Organize**: Click the "Organize" button to categorize files into `Frequently_Used` and `Least_Used` folders.

## Logs
All actions and errors are logged to `file_organizer.log`. Check this file for detailed operation records and troubleshooting.

## Screenshots

**Main GUI Window**

![File Organizer GUI](Screenshot.png)

## Contributions
Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m "Description of changes"`.
4. Push to the branch: `git push origin feature-name`.
5. Open a pull request.

## Future Enhancements

- Add a preview mode to display the files that will be moved.
- Support for excluding specific file types or folders.
- Real-time monitoring of file access.
- Cross-platform support for macOS and Linux.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact

**Author**: Emmanuel Tar  
**GitHub**: [emmanuel-tar](https://github.com/emmanuel-tar)  
**Email**: [YourEmail@example.com](mailto:YourEmail@example.com)
