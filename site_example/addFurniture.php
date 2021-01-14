<?php
if ($_GET['user'] != 'me') exit;
require_once('connections.php');

$id = isset($_POST['id']) ? $_POST['id'] : "";
$id = sanitizeString($id);

$toilet_count = isset($_POST['toilet_count']) ? $_POST['toilet_count'] : "";
$toilet_count = sanitizeString($toilet_count);

$toilet_model = isset($_POST['toilet_model']) ? $_POST['toilet_model'] : "";
$toilet_model = sanitizeString($toilet_model);

$bathroom_count = isset($_POST['bathroom_count']) ? $_POST['bathroom_count'] : "";
$bathroom_count = sanitizeString($bathroom_count);

$bathroom_model = isset($_POST['bathroom_model']) ? $_POST['bathroom_model'] : "";
$bathroom_model = sanitizeString($bathroom_model);

$sink_count = isset($_POST['sink_count']) ? $_POST['sink_count'] : "";
$sink_count = sanitizeString($sink_count);

$sink_model = isset($_POST['sink_model']) ? $_POST['sink_model'] : "";
$sink_model = sanitizeString($sink_model);

$washer_count = isset($_POST['washer_count']) ? $_POST['washer_count'] : "";
$washer_count = sanitizeString($washer_count);

$washer_model = isset($_POST['washer_model']) ? $_POST['washer_model'] : "";
$washer_model = sanitizeString($washer_model);

$refrigerator_count = isset($_POST['refrigerator_count']) ? $_POST['refrigerator_count'] : "";
$refrigerator_count = sanitizeString($refrigerator_count);

$refrigerator_model = isset($_POST['refrigerator_model']) ? $_POST['refrigerator_model'] : "";
$refrigerator_model = sanitizeString($refrigerator_model);

$kitchen_sink_count = isset($_POST['kitchen_sink_count']) ? $_POST['kitchen_sink_count'] : "";
$kitchen_sink_count = sanitizeString($kitchen_sink_count);

$kitchen_sink_model = isset($_POST['kitchen_sink_model']) ? $_POST['kitchen_sink_model'] : "";
$kitchen_sink_model = sanitizeString($kitchen_sink_model);

$stove_count = isset($_POST['stove_count']) ? $_POST['stove_count'] : "";
$sink_count = sanitizeString($sink_count);

$stove_model = isset($_POST['stove_model']) ? $_POST['stove_model'] : "";
$stove_model = sanitizeString($stove_model);

$bed_count = isset($_POST['bed_count']) ? $_POST['bed_count'] : "";
$bed_count = sanitizeString($bed_count);

$bed_model = isset($_POST['bed_model']) ? $_POST['bed_model'] : "";
$bed_model = sanitizeString($bed_model);

$cupboard_count = isset($_POST['cupboard_count']) ? $_POST['cupboard_count'] : "";
$cupboard_count = sanitizeString($cupboard_count);

$cupboard_model = isset($_POST['cupboard_model']) ? $_POST['cupboard_model'] : "";
$cupboard_model = sanitizeString($cupboard_model);


function sanitizeString($var) {
    $var = stripslashes($var);
    $var = strip_tags($var);
    $var = htmlentities($var, ENT_QUOTES, 	utf8_unicode_ci);
    return $var; }

// Формулирование запроса
$query = "INSERT INTO `furniture` (id, toilet_count, toilet_model, bathroom_count, bathroom_model,
sink_count, sink_model, washer_count, washer_model, refrigerator_count, refrigerator_model, kitchen_sink_count,
kitchen_sink_model, stove_count, stove_model, bed_count, bed_model, cupboard_count, cupboard_model)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)";

// Соединение и проверка
$link = mysqli_connect(HOST, USER, PASSWORD, DATABASE);
if ($link->connect_errno) {
    echo "Не удалось подключиться к MySQL: (" . $link->connect_errno . ") " . $link->connect_error; }

// Подготовка запроса
if (!($stmt = $link->prepare($query))) {
    echo "Не удалось подготовить запрос: (" . $link->errno . ") " . $link->error; }

// Выполнение запроса
if (!($stmt->bind_param('isisisisisisisisis', $toilet_count, $toilet_model, $bathroom_count, $bathroom_model,
    $sink_count, $sink_model, $washer_count, $washer_model, $refrigerator_count, $refrigerator_model, $kitchen_sink_count,
    $kitchen_sink_model, $stove_count, $stove_model, $bed_count, $bed_model, $cupboard_count, $cupboard_model))) {
    echo "Не удалось привязать параметры: (" . $stmt->errno . ") " . $stmt->error;}

if (!($stmt->execute())) {
    echo "Не удалось выполнить запрос: (" . $stmt->errno . ") " . $stmt->error;}

$stmt->close();
mysqli_close($link);
header('Location: /?user=me');
