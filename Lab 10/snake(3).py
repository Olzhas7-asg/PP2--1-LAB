# Разделение данных на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Создание и обучение модели логистической регрессии
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)
# Предсказание на тестовых данных
y_pred = model.predict(X_test)

# Оценка модели
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
report = classification_report(y_test, y_pred)
print("Точность модели:", accuracy)
print("Матрица ошибок:\n", conf_matrix)
print("Отчёт о классификации:\n", report)




