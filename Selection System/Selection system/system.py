def evaluate_candidate(achievements, leadership_skills, teamwork, relevance_to_theme):
    score = 0
    score += achievements * 0.4  # Учебные достижения
    score += leadership_skills * 0.3  # Лидерские качества
    score += teamwork * 0.2  # Умение работать в команде
    score += relevance_to_theme * 0.1  # Соответствие тематике форума
    return score

def filter_candidates(candidates):
    passed_candidates = []
    for candidate in candidates:
        score = evaluate_candidate(candidate['achievements'],
                                   candidate['leadership_skills'],
                                   candidate['teamwork'],
                                   candidate['relevance_to_theme'])
        if score >= passing_score:  # предполагаемая проходная оценка
            passed_candidates.append(candidate['name'])
    return passed_candidates

# json файлы
student_data = { 
    'Кандидаты': 
    {
        'теги' : ['Фамилия', 'инструкция'],
    }
}

passing_score = 75
passed_candidates = filter_candidates(student_data )

def result():
    return passed_candidates