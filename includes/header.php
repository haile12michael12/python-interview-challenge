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

    <title>yonatanbt furniture</title>
  </head>
  <body >
     <header class="main-header header-style-one">
    <!-- NAVBAR -->
    <nav class="top-nav" id="home">
      <div class="container">
        <div class="row justify-content-between">
          <div class="col-auto">
            <p>
              <i class="bx bxs-envelope"></i>
              <span>yonatanbtfurniture@gmail.com</span>
            </p>

            <p>
              <i class="bx bxs-phone-call"></i>
              <span>+251 995 27 2727 /911 51 6843</span>
            </p>
          </div>
         
          <div class="col-auto">
            <div class="social-links">
              <a target="_blank" href="https://www.facebook.com/ubonggjacob"
                ><i class="bx bxl-facebook"></i
              ></a>
               <a target="_blank" href="https://t.me/yonatanbt_furniture"
                ><i class="bx bxl-telegram"></i
              ></a>
              <a target="_blank" href="https://t.me/yonatanbt_furniture"
                ><i class="bx bxl-tiktok"></i
              ></a>
              <a target="_blank" href="https://www.twitter.com/in/ubonggjacob"
                ><i class="bx bxl-twitter"></i
              ></a>
              <a target="_blank" href="https://www.instagram.com/UbongJacob"
                ><i class="bx bxl-instagram"></i
              ></a>
              <a target="_blank" href="https://www.linkedin.com/in/yonatan-bt-furniture-72283521a/"
                ><i class="bx bxl-linkedin-square"></i
              ></a>

                          </div>
          </div>
        </div>
      </div>
    </nav>

    <nav class="navbar navbar-expand-lg bg-white sticky-top">
      <div class="container">
        <a class="navbar-brand" href="#">
        <img src ="assets/images/klogo.jpg" alt="" width="70" height="70">
         </a>

        <a class="navbar-brand" href="index.php">YonatanBT PLC </a>

        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNav"
          aria-controls="navbarNav"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav ms-auto">
            <li class="nav-item">
              <a class="nav-link" href="index.php">Home</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="about.php">About Us</a>
              
            </li>
            <li class="nav-item">
              <a class="nav-link" href="service.php">Services</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="job.php">Job</a>
            </li>
          
            <li class="nav-item">
              <a class="nav-link" href="office.php">Office</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="blog.php">News</a>
            </li>
             <li class="nav-item">
              <a class="nav-link" href="contact.php">Contact Us</a>
            </li>
          </ul>
          <form class="d-flex">
          <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
          
        </form>
        </div>
      </div>
      
    </nav>
  </header>
  </body>
  </html>