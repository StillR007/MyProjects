<?phpif ($_GET['user'] == 'me' and $_GET['id'] and $_GET['delete'] == 'yes') {    require_once('connections.php');    $query = "DELETE FROM houses WHERE id = '{$_GET['id']}'";    $link = mysqli_connect(HOST, USER, PASSWORD, DATABASE)    or die("Ошибка " . mysqli_error($link));    $result = mysqli_query($link, $query) or die("Ошибка " . mysqli_error($link));    mysqli_close($link);} else exit();header('Location: /?user=me');?>