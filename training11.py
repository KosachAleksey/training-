import logging

logging.basicConfig(
    level = logging.DEBUG,
    format = "%(asctime)s - %(levelname)s - %(message)s",
    filename = 'training11a.log',
    filemode = 'w',
    encoding = 'UTF-8'
)

logging.debug("Привет! Это я учусь!")

def divid(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        logging.error(f"Ошибка деления на 0: {e}")
        return None
    else:
        logging.info(f"Успешное действие. Результат: {result}")
        return result
    
print(f"Результат деления ", divid(10, 0))

print(f"Результат деления", divid(10, 2))



