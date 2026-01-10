import streamlit as st
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_groq import ChatGroq
from langchain.agents import initialize_agent, AgentType
import os

# السوارت الخاصة بك (API Keys)
os.environ["TAVILY_API_KEY"] = "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"
os.environ["GROQ_API_KEY"] = "Gsk_AJM7e0JKZ9eTJj1SyAd2WGdyb3FYlmSRNvhIcJSLv5mQcupkCaAG"

# إعداد واجهة التطبيق
st.set_page_config(page_title="خبير الاستشارة القانونية المغربي", page_icon="⚖️")
st.title("🏛️ مساعد الاستشارة القانوني الذكي (نسخة 2026)")
st.markdown("---")

# إعداد محرك الذكاء الاصطناعي (Groq Llama 3)
try:
    llm = ChatGroq(model_name="llama-3.3-70b-versatile", temperature=0.1)
    
    # إعداد أداة البحث في الأنترنت (Tavily)
    search_tool = TavilySearchResults(k=5)
    tools = [search_tool]

    # إنشاء العميل الذكي (Agent)
    agent = initialize_agent(
        tools, 
        llm, 
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, 
        verbose=True
    )

    # خانة إدخال الأسئلة
    query = st.text_input("اسأل عن أي قانون أو مستجد في القوانين المغربية:")

    if query:
        with st.spinner('جاري البحث والتحليل القانوني...'):
            # تخصيص البرومبت بناءً على هويتك كطالب قانون ومرشح
            prompt = (
                f"أنت مستشار قانوني مغربي خبير. السائل هو طالب قانون متخصص "
                f"يهتم بالاستشارة القانونية. أجب بدقة قانونية وباللغة العربية على: {query}. "
                f"ركز على القوانين والمراسيم المغربية المحينة لسنة 2026."
            )
            response = agent.run(prompt)
            st.success("النتيجة:")
            st.info(response)

except Exception as e:
    st.error(f"حدث خطأ فني: {e}")

# تذييل الصفحة الخاص بك
st.sidebar.markdown("---")
st.sidebar.write("👤 **المطور:** محمد أمونير")
st.sidebar.write("🎓 **الصفة:** طالب قانون")
st.sidebar.write("🗓️ **مشروع:** مستشار قانوني مغربي 2026")
