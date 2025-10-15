import streamlit as st
from agent import (
    generate_research_ideas,
    analyze_research_gap,
    suggest_methodology,
    suggest_statistical_methods,
    retrieve_related_studies,
    critique_study,
    academic_writer,
    format_final_report
)

st.set_page_config(page_title="وكيل الذكاء التربوي", layout="wide")
st.title("📚 وكيل الذكاء التربوي الذكي")

option = st.sidebar.selectbox("اختر الوحدة:", [
    "اقتراح أفكار بحثية",
    "تحليل الفجوات",
    "اقتراح المنهجية",
    "الأساليب الإحصائية",
    "استرجاع الدراسات السابقة",
    "تحليل نقدي للدراسات",
    "كتابة أكاديمية",
    "تنسيق التقرير النهائي"
])

if option == "اقتراح أفكار بحثية":
    domain = st.text_input("مجال التخصص")
    keywords = st.text_input("الكلمات المفتاحية")
    study_type = st.selectbox("نوع الدراسة", ["وصفية", "تجريبية", "ارتباطية"])
    if st.button("اقتراح أفكار"):
        st.write(generate_research_ideas(domain, keywords, study_type))

elif option == "تحليل الفجوات":
    topic = st.text_area("وصف الموضوع")
    keywords = st.text_input("الكلمات المفتاحية")
    if st.button("تحليل الفجوات"):
        st.write(analyze_research_gap(topic, keywords))

elif option == "اقتراح المنهجية":
    problem = st.text_area("صياغة مشكلة البحث")
    questions = st.text_area("الأسئلة البحثية")
    if st.button("اقتراح المنهجية"):
        st.write(suggest_methodology(problem, questions))

elif option == "الأساليب الإحصائية":
    research_type = st.selectbox("نوع الدراسة", ["كمية", "نوعية", "مختلطة"])
    variables = st.text_input("المتغيرات")
    goals = st.text_area("أهداف الدراسة")
    if st.button("اقتراح الأساليب الإحصائية"):
        st.write(suggest_statistical_methods(research_type, variables, goals))

elif option == "استرجاع الدراسات السابقة":
    topic = st.text_input("موضوع الدراسة")
    keywords = st.text_input("الكلمات المفتاحية")
    if st.button("استرجاع الدراسات"):
        st.write(retrieve_related_studies(topic, keywords))

elif option == "تحليل نقدي للدراسات":
    study_text = st.text_area("نص الدراسة أو ملخصها")
    if st.button("تحليل نقدي"):
        st.write(critique_study(study_text))

elif option == "كتابة أكاديمية":
    section = st.selectbox("القسم المطلوب", ["المقدمة", "الإطار النظري", "المنهجية", "النتائج", "الخاتمة"])
    notes = st.text_area("ملاحظات المحتوى")
    if st.button("كتابة الفقرة"):
        st.write(academic_writer(section, notes))

elif option == "تنسيق التقرير النهائي":
    sections = st.text_area("أدخل الأقسام كمحتوى JSON أو نص منسق")
    if st.button("تنسيق التقرير"):
        st.write(format_final_report(sections))
