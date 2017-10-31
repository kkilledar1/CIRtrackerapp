<?php

$method =$_Server['REQUEST_METHOD'];

if($method="POST){
	$requestBody= file_get_contents ('php://input');
	$jason=json_decode($requestBody);

	$Text=$json->result->parameters->Text;
 
         switch ($Text) {
           case 'hi':
        	$speech ="Hi,Nice to meet you";
			break;

		case 'bye'
			$speech ="Bye,good night";
			break;

		default:
			$speech = "sorry, I did not get that"
			break;
	}


        $response = new \stdClass ();
        $response->speech ="";
	$response->displayText ="";
	$response->source ="webhook";
	echo json_encode($response);

}
else
{
echo "Method not allwoed"
}


?>
