import os
import streamlit as st
from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.youtube import YouTubeTools
from dotenv import load_dotenv

load_dotenv()
os.environ["GROQ_API_KEY"] = GROQ_API_KEY = os.getenv("GROQ_API_KEY")

st.set_page_config(page_title="YouTube Video Summarizer Agent")
st.title("YouTube Video Summarizer Agent")
st.sidebar.info("Enter a YouTube URL and get a concise summary.")

youtube_url = st.text_input("YouTube URL", placeholder="https://www.youtube.com/watch?v=...")

if st.button("Summarize") and youtube_url:
    if not GROQ_API_KEY:
        st.error("Please set your GROQ_API_KEY in the environment.")
    else:
        agent = Agent(
            model=Groq(id="qwen/qwen3-32b"),
            tools=[YouTubeTools()],
            description="Agent that summarize YouTube Videos.",
            show_tool_calls=True,
            markdown=True
        )

        with st.spinner("Generating summary..."):
            run_response = agent.run(f"Summarize the content of this video:\n{youtube_url}", stream=False)
        
        content = None
        if run_response is None:
            st.error("Agent returned no response.")
        else:
            content = getattr(run_response, "content", None)
            summary_text = content if isinstance(content, str) else str(content)

        st.markdown("### Summary")
        st.write(summary_text)