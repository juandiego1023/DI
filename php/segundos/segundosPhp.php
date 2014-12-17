   <?php

   echo "<form>";
   echo "<fieldset>";
   echo "<h2><center>Segundos recibidos</center></h2>";


       $segundosRecibidos = $_GET['segundos'];
      

      function conversorSegundosHoras($tiempo_en_segundos) {
		$horas = floor($tiempo_en_segundos / 3600);
		$minutos = floor(($tiempo_en_segundos - ($horas * 3600)) / 60);
		$segundos = $tiempo_en_segundos - ($horas * 3600) - ($minutos * 60);
 
		$hora_texto = "";
		if ($horas > 0 ) {
			$hora_texto .= $horas . "hora/s ";
		}
 
		if ($minutos > 0 ) {
			$hora_texto .= $minutos . "minuto/s ";
		}
 
		if ($segundos > 0 ) {
			$hora_texto .= $segundos . "segundo/s";
		}
 
	return $hora_texto;
	}
	
	echo "<center>".conversorSegundosHoras($segundosRecibidos)."</center>";



   echo"</form>";	
   echo"</fieldset>";

?>
