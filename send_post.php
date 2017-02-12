<?php
//Connecting to sql db.
$connect = mysqli_connect(".\ADITYA","","","SMART.dbo.SMART_Registrations");
//Sending form data to sql db.
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 

$sql = "INSERT INTO MyGuests (Username, Password, Email, Phone)
VALUES ('John', 'Doe', 'john@example.com', '22222222')";

if ($conn->query($sql) === TRUE) {
    echo "New record created successfully";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();

?>