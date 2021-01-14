<?php

if ($_GET['user'] != 'me' and !($_GET['village_name']) and !($_GET['id_village'])) exit;

echo <<< END
<html>
<head>
    <meta charset="UTF-8">
    <title>Редактировать поселок</title>
    <link rel="stylesheet" href="style.css">
</head>

<body>
<h1><b>Редактировать поселок {$_GET['village_name']} id {$_GET['id_village']}</b></h1>
<form method="post" action="addVillage.php?user=me&village_name=village_name&id_village={$_GET['id_village']}">
    Введите имя поселка:<br>
    <input type="text" name="village_name" value="{$_GET['village_name']}"><br>
    Введите адрес поселка:<br>
    <input type="text" name="village_address"><br>
    
    <input type="submit" name="Отправить">
</form><br>
</body>
</html>

END;

?>
