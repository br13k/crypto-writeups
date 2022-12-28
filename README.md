<div align="center">

# Криптография. Разборы задач с forkbomb.

</div>

# 📌 Menu
- [CP](https://github.com/br13k/writeups#-cp)
- [Warmup](https://github.com/br13k/writeups#-warmup)
- [Basic Workout](https://github.com/br13k/writeups#-basic-workout)
- [*ML](https://github.com/br13k/writeups#-ml)
- [Caesar](https://github.com/br13k/writeups#-caesar)
- [Fried Pig](https://github.com/br13k/writeups#-fried-pig)
- [@bash](https://github.com/br13k/writeups#-bash)
- [Not easy](https://github.com/br13k/writeups#-not-easy)
- [Чай](https://github.com/br13k/writeups#-чаек)
- [PEMogite](https://github.com/br13k/writeups#-pemogite)
- [128 is new black](https://github.com/br13k/writeups#-128-is-new-black)
- [Bread 1](https://github.com/br13k/writeups#-bread-1)
- [P*Q=ban](https://github.com/br13k/writeups#-pqban)
- [Recursion](https://github.com/br13k/writeups#-recursion)

## 📌 CP

<div align="center">

  ​​​​​​</br>![image](https://user-images.githubusercontent.com/121574230/209855743-c2c91271-c4a0-4a9a-8659-6f7925336731.png)
  
</div>

Простенькая задачка на кодировку. Исходя из текста задачи + логики, понимаем, что ето russian language, значит декодим эти кракозябры с кодировкой WINDOWS-1251, например тут: https://2cyr.com/decode.

**Получаем флаг:** `Всем здарова! Представляем наш новый Флаг: три шесть шесть семь ноль два восемь`

[Menu](https://github.com/br13k/writeups#-menu)

## 📌 Warmup

<div align="center">

  ​​​​​​</br>![image](https://user-images.githubusercontent.com/121574230/209856859-8695b572-9bbf-41c2-803f-66471059a431.png)
  
</div>

Открываем txt и видим, что это base64, декодим и получаем небольшой текст с **флагом в конце**: 

`Flag is: 107d9d2175de7e82106313328ca0e291`

[Menu](https://github.com/br13k/writeups#-menu)

## 📌 Basic Workout

<div align="center">

  ​​​​​​</br>![image](https://user-images.githubusercontent.com/121574230/209857292-b36adcee-5b54-484c-aafc-462e6959d0e2.png)

</div>

Задача на знание кодировок base2, base16, base32, base58, base64, base256. Тупо выбираем правильные и получаем **флаг**: `spbctf{b4s1c_flag_1s_s0_bas1c}`

[Menu](https://github.com/br13k/writeups#-menu)

## 📌 *ML

<div align="center">

  ​​​​​​</br>![image](https://user-images.githubusercontent.com/121574230/209857666-5e921f08-cb85-4db8-95a5-b2fd88067cab.png)

</div>

HTML Escape. Закидываем на сайт https://dencode.com и получаем **флаг**: `spbctf{*mL_eNt1t1t1t1t1t1t1t1t11t1tt1}`

[Menu](https://github.com/br13k/writeups#-menu)

## 📌 Caesar

<div align="center">

  ​​​​​​</br>![image](https://user-images.githubusercontent.com/121574230/209857974-ace58487-a1a8-4c99-a777-898745aabf12.png)

</div>

Нам подсказывают, шо это шифр Цезаря. Идем сюда: https://planetcalc.ru/1434, ищем подходящий сдвиг и коммитим **флаг**: 

`Поздравлос! Флаг: девять восемь три один три три семь один два три!`

[Menu](https://github.com/br13k/writeups#-menu)

## 📌 Fried Pig

<div align="center">

  ​​​​​​</br>![image](https://user-images.githubusercontent.com/121574230/209858412-d19c42ba-5ea0-43b9-af48-8b5472126ab1.png)

</div>

Переходим по ссыли, копируем текст и анализируем его тут: https://www.dcode.fr/cipher-identifier, осознаем, что это шифр бекон 🥓, расшифровываем и собираем **флаг**: `spbctf{ILIKETOEATBACONFORBREAKFAST}`

![image](https://user-images.githubusercontent.com/121574230/209858816-59ef5ea0-5cf0-4e54-867a-78188cfe7847.png)

[Menu](https://github.com/br13k/writeups#-menu)

## 📌 @bash

<div align="center">

  ​​​​​​</br>![image](https://user-images.githubusercontent.com/121574230/209859101-d0419d32-55a2-4b73-84c2-ef29550c4ed4.png)

</div>

Подсказка в названии таски. Идем сюда: https://dencode.com, находим Atbash и засылаем **флаг**: `SPbCTF{lol_this_is_atbash}` 

[Menu](https://github.com/br13k/writeups#-menu)

## 📌 Not easy

<div align="center">

  ​​​​​​</br>![image](https://user-images.githubusercontent.com/121574230/209859466-927ce44f-535f-4cb4-89fa-1f08b7890694.png)

</div>

Говорят, что это affine, ок, идем сюды: https://www.dcode.fr/affine-cipher, расшифровываем и получаем **флаг**: `spbctf{hello_i_am_such_affine_cipher}`

[Menu](https://github.com/br13k/writeups#-menu)

## 📌 Чаек

<div align="center">

  ​​​​​​</br>![image](https://user-images.githubusercontent.com/121574230/209860261-8ae82fb2-96a1-4e6d-89a0-d47c12d0986d.png)

</div>

ПеРеРыВ нА чАй

[Menu](https://github.com/br13k/writeups#-menu)

## 📌 PEMogite

<div align="center">

  ​​​​​​</br>![image](https://user-images.githubusercontent.com/121574230/209860365-9ab4801f-746c-4137-b79d-471566c43637.png)

</div>

Сертификат. Идем на волшебный сайт: https://certificatedecoder.dev, вставляем туды сертификат и получаем **флажочек**: `spbctf{x509_is_awesome}`

![image](https://user-images.githubusercontent.com/121574230/209860578-5b3f2b0d-531f-4c44-b6b0-b0035ede2517.png)

[Menu](https://github.com/br13k/writeups#-menu)

## 📌 128 is new black

<div align="center">

  ​​​​​​</br>![image](https://user-images.githubusercontent.com/121574230/209860823-0f5f8a0e-d358-43e2-a600-154fb21680a8.png)

</div>

RSA, добрались. Говорят, что ответ любой множитель, значит идем сюда: factordb.com, вставляем наш n и копируем любой **множитель(флаг)**: `12933562732354470203`

![image](https://user-images.githubusercontent.com/121574230/209861077-ce6fcf56-edfe-4aec-b58a-497154104c1e.png)

[Menu](https://github.com/br13k/writeups#-menu)

## 📌 Bread 1

<div align="center">

  ​​​​​​</br>![image](https://user-images.githubusercontent.com/121574230/209861308-9d6fc19e-e22e-4927-bf80-ac764ae6cb61.png)

</div>

Это бАзА. https://www.dcode.fr/rsa-cipher, вставляем n, d, c и получаем **флаг**: `spbctf{lost_in_ddddd}`

[Menu](https://github.com/br13k/writeups#-menu)

## 📌 P*Q=ban

<div align="center">

  ​​​​​​</br>![image](https://user-images.githubusercontent.com/121574230/209861691-8ff688e7-3db9-452f-a654-da92305d0760.png)

</div>

При помощи того же http://factordb.com находим p или q: 

`86686136056545304660994252432156625773889066120498168631765739416745482493422987585296192063723736599263002976567595657636575621223824796036376969022114262822476015189850335269173530996691468705957636088921107674849266001665959963924041156092676589677858275687705781389349325292821902667932773664074397025057056395971127798212868512036542986007381764450802738622888457263247853466350831762343657190118694660520926555651420001826960963517554742865635266192601411342660123373292705629287891375739175779053722758700760074451754576829084967851492233558979316397070894234154863263130900750980110998751294240297623797935181147`

![image](https://user-images.githubusercontent.com/121574230/209862040-8c429f09-871d-4aa0-86e2-0b359911428d.png)

[Menu](https://github.com/br13k/writeups#-menu)

## 📌 Recursion

<div align="center">

  ​​​​​​</br>![image](https://user-images.githubusercontent.com/121574230/209862202-c67636d2-867b-4169-aae4-545b23b9b428.png)

</div>

Скачиваем файлы страницы
![image](https://user-images.githubusercontent.com/121574230/209862348-8de042d6-b5b6-4536-aec6-8f8a87ddb589.png)

Видим папку со всеми фреймами, исследуем и обращаем внимание на файл с коротким названием:
![image](https://user-images.githubusercontent.com/121574230/209863873-10952a40-2a94-4c97-b112-052b61567cb7.png)

Открыв его, наблюдаем следующее:
![image](https://user-images.githubusercontent.com/121574230/209863904-7f766af9-2d53-4c5e-b51b-f7213926384a.png)

Делаем вывод, что именно на нем обрывается рекурсия, значит ищем файл, в котором он упоминается. Рукми это делать долго, т.к файлов всего сотня, значит пишем простой скриптец на Python:

```Python
  import os


  files = os.listdir('Task_files')

  for file in files:
    text = ''
    if file.find('.html') != -1:
      with open('Task_files/'+file, 'r', encoding='utf8') as file2:
        for line in file2:
          text += line
    if text.find('1337.html') != -1:
      print(file)
```

![image](https://user-images.githubusercontent.com/121574230/209864608-f55cf3b1-dbf2-4214-bf79-38a13655ce15.png)

В результате наблюдаем два названия: сам файл 1337.html и тот, в котором есть ссылка на него - это и есть наш **флаг**: `78628734`

**И задумываемся, а эта таска вообще на криптографию??**

![image](https://user-images.githubusercontent.com/121574230/209864961-2300e817-04e4-47f0-a664-b59323dbfa0f.png)

[Menu](https://github.com/br13k/writeups#-menu)


# 📌 ВСЁ!

<div align="center">

  ​​​​​​</br>![image](https://media.tenor.com/HoFb_jBbB48AAAAC/ералаш.gif)
  
</div>

