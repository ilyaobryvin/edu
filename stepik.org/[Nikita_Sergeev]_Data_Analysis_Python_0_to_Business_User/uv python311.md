# Удалить старый venv если был
## Удалить ядро Jupyter (kernel)
jupyter kernelspec list
jupyter kernelspec uninstall fa-python

## Удалить venv fa-python
deactivate
rmdir /s /q C:\pyenvs\fa-python

# Ставим python и зависимости
## Создать новый venv на Python 3.11
uv venv --python 3.11 --seed C:\pyenvs\fa-python

## Поставить только нужные библиотеки для задания (Excel + факторный анализ + проверки)
uv pip install --python C:\pyenvs\fa-python\Scripts\python.exe numpy pandas scipy scikit-learn==1.1.3 statsmodels openpyxl xlsxwriter factor_analyzer pingouin ipykernel

## Поставить ядро ipykernel для нового окружения
C:\pyenvs\fa-python\Scripts\python -m ipykernel install --user --name fa-python --display-name "Python FA (3.11)"

## Проверка версий (чтобы убедиться что проблема ушла)
C:\pyenvs\fa-python\Scripts\python -c "import sys; import sklearn, factor_analyzer, pingouin, pandas, scipy; print(sys.version); print('sklearn', sklearn.version); print('factor_analyzer', factor_analyzer.version); print('pingouin', pingouin.version); print('pandas', pandas.version); print('scipy', scipy.version)"