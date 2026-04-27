# 🧙‍♂️ Python Text Art Generator: Harry Potter Edition

### 💻 Technical Portfolio | Language: Python
This project is an image-to-ASCII transformation engine that maps high-contrast pixel data into a character-based visual representation. It demonstrates the use of **Binary Classification** of pixel intensity and **Terminal Data Rendering**.

---

## 🚀 Overview
The script takes a high-contrast Black and White image (like the Harry Potter silhouette) and processes it as a binary data stream. By treating pixel values as either "Dark" or "Light," the program renders the image in the command line using the string `"HARRYPOTTER"` as the "pixel" medium.

---

## 🛠️ Technical Implementation
1. **Data Extraction:** Using the `PIL` (Pillow) library, the script extracts raw RGB data into a flattened list.
2. **Thresholding (Data Normalization):**
   * The script iterates through the pixel list.
   * Logic: If a pixel's RGB value is below $(151, 151, 151)$, it is mapped to `0` (Black).
   * Otherwise, it is mapped to `15` (White).
3. **Sequential Mapping:** The script uses the Modulo operator (`c % 11`) to cycle through the letters of "HARRYPOTTER" for every bit rendered.
4. **Terminal Styling:** Utilizes `Colorama` to apply Fore.BLACK and Fore.WHITE styles to the output for maximum contrast in CMD.



---

## 📂 Project Structure
```text
/Text-Art-Generator
│
├── /assets              # Original images (e.g., hp1.3.jpg)
├── /src                 # Main Python source code
├── /screenshot_output   # Reference images of the final result
└── README.md



📖 How to Run
1. Prerequisites
Before running the code, you need the Pillow and Colorama libraries. Install them by running:

Bash
pip install Pillow colorama
2. Prepare the Image
Make sure your image (e.g., hp1.3.jpg) is placed inside the assets/ folder.

3. Execution via CMD
Open your Command Prompt (CMD).

Navigate to the project's source directory:

Bash
cd "C:\Path\To\Your\Text-Art-Generator\src"
Execute the Python script:

Bash
python text_generator.py
4. Viewing the Output
Important: To see the full art clearly, hold Ctrl and Scroll Down with your mouse wheel to zoom out. This shrinks the characters so they form a sharp image, similar to the one in the screenshot_output/ folder.