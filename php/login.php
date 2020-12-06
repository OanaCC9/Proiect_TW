<?php
if(isset($_POST['signup-submit'])){

    require 'DB.php';

    $username = $_POST['uid'];
    $password = $_POST['pwd'];

    if(empty($username) || empty($password)) {
        header("Location: login.php?error=emptyfields&uid=".$username."&email=".$email);
        exit();
    }
    else if(!filter_var($email, FILTER_VALIDATE_EMAIL) && !preg_match("/^[a-zA-Z0-9]*$/", $username)){
        header("Location: Signup.html?error=invaliduidmailuid");
        exit();
    }
    else if(!filter_var($email, FILTER_VALIDATE_EMAIL)){
        header("Location: Signup.html?error=invalidmail&uid=".$username);
        exit();
    }
    else if(!preg_match("/^[a-zA-Z0-9]*$/", $username)){
        header("Location: Signup.html?error=invaliduid&email=".$email);
        exit();
    }
    else if($password !== $passwordRepeat){
        header("Location: Signup.html?error=passwordcheckuid=".$username);
        exit();
    }
    else {

        $sql = "SELECT username FROM sign_in WHERE username=?";
        $stmt = mysqli_stmt_init($conn);
        if (!mysqli_stmt_prepare($stmt,$sql)) {
            header("Location: Signup.html?error=sqlerror");
            exit();
        }
        else {
            mysqli_stmt_bind_param($stmt, "s", $username);
            mysqli_stmt_execute($stmt);
            mysqli_stmt_store_result($stmt);
            $resultCheck = mysqli_stmt_num_rows($stmt);
            if ($resultCheck > 0) {
                header("Location: Signup.html?error=userTaken&mail=".$email);
                exit();
            }
            else {
                $sql = "INSERT INTO sign_in (username, mail, pwd) VALUES (?, ?, ?)";
                $stmt = mysqli_stmt_init($conn);
                if (!mysqli_stmt_prepare($stmt,$sql)) {
                    header("Location: Signup.html?error=sqlerror");
                    exit();
                }
                else {
                    $hashedPwd = password_hash($password, PASSWORD_DEFAULT);
                    mysqli_stmt_bind_param($stmt, "sss", $username, $email, $hashedPwd);
                    mysqli_stmt_execute($stmt);
                    header("Location: Signup.html?signup=success");
                    exit();
                }
            }
        }
    }

    mysqli_stmt_close($stmt);
    mysqli_close($conn);

}

else{
    header("Location: Signup.html?signup=success");
                    exit();
}