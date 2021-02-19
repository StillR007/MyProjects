<?php

if ($_GET['user'] != 'me') exit;

echo <<< END
<html>
    <head>
        <title>Удалить поселок</title>
        <link rel="stylesheet" href="style.css">
    </head>
</html>
END;

echo "<br><b>Удалить поселок {$_GET['village_name']}?</b>";
echo "<br><a href='delVillage.php?user=me&delete=yes&village_name={$_GET['village_name']}'>Да</a>";
echo "<br><a href='index.php?user=me'>Отмена</a><br>";
