<?php

if ($_GET['user'] != 'me') exit;

echo <<< END
<html>
    <head>
        <title>Удалить дом</title>
        <link rel="stylesheet" href="style.css">
    </head>
</html>
END;

echo "<br><b>Удалить дом id {$_GET['id']}?</b>";
echo "<br><a href='delHouse.php?user=me&delete=yes&id={$_GET['id']}'>Да</a>";
echo "<br><a href='index.php?user=me'>Отмена</a><br>";