<?php
if ($_GET['user'] != 'me') exit;
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

$query = "INSERT INTO `villages` (village_name, village_address)
VALUES (?, ?)";

// Соединение и проверка
$link = mysqli_connect(HOST, USER, PASSWORD, DATABASE);
if ($link->connect_errno) {
    echo "Не удалось подключиться к MySQL: (" . $link->connect_errno . ") " . $link->connect_error; }

// Подготовка запроса
if (!($stmt = $link->prepare($query))) {
    echo "Не удалось подготовить запрос: (" . $link->errno . ") " . $link->error; }

// Выполнение запроса
if (!($stmt->bind_param('ss', $village_name, $village_address))) {
    echo "Не удалось привязать параметры: (" . $stmt->errno . ") " . $stmt->error;}

if (!($stmt->execute())) {
    echo "Не удалось выполнить запрос: (" . $stmt->errno . ") " . $stmt->error;}

$stmt->close();
mysqli_close($link);
header('Location: /?user=me');

