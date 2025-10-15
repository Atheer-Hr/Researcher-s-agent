import openai
openai.api_key = "ضع مفتاح OpenAI هنا"

# وحدة مشتركة لاستدعاء GPT
def ask_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=1200
    )
    return response['choices'][0]['message']['content']

# 1. اقتراح أفكار بحثية
def generate_research_ideas(domain, keywords, study_type):
    prompt = f"""
    اقترح 3 أفكار بحثية حديثة في مجال "{domain}" باستخدام الكلمات المفتاحية: {keywords}.
    نوع الدراسة: {study_type}. لكل فكرة: عنوان، مبرر، الفجوة، المنهجية.
    """
    return ask_gpt(prompt)

# 2. تحليل الفجوات وتحديد المشكلة
def analyze_research_gap(topic_description, keywords):
    prompt = f"""
    حلل الموضوع التالي: "{topic_description}" باستخدام الكلمات المفتاحية: {keywords}.
    قدم: مشكلة البحث، الفجوات، 3 أسئلة بحثية، واقتراح للمنهج.
    """
    return ask_gpt(prompt)

# 3. اقتراح المنهجية والعينة والأدوات
def suggest_methodology(problem_statement, research_questions):
    prompt = f"""
    بناءً على المشكلة: "{problem_statement}" والأسئلة: {research_questions}.
    اقترح: المنهج، حجم العينة، أدوات جمع البيانات، ومبررات علمية.
    """
    return ask_gpt(prompt)

# 4. اقتراح الأساليب الإحصائية
def suggest_statistical_methods(research_type, variables, goals):
    prompt = f"""
    نوع الدراسة: {research_type}، المتغيرات: {variables}، الأهداف: {goals}.
    اقترح: الأساليب الإحصائية المناسبة، مبررات، شروط التطبيق.
    """
    return ask_gpt(prompt)

# 5. استرجاع الدراسات السابقة
def retrieve_related_studies(topic, keywords):
    prompt = f"""
    ابحث عن 3 دراسات عربية و3 أجنبية حول "{topic}" باستخدام: {keywords}.
    لكل دراسة: العنوان، المؤلف، السنة، المنهج، النتائج.
    """
    return ask_gpt(prompt)

# 6. تحليل نقدي للدراسات
def critique_study(study_text):
    prompt = f"""
    حلل نقديًا الدراسة التالية: "{study_text}" من حيث المنهج، العينة، الإحصاء، النتائج، القوة والضعف.
    """
    return ask_gpt(prompt)

# 7. كتابة أكاديمية
def academic_writer(section_type, content_notes):
    prompt = f"""
    اكتب فقرة علمية لقسم "{section_type}" بناءً على: {content_notes}.
    بأسلوب أكاديمي رصين.
    """
    return ask_gpt(prompt)

# 8. تنسيق التقرير النهائي
def format_final_report(sections_dict):
    prompt = f"""
    نسّق التقرير النهائي باستخدام الأقسام التالية: {sections_dict}.
    اجعل التنسيق جاهزًا للتحكيم الأكاديمي.
    """
    return ask_gpt(prompt)
