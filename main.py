import telebot
from telebot import types

API_TOKEN = '5554445689:AAEcSZr4BCBMcEVGGaGXaaKs62NRZWTtNhI'

bot = telebot.TeleBot(API_TOKEN)

# Переместил Ваши кнопки и клавиатуры отдельно от кода.
kb = types.InlineKeyboardMarkup(row_width=1)
alcohol_types = types.InlineKeyboardButton(text='Производство алкоголя', callback_data='alcohol_types')
kb.add(alcohol_types)

kb1 = types.InlineKeyboardMarkup(row_width=1)
botany = types.InlineKeyboardButton(text='Ботаникалы', callback_data='botany')
kb1.add(botany)

kb2 = types.InlineKeyboardMarkup(row_width=1)
fruits = types.InlineKeyboardButton(text='Фрукты и ягоды', callback_data='fruits')
kb2.add(fruits)

kb3 = types.InlineKeyboardMarkup(row_width=1)
corn = types.InlineKeyboardButton(text='Зерновые', callback_data='corn')
kb3.add(corn)

kb4 = types.InlineKeyboardMarkup(row_width=1)
grape = types.InlineKeyboardButton(text='Виноград', callback_data='grape')
kb4.add(grape)

kb5 = types.InlineKeyboardMarkup(row_width=1)
fermentation = types.InlineKeyboardButton(text='Ферментация', callback_data='fermentation')
kb5.add(fermentation)

kb6 = types.InlineKeyboardMarkup(row_width=1)
kombucha = types.InlineKeyboardButton(text='Комбуча', callback_data='kombucha')
kb6.add(kombucha)

kb7 = types.InlineKeyboardMarkup(row_width=1)
distillation = types.InlineKeyboardButton(text='Дистилляция', callback_data='distillation')
kb7.add(distillation)

kb8 = types.InlineKeyboardMarkup(row_width=1)
pot_still = types.InlineKeyboardButton(text='Пот Стилл', callback_data='pot_still')
kb8.add(pot_still)

kb9 = types.InlineKeyboardMarkup(row_width=1)
rectification = types.InlineKeyboardButton(text='Ректификация', callback_data='rectification')
kb9.add(rectification)

kb10 = types.InlineKeyboardMarkup(row_width=1)
excerpt = types.InlineKeyboardButton(text='Выдержка', callback_data='excerpt')
kb10.add(excerpt)

kb11 = types.InlineKeyboardMarkup(row_width=1)
maceration = types.InlineKeyboardButton(text='Мацерация', callback_data='maceration')
kb11.add(maceration)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Приветствую вас на обучающем курсе по барному ассортименту ресторана Телеграф.",
                     reply_markup=kb)


# Функция callback_query_handler вносится один раз для обработки всех событий
@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    if call.data == 'alcohol_types':
        file = open('alcohol_types.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file,
                       'Выделяют 4 группы сырья для производства алкоголя. Разберем каждую отдельно.', reply_markup=kb1)
    elif call.data == 'botany':
        bot.send_message(call.message.chat.id,
                         'Большое количество алкогольных напитков получают на основе растений. Например: текила, ром, мескаль. '
                         'Как правило, из растений добывают сладкий сок, который сбраживают, а затем перегоняют',
                         reply_markup=kb2)
        # Переход дальше не настроен, вы можете ссылаться на свои дальнейшие блоки или же вернуться к главному меню.
    elif call.data == 'fruits':
        bot.send_message(call.message.chat.id,
                         'Из большинства фруктов можно получать различные алкогольные напитки. '
                         'Самыми известными напитками на основе фруктов являются такие напитки как: '
                         'кальвадос, сидр, кирш, фруктовые шнапсы, сливовица и прочие плодовые дистилляты.',
                         reply_markup=kb3)
    elif call.data == 'corn':
        bot.send_message(call.message.chat.id,
                         'Виски, джин, водку делают на основе зерна. '
                         'Самое используемое зерно — ячмень, который содержит большое количество крахмала в сердцевине. '
                         'Во время проращивания зерна крахмал превращается в сахара, необходимые для брожения. '
                         'Также часто используют кукурузу, пшеницу, рис.',
                         reply_markup=kb4)
    elif call.data == 'grape':
        bot.send_message(call.message.chat.id,
                         'Большое количество алкогольных напитков производят на основе винограда: '
                         'тихие вина, игристые вина, портвейн, херес, вермут, марсала, коньяк, арманьяк, граппа, бренди, марк, писко, чача...'
                         'На данный момент выделено около 10 тысяч сортов винограда, из которого делают алкоголь. '
                         'Винные ягоды должны обладать определенными качествами, например, стабильной и высокой урожайностью, '
                         'определенными вкусовыми свойствами и своеобразным сортовым ароматом. '
                         'У винного винограда толстая кожица, небольшой размер ягод и большее содержание сахара',
                         reply_markup=kb5)
    elif call.data == 'fermentation':
        file1 = open('fermentation.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file1,
                       'Ферментация - это процесс, когда микроорганизмы (бактерии, дрожжи, плесень) '
                       'превращают сахар в другое вещество при отсутствии кислорода. Само слово в переводе с латинского означает "до кипения". '
                       'Так древние римляне описали процесс брожения вина по аналогии с кипением, когда увидели пузырящиеся чаны с виноградом.',
                       )
        bot.send_message(call.message.chat.id,
                         'За процесс брожения отвечают микроорганизмы – дрожжи, которые были открыты лишь в середине XIX века.'
                         'Путем брожения можно получать алкогольные напитки крепостью не выше 16% - от более высокой концентрации спирта дрожжи погибают.'
                         'Брожение — это довольно сложная химическая реакция, во время которой сахар преобразуется в этиловый спирт. '
                         'Результат этого процесса будет успешным лишь при строгом соблюдении температурного режима и правильно выбранной норме продуктов.'
                         'Температура воздуха в помещении во время брожения должна быть не ниже 18° С и не выше 24° С. '
                         'При более низкой температуре, особенно в начале процесса, процесс может затормозиться, так как холод замедляет жизнедеятельность дрожжей. '
                         'Если брожение приостановилось, хотя весь сахар еще не выбродил, нужно «разбудить» дрожжи, перемешав сусло, а затем поднять температуру до нормы. '
                         'Высокая температура опасна для сусла, поскольку она губительно действует на жизнедеятельность дрожжей. '
                         'Даже понижение ее до нормы уже не возобновит процесс брожения.', reply_markup=kb6)
    elif call.data == 'kombucha':
        file2 = open('kombucha.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file2,
                       'Комбуча - это кислый и слегка газированный ферментированный напиток из подслащенного чая (традиционно).'
                       'Напиток зародился около 200 г до н.э. на территории современного Китая.'
                       ' Благодаря усилиям корейского врача Комбу, он попал в Японию. Название можно преревести, как "чай Комбу".'
                       'Исторически комбучу пили в Японии, Корее, КИтае, Вьетнаме и некоторых восточных частях России.',
                       reply_markup=kb7)

    elif call.data == 'distillation':
        file3 = open('distillation.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file3,
                       'Дистилляция – это процесс отделения спирта от примесей и воды. '
                       'Принцип дистилляции несложен, дело в том, что при нагревании спирт закипает раньше, чем вода. '
                       'Температура кипения спирта 78.3*. Затем спиртовые пары конденсируются, вновь превращаясь в жидкость.'
                       'Первые сведения о дистилляции относятся к I веку и упоминаются в работах греческих алхимиков в Александрии (Египет)',
                       reply_markup=kb8)
    elif call.data == 'pot_still':
        file4 = open('cubes.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file4,
                       'Пот Стилл – это самый первый способ получения крепкого спирта, который придумал человек. Для осуществления этого типа перегонки используют медный аппарат pot still (пот стилл).'
                       'Принцип дистилляции заключается в следующем:'
                       '❗️Разница температур кипения фракций'
                       '❗️Испарение жидкости с последующим охлаждением и конденсацией паров.'
                       'Для осуществления перегонки вино или брагу заливают в емкость с подогревом и начинают нагревать, '
                       'алкогольные пары поднимаются в верхнюю часть емкости, где находится изогнутая трубка (лебединая шея), а затем конденсируются в змеевике.')
        bot.send_message(call.message.chat.id,
                         'После первой перегонки, как правило, крепость спирта 28-30%. В процессе перегонки мастер дистилляции отделяет начальные '
                         '(«головы») и конечные («хвосты») фракции перегонки, оставляя лишь самый крепкий и чистый спирт («сердце перегона»). '
                         'При такой перегонке трудно сразу получить спирт высокой крепости и отделить его от примесей, поэтому традиционную перегонку совершают несколько раз.'
                         'На выходе мы получаем дистиллят крепостью 72%, который обладает органолептическими свойствами исходного сырья. Цифра 72% означает, сколько в литре   процентов спирта.'
                         ' В данном случае у нас 72% спирта, а остальные 28% - это примеси, которые и передают вкусо-ароматические свойства сырья.'
                         'Данный метод перегонки используют для таких напитков как: бренди, коньяк, виски, некоторые виды рома, плодовые дистилляты, в меньшей степени текилу.',
                         reply_markup=kb9),
    elif call.data == 'rectification':
        file5 = open('distillation2.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file5,
                       'Непрерывная перегонка - Этот способ дистилляции был изобретен в середине XIX века. '
                       'Для перегонки используют аппарат, названный в честь создателя «Coffey still» или «Patent still» или «колонны непрерывного цикла». '
                       'Сегодня большая часть питьевого спирта производится именно этим способом, так как данный способ позволяет производить алкоголь в больших количествах. '
                       'Этот аппарат сделан из нержавейки и представляет из себя колонны высотой до 20 м, расположенные парами. С одной стороны в эти колонны поступает охлажденная брага, а с другой стороны вытекает спирт.')
        bot.send_message(call.message.chat.id,
                         ' Внутри одной из колонн находятся медные тарелки, по которым стекает подаваемая брага, на встречу браге подается разогретый пар. '
                         'Нагретый пар забирает из браги пары алкоголя и поднимается вверх, а остатки бражки (примеси падают вниз). Пары алкоголя и водяные пары поступают во вторую колонну (ректификатор) где и конденсируются. '
                         'На выходе крепость получаемого спирта 98% и такой спирт содержит минимальное количество примесей. Этот аппарат работает до тех пор пока подают брагу и горячий спирт.'
                         'Непрерывной перегонкой получают водочный спирт, спирт для производства джина, водки и некоторых разновидностей текилы и рома.',
                         reply_markup=kb10)
    elif call.data == 'excerpt':
        file6 = open('excerpt.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file6,
                       'Во время хранения спиртного напитка в дубовой бочке, со спиртом происходят изменения, влияющие на его качества, характеристики и свойства:'
                       '- окисление (Благодаря тому, что дубовая бочка имеет поры, дистиллят активно контактирует с кислородом и в нём образуются новые соединения которые улучшают свойства напитка.'
                       '- сложные реакции образования веществ (Под воздействием температуры и кислорода, во время выдержки алкогольный напиток приобретает особый вкус, аромат, цвет и послевкусие.)'
                       '- последняя стадия процесса изготовления алкогольного напитка, дающая ему до 70% аромата (и цвета) .',
                       reply_markup=kb11)
    elif call.data == 'maceration':
        file7 = open('maceration.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file7,
                       'Мацерация - это настаивание растительного сырья (трав, специй, кореньев, фруктов, ягод и т.д.) на спирту.')


if __name__ == '__main__':
    # schedule.every().day.at('22:11').do(send_message)
    # Thread(target=schedule_checker).start()
    bot.infinity_polling()
