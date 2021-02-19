<?php
if ($_GET['user'] != 'me') exit;

echo <<< END
<html>
<head>
    <meta charset="UTF-8">
    <title>Добавить поселок</title>
    <link rel="stylesheet" href="style.css">
</head>

<body>
<h1><b>Добавить поселок</b></h1>
<form method="post" action="addVillage.php?user=me">
    
    Введите название экопоселка:<br>
    <input type="text" name="village_name"><br>
    Введите адрес поселка:<br>
    <input type="text" name="village_address"><br>
    
    <input type="submit" name="Отправить">
</form><br>
</body>
</html>

END;

?>