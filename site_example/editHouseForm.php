<?php

if ($_GET['user'] != 'me') exit;

echo <<< END
<html>
<head>
    <meta charset="UTF-8">
    <title>Редактировать дом</title>
    <link rel="stylesheet" href="style.css">
</head>

<body>
<h1><b>Редактировать дом id {$_GET['id']}</b></h1>
<form method="post" action="editHouse.php?user=me&id={$_GET['id']}">
    Выберите экопоселок:<br>
    <p><select name="village_name" size="1">
            <option selected value="Green_eagle">Green_eagle</option>
            <option value="Green_cherry">Green_cherry</option>
        </select><br>
        Введите модель дома:<br>
        <input type="text" name="house_model" value="Zyland M"><br>
        Введите количество модулей дома:<br>
        <input type="number" name="moduls_count" value="2" step="1" min="1" max="50"><br>
        Введите общую площадь дома:<br>
        <input type="number" name="total_area" value="100" step="1" min="1" max="500"><br>
        Введите отапливаемую площадь дома:<br>
        <input type="number" name="living_area" value="50" step="1" min="1" max="500"><br>
        Введите количество этажей:<br>
        <input type="number" name="floors" value="1" step="1" min="1" max="5"><br>
        Введите цену аренды:<br>
        <input type="number" name="rent_price" value="30000" step="1" min="1" max="100000"><br>
        Введите цену продажи:<br>
        <input type="number" name="sell_price" value="1800000" step="1" min="1" max="50000000"><br>
        Введите количество спальных мест:<br>
        <input type="number" name="sleeping_areas" value="3" step="1" min="1" max="50"><br>
        Введите отопление:<br>
        <input type="text" name="heating" value="ИК-обогреватели"><br>
        Введите количество ванных комнат:<br>
        <input type="number" name="bathroom_count" value="1" step="1" min="1" max="5"><br>
        Введите количество террас:<br>
        <input type="number" name="terrace_count" value="1" step="1" min="1" max="5"><br>
        Введите количество спален:<br>
        <input type="number" name="bedroom_count" value="1" step="1" min="1" max="5"><br>

        <input type="submit" name="Отправить">
</form><br>
</body>
</html>

END;

?>
