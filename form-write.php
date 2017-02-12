$subject = $_POST['subject'];
$message = $_POST['message'];
$output = "Subject: {$subject}\n";
$output.= "Message: {$message}";
file_put_contents("form.txt",$output);