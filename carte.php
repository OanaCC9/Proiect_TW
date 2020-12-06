<?php 
 if(isset($_GET['ID'])){
     require_once'../../require/connect133p.php';
     $ID = mysqli_real_escape_string($dbc, $_GET['ID']);

     $sql = "SELECT * FROM book WHERE image_ID='$ID'";
     $result = mysqli_querry($dbc, $sql) or die ("Bad Querry: $sql");
     $row = mysqli_fetch_array($result);

     

     $result = mysqli_querry($dbc, $sql) or die ("Bad Querry: $sql");

     if(isset($_GET['post'])){
         $name = mysqli_real_escape_string($dbc, $_GET['name']);
         $title = mysqli_real_escape_string($dbc, $_GET['title']);
         $post = mysqli_real_escape_string($dbc, $_GET['post']);

         $sql = "INSERT INTO ... (name, title ,comment, B_ID) values ('$name', '$title', '$post', '$ID');";
         $result = mysqli_querry($dbc, $sql) or die ("Bad Insert: $sql");
     }

    } else {
        header('Location: view.php');
    } 