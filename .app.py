import streamlit as st
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_groq import ChatGroq
from langchain.agents import initialize_agent, AgentType
import os

# السوارت مدموجين واجدين
os.environ["TAVILY_API_KEY"] = "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"
os.environ["GROQ_API_KEY"] = "Gsk_AJM7e0JKZ9eTJj1SyAd2WGdyb3FYlmSRNvhIcJSLv5mQcupkCaAG"

st.set_page_config(page_title="خبير الصفقات المغربي", page_icon="⚖️")
st.title("🏛️ مساعد الصفقات العمومية الذكي")

llm = ChatGroq(model_name="llama-3.3-70b-versatile", temperature=0.1)
search_tool = TavilySearchResults(k=5)
tools = [search_tool]

agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

query = st.text_input("اسألني عن قوانين الصفقات العمومية المغربية:")

if query:
    with st.spinner('جاري البحث والتحليل...'):
        try:
            prompt = f"أنت مستشار قانوني مغربي. السائل طالب قانون. أجب بدقة على: {query}. ركز على قوانين 2026."
            response = agent.run(prompt)
            st.info(response)
        except Exception as e:
            st.error(f"خطأ: {e}")
