   <?php

   echo "<form>";
   echo "<fieldset>";
   echo "<h1><center>Datos personales (recibidos)</center></h1>";


       $nombre = $_GET['nombre'];

       $apellidos = $_GET['apellidos'];

       $posicionEdad=$_GET['edad'];	

	$edad = array(
	 1 => 'Menos de 20 años',
	 2 => 'Entre 20 y 39 años',
	 3 => 'Entre 40 y 59 años',
	 3 => '60 años o más' );

 	

       $peso = $_GET['peso'];

       $sekso= $_GET['sekso'];

       $estadoCivil=$_GET['estadoCivil'];

       $aficiones=$_GET['aficion'];

       

       echo "<br/>   Nombre: ". $nombre;

       echo "<br/>   Apellidos: ". $apellidos;

       echo "<br/>   Edad: ". $edad[$posicionEdad]."<br/>";

       echo "<br/>   Peso: ". $peso;

       echo "<br/>   Sexo: ". $sekso;

       echo "<br/>   Estado civil: ". $estadoCivil;

       echo "<br/>   Aficion: ";
       foreach($aficiones as $aficion){
       	echo $aficion;
       }

	




   echo"</form>";	
   echo"</fieldset>";

?>
