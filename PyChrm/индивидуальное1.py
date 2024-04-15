# Открываем файл для чтения
with open('text.txt', 'r') as file:
    text = file.read()

# Разделяем текст на предложения
sentences = text.split('.')

# Инициализируем списки для вопросительных и восклицательных предложений
question_sentences = []
exclamation_sentences = []

# Итерируем по всем предложениям и добавляем их в соответствующие списки
for sentence in sentences:
    if len(sentence) > 0:
        if sentence.strip()[-1] == '?':
            question_sentences.append(sentence.strip() + '.')
        elif sentence.strip()[-1] == '!':
            exclamation_sentences.append(sentence.strip() + '.')

# Выводим вопросительные предложения
print("Вопросительные предложения:")
for question in question_sentences:
    print(question)

# Выводим восклицательные предложения
print("\nВосклицательные предложения:")
for exclamation in exclamation_sentences:
    print(exclamation)
