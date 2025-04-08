# pdss_app.py
# 필요한 라이브러리 설치 안내:
# pip install streamlit

import streamlit as st

# -------------------------------
# 1. 도입 증상 체크리스트 (총 13개 증상)
# -------------------------------
symptoms_ko = [
    "심장이 빠르게 뛰거나 두근거림",
    "가슴 통증 또는 불편감",
    "오한 또는 열감",
    "땀 흘림",
    "메스꺼움",
    "떨림 또는 몸이 흔들림",
    "어지러움 또는 기절할 것 같은 느낌",
    "통제력을 잃거나 미쳐버릴 것 같은 두려움",
    "숨 가쁨",
    "비현실감",
    "죽을 것 같은 두려움",
    "목이 조여오는 느낌",
    "무감각 또는 저림"
]
symptoms_en = [
    "Rapid or pounding heartbeat",
    "Chest pain or discomfort",
    "Chills or hot flushes",
    "Sweating",
    "Nausea",
    "Trembling or shaking",
    "Dizziness or faintness",
    "Fear of losing control or going crazy",
    "Breathlessness",
    "Feelings of unreality",
    "Fear of dying",
    "Feeling of choking",
    "Numbness or tingling"
]

# -------------------------------
# 2. PDSS 문항 데이터 구성 (7개 문항)
# -------------------------------
pdss_questions = [
    {
        "id": 1,
        "question_ko": "지난 일주일 동안 공황 발작 및 제한적 증상 발작을 얼마나 자주 경험하셨습니까?",
        "question_en": "How many panic and limited symptoms attacks did you have during the week?",
        "description_ko": "이 항목은 지난 일주일 동안 공황 발작 및 제한적 증상 발작의 빈도를 평가합니다.",
        "description_en": "This item assesses the frequency of panic attacks and limited symptom attacks during the past week.",
        "choices": [
            {
                "score": 0,
                "ko": "공황 발작이나 제한적 증상 발작이 전혀 없었음",
                "en": "No panic or limited symptom episodes",
                "response_text_ko": "지난 한 주 동안 전혀 공황 발작이나 제한적 증상 발작을 경험하지 않았습니다.",
                "response_text_en": "I did not experience any panic or limited symptom attacks during the past week."
            },
            {
                "score": 1,
                "ko": "경미: 완전한 공황 발작은 없었고, 제한적 증상 발작이 하루에 한 번 이하로 발생함",
                "en": "Mild: no full panic attacks and no more than 1 limited symptom attack/day",
                "response_text_ko": "제가 경험한 공황 증상은 경미하여 하루에 한 번 이하의 제한적 증상 발작이 있었습니다.",
                "response_text_en": "I experienced mild symptoms with no full panic attacks and no more than one limited symptom attack per day."
            },
            {
                "score": 2,
                "ko": "중등도: 완전한 공황 발작이 1~2회 있었거나, 제한적 증상 발작이 하루에 여러 번 발생함",
                "en": "Moderate: 1 or 2 full panic attacks and/or multiple limited symptom attacks/day",
                "response_text_ko": "지난 일주일 동안 1~2회의 완전한 공황 발작이나 하루에 여러 번의 제한적 증상 발작이 있었습니다.",
                "response_text_en": "I had 1 or 2 full panic attacks and/or multiple limited symptom attacks in the past week."
            },
            {
                "score": 3,
                "ko": "심각: 완전한 공황 발작이 2회 이상 있었으나 평균적으로 하루에 한 번을 넘지 않음",
                "en": "Severe: more than 2 full attacks but not more than 1/day on average",
                "response_text_ko": "완전한 공황 발작이 2회 이상 있었으나, 평균적으로 하루에 한 번을 넘지 않았습니다.",
                "response_text_en": "I experienced more than two full panic attacks, but on average, not more than one per day."
            },
            {
                "score": 4,
                "ko": "극심: 완전한 공황 발작이 하루에 한 번 이상 발생했고, 일주일 중 대부분의 날에 발생함",
                "en": "Extreme: full panic attacks occurred more than once a day, more days than not",
                "response_text_ko": "매일 한 번 이상, 일주일의 대부분 날에 완전한 공황 발작을 경험하였습니다.",
                "response_text_en": "I had full panic attacks occurring more than once a day on most days of the week."
            }
        ]
    },
    {
        "id": 2,
        "question_ko": "지난 일주일 동안 공황 발작(또는 제한적 증상 발작)이 있었다면, 발작이 발생했을 당시 얼마나 고통스럽고 무서웠습니까? (발작이 여러 번 있었다면 평균적인 정도를 평가해 주세요. 공황 발작은 없었지만 제한적 증상 발작이 있었다면, 제한적 증상 발작에 대해 답해 주세요.)",
        "question_en": "If you had any panic attacks during the past week, how distressing (uncomfortable, frightening) were they while they were happening? (If you had more than one, give an average rating. If you didn't have any panic attacks but did have limited symptom attacks, answer for the limited symptom attacks.)",
        "description_ko": "이 항목은 발작의 강도와 고통 정도를 평가합니다.",
        "description_en": "This item assesses the distress level of the panic or limited symptom attacks.",
        "choices": [
            {
                "score": 0,
                "ko": "전혀 고통스럽지 않았거나, 지난 일주일 동안 발작이 전혀 없었음",
                "en": "Not at all distressing, or no panic or limited symptom attacks during the past week",
                "response_text_ko": "지난 한 주 동안 발작이 전혀 없었거나, 발작이 있었더라도 전혀 고통스럽지 않았습니다.",
                "response_text_en": "I did not experience any panic or limited symptom attacks, or if I did, they were not distressing at all."
            },
            {
                "score": 1,
                "ko": "약간 고통스러웠음 (그다지 강렬하지 않았음)",
                "en": "Mildly distressing (not too intense)",
                "response_text_ko": "발작이 약간 고통스러웠으나, 크게 강렬하지 않았습니다.",
                "response_text_en": "The attacks were mildly distressing, not too intense."
            },
            {
                "score": 2,
                "ko": "중간 정도로 고통스러웠음 (강렬했지만 감당 가능했음)",
                "en": "Moderately distressing (intense, but still manageable)",
                "response_text_ko": "발작은 강렬했으나 감당 가능한 정도였습니다.",
                "response_text_en": "The attacks were moderately distressing; they were intense but still manageable."
            },
            {
                "score": 3,
                "ko": "매우 고통스러웠음 (매우 강렬했음)",
                "en": "Severely distressing (very intense)",
                "response_text_ko": "발작이 매우 고통스러웠고, 강렬하게 느껴졌습니다.",
                "response_text_en": "The attacks were severely distressing and very intense."
            },
            {
                "score": 4,
                "ko": "극도로 고통스러웠음 (모든 발작에서 극심한 고통을 느낌)",
                "en": "Extremely distressing (extreme distress during all attacks)",
                "response_text_ko": "모든 발작에서 극심한 고통을 경험하였습니다.",
                "response_text_en": "I experienced extreme distress during all the attacks."
            }
        ]
    },
    {
        "id": 3,
        "question_ko": "지난 일주일 동안, 다음 공황 발작이 언제 발생할지에 대해 또는 발작과 관련된 두려움(예: 발작이 신체적/정신적 건강 문제의 신호일 수 있다는 걱정, 또는 사회적으로 당황할 수 있다는 두려움)에 대해 얼마나 자주 걱정하거나 불안해하셨습니까?",
        "question_en": "During the past week, how much have you worried or felt anxious about when your next panic attack would occur or about fears related to the attacks (for example, that they could mean you have physical or mental health problems or could cause you social embarrassment)?",
        "description_ko": "이 항목은 다음 발작의 발생이나 발작에 대한 두려움으로 인한 걱정 및 불안의 빈도를 평가합니다.",
        "description_en": "This item assesses the level of worry or anxiety about the onset of the next panic attack or fears related to the attacks.",
        "choices": [
            {
                "score": 0,
                "ko": "전혀 걱정하지 않음",
                "en": "Not at all",
                "response_text_ko": "발작에 대해 전혀 걱정하거나 불안해하지 않았습니다.",
                "response_text_en": "I did not worry or feel anxious about the attacks at all."
            },
            {
                "score": 1,
                "ko": "가끔 또는 경미하게 걱정함",
                "en": "Occasionally or only mildly",
                "response_text_ko": "가끔 또는 경미하게 걱정하였습니다.",
                "response_text_en": "I occasionally or only mildly worried about it."
            },
            {
                "score": 2,
                "ko": "자주 또는 중간 정도로 걱정함",
                "en": "Frequently or moderately",
                "response_text_ko": "비교적 자주 혹은 중간 정도로 걱정하였습니다.",
                "response_text_en": "I frequently or moderately worried about it."
            },
            {
                "score": 3,
                "ko": "매우 자주 또는 매우 불안하게 걱정함",
                "en": "Very often or to a very disturbing degree",
                "response_text_ko": "매우 자주 혹은 상당히 불안한 정도로 걱정하였습니다.",
                "response_text_en": "I worried very often or to a very disturbing degree about it."
            },
            {
                "score": 4,
                "ko": "거의 끊임없이, 그리고 일상생활에 지장을 줄 정도로 걱정함",
                "en": "Nearly constantly and to a disabling extent",
                "response_text_ko": "거의 끊임없이, 일상생활에 지장을 줄 정도로 걱정하였습니다.",
                "response_text_en": "I worried nearly constantly, to the extent that it interfered with my daily activities."
            }
        ]
    },
    {
        "id": 4,
        "question_ko": "지난 일주일 동안, 공황 발작에 대한 두려움 때문에 피하거나 두려움을 느꼈던 장소나 상황(예: 대중교통, 영화관, 군중, 다리, 터널, 쇼핑몰, 혼자 있는 것 등)이 있었습니까? 또는 그러한 상황이 실제로 발생했다면 피했을 것 같은 상황이 있었습니까? 만약 위의 질문 중 하나라도 ‘예’라면, 지난 일주일 동안 이러한 장소나 상황에 대한 두려움과 회피 수준을 평가해 주세요.",
        "question_en": "During the past week were there any places or situations (e.g., public transportation, movie theaters, crowds, bridges, tunnels, shopping malls, being alone) you avoided, or felt afraid of (uncomfortable in, wanted to avoid or leave), because of fear of having a panic attack? Are there any other situations that you would have avoided or been afraid of if they had come up during the week, for the same reason? If yes to either question, please rate your level of fear and avoidance this past week.",
        "description_ko": "이 항목은 공황 발작의 두려움으로 인한 특정 장소나 상황에 대한 회피 및 두려움의 정도를 평가합니다.",
        "description_en": "This item assesses the degree of fear and avoidance of places or situations due to the fear of experiencing a panic attack.",
        "choices": [
            {
                "score": 0,
                "ko": "없음: 두려움이나 회피가 전혀 없음",
                "en": "None: no fear or avoidance",
                "response_text_ko": "어떠한 장소나 상황에 대해서도 두려움이나 회피를 경험하지 않았습니다.",
                "response_text_en": "I experienced no fear or avoidance of any place or situation."
            },
            {
                "score": 1,
                "ko": "경미: 가끔 두려움이나 회피가 있었지만, 대부분 상황을 견디거나 마주할 수 있었음. 생활방식에 거의 영향을 미치지 않음",
                "en": "Mild: occasional fear and/or avoidance but I could usually confront or endure the situation. There was little or no modification of my lifestyle due to this",
                "response_text_ko": "가끔 두려움이나 회피를 경험하였으나, 대부분의 상황은 견딜 수 있었고 생활에 큰 변화는 없었습니다.",
                "response_text_en": "I experienced occasional fear or avoidance, but I was generally able to face the situations with minimal impact on my lifestyle."
            },
            {
                "score": 2,
                "ko": "중등도: 눈에 띄는 두려움이나 회피가 있었지만 여전히 감당 가능했음. 일부 상황은 회피했으나, 동행자와 함께라면 마주할 수 있었음. 생활방식에 어느 정도 변화가 있었으나 전반적인 기능에는 지장이 없었음",
                "en": "Moderate: noticeable fear and/or avoidance but still manageable. I avoided some situations, but I could confront them with a companion. There was some modification of my lifestyle because of this, but my overall functioning was not impaired",
                "response_text_ko": "눈에 띄는 두려움이나 회피를 경험하였으나, 동행자의 도움으로 대부분의 상황을 극복할 수 있었습니다.",
                "response_text_en": "I experienced noticeable fear or avoidance, but with support I was able to manage most situations."
            },
            {
                "score": 3,
                "ko": "심각: 광범위한 회피가 있었음. 일상생활을 유지하기 위해 상당한 조정이 필요했음",
                "en": "Severe: extensive avoidance. Substantial modification of my lifestyle was required to accommodate the avoidance making it difficult to manage usual activities",
                "response_text_ko": "광범위한 회피로 인해 일상생활에 상당한 어려움이 있었습니다.",
                "response_text_en": "I experienced extensive avoidance that significantly impacted my daily activities."
            },
            {
                "score": 4,
                "ko": "극심: 만연하고 기능을 심각하게 제한하는 수준의 두려움과 회피가 있었음. 생활방식에 큰 변화가 필요했고, 중요한 일들을 수행하지 못했음",
                "en": "Extreme: pervasive disabling fear and/or avoidance. Extensive modification in my lifestyle was required such that important tasks were not performed",
                "response_text_ko": "매우 심각한 두려움과 회피로 인해 생활방식에 큰 변화가 있었으며, 중요한 일들을 수행하지 못했습니다.",
                "response_text_en": "I experienced pervasive and disabling fear and avoidance that severely impacted my ability to perform important tasks."
            }
        ]
    },
    {
        "id": 5,
        "question_ko": "지난 일주일 동안, 공황 발작 때와 유사한 신체적 감각을 유발하거나 공황 발작을 촉발할 수 있다는 이유로 피하거나 두려워했던 활동들(예: 신체적 운동, 성관계, 뜨거운 샤워나 목욕, 커피 마시기, 흥미롭거나 무서운 영화 보기 등)이 있었습니까? 또는 그러한 활동이 실제로 발생했다면 피했을 것 같은 활동이 있었습니까? 만약 위 질문 중 하나라도 ‘예’라면, 지난 일주일 동안 이러한 활동에 대한 두려움과 회피 수준을 평가해 주세요.",
        "question_en": "During the past week, were there any activities (e.g., physical exertion, sexual relations, taking a hot shower or bath, drinking coffee, watching an exciting or scary movie) that you avoided, or felt afraid of (uncomfortable doing, wanted to avoid or stop), because they caused physical sensations like those you feel during panic attacks or that you were afraid might trigger a panic attack? Are there any other activities that you would have avoided or been afraid of if they had come up during the week for that reason? If yes to either question, please rate your level of fear and avoidance of those activities this past week.",
        "description_ko": "이 항목은 신체적 감각으로 인해 공황 발작이 촉발될 수 있다는 두려움으로 특정 활동에 대한 회피와 두려움의 정도를 평가합니다.",
        "description_en": "This item assesses the level of fear and avoidance of activities that cause physical sensations similar to those experienced during panic attacks, or that may trigger a panic attack.",
        "choices": [
            {
                "score": 0,
                "ko": "신체적 감각으로 인한 두려움이나 회피가 전혀 없음",
                "en": "No fear or avoidance of situations or activities because of distressing physical sensations",
                "response_text_ko": "특정 활동이나 상황에서 신체적 감각으로 인한 두려움이나 회피를 전혀 경험하지 않았습니다.",
                "response_text_en": "I experienced no fear or avoidance due to distressing physical sensations."
            },
            {
                "score": 1,
                "ko": "경미: 가끔 두려움이나 회피가 있었지만, 대부분은 큰 불편 없이 활동을 수행할 수 있었음. 생활방식에 거의 변화가 없었음",
                "en": "Mild: occasional fear and/or avoidance, but usually I could confront or endure with little distress activities that cause physical sensations. There was little modification of my lifestyle due to this",
                "response_text_ko": "가끔 두려움을 느꼈으나, 대부분의 활동은 큰 문제 없이 수행할 수 있었습니다.",
                "response_text_en": "I experienced mild fear, but I was generally able to carry out the activities without significant disruption."
            },
            {
                "score": 2,
                "ko": "중등도: 눈에 띄는 회피가 있었으나 감당 가능했음. 생활방식에 분명한 변화는 있었지만 전반적인 기능은 유지되었음",
                "en": "Moderate: noticeable avoidance but still manageable. There was definite, but limited, modification of my lifestyle such that my overall functioning was not impaired",
                "response_text_ko": "활동에 대해 눈에 띄는 회피를 경험하였으나, 감당 가능한 수준이었습니다.",
                "response_text_en": "I experienced noticeable avoidance, but it was still manageable."
            },
            {
                "score": 3,
                "ko": "심각: 광범위한 회피가 있었음. 생활방식이 크게 변화하거나 기능에 방해가 있었음",
                "en": "Severe: extensive avoidance. There was substantial modification of my lifestyle or interference in my functioning",
                "response_text_ko": "활동으로 인한 두려움 때문에 광범위한 회피를 경험하였고, 생활에 크게 영향을 미쳤습니다.",
                "response_text_en": "I experienced extensive avoidance that significantly interfered with my functioning."
            },
            {
                "score": 4,
                "ko": "극심: 만연하고 기능을 심각하게 제한하는 회피가 있었음. 이로 인해 생활방식이 크게 변화하여 중요한 일이나 활동을 수행하지 못했음",
                "en": "Extreme: pervasive and disabling avoidance. There was extensive modification in my lifestyle due to this such that important tasks or activities were not performed",
                "response_text_ko": "극심한 회피로 인해 중요한 활동이나 일들을 수행하지 못했습니다.",
                "response_text_en": "I experienced pervasive avoidance that severely limited my ability to perform important tasks or activities."
            }
        ]
    },
    {
        "id": 6,
        "question_ko": "지난 일주일 동안, 위에서 언급된 증상들(공황 및 제한적 증상 발작, 발작에 대한 걱정, 발작으로 인한 상황 및 활동에 대한 두려움)이 귀하의 직장 업무나 가사 책임을 수행하는 데 얼마나 방해가 되었습니까? (만약 지난주에 직장이나 가사 책임이 평소보다 적었다면, 평소 수준의 책임이 있었다면 어떻게 했을지를 기준으로 답해 주세요.)",
        "question_en": "During the past week, how much did the above symptoms altogether (panic and limited symptom attacks, worry about attacks, and fear of situations and activities because of attacks) interfere with your ability to work or carry out your responsibilities at home? (If your work or home responsibilities were less than usual this past week, answer how you think you would have done if the responsibilities had been usual.)",
        "description_ko": "이 항목은 증상들이 직장 또는 가사 책임 수행에 미치는 방해 정도를 평가합니다.",
        "description_en": "This item assesses the extent to which the symptoms interfered with work or home responsibilities.",
        "choices": [
            {
                "score": 0,
                "ko": "직장 또는 가사 책임에 전혀 방해되지 않음",
                "en": "No interference with work or home responsibilities",
                "response_text_ko": "증상으로 인해 직장 업무나 가사 책임 수행에 전혀 방해가 없었습니다.",
                "response_text_en": "I experienced no interference with my work or home responsibilities."
            },
            {
                "score": 1,
                "ko": "약간의 방해는 있었지만, 이러한 문제들이 없었다면 할 수 있었던 일들을 거의 다 수행할 수 있었음",
                "en": "Slight interference with work or home responsibilities, but I could do nearly everything I could if I didn't have these problems",
                "response_text_ko": "증상으로 약간의 방해는 있었으나, 대부분의 일들은 수행할 수 있었습니다.",
                "response_text_en": "I experienced slight interference, but I was able to manage nearly all of my responsibilities."
            },
            {
                "score": 2,
                "ko": "직장 또는 가사 책임 수행에 뚜렷한 방해가 있었으나, 여전히 필요한 일들을 해낼 수 있었음",
                "en": "Significant interference with work or home responsibilities, but I still could manage to do the things I needed to do",
                "response_text_ko": "증상으로 인해 뚜렷한 방해가 있었으나, 필요한 일들은 수행할 수 있었습니다.",
                "response_text_en": "I experienced significant interference, but I was still able to complete my necessary tasks."
            },
            {
                "score": 3,
                "ko": "직장 또는 가사 책임에 상당한 지장이 있었음. 이러한 문제들로 인해 많은 중요한 일들을 수행하지 못했음",
                "en": "Substantial impairment in work or home responsibilities; there were many important things I couldn't do because of these problems",
                "response_text_ko": "증상으로 인해 직장 업무나 가사 책임에 상당한 지장이 있었으며, 많은 중요한 일들을 수행하지 못했습니다.",
                "response_text_en": "I experienced substantial impairment, and many important tasks could not be completed due to these issues."
            },
            {
                "score": 4,
                "ko": "극심하고 마비적인 수준의 방해로 인해, 직장 또는 가사 책임을 거의 수행하지 못했음",
                "en": "Extreme, incapacitating impairment such that I was essentially unable to manage any work or home responsibilities",
                "response_text_ko": "증상으로 인해 극심하게 마비되어 직장 업무나 가사 책임을 거의 수행하지 못했습니다.",
                "response_text_en": "I experienced extreme, incapacitating impairment that rendered me essentially unable to manage any work or home responsibilities."
            }
        ]
    },
    {
        "id": 7,
        "question_ko": "지난 일주일 동안, 공황 발작 및 제한적 증상 발작, 발작에 대한 걱정, 발작으로 인한 상황 및 활동에 대한 두려움이 귀하의 사회생활에 얼마나 방해가 되었습니까? (만약 지난주에 사회적 활동 기회가 적었다면, 그런 기회가 있었다면 어땠을지를 기준으로 답해 주세요.)",
        "question_en": "During the past week, how much did panic and limited symptom attacks, worry about attacks and fear of situations and activities because of attacks interfere with your social life? (If you didn't have many opportunities to socialize this past week, answer how you think you would have done if you did have opportunities.)",
        "description_ko": "이 항목은 증상들이 사회생활에 미치는 영향 정도를 평가합니다.",
        "description_en": "This item assesses the extent to which the symptoms interfered with social life.",
        "choices": [
            {
                "score": 0,
                "ko": "사회생활에 전혀 방해되지 않음",
                "en": "No interference",
                "response_text_ko": "사회생활에 전혀 방해를 느끼지 않았습니다.",
                "response_text_en": "I experienced no interference with my social life."
            },
            {
                "score": 1,
                "ko": "사회적 활동에 약간의 방해는 있었지만, 이러한 문제들이 없었다면 할 수 있었던 사회적 활동을 거의 모두 할 수 있었음",
                "en": "Slight interference with social activities, but I could do nearly everything I could if I didn't have these problems",
                "response_text_ko": "사회적 활동에 약간의 방해가 있었으나, 대부분의 활동은 수행할 수 있었습니다.",
                "response_text_en": "I experienced slight interference, but I was able to engage in almost all social activities."
            },
            {
                "score": 2,
                "ko": "사회적 활동에 뚜렷한 방해가 있었으나, 노력을 기울이면 대부분의 활동을 할 수 있었음",
                "en": "Significant interference with social activities but I could manage to do most things if I made the effort",
                "response_text_ko": "사회적 활동에 뚜렷한 방해가 있었으나, 노력을 통해 대부분의 활동에 참여할 수 있었습니다.",
                "response_text_en": "I experienced significant interference, but with effort I managed to participate in most social activities."
            },
            {
                "score": 3,
                "ko": "사회적 활동에 상당한 지장이 있었음. 이러한 문제들로 인해 많은 사회적 활동을 하지 못했음",
                "en": "Substantial impairment in social activities; there are many social things I couldn't do because of these problems",
                "response_text_ko": "사회적 활동에 상당한 지장이 있었으며, 많은 사회적 활동을 하지 못했습니다.",
                "response_text_en": "I experienced substantial impairment, and I could not engage in many social activities due to these issues."
            },
            {
                "score": 4,
                "ko": "극심하고 마비적인 수준의 방해로 인해, 거의 어떠한 사회적 활동도 하지 못했음",
                "en": "Extreme, incapacitating impairment, such that there was hardly anything social I could do",
                "response_text_ko": "극심한 지장으로 인해 사회적 활동을 거의 하지 못했습니다.",
                "response_text_en": "I experienced extreme, incapacitating impairment that left me with hardly any social activities."
            }
        ]
    }
]

# -------------------------------
# 3. 세션 상태 초기화
# -------------------------------
if "confirmed" not in st.session_state:
    st.session_state.confirmed = False
if "submitted" not in st.session_state:
    st.session_state.submitted = False
if "answers" not in st.session_state:
    st.session_state.answers = {}  # 각 질문 id별 답변 점수를 저장 (예: {1: score, 2: score, ...})
if "full_panic" not in st.session_state:
    st.session_state.full_panic = False
if "attack_type" not in st.session_state:
    st.session_state.attack_type = ""
if "selected_symptoms_ko" not in st.session_state:
    st.session_state.selected_symptoms_ko = []
if "selected_symptoms_en" not in st.session_state:
    st.session_state.selected_symptoms_en = []

# -------------------------------
# 4. 앱 UI 구성
# -------------------------------
st.title("공황장애 심각도 평가 (PDSS)")

# 도입 증상 체크리스트 페이지: st.session_state.confirmed가 False인 경우
if not st.session_state.confirmed:
    st.header("도입 증상 체크리스트")
    st.write("다음 13개 증상 중 해당되는 증상을 모두 선택하세요:")
    
    checked_symptoms = []
    for idx, symptom in enumerate(symptoms_ko):
        if st.checkbox(symptom, key=f"symptom_{idx}"):
            checked_symptoms.append(symptom)
    
    if st.button("증상 선택 완료"):
        st.session_state.selected_symptoms_ko = checked_symptoms
        st.session_state.selected_symptoms_en = [symptoms_en[idx] for idx, s in enumerate(symptoms_ko) if s in checked_symptoms]
        # full_panic 판별 및 attack_type 결정
        if len(checked_symptoms) >= 4:
            st.session_state.full_panic = True
            st.session_state.attack_type = "완전한 공황발작"
        else:
            st.session_state.full_panic = False
            st.session_state.attack_type = "제한된 불안발작"
        st.session_state.confirmed = True
        st.success(f"증상 선택 완료 ({st.session_state.attack_type})")
        
# 평가 문항 페이지: 증상 체크가 완료되고 제출 전인 경우
elif st.session_state.confirmed and not st.session_state.submitted:
    st.header("PDSS 평가 문항")
    st.write("아래 질문에 답해주세요. 모든 질문은 한국어로 제공되며, 선택지는 해당 점수(인덱스)가 곧 점수가 됩니다.\n\n*주의: 문항 1번은 공황 여부(full_panic)에 따라 선택지 범위가 달라집니다.*")
    
    for q in pdss_questions:
        qid = q["id"]
        if qid == 1 and not st.session_state.full_panic:
            choices = [choice for choice in q["choices"] if choice["score"] <= 2]
        else:
            choices = q["choices"]
            
        option_texts = [f"({c['score']}) {c['ko']}" for c in choices]
        # 드롭다운 메뉴 (selectbox) 사용
        answer = st.selectbox(q["question_ko"], options=option_texts, key=f"q_{qid}")
        try:
            selected_score = int(answer.split(")")[0].replace("(", "").strip())
        except Exception:
            selected_score = 0
        st.session_state.answers[qid] = {"score": selected_score, "choice": answer}
        
    if st.button("제출"):
        st.session_state.submitted = True

# 결과 출력 페이지: st.session_state.submitted가 True인 경우
elif st.session_state.submitted:
    st.header("Evaluation Result")
    
    total_score = sum([st.session_state.answers[q["id"]]["score"] for q in pdss_questions])
    
    if total_score <= 7:
        interpretation = "Minimal or no symptoms"
    elif total_score <= 14:
        interpretation = "Mild symptoms. Some impairment"
    elif total_score <= 21:
        interpretation = "Moderate symptoms. Significant impairment. Treatment recommended"
    else:
        interpretation = "Severe symptoms. Disabling. Treatment strongly recommended"
    
    result_text = f"[Panic Disorder Severity Scale (PDSS)]\n\n"
    for q in pdss_questions:
        qid = q["id"]
        q_title_en = q["question_en"]
        answer_score = st.session_state.answers[qid]["score"]
        if qid == 1 and not st.session_state.full_panic:
            applicable_choices = [choice for choice in q["choices"] if choice["score"] <= 2]
        else:
            applicable_choices = q["choices"]
        chosen_choice = next((choice for choice in applicable_choices if choice["score"] == answer_score), None)
        chosen_text = chosen_choice["response_text_en"] if chosen_choice is not None else ""
        # "Score:" 문자열 없이 단순히 (점수)로 출력
        result_text += f"{qid}. {q_title_en}\n   ({answer_score}) {chosen_text}\n\n"
    result_text += f"Total Score: {total_score}\nInterpretation: {interpretation}\n"
    
    st.code(result_text, language="python")
    
    if st.button("재시작"):
        for key in ["confirmed", "submitted", "answers", "full_panic", "attack_type", "selected_symptoms_ko", "selected_symptoms_en"]:
            if key in st.session_state:
                del st.session_state[key]
        st.experimental_rerun()
