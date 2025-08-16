YouTube Video Summarizer Agent 🎥📝
A Streamlit web app that uses the Agno Framework with Groq LLM to automatically summarize YouTube videos.
Simply enter a YouTube video URL, and the app will attempt to fetch captions and generate a concise, human-readable summary.

🚀 Features
Automatic YouTube Transcript Retrieval — Fetches video captions (if available).
AI-Powered Summarization — Uses the Groq Qwen 32B model to generate a clean summary.
User-Friendly Interface — Built with Streamlit for a quick and interactive experience.
Environment-Based API Key Handling — Keeps your API key safe via .env file.
Error Handling — Detects when captions are not available.

📂 Project Structure
bash
Copy
Edit
.
├── app.py              # Main Streamlit application
├── .env                # Environment variables (contains GROQ_API_KEY)
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
🛠️ Installation
Clone the repository

bash
Copy
Edit
git clone https://github.com/your-username/youtube-video-summarizer-agent.git
cd youtube-video-summarizer-agent
Create a virtual environment

bash
Copy
Edit
python -m venv myvenv
source myvenv/bin/activate     # On Mac/Linux
myvenv\Scripts\activate        # On Windows
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Set up environment variables
Create a .env file in the project root:

ini
Copy
Edit
GROQ_API_KEY=your_api_key_here
📜 Usage
Run the Streamlit app

bash
Copy
Edit
streamlit run app.py
Open in Browser
The app will open at:


🧠 How It Works
Step 1: User enters a YouTube URL.

Step 2: YouTubeTools tries to fetch the transcript using youtube-transcript-api.

Step 3: Transcript is passed to the Groq Qwen 32B model.

Step 4: AI generates a concise, human-friendly summary.

Step 5: Summary is displayed in the Streamlit app.

📦 Dependencies
Streamlit – Web UI framework

Agno Framework – Agent orchestration

Groq Python SDK – Groq API access

YouTube Transcript API – Transcript retrieval

python-dotenv – Environment variable management

⚠️ Limitations
The app requires captions to generate a detailed summary.
If captions are disabled or auto-generated in an unsupported language, the summary may be based only on metadata.
Internet connection required for API calls.

📄 License
This project is licensed under the MIT License – you are free to use, modify, and distribute it.

💡 Future Improvements
Support for multi-language captions.
Option to summarize without captions (using audio transcription).
Export summary as PDF or TXT.
Adjustable summary length.