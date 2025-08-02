# bckground-removl-api

🌟 Background Removal ML Model Setup Guide
Heyy, this is how you run our background removal model and use it in Firebase!

🔧 1. Setup
Download the project folder background_removal_app/

Make sure you have Python installed (3.8+)

Open terminal and do:

bash
Copy
Edit
cd background_removal_app
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app:app --reload
🌐 2. Test the API in Browser
After running, open browser and go to:
👉 http://127.0.0.1:8000/docs

Upload any image and test it.

You’ll get a base64 image in response.

🚀 3. Use it in Firebase App
Send a POST request to http://127.0.0.1:8000/remove-background

Content-Type: multipart/form-data

Field name: file

The response will be like:

json
Copy
Edit
{
  "status": "success",
  "image_base64": "<base64 string>"
}
You can decode and show this image in frontend.
