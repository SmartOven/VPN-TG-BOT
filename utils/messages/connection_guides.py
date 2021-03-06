guide_not_ready_message = """
Гайд по настройке устройства с данной ОС еще в разработке☹
"""

guide_finish_message = """
Гайд закрыт!
"""

ask_guide_message = """
Выберите для какой операционной системы вам нужен гайд
"""

cancel_guide_message = """
Чтобы выйти из гайда нажмите кнопку ***Вернуться в меню*** на встроенной клавиатуре
"""

windows_guide_messages = [
    # Start message
    "Настройка VPN-подключения. Гайд для Windows:",

    # Step 1
    "Нажмите правой кнопкой мыши на предыдущее сообщение с сертификатом и выберите "
    "***\"Открыть папку с файлом\"***. Запомните, куда скачался сертификат (либо, например, скопируйте его в папку "
    "***\"Загрузки\"***)",

    # Step 2
    "Нажмите ***Win+R*** на клавиатуре. В открывшемся диалоговом окне введите ***mmc.exe*** - у вас откроется ***Консоль "
    "управления Windows***",

    # Step 3
    "Нажмите на ***\"Файл\"***, выберите ***\"Добавить или удалить оснастку\"***\nВ открывшемся окне в левом столбце ***\"Доступные "
    "оснастки\"*** выберите вариант ***\"Сертификаты\"***. Нажмите кнопку ***\"Добавить\"*** посередине окна\nОткроется еще одно "
    "окно - выберите ***\"учетной записи компьютера\"***, далее ***\"локальным компьютером\"*** затем нажмите на ***\"Готово\"*** (окно "
    "закроется)\nНажмите ***\"ОК\"*** в оставшемся окне - оно тоже закроется.",

    # Step 4
    "В левой части окна, слева от ***\"Сертификаты (локальный компьютер)\"***, нажмите на значок стрелки - развернется список"
    " папок сертификатов. Найдите в этом списке ***\"Доверенные корневые центры сертификации\"*** и тоже разверните список. В"
    " этом списке будет папка ***\"Сертификаты\"*** - выберите ее (нажатием левой клавишей мыши), затем нажмите на нее "
    "правой клавишей мыши, выберите ***\"Все задачи\"***, ***\"Импорт...\"* - откроется меню импорта сертификатов",

    # Step 5
    "Нажмите ***\"Далее\"***, затем ***\"Обзор\"*** - откроется окно выбора файла с диска\nВ этом окне, снизу справа, в списке "
    "форматов файлов вместо ***\"Сертификат Х.509\"*** выберите ***\"Все файлы\"***. Найдите скачанный ранее сертификат и "
    "выберите его кнопкой ***\"Открыть\"***. Нажмите ***\"Далее\"***, еще раз ***\"Далее\"*** и ***\"Готово\"***\nПоявится окно с текстом "
    "***\"Импорт успешно выполнен\"*** - нажмите ***\"ОК\"***\nЗакройте ***Консоль управления Windows*** и в диалоговом окне с "
    "текстом ***\"Сохранить параметры консоли\"*** нажмите ***\"Нет\"***",

    # Step 6
    "Откройте ***Панель управления***, раздел ***\"Сеть и интернет\"***, ***\"Центр управления сетями и общим доступом\"***, ***\"Создание и "
    "настройка нового подключения или сети\"***\nВыберите вариант ***\"Подключение к рабочему месту\"***, ***\"Использовать мое "
    "подключение к Интернету (VPN)\"***\nВ поле ***\"Адрес в интернете\"*** впишите IP из предыдущего сообщения и нажмите ***\"Создать\"***, "
    "в поле ***\"Имя объекта назначения\"*** впишите удобное для вас название VPN соединения, например, ***MyVPN***",

    # Step 7
    "Откройте ***Настройки***, раздел ***\"Сеть и интернет\"***, ***\"VPN\"***\nВыберите созданное VPN-соединение, ***\"Дополнительные "
    "параметры\"***, и в свойствах подключения нажмите на ***\"Изменить\"***\nВ поля ***\"Имя пользователя\"*** и ***\"Пароль\"*** введите "
    "логин и пароль из предыдущего сообщения и нажмите ***\"Сохранить\"***",

    # Step 8
    "Нажмите на иконку ***Сеть*** на панели задач. Вверху списка, над доступными Wi-Fi сетями, появится "
    "VPN-соединение с указанным вами ранее названием. Нажмите на него, затем на ***\"Подключиться\"***\nГотово - ваше "
    "VPN-соединение установлено😎"
]

android_guide_messages = [
    # Start message
    "Настройка VPN-подключения. Гайд для Android:",

    # Step 1
    "Загрузите ***Клиент strongSwan VPN*** из [Play Store]("
    "https://play.google.com/store/apps/details?id=org.strongswan.android)",

    # Step 2
    "Нажмите на файл сертификата, который прикреплен в предыдущем сообщении. В появившемся окне выберите "
    "***Клиент strongSwan VPN*** и нажмите ***Только сейчас***, а затем ***Import certificate***",

    # Step 3
    "Откройте скачанное приложение ***Клиент strongSwan***\nНажмите на ***Добавить VPN профиль***",

    # Step 4
    "В поле ***Сервер*** впишите IP из предыдущего сообщения, в поля ***Логин*** и ***Пароль*** впишите логин и пароль из предыдущего сообщения. В поле "
    "***Название профиля*** впишите удобное для вас название VPN соединения, например, ***MyVPN***\nУберите галочку ***Выбрать "
    "автоматически*** и нажмите на ***Выбрать сертификат СА***",

    # Step 5
    "Выберите вкладку ***Imported***. Если она пустая - нажмите на троеточие, а затем на ***Обновить сертификат "
    "СА***.\nНажмите на появившийся сертификат, а затем на ***Сохранить***\n",

    # Step 6
    "Нажмите на созданный профиль\nЕсли появятся диалоговые окна ***\"Запрос на подключение\"*** и/или ***\"Disable "
    "battery optimizations\"*** - соглашаемся и разрешаем. Если необходимо - повторно нажимаем на профиль\nГотово - "
    "ваше VPN-соединение установлено😎"
]

ios_guide_messages = [
    # Start message
    "Настройка VPN-подключения. Гайд для iOS:",

    # Step 1
    "Нажмите на файл сертификата, который прикреплен в предыдущем сообщении, нажмите на кнопку сохранения, "
    "затем выберите ***Сохранить в Файлы*** и сохраните в папку ***Загрузки*** в разделе ***iPhone***.",

    # Step 2
    "Откройте приложение ***Мои файлы***. В нем найдите папку ***Загрузки***, а в ней - скачанный сертификат\nНажмите на "
    "него (один или несколько раз) - должна появиться надпись ***Профиль загружен***. Нажмите ***Закрыть***",

    # Step 3
    "Откройте приложение ***Настройки***. Пролистайте вниз и выберите ***Основные***, там выберите ***VPN и управление "
    "устройством***\nВнизу появится список с названием ***Загруженный профиль***, в этом списке будет скачанный вами "
    "сертификат - нажмите на него. В появившемся окне нажмите на ***Установить***, введите пароль, нажимайте на "
    "***Установить***, а затем на ***Готово***. После этого сертификат появится в списке ***Профиль конфигурации***",

    # Step 4
    "Нажмите на ***VPN  Не подключено >***, затем ***Добавить конфигурацию VPN...***\nВ поле ***Описание*** впишите удобное "
    "для вас название VPN соединения, например, ***MyVPN***\nВ поля ***Сервер*** и ***Удаленный ID*** впишите IP из предыдущего сообщения, "
    "в поля ***Имя пользователя*** и ***Пароль*** впишите логин и пароль из предыдущего сообщения. В поле ***Локальный ID*** впишите цифру "
    "1\nНажмите ***Готово***. Нажмите на слайдер в графе ***Статус***, чтобы активировать его.\n Готово - ваше "
    "VPN-соединение установлено😎"
]
