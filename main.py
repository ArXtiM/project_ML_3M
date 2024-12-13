import pandas as pd



# Путь к загруженному файлу

cleaned_train_path = 'cleaned_train.csv'



# Загрузка данных

cleaned_train_data = pd.read_csv(cleaned_train_path)



# Анализ данных: базовая статистика по столбцам

column_summary = {

    "column_name": cleaned_train_data.columns,

    "missing_ratio": cleaned_train_data.isnull().mean().values,  # Доля пропущенных значений

    "zero_ratio": (cleaned_train_data == 0).mean().values,       # Доля нулевых значений

    "unique_values": cleaned_train_data.nunique().values         # Количество уникальных значений

}



# Создаем DataFrame с результатами анализа

column_analysis = pd.DataFrame(column_summary)

column_analysis.sort_values(by=["missing_ratio", "zero_ratio"], ascending=False, inplace=True)



# Вывод первых строк анализа и форма набора данных

print(column_analysis.head(), cleaned_train_data.shape)