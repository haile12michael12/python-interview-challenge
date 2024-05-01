 <?php
    include "admin/conn.php";

    //fetch settings
    $settings = mysqli_query($con,"SELECT * FROM settings");
    $setting  = mysqli_fetch_array($settings);
?>

 <!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />

    <link rel="stylesheet" href="./assets/css/bootstrap.min@5.2.0.css.css" />
    <link rel="stylesheet" href="./assets/css/boxicons.min.css" />
    <link rel="stylesheet" href="./assets/css/owl.carousel.min.css" />
    <link rel="stylesheet" href="./assets/css/owl.theme.default.min.css" />
    <link rel="stylesheet" href="./assets/css/styles.css" />

    <title>About Us - <?php echo $setting['site_name']; ?></title>
  </head>
  
 <!-- ABOUT -->
 <?php require "includes/header.php"; ?>
     <script src="./javascript/jquery-3.6.0.js"></script>
    <script src="./javascript/bootstrap@5.2.0.min.js"></script>
    <script src="./javascript/owl.carousel.min.js"></script>
    <script src="./javascript/app.js"></script>
    <?php require "includes/footer.php"; ?>