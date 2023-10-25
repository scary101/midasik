import time
import winsound
import random
from colorama import *
init(autoreset=True)


def red(txt):
    init(autoreset=True)
    txt = Fore.RED + txt
    return txt
def green(txt):
    txt = Fore.GREEN + txt
    return txt
def yellow(txt):
    txt = Fore.YELLOW + txt
    return txt
def blue(txt):
    txt = Fore.BLUE + txt
    return txt


def plavno(x):
    for char in x:
        print(char, end='', flush=True)
        time.sleep(0.07)
def fight( Damage, kubic):
    a = (Damage + kubic)
    return a

userHP = 100
monstrHP = 100

magInv = ["Клинок", "Огненный посох"]
warInv = ["Экскалибур", "Деревяный щит"]
archerInv = ["Кинжал", "Лук и стрелы"]
mainInv = []
weaponDamage = []
print("Создание персонажа"
      "\nВведите свое имя:")
name = input()
print("Выберите клсс:"
      f"\n 1. Маг - Оружие: {', '.join(magInv)}. Сильные стороны: сопротивление к магии, повышенный урон по некоторым существам"
      f"\n 2. Войн - Оружие: {', '.join(warInv)}. Сильные стороны: получает меньше урона от физических атак "
      f"\n 3. Лучник - Оружие: {', '.join(archerInv)}. Сильные стороны: бесшумное перемещение, дальнобойные атаки")
userclass = input()
if userclass == "1":
    userclass = "Маг"
    mainInv = magInv
    weaponDamage = [10, 20]
if userclass == "2":
    userclass = "Войн"
    mainInv = warInv
    weaponDamage = [25, 5]
if userclass == "3":
    userclass = "Лучник"
    mainInv = archerInv
    weaponDamage = [10, 22]
personaj = {'name': name, 'class': userclass, "leninv": len(mainInv)}

print(f"ДА НАЧНЕТЬСЯ ВЕЛИЧАЙШЕЕ ПУТИШЕСТВИЕ {userclass}a, ПО ИМЕНИ {name}")
print("Выберите куда отправиться:"
      "\n1. Темный лес")
user_input = input()
if user_input == "1":
    print(
        f"Акт 1. \"Начало\""
        f"\nВы, великий {userclass}, по имени {name}, долго странсвуйте в поисках несметного богатсва, посещая различные места, со своей историей, но тщетно."
        f"\nОднажды вы забредаете в темный лес, по легендам, там находится секретный вход в саму преисподню, где дьявол спрятал свои богатсва"
        f"{name} идет по заросшей дороге, натыкаясь на развилку",
        green("\nКуда дальше?",),
        yellow("\n1. Повернуть направо \n2. Повернуть налево"))
    user_input = input()
    if user_input == "1":
        print(f"{name} поварачивает направо и выходит на лесную опушку, где ничего не находит и возвращаеться назад",
              yellow(f"\n2.Повернуть налево"))
        user_input = input()
    if user_input == "2":
        print(f"{name} поварачивает налево и натыкаеться на озеро.", green(" Вам хочеться пить"),
              yellow("\n 1. Утолить жажду"),
             yellow(f"\n 2. Пройти мимо"))
    user_input = input()
    if user_input == "1":
        print("Вы выпиваете воды и чувствуете легкое помутнение, у вас темнеет в глаза и вы погибаете",
              red("\nGAME OVER. Вы отравились водой"))
        exit()
    if user_input == "2":
        print("Вы проходите мимо озера, не смотря на жажду, понимая что может таить эта вода"
              "\nОт жажды вас клонит сон, в прильнули к большому дубу и закрыли глаза ...")

    print("Акт 2.\"Контракт с дьяволом\""
          "\nВы чувсвуйте холодное дуновение ветра, жажда больше вас не мучает. "
          "\nОткрыв глаза вы видете совсем не знакомое место. Вокруг стало темнее, ощущение что ночь."
          "\nПред вами предстает краснокаменная арка, за каторой лежит дорого из этого же керпича"
          "\nНа одном из столбов арки вы замечате пергамент, он гласит:",
          red(f"\nПриветсвую тебя {userclass} по имени {name}. Если ты очутился здесь, значит ты достоин."),
          f"\nДостоин пройти мое испытание, в конце которого тебя ждет награда.",
          f"\nЧтобы начать его, подпиши сей свиток кровью, пройди зквозь сие врата, и прояви свои наилучшие качества ",
          f"\nP.S. Не сворачивай с краснокаменной дороги, иначе ждет тебя смерть",
          green("\nСогласиться ли? Думаете вы.",),
          yellow("\n1.Подписать свиток и начать испытание"),
          yellow("\n2.Отказаться"))
    user_input = input()
    if user_input == "2":
        print("Вы разворачиваетесь и уходите",
              red("\n Конец игры"))
        exit()
    if user_input == "1":
        print(
            f"Великий {userclass} вытаскивает из ножен свой {mainInv[0]}, и острым лезвием делает рану на своем пальце."
            f"\nАккуратным движением руки выводит свое имя. Теперь внизу свитка красовалась ярко-алая надпись:"
            f"\n\"{name}\""
            f"\nЧерез мнгновение, кровь исчезла, и вспыхнул пергамент, и развеялся пепел его"
            f"\n\"Отступать некуда\" - думаете вы, ступая на краснокаменную дорогу")
    print("Акт 3. \"Мост\""
          "\nВы уже с час идете по подороге, вокруг вас густой лес, \"Пока слишком легко\" - думаете вы."
          "\nВы слышате журчание воды, пройдя еще немного, вы видите мост, алую реку, и неизвестное существо, что стоит посередине"
          f"\n\"Стой! Назовись сметрный\"- говорит великан, лицо которого походило на козла"
          f"\n\"Я великий {userclass} из Минас-Тирит, звать меня {name}\". "
          f"\n\"Чтобы дальше пройти ты должен ответы на мои загадки найти, иначе будешь поглощен водами великого Карнера\""
          f"\n\"Говори.\"- отвечаете вы",
          yellow(f"\nИтак первая гласит:\"Не отыскать её корней, Верхушка выше тополей. Всё круче вверх она идёт -А не растёт.\""),
          green(f"\nВторая:\"Без голоса кричит, Без крыльев - а летает, И безо рта свистит, И без зубов кусает.\""),
          red(f"\nТретья:\"Её не увидать, в руках не подержать, Не услышать ухом, не почуять нюхом. Царит над небесами, таится в каждой яме. "),
          red(f"\n         Она была в начале и будет после всех. Любую жизнь кончает и убивает смех\""),
          f"\nОтвет на загадки пиши c заглавной буквы в иминительном падеже")
    schet = 0
    while schet != 3:
        print(green("Введите ответ на первую загадку"))
        otvet1= input()
        if otvet1 == "Гора":
            print(blue("Правильно!"))
            schet += 1
            while schet != 3:
                print(green("Введите ответ на вторую загадку"))
                otvet2 = input()
                if otvet2 == "Ветер":
                    print(blue("Правильно!"))
                    schet += 1
                    while schet != 3:
                        print(green("Введите ответ на третью загадку"))
                        otvet3 = input()
                        if otvet3 == "Тьма":
                            print(blue("Правильно!"))
                            schet += 1
                        else:
                            print(red("Думаю ответ не правильный, надо подумать еще"))
                else:
                    print(red("Думаю ответ не правильный, надо подумать еще"))
        else:
            print(red("Думаю ответ не правильный, надо подумать еще"))

    print("\"КАК!? ТЫ СМОГ РАЗГАДТЬ ВСЕ ТРИ, ЕЩЕ НИКОМУ НЕ УДОВАЛОСЬ ЭТО СДЕЛАТЬ!\""
          f"\n\"Вижу мудрый ты {name}, Великий {userclass} из Минас-Тирита. Не смею я преграждать тебе путь\" "
          f"\nВеликан отходит в сторону, вы проходите мимо, пересекая кровавую реку. Путь предстаит долгий...")
    print("Акт 3\"Первый бой\""
          "\nВы продолжаете двигаться по дорого, вдруг, из темного леса, выпрыгивает Кархарот(волкоподобное существо) и преграждает вам путь"
          "\nВаши дейсвтия:")

    userHP = 100
    karahortHP = 100
    karahortDamage = 10
    while karahortHP > 0:
        print(yellow(f"1.Исползовать {mainInv[0]}"),
              yellow(f"\n2.Использовать {mainInv[1]}"))
        user_input = input()
        if user_input == "1":
            dam = weaponDamage[0]
            h = 0
        else:
            dam = weaponDamage[1]
            h = 1
        kubik = random.randint(1, 20)
        a = fight(dam, kubik)
        karahortHP -= a
        print(f"Используя {mainInv[h]} вы нанесли монстру", a, f"урона, где {dam} - урон оружия, {kubik} - доп урон, hp монстра - {karahortHP}")
        kubik = random.randint(1, 15)
        b = fight(karahortDamage, kubik)
        userHP -= b
        print("Карахорт, используя свои когти наносит вам урон равный", b, f"где {karahortDamage} - основной урон, {kubik} - доп урон, ваше здоровье - {userHP}")
        if userHP <= 0:
            print("Вас яростно растерзал Карахорт, вы мертвы"
                  "\n GAME OVER")
            exit()
    print("Победив Карахорта, вы обыскиваете его и находите странный пузырек красного цвета",
          green("\nЧто с ним сделать?"),
          yellow("\n1.Выпить, повысив здоровье до 100"),
          yellow("\n2.Положить в инвентар"))
    user_input = input()
    if user_input == "1":
        print(f"Здоровье было равно {userHP}, стало равно 100")
        userHP = 100
    if user_input == "2":
        mainInv.append("Зелье здоровья")
        print("К вам в инвнтарь было добавлено зелье здоровья. Теперь у вас в инвентаре есть"
              "\n", '(', ', '.join(mainInv),')')
    print("Была трудная битва, но вы смогли одолеть монстра и продолжаете двигаться дальше"
          "\n Справа вы видите опушку леса и маленький дом стоящий на ней. К домику ведет маленькая тропинка.", green("Может пойти посмотреть?"), yellow("\n1.Пойти посмотреть \n2.Проигнорировать"))
    user_input = input()
    if user_input == "1":
        print("Вы ступаете с дороги, проходите по тропинке и заходите в дом."
              "\n\"Вроде обыч...\" Не успеваете вы подумать как из неоткуда возникает темная фигура и говорит:"
              "\n\" А я ведь предупреждал, не сворачивай. Ты провалил испытание, и будешь теперь страдать в аду...\""
              "\n Вы нарушили главное правило испытания, за это вас забрал в ад дьявол.")
        exit()
    if user_input == "2":
        print("Вспомнив о предупреждении на том свитке, вы не решаетесь ивпытывать судбьу и проходите мимо")
    print("Акт 4.\"Странная шкатулка\""
          "\nНе поподясь в ловушку с домом, вы идете дальше. На дороге вы замечаете странную шкатулку"
          "\nПолнявши ее, вы замечаете странную кнопку:"
          "\n1.Попробовать открыть шкатулку силой"
          "\n2.Нажать на кнопку")
    user_input = input()
    if user_input == "1":
        print("Как бы вы сильно не старались, шкатулка не ломаеться, может все таки нажать на кнопку?"
              "\n2. Нажать на кнопку")
        user_input = input()
    if user_input == "2":
        print("Нажав на кнопку происходит следующее:")

        while user_input != "Друг":
            chastota = 500
            tire = 500
            tochka = 200

            winsound.Beep(chastota, tire)
            winsound.Beep(chastota, tire)
            time.sleep(0.7)
            winsound.Beep(chastota, tire)
            winsound.Beep(chastota, tire)
            winsound.Beep(chastota, tire)
            time.sleep(0.7)
            winsound.Beep(chastota, tochka)
            winsound.Beep(chastota, tire)
            winsound.Beep(chastota, tochka)
            winsound.Beep(chastota, tochka)
            time.sleep(0.7)
            winsound.Beep(chastota, tochka)
            winsound.Beep(chastota, tire)
            winsound.Beep(chastota, tire)
            time.sleep(0.7)
            winsound.Beep(chastota, tochka)
            winsound.Beep(chastota, tochka)
            time.sleep(0.7)
            winsound.Beep(chastota, tire)
            winsound.Beep(chastota, tochka)
            winsound.Beep(chastota, tochka)
            time.sleep(0.7)
            winsound.Beep(chastota, tochka)
            winsound.Beep(chastota, tire)
            winsound.Beep(chastota, tochka)
            time.sleep(0.7)
            winsound.Beep(chastota, tochka)
            winsound.Beep(chastota, tochka)
            winsound.Beep(chastota, tire)
            time.sleep(0.7)
            winsound.Beep(chastota, tire)
            winsound.Beep(chastota, tire)
            winsound.Beep(chastota, tochka)
            time.sleep(0.7)
            winsound.Beep(chastota, tochka)
            winsound.Beep(chastota, tochka)
            time.sleep(0.7)
            winsound.Beep(chastota, tire)
            winsound.Beep(chastota, tire)
            winsound.Beep(chastota, tire)
            time.sleep(0.7)
            winsound.Beep(chastota, tire)
            time.sleep(0.7)
            winsound.Beep(chastota, tire)
            winsound.Beep(chastota, tochka)
            winsound.Beep(chastota, tire)
            time.sleep(0.7)
            winsound.Beep(chastota, tochka)
            winsound.Beep(chastota, tire)
            winsound.Beep(chastota, tochka)
            time.sleep(0.7)
            winsound.Beep(chastota, tire)
            winsound.Beep(chastota, tire)
            winsound.Beep(chastota, tire)
            time.sleep(0.7)
            winsound.Beep(chastota, tochka)
            winsound.Beep(chastota, tire)
            winsound.Beep(chastota, tire)
            winsound.Beep(chastota, tire)
            print("Введите 1. Чтобы послушать еще раз или дайте ответ")
            user_input = input()
    print("Друг, проговариваете вы, с ухмылкой. Вдруг, кнопка странной коробки выдвинулась, где вы обнаружили", red(" странное кольцо"))
    print("Добавлен новый предмет в инвентарь")
    ring = "Странное кольцо"
    mainInv.append(ring)
    print("Надев его, вы ощущаете странное чувство. Будто организм стал здоровее, а оружие в руках держится крепче"
          f"\n Характеристики персонажа увеличины: базовый урон увеличен на 5")
    weaponDamage[0] += 5
    weaponDamage[1] += 5
    print("Акт 5. \"КОНЕЦ!?\""
          "\n Вот уже сутки вы надодитесь в пути. Усталости вы не чувствуете, вокруг всегда сумрак"
          "\n Когда же конец? - думаете вы, продолжая свой путь"
          "\n Вдруг, вы видете как обрывается дорога, дальше непроходимый лес"
          "\n \"Конец\ - проговариваете шопотом. \"Да не может быть\""
          "\n Выберите дейсвие:"
          "\n 1.Сойти с дороги и пойти в лес"
          "\n 2. Осмотреться")
    user_input = input()
    if user_input == "1":
        print("Вы нарушили правило испытания, сошли с дороги. кара немедленно настигла вас"
              "\n GAME OVER")
    if user_input == "2":
        print("Осматревшись, на полу вы замечаете торчащие керпичики в ряд. Всего их 6"
              "\n Вы встаете на него, он продавливется, встаете на другой, тот тоже продавливается и все два возврощаются в исходно положение"
              "\n Видимо здесь есть закономерност"
              "\n НУЖНО УГАДАТЬ ПОСЛЕДОВАТЕЛЬНОСТЬ"
              "\nНачинайте гаступать на кирпичики")
    key = ['1','2','3','4','5','6']
    key1 = []
    while key1 != ["2", '1', '6', '3', '5', '4']:
        user = input()
        if user == "2":
            key1.append("2")
            user = input()
            if user == "1":
                key1.append('1')
                user = input()
                if user == "6":
                    key1.append('6')
                    user = input()
                    if user == "3":
                        key1.append('3')
                        user = input()
                        if user == "5":
                            key1.append('5')
                            user = input()
                            if user == "4":
                                key1.append('4')
                                print("Получилось! Вы чувсвтуете как жрожжит земля под ногами...")
                                break
                            else:
                                print(red("Не правильный кирпич. ВСЕ кирпичи выдвинулись обратно"))
                                continue
                        else:
                            print(red("Не правильный кирпич. ВСЕ кирпичи выдвинулись обратно"))
                            continue
                    else:
                        print(red("Не правильный кирпич. ВСЕ кирпичи выдвинулись обратно"))
                        continue
                else:
                    print(red("Не правильный кирпич. ВСЕ кирпичи выдвинулись обратно"))
                    continue
            else:
                print(red("Не правильный кирпич. ВСЕ кирпичи выдвинулись обратно"))
                continue
        else:
            print(red("Не правильный кирпич. ВСЕ кирпичи выдвинулись обратно"))
            continue
    print("Из земли возникают врата, вы слышате чей - то голос за ними, войдя в них у увидели..."
          "\n ПРОДОЛЖЕНИЕ СЛЕДУЕТ")