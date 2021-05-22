<?php

$name = $_POST['name'];
$email = $_POST['email'];
$subject = $_POST['subject'];
$message = $_POST['message']
$token = "1705544327:AAGWzHVDynzlbd9qBqKkRxhX6kSOBFyk5pE";
$chat_id = "-567901080";
$arr = array(
  'Name: ' => $name,
  'Email Адрес: ' => $email,
  'subject: ' => $subject,
  'Message: ' => $message
);

foreach($arr as $key => $value) {
  $txt .= "<b>".$key."</b> ".$value."%0A";
};

$sendToTelegram = fopen("https://api.telegram.org/bot{$token}/sendMessage?chat_id={$chat_id}&parse_mode=html&text={$txt}","r");

if ($sendToTelegram) {
  header('Location: index.html');
} else {
  echo "Error";
}
?>