<?php

session_start();

echo '<style>

div {
	width: 30%;
	margin: 10% 35%;
	text-align: center;
	font-size: 28px;
}

input[type=submit]{

	font-size: 18px;
	border: none;
	padding: 10px 20px;
	border-radius: 2px;
	cursor: pointer;
	background: blue;
	color: #fff;
}

input[type=text]{
	font-size: 18px;
	width: 40px;
}

</style>';

echo "<div><p>Ой... От Вас большое кол-во запросов</p>";


if(empty($_POST['result']) || empty($_POST['send'])){

mt_srand ((double) microtime() * 1000000);
$p1 = mt_rand(1,10);
$p2 = mt_rand(1,10);

$_SESSION['result']=$p1+$p2;


echo'
<form method="post" action="">
<span>'.$p1.'</span>
<span>+</span>
<span>'.$p2.'</span>
<span>=</span>
<input type="text" name="result" maxlength="2">
<input type="submit" name="send" value="Снять блокировку">
</form></div>
';
}else{

	if ($_SESSION['result']==$_POST['result']){

		$IP = $_SERVER['REMOTE_ADDR'];	
		$comm = "./update.sh ".$IP;
		if(system($comm)) echo "OK...";
		 exit("<meta charset=utf-8><meta http-equiv='Refresh' content='2, URL=http://info-linux.ru:8080'>");

	}else{
		$_SESSION['result']='';
		echo "<p>Попробуйте еще раз...</p>";
		 exit("<meta charset=utf-8><meta http-equiv='Refresh' content='2, URL=http://ban.info-linux.ru:8080/ban/index.php'>");
	}

}



