<?php
    $filetxt = 'JSONs/list.json';

    $formdata = array(
        'username'=> $_POST['username'],
        'password'=> $_POST['password'],
        'email'=> $_POST['email'],
		'phone'=> $_POST['phone']
    );

    $arr_data = array();  
    $jsondata = file_get_contents($filetxt);
    $arr_data = json_decode($jsondata, true);
    $arr_data[] = $formdata;
    $jsondata = json_encode($arr_data, JSON_PRETTY_PRINT);
    file_put_contents('JSONs/list.json', $jsondata);

    $form_state['redirect'] = false;

?>