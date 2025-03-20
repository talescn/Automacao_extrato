# Payment Processing Automation

This project is a financial process automation using Python, designed to facilitate payment processing in a specific system.

## Recent Updates

### [Today's Date]

- **Function `check_for_stop`:** Added to check if the 'q' key was pressed, allowing the script to be interrupted at any time.
- **Adjustment in `lancar_baixa`:** Included the use of the "delete" key to ensure the input field is cleared before entering new data.
- **Interruption Pop-up:** Implemented a pop-up that informs the user when no corresponding payment is found, improving user interaction with the system.

## Main Features

- **Automated Navigation:** Uses the `pyautogui` library to simulate clicks and keyboard inputs, automatically navigating through the financial system.
- **Value Capture:** Captures installment values directly from the system interface and processes them for verification.
- **PDF Data Extraction:** Uses `pdfplumber` to extract values from bank statements in PDF, facilitating comparison with installment values.
- **Payment Verification:** Compares captured values with extracted values from statements to verify if payments have been made.
- **Payment Processing:** If a corresponding payment is found, the automation processes the payment in the system.
- **Window Activation:** Uses `pygetwindow` to activate the necessary application window before starting the automation.

## Technologies Used

- **Python:** Main programming language for automation.
- **PyAutoGUI:** For GUI automation.
- **PyGetWindow:** For application window manipulation.
- **PDFPlumber:** For text extraction from PDFs.
- **Pytesseract:** For OCR, if necessary.
- **Pandas:** For data manipulation, if necessary.
- **Pyperclip:** For clipboard manipulation.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repository.git
   ```
2. Navigate to the project directory:
   ```bash
   cd your-repository
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the main script:
   ```bash
   python main.py
   ```
2. Follow the on-screen instructions to start the automation.

## Contribution

See [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.