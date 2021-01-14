<?php
if ($_GET['user'] != 'me' and !$_GET['village_name'] and !$_GET['id_village']) exit;
require_once('connections.php');

function sanitizeString($var) {
    $var = stripslashes($var);
    $var = strip_tags($var);
    $var = htmlentities($var, ENT_QUOTES, utf8_unicode_ci);
    return $var; }

$village_name = isset($_POST['village_name']) ? $_POST['village_name'] : "";
$village_name = sanitizeString($village_name);

$village_address = isset($_POST['village_address']) ? $_POST['village_address'] : "";
$village_address = sanitizeString($village_address);

// Формулирование запроса
$query = "UPDATE villages SET village_name = '{$village_name}', village_address = '{$village_address}' WHERE id_village = '{$_GET['id_village']}'";


// Соединение и проверка
$link = mysqli_connect(HOST, USER, PASSWORD, DATABASE);
if ($link->connect_errno) {
    echo "Не удалось подключиться к MySQL: (" . $link->connect_errno . ") " . $link->connect_error; }

// Выполнение запроса
$result = mysqli_query($link, $query) or die("Ошибка " . mysqli_error($link));

// Выход
mysqli_close($link);
header('Location: /?user=me');