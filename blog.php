<?php

    error_reporting(0);
    include "admin/conn.php";

  
    //fetch blogs 
    //fetch blog
    $blog = mysqli_query($con,"SELECT * FROM blog ORDER BY id DESC");

    //fetch category

    $cat = mysqli_query($con,"SELECT * FROM category ORDER BY id DESC");


    //fetch recent post
    $recent = mysqli_query($con,"SELECT * FROM blog ORDER BY id DESC LIMIT 4");
    
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

    <title>Our Blogs - <?php echo $setting['site_name']; ?></title>
  </head>
  <?php require "includes/header.php"; ?>
  
    <!-- BlOG -->
    <section id="blog">
      <div class="container">
        <div class="row">
          <div class="col-12 intro text-center">
            <h6>Our Blog</h6>
            <h1>Latest Blog Post</h1>
            <p>
              Contrary to popular belief, Lorem Ipsum is not simply random text.
              It has roots in a piece of classical Latin literature from 45 BC,
              making it over 2000 years old
            </p>
          </div>
        </div>
        <div class="row g-md-4">
          <div class="col-lg-4">
            <div class="blog-post">
              <a href="#blog" class="tag">Web Design</a>
              <img src="./images/project5.jpg" />
              <small>12 Dec 2022</small>
              <h4><a href="#blog">Web Design in 2022</a></h4>
              <p>
                Contrary to popular belief, Lorem Ipsum is not simply random
                text. It has roots in a piece of classical Latin literature from
                45 BC, making it over 2000 years old
              </p>
            </div>
          </div>
          <div class="col-lg-4">
            <div class="blog-post">
              <a href="#blog" class="tag">Web Design</a>
              <img src="./images/project1.jpg" />
              <small>12 Dec 2022</small>
              <h4><a href="#blog">Web Design in 2022</a></h4>
              <p>
                Contrary to popular belief, Lorem Ipsum is not simply random
                text. It has roots in a piece of classical Latin literature from
                45 BC, making it over 2000 years old
              </p>
            </div>
          </div>
          <div class="col-lg-4">
            <div class="blog-post">
              <a href="#blog" class="tag">Web Design</a>
              <img src="./images/project3.jpg" />
              <small>12 Dec 2022</small>
              <h4><a href="#blog">Web Design in 2022</a></h4>
              <p>
                Contrary to popular belief, Lorem Ipsum is not simply random
                text. It has roots in a piece of classical Latin literature from
                45 BC, making it over 2000 years old
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>
<script src="./javascript/bootstrap@5.2.0.min.js"></script>
    <script src="./javascript/owl.carousel.min.js"></script>
    <script src="./javascript/app.js"></script>
    <?php require "includes/footer.php"; ?>