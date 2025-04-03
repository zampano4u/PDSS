import streamlit as st
import re

st.set_page_config(page_title="PDSS Assessment", layout="wide")

# 세션 상태 초기화
if "submitted" not in st.session_state:
    st.session_state.submitted = False
if "symptoms" not in st.session_state:
    st.session_state.symptoms = []
if "full_panic" not in st.session_state:
    st.session_state.full_panic = False
if "show_questions" not in st.session_state:
    st.session_state.show_questions = False

# 도입 UI (한국어)
st.title("PDSS (Panic Disorder Severity Scale) 검사")
st.markdown("다음 질문들 중 몇몇은 ‘공황 발작(panic attacks)’ 또는 ‘제한적 증상 발작(limited symptom attacks)’과 관련이 있습니다.")
st.markdown("- 공황 발작은 아래에 나열된 증상 중 **최소 4가지 이상**이 10분 이내에 최고조에 도달하는 갑작스러운 두려움 또는 불쾌감의 급상승입니다.")
st.markdown("- 제한적 증상 발작은 위 증상 중 4개 미만을 동반하는 공황 발작 유사한 에피소드입니다.")
st.markdown("### 지난 일주일 동안 경험한 다음 증상들을 모두 선택해 주세요:")

symptom_list = [
    "심계항진 또는 빠른 심장박동",
    "발한",
    "몸 떨림 또는 전율",
    "숨이 가쁘거나 질식할 것 같은 느낌",
    "질식감",
    "흉통 또는 흉부 불편감",
    "메스꺼움 또는 복부 불편감",
    "어지러움, 불안정감, 머리가 띵함 또는 실신할 것 같은 느낌",
    "비현실감 또는 자신으로부터 떨어져 있는 느낌",
    "통제력을 잃거나 미칠 것 같은 두려움",
    "죽을 것 같은 공포",
    "감각이 둔해지거나 따끔거림",
    "오한 또는 열감"
]

selected = []
for symptom in symptom_list:
    if st.checkbox(symptom):
        selected.append(symptom)

if st.button("확인"):
    st.session_state.submitted = True
    st.session_state.symptoms = selected
    st.session_state.full_panic = len(selected) >= 4
    st.session_state.show_questions = len(selected) > 0

if st.session_state.submitted:
    if len(st.session_state.symptoms) == 0:
        st.warning("공황 또는 제한된 증상 발작 증상이 보고되지 않았습니다. 총점은 0점입니다.")
        st.code("Panic Disorder Severity Scale (PDSS)\n\nTotal Score: 0\nClinical Interpretation: No or minimal panic disorder symptoms")
        st.stop()
    else:
        if st.session_state.full_panic:
            st.success("공황 발작입니다.")
        else:
            st.info("제한된 증상발작을 경험하고 계십니다.")

# 질문 선택지 반환 함수 (동적 선택지 포함)
def get_choices(q_id):
    if q_id == 1 and not st.session_state.full_panic:
        return [
            "(0) 전혀 없었음",
            "(1) 경미함: 제한적 증상 발작이 하루 1회 이하",
            "(2) 중간 정도: 제한적 증상 발작이 하루에도 여러 번"
        ]
    elif q_id == 1:
        return [
            "(0) 전혀 없었음",
            "(1) 경미함: 완전한 공황 발작은 없었고 제한적 증상 발작도 하루 1회 이하",
            "(2) 중간 정도: 완전한 공황 발작 1~2회 또는 제한적 증상 발작이 하루에도 여러 번",
            "(3) 심함: 완전한 공황 발작이 3회 이상이지만 하루 평균 1회를 넘지 않음",
            "(4) 매우 심함: 하루에 1회 이상 완전한 공황 발작이 있었고, 대부분의 날에서 나타남"
        ]
    else:
        choices_dict = {
            2: [
                "전혀 고통스럽지 않거나 발작이 없었음 (0)",
                "약간 고통스러웠음 (심하지 않음) (1)",
                "보통 수준으로 고통스러웠음 (강렬하나 참을 수 있었음) (2)",
                "매우 고통스러웠음 (3)",
                "극도로 고통스러웠음 (모든 발작에서 극심한 고통) (4)"
            ],
            3: [
                "전혀 걱정하지 않음 (0)",
                "가끔 또는 약간 걱정함 (1)",
                "자주 또는 보통 수준으로 걱정함 (2)",
                "항상 걱정함 (3)",
                "지속적으로 극심하게 걱정함 (4)"
            ],
            4: [
                "전혀 회피하지 않음 (0)",
                "가끔 회피함 (1)",
                "자주 회피함 (2)",
                "거의 항상 회피함 (3)",
                "매우 심각하게 회피함 (4)"
            ],
            5: [
                "전혀 피하지 않음 (0)",
                "약간 피함 (1)",
                "보통 수준으로 피함 (2)",
                "매우 피함 (3)",
                "극도로 피함 (4)"
            ],
            6: [
                "전혀 업무에 지장이 없음 (0)",
                "약간 업무에 지장이 있음 (1)",
                "보통 수준으로 업무에 지장이 있음 (2)",
                "상당히 업무에 지장이 있음 (3)",
                "매우 업무에 지장이 있음 (4)"
            ],
            7: [
                "전혀 사회적 활동에 지장이 없음 (0)",
                "약간 사회적 활동에 지장이 있음 (1)",
                "보통 수준으로 사회적 활동에 지장이 있음 (2)",
                "상당히 사회적 활동에 지장이 있음 (3)",
                "매우 사회적 활동에 지장이 있음 (4)"
            ]
        }
        return choices_dict[q_id]

# 질문 텍스트 (한국어 UI)
korean_questions = {
    1: "1. 공황 발작 빈도",
    2: "2. 발작 중 고통 정도",
    3: "3. 예기 불안",
    4: "4. 상황 회피",
    5: "5. 신체 감각 회피",
    6: "6. 업무 기능 장애",
    7: "7. 사회적 장애"
}

# 결과 출력용 영어 질문 라벨
english_questions = {
    1: "Frequency of Panic Attacks",
    2: "Distress During Attacks",
    3: "Anticipatory Anxiety",
    4: "Situational Avoidance",
    5: "Avoidance of Physical Sensations",
    6: "Work Functioning Impairment",
    7: "Social Impairment"
}

# 각 질문별 점수에 대응하는 영어 표현
q1_mapping_full = {0: "None", 1: "Mild", 2: "Moderate", 3: "Severe", 4: "Very Severe"}
q1_mapping_limited = {0: "None", 1: "Mild", 2: "Moderate"}
default_mapping = {0: "None", 1: "Mild", 2: "Moderate", 3: "Severe", 4: "Very Severe"}

# 7개 문항에 대해 사용자 응답 수집 (selectbox)
answers = {}
for q_id in range(1, 8):
    choices = get_choices(q_id)
    answers[q_id] = st.selectbox(korean_questions[q_id], choices, key=f"q{q_id}")

# 결과 계산 버튼
if st.button("결과 확인"):
    total_score = 0
    result_lines = []
    # 각 문항의 응답에서 점수를 추출하고 영어 표현으로 변환
    for q_id in range(1, 8):
        answer = answers[q_id]
        score_match = re.search(r"\(?(\d+)\)?", answer)
        if score_match:
            score = int(score_match.group(1))
        else:
            score = 0
        total_score += score
        if q_id == 1:
            descriptor = q1_mapping_full.get(score, "") if st.session_state.full_panic else q1_mapping_limited.get(score, "")
        else:
            descriptor = default_mapping.get(score, "")
        result_lines.append(f"{q_id}. {english_questions[q_id]}: {descriptor} ({score})")
    
    # 총점에 따른 임상적 해석 (예시 기준)
    if total_score <= 5:
        interpretation = "No or minimal panic disorder symptoms"
    elif total_score <= 12:
        interpretation = "Mild panic symptoms"
    elif total_score <= 19:
        interpretation = "Moderate panic symptoms"
    else:
        interpretation = "Severe panic symptoms"
    
    # 도입 질문에서 선택한 증상들을 영어로 변환
    symptom_translations = {
        "심계항진 또는 빠른 심장박동": "Palpitations",
        "발한": "Sweating",
        "몸 떨림 또는 전율": "Trembling",
        "숨이 가쁘거나 질식할 것 같은 느낌": "Shortness of breath",
        "질식감": "Choking sensation",
        "흉통 또는 흉부 불편감": "Chest pain",
        "메스꺼움 또는 복부 불편감": "Nausea",
        "어지러움, 불안정감, 머리가 띵함 또는 실신할 것 같은 느낌": "Dizziness",
        "비현실감 또는 자신으로부터 떨어져 있는 느낌": "Depersonalization",
        "통제력을 잃거나 미칠 것 같은 두려움": "Fear of losing control",
        "죽을 것 같은 공포": "Fear of dying",
        "감각이 둔해지거나 따끔거림": "Numbness or tingling",
        "오한 또는 열감": "Chills or hot flushes"
    }
    selected_symptoms_en = [symptom_translations.get(sym, sym) for sym in st.session_state.symptoms]
    symptoms_line = ", ".join(selected_symptoms_en)
    
    # 결과 텍스트 구성 (출력은 st.code()로만)
    result_text = "Panic Disorder Severity Scale (PDSS)\n"
    result_text += f"Symptoms checked: {symptoms_line}\n\n"
    for line in result_lines:
        result_text += line + "\n"
    result_text += f"\nTotal Score: {total_score}\n"
    result_text += f"Clinical Interpretation: {interpretation}"
    
    st.code(result_text)
