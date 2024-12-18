# Анализ на производителността на BG GPT 2.6B модел

## Архитектура и спецификации
- **Базов модел**: LLaMA архитектура
- **Размер**: 2.6 милиарда параметра
- **Интерфейс**: Chainlit чат интерфейс
- **Език**: Български

## Тестова среда
- **Процесор**: Intel(R) Core(TM) i7-6700HQ CPU @ 2.60GHz
- **Ядра**: 4 физически ядра / 8 логически нишки (с Hyper-Threading)
- **RAM**: 16.0 GB
- **Операционна система**: Windows 10 64-bit

## Анализ на запитванията

| Запитване | Текст на запитване | Токени | Време (сек) | Токени/сек |
|-----------|-------------------|---------|-------------|-------------|
| 1 | Какво знаеш за Уникредит Булбанк? | 117 | 36.73 | 3.19 |
| 2 | Традиционни български ястия | 27 | 7.03 | 3.84 |
| 3 | Какво е ракия? | 77 | 21.93 | 3.51 |
| 4 | Дай ми финансов съвет | 47 | 14.43 | 3.26 |

## Производителност

### Време за зареждане
- **Константно време**: 5523.04 ms (5.5 секунди)
- **Стабилност**: Консистентно време за зареждане при всички тестове

### Скорост на генериране
- **Средна скорост**: 3.45 токена в секунда
- **Най-висока скорост**: 3.84 токена/сек (кратки запитвания)
- **Най-ниска скорост**: 3.19 токена/сек (дълги запитвания)

### Латентност
- **Prompt eval time**: ~0.00 ms
- **Първоначален отговор**: Незабавен след зареждане

## Наблюдения и изводи

1. **Производителност според типа запитване**:
   - Кратки запитвания се обработват по-ефективно
   - Финансови теми изискват повече време за обработка
   - Културни теми се генерират по-бързо

2. **Стабилност**:
   - Консистентно време за зареждане
   - Предвидима производителност
   - Надеждна работа без прекъсвания

3. **Ограничения**:
   - CPU-базирано изпълнение ограничава максималната скорост
   - Времето за генериране расте линейно с дължината на отговора

## Графично представяне на скоростта

```
Скорост (токени/сек)
4.0 |    *
3.8 |      *
3.6 |        *
3.4 |          *
3.2 |            *
3.0 |              
    +----------------
     1  2  3  4  
     Номер на запитване
```

## Препоръки за оптимизация
- Добавяне на GPU ускорение
- Оптимизация на размера на контекста
- Кеширане на често използвани заявки
- Балансиране на натоварването при множество заявки

Моделът показва стабилна производителност за CPU-базирано изпълнение, с добър баланс между скорост и качество на генерираните отговори.