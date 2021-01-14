<?php
if ($_GET['user'] != 'me') exit;
require_once 'connections.php';


echo <<< END
<html>

<head>
    <meta charset="UTF-8">
    <title>Добавить мебель и технику</title>
    <link rel="stylesheet" href="style.css">
</head>

<body>
    <h1><b>Добавить мебель и технику</b></h1>

    <form method="post" action="addFurniture.php?user=me">
    Введите id дома:
    <input type="number" name="id" pattern="[0-9]{2,5}" step="1" min="1" title="От 2 до 5 цифр"><br>
    
    <h2><b>Ванная комната</b></h2>

    Количество унитазов:<br>
    <input type="number" name="toilet_count" value="1" step="1" min="0" max="5"><br>
    Модель унитаза:<br>
    <input type="text" name="toilet_model"><br>
    Количество ванн:<br>
    <input type="number" name="bathroom_count" value="1" step="1" min="0" max="5"><br>
    Модель ванн:<br>
    <input type="text" name="bathroom_model"><br>
    Количество раковин:<br>
    <input type="number" name="sink_count" value="1" step="1" min="0" max="5"><br>
    Модель раковин:<br>
    <input type="text" name="sink_model"><br>
    Количество стиральных машин:<br>
    <input type="number" name="washer_count" value="1" step="1" min="0" max="5"><br>
    Модель стиральных машин:<br>
    <input type="text" name="washer_model"><br>
    
    <h2><b>Кухня</b></h2>
    Количество холодильников:<br>
    <input type="number" name="refrigerator_count" value="1" step="1" min="0" max="5"><br>
    Модель холодильника:<br>
    <input type="text" name="refrigerator_model"><br>
    Количество раковин:<br>
    <input type="number" name="kitchen_sink_count" value="1" step="1" min="0" max="5"><br>
    Модель раковин:<br>
    <input type="text" name="kitchen_sink_model"><br>
    Количество плит:<br>
    <input type="number" name="stove_count" value="1" step="1" min="0" max="5"><br>
    Модель плит:<br>
    <input type="text" name="stove_model"><br>

    <h2><b>Спальня</b></h2>
    Количество кроватей:<br>
    <input type="number" name="bed_count" value="1" step="1" min="0" max="5"><br>
    Модель кроватей:<br>
    <input type="text" name="bed_model"><br>
    Количество шкафов:<br>
    <input type="number" name="cupboard_count" value="1" step="1" min="0" max="5"><br>
    Модель шкафов:<br>
    <input type="text" name="cupboard_model"><br>
    
    <input type="submit" name="Отправить">
    </form>
</body>
</html>


END;




