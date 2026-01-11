import streamlit as st
import os

# --- إعداد الصفحة ---
st.set_page_config(page_title="خبير الصفقات - Safaqat IA", page_icon="⚖️")

# --- العنوان والتقديم ---
st.title("⚖️ مساعد الصفقات العمومية الذكي")
st.caption("مطور من طرف: محمد أمونير | مشروع انتخابات 2026")

# --- التحقق من السوارت (باش ميبقاش يطلع Error خايب) ---
# حطينالك السوارت هنا مؤقتاً باش السيت يشعل ليك دابة.
# من بعد غانوريك كيفاش تخبيهم فـ Secrets باش يكون احترافي.
os.environ["TAVILY_API_KEY"] = "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"
os.environ["GROQ_API_KEY"] = "Gsk_AJM7e0JKZ9eTJj1SyAd2WGdyb3FYlmSRNvhIcJSLv5mQcupkCaAG"

try:
    from langchain_groq import ChatGroq
    from langchain_community.tools.tavily_search import TavilySearchResults
    from langchain.agents import initialize_agent, AgentType

    # إعداد المحرك (Llama 3)
    llm = ChatGroq(model_name="llama-3.3-70b-versatile", temperature=0.3)
    
    # إعداد البحث
    search = TavilySearchResults(k=3)
    
    # إنشاء العميل الذكي
    agent = initialize_agent(
        [search],
        llm,
        agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )

    # خانة السؤال
    query = st.text_input("شنو بغيتي تعرف على قانون الصفقات العمومية؟")

    if query:
        with st.spinner('جاري البحث في النصوص القانونية...'):
            prompt = f"أنت خبير قانوني مغربي. أجب بالعربية والدارجة عن: {query}. اعتمد على قانون الصفقات العمومية المغربي."
            response = agent.run(prompt)
            st.success("الجواب:")
            st.write(response)

except ImportError as e:
    st.error("مشكل في تثبيت المكتبات. تأكد من requirements.txt")
    st.error(e)
except Exception as e:
    st.error(f"وقع خطأ غير متوقع: {e}")

