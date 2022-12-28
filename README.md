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

## 📌 CP

<div align="center">

  ​​​​​​</br>![image](https://user-images.githubusercontent.com/121574230/209855743-c2c91271-c4a0-4a9a-8659-6f7925336731.png)
  
</div>

Простенькая задачка на кодировку. Исходя из текста задачи + логики, понимаем, что ето russian language, значит декодим эти кракозябры на любом сайте с кодировкой WINDOWS-1251, например тут: https://2cyr.com/decode.

**Получаем флаг:** `Всем здарова! Представляем наш новый Флаг: три шесть шесть семь ноль два восемь`

## 📌 Warmup

<div align="center">

  ​​​​​​</br>![image](https://user-images.githubusercontent.com/121574230/209856859-8695b572-9bbf-41c2-803f-66471059a431.png)
  
</div>

Открываем txt и видим, что это base64, декодим и получаем небольшой текст с **флагом в конце**: 

`Flag is: 107d9d2175de7e82106313328ca0e291`

## 📌 Basic Workout

<div align="center">

  ​​​​​​</br>![image](https://user-images.githubusercontent.com/121574230/209857292-b36adcee-5b54-484c-aafc-462e6959d0e2.png)

</div>

Задача на знание кодировок base2, base16, base32, base58, base64, base256. Тупо выбираем правильные и получаем **флаг**: `spbctf{b4s1c_flag_1s_s0_bas1c}`

## 📌 *ML

<div align="center">

  ​​​​​​</br>![image](https://user-images.githubusercontent.com/121574230/209857666-5e921f08-cb85-4db8-95a5-b2fd88067cab.png)

</div>

HTML Escape. Закидываем на сайт https://dencode.com и получаем **флаг**: `spbctf{*mL_eNt1t1t1t1t1t1t1t1t11t1tt1}`

## 📌 Caesar

<div align="center">

  ​​​​​​</br>![image](https://user-images.githubusercontent.com/121574230/209857974-ace58487-a1a8-4c99-a777-898745aabf12.png)

</div>

Нам подсказывают, шо это шифр Цезаря. Идем сюда: https://planetcalc.ru/1434, ищем подходящий сдвиг и коммитим **флаг**: 

`Поздравлос! Флаг: девять восемь три один три три семь один два три!`

## 📌 Fried Pig

<div align="center">

  ​​​​​​</br>![image](https://user-images.githubusercontent.com/121574230/209858412-d19c42ba-5ea0-43b9-af48-8b5472126ab1.png)

</div>

Переходим по ссыли, копируем текст и анализируем его тут: https://www.dcode.fr/cipher-identifier, осознаем, что это шифр бекон 🥓, расшифровываем и собираем **флаг**: `spbctf{ILIKETOEATBACONFORBREAKFAST}`

![image](https://user-images.githubusercontent.com/121574230/209858816-59ef5ea0-5cf0-4e54-867a-78188cfe7847.png)

## 📌 @bash

<div align="center">

  ​​​​​​</br>![image](https://user-images.githubusercontent.com/121574230/209859101-d0419d32-55a2-4b73-84c2-ef29550c4ed4.png)

</div>
