# -*- coding: utf-8 -*-
# PDSS 평가 웹앱 (CSV 없이 실행 가능)
# 필요한 라이브러리 설치: pip install streamlit

import streamlit as st

# 문항 및 선택지 데이터 (자동 생성된 리스트)
# PDSS 문항 및 선택지 리스트 (CSV로부터 자동 생성됨)

questions_ko = [
    "제한된 증상삽화를 포함한 공황발작의 빈도",
    "제한된 증상삽화를 포함한 공황발작 동안의 고통",
    "예기불안의 정도 (공황과 연관된 공포, 염려, 걱정)",
    "광장공포증적 공포/회피",
    "공황과 연관된 감각에 대한 두려움/회피",
    "공황장애로 인한 직무 수행의 장애",
    "공황장애로 인한 사회적 기능의 장애",
]

questions_en = [
    "Frequency of panic attacks including incomplete symptom attacks",
    "Distress during panic attacks including incomplete symptom attacks",
    "Severity of anticipatory anxiety (fear, worry, concern related to panic)",
    "Agoraphobic fear/avoidance",
    "Fear/avoidance of physical sensations related to panic",
    "Impairment in occupational functioning due to panic disorder",
    "Impairment in social functioning due to panic disorder",
]

answers_ko = [
    [
        "0. 공황이나 제한된 증상삽화가 없음.",
        "1. (경도) 완전한 공황발작이 주당 평균 1회 미만이고, 제한된 증상삽화는 하루에 한 번을 넘지 않음.",
        "2. (중등도) 완전한 공황발작이 주당 1~2회 발생하거나, 제한된 증상삽화가 하루에 여러 번 있음.",
        "3. (심함) 완전한 공황발작이 주당 3회 이상 있으나, 평균적으로 하루에 1회를 넘지 않음.",
        "4. (극심함) 완전한 공황발작이 매일 1회 이상 있으며, 공황발작이 있는 날이 없는 날보다 많음."
    ],
    [
        "0. 공황발작이나 제한된 증상삽화가 없거나, 발작 중 고통이 없음.",
        "1. (경도) 고통은 경미하나 활동에 거의 또는 전혀 지장을 주지 않아 계속 활동할 수 있음.",
        "2. (중등도) 고통은 상당하지만 견딜 수 있으며, 활동을 계속하고 집중도 유지할 수 있음.",
        "3. (심함) 고통이 심해 활동에 많은 지장을 주고, 집중하지 못하거나 활동을 중단해야 함.",
        "4. (극심함) 고통이 매우 심하여 아무것도 할 수 없음. 장소나 상황에서 벗어나려 하며, 그대로 있으면 극심한 고통과 집중력 저하를 경험함."
    ],
    [
        "0. 공황에 대한 걱정이 없음.",
        "1. (경도) 가끔 공황에 대한 두려움, 걱정, 염려가 있음.",
        "2. (중등도) 공황에 대한 걱정, 두려움, 염려가 자주 있으나 불안하지 않은 시간도 있음. 생활방식에 일부 변화는 있으나 전반적인 기능에는 장애가 없음.",
        "3. (심함) 공황에 대한 두려움, 걱정, 염려에 집착하게 되며, 집중력 및 기능 수행에 상당한 지장이 있음.",
        "4. (극심함) 불안이 거의 지속적으로 나타나며, 공황에 대한 두려움, 걱정, 염려로 인해 중요한 과제를 수행할 수 없음."
    ],
    [
        "0. 없음. 두려움이나 회피가 없음.",
        "1. (경도) 간헐적인 두려움이나 회피가 있으나, 대부분 상황을 직면하거나 견딜 수 있음. 생활방식 변화는 거의 없음.",
        "2. (중등도) 현저한 두려움이나 회피가 있으나 견딜 수 있음. 두려운 상황을 피하긴 하나, 다른 사람이 있으면 직면 가능함. 생활방식이 다소 변화되지만 전반적 기능에는 큰 영향 없음.",
        "3. (심함) 광범위한 회피가 있으며, 공포에 적응하기 위해 생활방식이 상당히 변화되어 일상 활동 수행이 어려움.",
        "4. (극심함) 전반적인 두려움 및 회피로 인해 무능력 상태에 이름. 생활방식이 광범위하게 변화되어 중요한 일을 수행할 수 없음."
    ],
    [
        "0. 고통스러운 신체감각을 유발하는 상황이나 활동에 대한 두려움이나 회피가 없음.",
        "1. (경도) 간헐적인 두려움이나 회피가 있으나, 신체감각 유발 상황이나 활동을 거의 고통 없이 대체로 견디거나 직면할 수 있음. 생활방식 변화는 거의 없음.",
        "2. (중등도) 뚜렷한 회피가 있으나 아직 견딜 수 있음. 생활방식 변화가 명확히 있으나 제한적이며 전반적 기능은 유지됨.",
        "3. (심함) 광범위한 회피가 있어 생활방식이 상당히 변화되며 기능 수행에 지장이 있음.",
        "4. (극심함) 전반적인 회피로 인해 무능력 상태에 이름. 생활방식이 광범위하게 변화되어 중요한 활동을 수행할 수 없음."
    ],
    [
        "0. 공황장애 증상으로 인한 지장이 없음.",
        "1. (경도) 약간의 지장이 있음. 예전보다 일에 어려움을 느끼나 여전히 직무를 잘 수행함.",
        "2. (중등도) 증상으로 인해 명백한 지장이 있으나 견딜 수 있음. 직무 수행에 어려움은 있지만 외부에서는 큰 변화 없이 잘 해내는 것으로 보임.",
        "3. (심함) 결근하거나 며칠간 전혀 일을 할 수 없는 등, 다른 사람이 알아차릴 정도로 직무 수행에 상당한 지장이 있음.",
        "4. (극심함) 증상으로 인해 무능력 상태가 되어 일(또는 학업, 가사 등)을 전혀 할 수 없음."
    ],
    [
        "0. 지장이 없음.",
        "1. (경도) 약간의 지장이 있음. 사회활동에서 질적으로 다소 제약을 느끼지만, 사적 기능은 유지됨.",
        "2. (중등도) 사회생활에 명백한 지장이 있으나 여전히 참여 가능함. 사회활동은 다소 줄었고, 대인관계에서 예전보다 어려움을 느끼나 대부분의 일상적인 사회활동은 수행 가능함.",
        "3. (심함) 사회적 기능 수행에 상당한 지장이 있음. 사회활동이 현저히 줄었고, 타인과의 교제에 많은 어려움이 있음. 억지로 교제는 가능하나 대부분의 사회적 상황에 잘 적응하지 못하거나 즐기지 못함.",
        "4. (극심함) 증상으로 인해 무능력 상태가 됨. 집 밖을 거의 나가지 않으며, 사람들과의 관계가 단절됨."
    ],
]

answers_en = [
    [
        "0. No panic or limited symptom episodes",
        "1. Mild: no full panic attacks and no more than 1 limited symptom attack/day",
        "2. Moderate: 1 or 2 full panic attacks and/or multiple limited symptom attacks/day",
        "3. Severe: more than 2 full attacks but not more than 1/day on average",
        "4. Extreme: full panic attacks occurred more than once a day, more days than not"
    ],
    [
        "0. Not at all distressing, or no panic or limited symptom attacks during the past week",
        "1. Mildly distressing (not too intense)",
        "2. Moderately distressing (intense, but still manageable)",
        "3. Severely distressing (very intense)",
        "4. Extremely distressing (extreme distress during all attacks)"
    ],
    [
        "0. Not at all",
        "1. Occasionally or only mildly",
        "2. Frequently or moderately",
        "3. Very often or to a very disturbing degree",
        "4. Nearly constantly and to a disabling extent"
    ],
    [
        "0. None: no fear or avoidance",
        "1. Mild: occasional fear and/or avoidance but I could usually confront or endure the situation. There was little or no modification of my lifestyle due to this",
        "2. Moderate: noticeable fear and/or avoidance but still manageable. I avoided some situations, but I could confront them with a companion. There was some modification of my lifestyle because of this, but my overall functioning was not impaired",
        "3. Severe: extensive avoidance. Substantial modification of my lifestyle was required to accommodate the avoidance making it difficult to manage usual activities",
        "4. Extreme: pervasive disabling fear and/or avoidance. Extensive modification in my lifestyle was required such that important tasks were not performed"
    ],
    [
        "0. No fear or avoidance of situations or activities because of distressing physical sensations",
        "1. Mild: occasional fear and/or avoidance, but usually I could confront or endure with little distress activities that cause physical sensations. There was little modification of my lifestyle due to this",
        "2. Moderate: noticeable avoidance but still manageable. There was definite, but limited, modification of my lifestyle such that my overall functioning was not impaired",
        "3. Severe: extensive avoidance. There was substantial modification of my lifestyle or interference in my functioning",
        "4. Extreme: pervasive and disabling avoidance. There was extensive modification in my lifestyle due to this such that important tasks or activities were not performed"
    ],
    [
        "0. No interference with work or home responsibilities",
        "1. Slight interference with work or home responsibilities, but I could do nearly everything I could if I didn’t have these problems",
        "2. Significant interference with work or home responsibilities, but I still could manage to do the things I needed to do",
        "3. Substantial impairment in work or home responsibilities; there were many important things I couldn’t do because of these problems",
        "4. Extreme, incapacitating impairment such that I was essentially unable to manage any work or home responsibilities"
    ],
    [
        "0. No interference",
        "1. Slight interference with social activities, but I could do nearly everything I could if I didn’t have these problems",
        "2. Significant interference with social activities but I could manage to do most things if I made the effort",
        "3. Substantial impairment in social activities; there are many social things I couldn’t do because of these problems",
        "4. Extreme, incapacitating impairment, such that there was hardly anything social I could do"
    ],
]


# 증상 체크리스트 (한글/영문 병렬 리스트)
symptoms_ko = [
    "심계항진", "떨림", "숨가쁨", "질식감", "흉통", "메스꺼움", "어지러움",
    "비현실감", "통제불능 느낌", "죽을 것 같은 두려움", "이상감각", "오한 또는 열감", "사지 마비"
]
symptoms_en = [
    "Rapid heartbeat", "Trembling", "Shortness of breath", "Choking feeling", "Chest pain",
    "Nausea", "Dizziness", "Derealization", "Fear of losing control", "Fear of dying",
    "Paresthesia", "Chills or hot flushes", "Numbness"
]

st.title("공황장애 심각도 평가 (PDSS)")

# 상태 초기화
if "confirmed" not in st.session_state:
    st.session_state.confirmed = False
if "selected_symptoms" not in st.session_state:
    st.session_state.selected_symptoms = []

# 도입 질문 화면
if not st.session_state.confirmed:
    st.subheader("다음 증상 중 지난 1주일 동안 경험한 것을 모두 선택하세요:")
    selected_ko = []
    for idx, symptom in enumerate(symptoms_ko):
        if st.checkbox(symptom, key=f"symptom_{idx}"):
            selected_ko.append(symptom)
    if st.button("증상 선택 완료"):
        st.session_state.selected_symptoms = selected_ko
        st.session_state.confirmed = True
    st.stop()

# 평가 문항 화면
selected_ko = st.session_state.selected_symptoms
selected_en = [symptoms_en[symptoms_ko.index(sym)] for sym in selected_ko]
full_panic = len(selected_ko) >= 4

st.subheader("PDSS 평가 문항")

scores = []
for i in range(7):
    question = questions_ko[i]
    st.markdown(f"**{i+1}. {question}**")
    options = answers_ko[i]
    if i == 0 and not full_panic:
        options = options[:3]
    score = st.selectbox("선택하세요", options, key=f"q{i}")
    score_index = options.index(score)
    scores.append(score_index)

# 결과 출력
if st.button("결과 확인"):
    total_score = sum(scores)
    st.subheader("평가 결과 (영문 출력)")
    output = "Panic Disorder Severity Scale (PDSS) Results\n\n"
    output += "Symptoms checked: " + ", ".join(selected_en) + "\n\n"
    for i in range(7):
        q_en = questions_en[i]
        a_en = answers_en[i][scores[i]]
        output += f"{i+1}. {q_en}\n{a_en} (Score: {scores[i]})\n\n"
    output += f"Total Score: {total_score}\n"
    if total_score <= 7:
        interp = "Minimal or no symptoms"
    elif total_score <= 14:
        interp = "Mild symptoms. Some impairment"
    elif total_score <= 21:
        interp = "Moderate symptoms. Significant impairment. Treatment recommended"
    else:
        interp = "Severe symptoms. Disabling. Treatment strongly recommended"
    output += f"Interpretation: {interp}"
    st.code(output)