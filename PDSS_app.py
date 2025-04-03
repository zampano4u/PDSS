import streamlit as st

st.title("PDSS 평가 (Panic Disorder Severity Scale)")

# 세션 상태 초기화
if "symptom_confirmed" not in st.session_state:
    st.session_state.symptom_confirmed = False
if "selected_symptoms" not in st.session_state:
    st.session_state.selected_symptoms = []
if "checkbox_states" not in st.session_state:
    st.session_state.checkbox_states = {s: False for s in range(13)}

# 증상 리스트
symptoms = [
    "1. 갑작스럽게 심장이 빨리 뛰거나 두근거림", 
    "2. 땀이 남", 
    "3. 몸이 떨리거나 전율이 느껴짐", 
    "4. 숨이 가쁘거나 질식할 것 같은 느낌", 
    "5. 흉부 통증 또는 불편감", 
    "6. 메스꺼움 또는 복부 불편감", 
    "7. 어지럽거나 불안정하거나 실신할 것 같은 느낌", 
    "8. 비현실감 또는 이인증", 
    "9. 통제력을 잃거나 미칠 것 같은 두려움", 
    "10. 죽을 것 같은 공포", 
    "11. 감각이 둔해지거나 따끔거림", 
    "12. 오한 또는 열감", 
    "13. 이 중 해당되는 증상이 전혀 없음"
]

# 도입 질문 UI
if not st.session_state.symptom_confirmed:
    st.markdown("### 📝 도입 질문: 최근 일주일 동안 다음 증상 중 어떤 것이 있었습니까?")
    selected = []
    for i, symptom in enumerate(symptoms):
        checked = st.checkbox(symptom, value=st.session_state.checkbox_states[i], key=f"symptom_{i}")
        st.session_state.checkbox_states[i] = checked
        if checked:
            selected.append(symptom)

    if st.button("✅ 선택 완료 후 계속하기"):
        st.session_state.selected_symptoms = selected
        st.session_state.symptom_confirmed = True

# 이후 문항
if st.session_state.symptom_confirmed:
    selected_symptoms = st.session_state.selected_symptoms

    full_panic = True
    if "13. 이 중 해당되는 증상이 전혀 없음" in selected_symptoms:
        full_panic = False
    elif len(selected_symptoms) < 4:
        full_panic = False

    responses = {}

    st.markdown("### 1) 제한된 증상삽화들을 포함한 공황발작의 빈도")
    if full_panic:
        options_q1 = [
            "0 공황이나 제한된 증상삽화가 없음.",
            "1 (경도) 완전한 공황이 주당 평균 1회 미만이고 제한된 증상삽화는 하루에 한 번을 넘지 않는 경우.",
            "2 (중등도) 완전한 공황발작이 주당 1회 혹은 2회, 그리고 혹은 제한된 증상삽화들은 하루에 여러번 있는 경우.",
            "3 (심함) 완전한 공황발작이 주당 3회 이상 있으나, 평균 1일 1회 이상을 넘지 않아야 한다.",
            "4 (극심함) 완전한 공황발작이 매일 1회 이상 있고, 공황발작이 있는 날이 없는 날보다 많은 경우."
        ]
    else:
        options_q1 = [
            "0 공황이나 제한된 증상삽화가 없음.",
            "1 (경도) 완전한 공황이 주당 평균 1회 미만이고 제한된 증상삽화는 하루에 한 번을 넘지 않는 경우.",
            "2 (중등도) 완전한 공황발작이 주당 1회 혹은 2회, 그리고 혹은 제한된 증상삽화들은 하루에 여러번 있는 경우."
        ]
    response_q1 = st.selectbox("1번 문항에 대한 응답을 선택하세요.", options_q1)
    responses["1) 제한된 증상삽화들을 포함한 공황발작의 빈도"] = response_q1
    score_q1 = int(response_q1[0])
    scores = [score_q1]

    # 나머지 문항
    questions = {
        "2) 제한된 증상삽화들을 포함한 공황발작 동안의 고통": [
            "0 공황발작이나 제한된 증상삽화가 없거나 삽화동안 고통이 없음.",
            "1 (경도) 고통이 경미하나 활동에 거의 혹은 전혀 지장을 주지 않아 계속 활동할 수 있다.",
            "2 (중등도) 고통이 상당히 있으나 견딜만하고 힘들기는 하지만 활동을 계속하고 집중을 유지할 수 있다.",
            "3 (심함) 고통이 심하고 활동에도 지장을 많이 받으며 집중을 못하고 혹은 활동을 중단해야 함.",
            "4 (극심함) 고통이 아주 심하고 아무것도 못하게 만든다. 활동을 중단해야만 한다. 가능하다면 장소나 상황을 벗어나려고 하고, 그대로 남아 있다면 굉장히 고통스럽고 집중도 할 수 없다."
        ],
        "3) 예기불안의 정도(공황과 연관된 공포, 염려, 걱정)": [
            "0 공황에 대한 걱정이 없다.",
            "1 (경도) 가끔 공황에 대한 두려움, 걱정, 염려가 있다.",
            "2 (중등도) 종종 공황에 대한 걱정, 두려움, 염려가 있으나 불안하지 않을 때도 있음. 생활 방식이 눈에 띌 만큼 변화하지만 아직 견딜 수 있는 정도이고 전반적인 기능의 장애가 없다.",
            "3 (심함) 공황에 대한 두려움, 걱정, 염려에 집착하는 상태, 집중하고 혹은 효과적으로 기능을 수행하는데 상당한 지장이 있다.",
            "4 (극심함) 불안이 거의 끊임없이 나타나고 아무런 일도 하지 못하게 만든다. 공황에 대한 두려움, 걱정, 염려 때문에 중요한 과제를 수행할 수 없다."
        ],
        "4) 광장공포증적 공포/회피": [
            "0 없음. 두려움이나 회피가 없다.",
            "1 (경도) 간헐적인 두려움 혹은 회피가 있다. 그러나 대게 상황을 직면하거나 견뎌낼 수 있음. 생활방식이 거의 또는 전혀 변화되지 않는다.",
            "2 (중등도) 현저한 두려움이나 회피가 있지만 견딜 수 있다. 두려운 상황을 피하긴 하지만 다른 사람이 있으면 직면할 수 있다. 생활방식이 약간 변화되지만 전반적 기능에는 지장이 없다.",
            "3 (심함) 광범위한 회피가 있다. 공포증에 적응하기 위해서 생활방식의 상당부분이 변화되고 일상 활동을 하기 어렵다.",
            "4 (극심함) 전반적인 두려움 혹은 회피가 있어 무능력하게 된다. 생활방식이 광범위하게 변화되어 중요한 일을 할 수 없다."
        ],
        "5) 공황과 연관된 감각에 대한 두려움/회피": [
            "0 고통스런 신체감각을 유발하는 상황이나 활동에 대한 두려움이나 회피가 없다.",
            "1 (경도) 간헐적인 두려움이나 회피가 있다. 그러나 신체감각을 유발하는 활동이나 상황들을 거의 고통 없이 대개 직면하거나 견딜 수 있다. 생활방식의 변화는 거의 없다.",
            "2 (중등도) 뚜렷한 회피가 있다. 그러나 아직 견딜 수 있음. 생활방식의 변화가 명백히 있으나 제한된 정도이고 전반적 기능에는 지장이 없다.",
            "3 (심함) 광범위한 회피가 있어 생활방식이 상당히 변화되거나 기능에 지장이 있다.",
            "4 (극심함) 전반적인 회피가 있어 무능력하게 만든다. 생활방식이 광범위하게 변화되어 중요한 일이나 활동을 수행할 수 없다."
        ],
        "6) 공황장애로 인한 직무 수행의 장해": [
            "0 공황장애 증상으로 인한 지장이 없다.",
            "1 (경도) 약간의 지장이 있다. 전보다 일하는데 어려움을 느끼지만 아직 직무를 잘 수행한다.",
            "2 (중등도) 증상으로 인해 명백한 지장이 있으나 아직 견딜 수 있음. 직무 수행에 어려움이 있지만 다른 사람들이 보기엔 특별히 달라진 것 없이 잘 해낸다.",
            "3 (심함) 결근하거나 며칠간 일을 전혀 할 수 없는 것과 같이 다른 사람들이 알아차릴 정도로 직무 수행에 상당한 지장이 있다.",
            "4 (극심함) 증상으로 인해 무능력하게 되고, 일을 할 수 없음(혹은 학교에 갈 수 없거나 가사일을 해낼 수 없다.)"
        ],
        "7) 공황장애로 인한 사회적 기능의 장해": [
            "0 지장이 없다.",
            "1 (경도) 약간의 지장이 있다. 사회활동에 있어 질적으로 다소 지장이 있음을 느끼지만 사적 기능은 아직 괜찮다.",
            "2 (중등도) 사회생활에 있어 명백한 지장이 있지만 아직 해나갈 수 있다. 사회활동이 약간 줄어들고 이전보다 대인관계를 다소 잘 하지 못하지만, 대부분의 일상적인 사회활동에 아직 참여할 수 있다.",
            "3 (심함) 사회적 수행능력에 상당한 지장이 있다. 사회활동이 현저히 감소하고 혹은 다른 사람들과 교제하는데 어려움이 많다.",
            "4 (극심함) 증상으로 인해 무능력하게 된다. 집 밖에 나가거나 다른 사람들과 어울리는 일이 드물고 공황장애로 인해 사람들과 관계가 단절된다."
        ]
    }

    for q, opts in questions.items():
        selected = st.selectbox(q, opts)
        responses[q] = selected
        scores.append(int(selected[0]))

    if st.button("결과 보기"):
        total_score = sum(scores)

        if total_score <= 7:
            interpretation = "공황장애 증상이 거의 없거나 매우 경미한 상태입니다."
        elif total_score <= 14:
            interpretation = "경미한 공황장애 증상으로, 일부 일상 활동에 영향을 미칠 수 있습니다."
        elif total_score <= 21:
            interpretation = "중등도 공황장애 증상으로, 일상생활에 상당한 영향을 미치며 치료가 필요합니다."
        else:
            interpretation = "고도 공황장애 증상으로, 발작이 빈번하고 강도가 매우 강하며, 일상적인 활동이나 대인 관계에 큰 장애를 초래할 수 있습니다."

        result_text = "PDSS 평가 결과\n\n"
        for q, a in responses.items():
            result_text += f"{q}\n응답: {a}\n\n"

        result_text += f"총점 (Total Score): {total_score}\n"
        result_text += f"임상적 해석 (Clinical Interpretation): {interpretation}\n\n"
        result_text += "도입 질문에서 선택된 증상 (Symptoms selected):\n"
        result_text += ", ".join(selected_symptoms) if selected_symptoms else "None"

        st.code(result_text)
