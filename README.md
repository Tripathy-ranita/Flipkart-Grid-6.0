# Flipkart-Grid-6.0
<h2>Introduction</h2>

<h2>Explanation PPT</h2>
<p>Here is the link to the explanation ppt. <a href="">Click here</a></p>
</br>

<h2>Video Solution</h2>
<p>Here is the link to the video solution. <a href="">Click here</a></p>
</br>

<h2>Tesseract OCR</h2>

To download and set up Tesseract OCR, follow these steps:

**Step 1: Download Tesseract OCR**

1. Go to the official Tesseract GitHub page: [Tesseract at GitHub](https://github.com/tesseract-ocr/tesseract).

2. For Windows users, you can directly download the installer from [UB Mannheim Tesseract Repository](https://github.com/UB-Mannheim/tesseract/wiki):

   - Choose the latest version of the Windows installer (usually it will be an `.exe` file).
   - Download the file and run the installer.

**Step 2: Install Python Libraries**

To use Tesseract with Python, you will need to install the pytesseract library:

```
pip install pytesseract
```

**Step 3: Configure Tesseract in Python (Windows)**
</br></br>
Once Tesseract is installed, you will need to point Python to the `tesseract.exe` file. Here’s how to do that:

1. **Find the Tesseract Executable**:
    - By default, Tesseract is installed in: `C:\Program Files\Tesseract-OCR\tesseract.exe`.
      
2. **Configure the Path in Python**: Add this line to your Python code to configure the path to the Tesseract executable:

```
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

**Step 4 : Test the Setup**
</br>

You can use the following code to test if Tesseract is working:

```
from PIL import Image
import pytesseract

# Set the path to the Tesseract executable (for Windows)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Open an image
image = Image.open('sample_image.png')

# Perform OCR on the image
text = pytesseract.image_to_string(image)

print("Detected Text:")
print(text)
```

**Step 5 : Add Tesseract to PATH (Optional)**

You can add the Tesseract folder to your system's PATH environment variable so that you don't need to specify the path to `tesseract.exe` in your Python script every time.

1. **Open System Properties**:
   - Go to **Control Panel > System and Security > System > Advanced System Settings**.

2. **Environment Variables**:
   - Click on **Environment Variables**.

3. **Edit PATH**:
   - Under **System variables**, find the **Path** variable, select it, and click **Edit**.

4. **Add New Path**:
   - Click **New** and add the path to the Tesseract executable (e.g., `C:\Program Files\Tesseract-OCR\`).

After this step, you will no longer need to explicitly define the path to the Tesseract executable in your Python code.
</br>

<h2>Installation</h2>
For expiration_date_verification.py ( to verify the expiry date of a packaged item )
</br>


1. Run the following commands for the installation of the requireds libraries:

```
pip install pillow pytesseract opencv-python numpy

[Note: If error is met while installing, then run the install command separately.
For example, pip install opencv-python, pip install numpy, pip install pillow, pip install pytesseract]
```

2. Run the Python file using the following command:

```
  python expiration_date_verification.py
```

</br>
For fresh_produce_inspection.py ( to inspect the quality of fresh produce )
</br>
1. Run the following commands for the installation of the requireds libraries:

```
pip install opencv-python numpy

[Note: If error is met while installing, then run the install command separately.
For example, pip install opencv-python, pip install numpy]
```

2. Run the Python file using the following command:

```
  python fresh_produce_inspection.py
```
</br>

<h2>License</h2>
<p>This project is released under the MIT License. See the <a href="https://github.com/Silent18Killer/Face-Emotion-Recognition/blob/main/LICENSE">LICENSE</a> file for more information.</p>
</br>

<h2>Programming Languages Used</h2>
<div align="center">
  <img aligh="center" src="https://skillicons.dev/icons?i=python,opencv" alt="Languages and Tools">
</div>
</br>

<h2>Developers</h2>
<ul>
  <li><a href="https://github.com/Silent18Killer">Silent18Killer</a></li>
  <li><a href="https://github.com/deepcodess">deepcodess</a></li>
  <li><a href="https://github.com/RanitaTripathy">Tripathy-ranita</a></li>
</ul>
