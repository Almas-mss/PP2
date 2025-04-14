from configparser import ConfigParser  # Парсер для .ini файлов


def load_config(filename='config/database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)

    config = {}
    if parser.has_section(section): #postgresql деген section бар болса
        params = parser.items(section)  # get key-value
        for param in params:
            config[param[0]] = param[1]  # dictionary толтыру
    else:
        print("NOT CONNECTED TO DB!!!")
        # raise Exception(f"Section {section} not found in {filename}")

    return config