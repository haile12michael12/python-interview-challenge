<?php
    include "admin/conn.php";

    //fetch settings
    $settings = mysqli_query($con,"SELECT * FROM settings");
    $setting  = mysqli_fetch_array($settings);


    // fetch testimonials
    $testi = mysqli_query($con,"SELECT * FROM testimonials");

    //fetch blog
    $blog = mysqli_query($con,"SELECT * FROM blog");


     //fetch services
    $services = mysqli_query($con,"SELECT * FROM services ORDER BY id DESC LIMIT 3");

?>
<?php require "includes/header.php"; ?>

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
     <meta name="description" content="" />
     <meta name="keywords" content="bootstrap, bootstrap4" />
  <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap" rel="stylesheet">
    <!-- Bootstrap CSS -->
    <link href="./assets/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ" crossorigin="anonymous">
    <link href="./assets/css/tiny-slider.css" rel="stylesheet">
    <link rel="stylesheet" href="./assets/css/boxicons.min.css" />
    <link rel="stylesheet" href="./assets/css/owl.carousel.min.css" />
    <link rel="stylesheet" href="./assets/css/owl.theme.default.min.css" />
    <link rel="stylesheet" href="./assets/css/styles.css" />
    <link rel="preconnect" href="https://fonts.gstatic.com">
 <link href=".assets/images/favicon.ico" rel="icon">
    <title><?php echo $setting['site_name']; ?> -yonatanbt furniture</title>
    <style>

.hero {
  background: #3b5d50;
  padding: calc(4rem - 30px) 0 0rem 0; }
  @media (min-width: 768px) {
    .hero {
      padding: calc(4rem - 30px) 0 4rem 0; } }
  @media (min-width: 992px) {
    .hero {
      padding: calc(8rem - 30px) 0 8rem 0; } }
  .hero .intro-excerpt {
    position: relative;
    z-index: 4; }
    @media (min-width: 992px) {
      .hero .intro-excerpt {
        max-width: 450px; } }
  .hero h1 {
    font-weight: 700;
    color: #ffffff;
    margin-bottom: 30px; }
    @media (min-width: 1400px) {
      .hero h1 {
        font-size: 54px; } }
  .hero p {
    color: rgba(255, 255, 255, 0.5);
    margin-botom: 30px; }
  .hero .hero-img-wrap {
    position: relative; }
    .hero .hero-img-wrap img {
      position: relative;
      top: 0px;
      right: 0px;
      z-index: 2;
      max-width: 780px;
      left: -20px; }
      @media (min-width: 768px) {
        .hero .hero-img-wrap img {
          right: 0px;
          left: -100px; } }
      @media (min-width: 992px) {
        .hero .hero-img-wrap img {
          left: 0px;
          top: -80px;
          position: absolute;
          right: -50px; } }
      @media (min-width: 1200px) {
        .hero .hero-img-wrap img {
          left: 0px;
          top: -80px;
          right: -100px; } }
    .hero .hero-img-wrap:after {
      content: "";
      position: absolute;
      width: 255px;
      height: 217px;
      background-image: url("../images/dots-light.svg");
      background-size: contain;
      background-repeat: no-repeat;
      right: -100px;
      top: -0px; }
      @media (min-width: 1200px) {
        .hero .hero-img-wrap:after {
          top: -40px; } }
    </style>
  </head>
  <body>

<div id="preloader">
        <div class="loader"></div>
    </div>

    <div class="hero">
        <div class="container">
          <div class="row justify-content-between">
            <div class="col-lg-5">
              <div class="intro-excerpt">
                <h1>Modern Design <span clsas="d-block">Elevate Your Home With Exquisite Wood Furniture</span></h1>
                <p class="mb-4">Donec vitae odio quis nisl dapibus malesuada. Nullam ac aliquet velit. Aliquam vulputate velit imperdiet dolor tempor tristique.</p>
                <p><a href="" class="btn btn-secondary me-2">Shop Now</a><a href="#" class="btn btn-white-outline">Explore</a></p>
              </div>
            </div>
            <div class="col-lg-7">
              <div class="hero-img-wrap">
                <img src="./assets/images/couch.jpg" class="img-fluid">
              </div>
            </div>
          </div>
        </div>
      </div>
    
  <?php include"pages/catagories.php"; ?>

        
    <!-- Feature Start -->
    <div class="container-xxl py-5">
        <div class="container">
            <div class="row g-5">
                <div class="col-md-6 col-lg-3 wow fadeIn" data-wow-delay="0.1s">
                    <div class="d-flex align-items-center justify-content-between mb-2">
                        <div class="d-flex align-items-center justify-content-center bg-light" style="width: 60px; height: 60px;">
                            <i class="fa fa-user-check fa-2x text-primary"></i>
                        </div>
                        <h1 class="display-1 text-light mb-0">01</h1>
                    </div>
                    <h5>Creative Designers</h5>
                </div>
                <div class="col-md-6 col-lg-3 wow fadeIn" data-wow-delay="0.3s">
                    <div class="d-flex align-items-center justify-content-between mb-2">
                        <div class="d-flex align-items-center justify-content-center bg-light" style="width: 60px; height: 60px;">
                            <i class="fa fa-check fa-2x text-primary"></i>
                        </div>
                        <h1 class="display-1 text-light mb-0">02</h1>
                    </div>
                    <h5>Quality Products</h5>
                </div>
                <div class="col-md-6 col-lg-3 wow fadeIn" data-wow-delay="0.5s">
                    <div class="d-flex align-items-center justify-content-between mb-2">
                        <div class="d-flex align-items-center justify-content-center bg-light" style="width: 60px; height: 60px;">
                            <i class="fa fa-drafting-compass fa-2x text-primary"></i>
                        </div>
                        <h1 class="display-1 text-light mb-0">03</h1>
                    </div>
                    <h5>Free Consultation</h5>
                </div>
                <div class="col-md-6 col-lg-3 wow fadeIn" data-wow-delay="0.7s">
                    <div class="d-flex align-items-center justify-content-between mb-2">
                        <div class="d-flex align-items-center justify-content-center bg-light" style="width: 60px; height: 60px;">
                            <i class="fa fa-headphones fa-2x text-primary"></i>
                        </div>
                        <h1 class="display-1 text-light mb-0">04</h1>
                    </div>
                    <h5>Customer Support</h5>
                </div>
            </div>
        </div>
    </div>
    <!-- Feature Start -->



    

   <?php include"pages/notification.php"; ?>
   <?php include"pages/gallery.php"; ?>
 <?php include"pages/testimonial.php"; ?>

<section class="bg-secondary pt-5">
    <div class="container">
      <div class="row justify-content-center pt-5 my-5">
        <div class="col-md-6 pt-5 text-center">
          <h2 class="display-5 pt-5 fw-bold">Why Choose us?</h2>
          <p class="text-dark">Lorem ip odio ratione consectetur consequatur excepturi natus illo illum incidunt minus fuga quod enim omnis!</p>
        </div>
      </div>

      <div class="row mb-5">
        <div class="col-md-3" data-aos="fade-in" data-aos-delay="0">
          <div class="py-5">
            <div class="row g-1">
              <div class="col-md-3">
                <svg width="40" height="40" viewBox="0 0 24 24" class="text-dark"><use xlink:href="#check"></use></svg>
              </div>
              <div class="col-md-9">
                <h5 class="text-capitalize my-1">High Quality</h5>
                <p class="text-dark">At imperdiet dui accumsan sit amet quis.</p>
              </div>
            </div>
          </div>
        </div>
        <div class="col-md-3" data-aos="fade-in" data-aos-delay="300">
          <div class="py-5">
            <div class="row g-1">
              <div class="col-md-3">
                <svg width="40" height="40" viewBox="0 0 24 24" class="text-dark"><use xlink:href="#cart"></use></svg>
              </div>
              <div class="col-md-9">
                <h5 class="text-capitalize my-1">Wide Variety</h5>
                <p class="text-dark">At imperdiet dui accumsan sit amet quis.</p>
              </div>
            </div>
          </div>
        </div>
        <div class="col-md-3" data-aos="fade-in" data-aos-delay="600">
          <div class="py-5">
            <div class="row g-1">
              <div class="col-md-3">
                <svg width="40" height="40" viewBox="0 0 24 24" class="text-dark"><use xlink:href="#heart"></use></svg>
              </div>
              <div class="col-md-9">
                <h5 class="text-capitalize my-1">Popular Brands</h5>
                <p class="text-dark">At imperdiet dui accumsan sit amet quis.</p>
              </div>
            </div>
          </div>
        </div>
        <div class="col-md-3" data-aos="fade-in" data-aos-delay="900">
          <div class="py-5">
            <div class="row g-1">
              <div class="col-md-3">
                <svg width="40" height="40" viewBox="0 0 24 24" class="text-dark"><use xlink:href="#arrow-cycle"></use></svg>
              </div>
              <div class="col-md-9">
                <h5 class="text-capitalize my-1">Home Delivery</h5>
                <p class="text-dark">At imperdiet dui accumsan sit amet quis.</p>
              </div>
            </div>
          </div>
        </div>
        <div class="col-md-3" data-aos="fade-in" data-aos-delay="0">
          <div class="py-5">
            <div class="row g-1">
              <div class="col-md-3">
                <svg width="40" height="40" viewBox="0 0 24 24" class="text-dark"><use xlink:href="#calendar"></use></svg>
              </div>
              <div class="col-md-9">
                <h5 class="text-capitalize my-1">Free Installation</h5>
                <p class="text-dark">At imperdiet dui accumsan sit amet quis.</p>
              </div>
            </div>
          </div>
        </div>
        <div class="col-md-3" data-aos="fade-in" data-aos-delay="300">
          <div class="py-5">
            <div class="row g-1">
              <div class="col-md-3">
                <svg width="40" height="40" viewBox="0 0 24 24" class="text-dark"><use xlink:href="#shopping-bag"></use></svg>
              </div>
              <div class="col-md-9">
                <h5 class="text-capitalize my-1">Pick up in store</h5>
                <p class="text-dark">At imperdiet dui accumsan sit amet quis.</p>
              </div>
            </div>
          </div>
        </div>
        <div class="col-md-3" data-aos="fade-in" data-aos-delay="600">
          <div class="py-5">
            <div class="row g-1">
              <div class="col-md-3">
                <svg width="40" height="40" viewBox="0 0 24 24" class="text-dark"><use xlink:href="#gift"></use></svg>
              </div>
              <div class="col-md-9">
                <h5 class="text-capitalize my-1">Special packaging</h5>
                <p class="text-dark">At imperdiet dui accumsan sit amet quis.</p>
              </div>
            </div>
          </div>
        </div>
        <div class="col-md-3" data-aos="fade-in" data-aos-delay="900">
          <div class="py-5">
            <div class="row g-1">
              <div class="col-md-3">
                <svg width="40" height="40" viewBox="0 0 24 24" class="text-dark"><use xlink:href="#arrow-cycle"></use></svg>
              </div>
              <div class="col-md-9">
                <h5 class="text-capitalize my-1">free global returns</h5>
                <p class="text-dark">At imperdiet dui accumsan sit amet quis.</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    
    </div>
    <style>

    </style>
  </section>
    <script src="./assets/javascript/jquery-3.6.0.js"></script>
    <script src="./assets/javascript/bootstrap@5.2.0.min.js"></script>
    <script src="./assets/javascript/owl.carousel.min.js"></script>
    <script src="./javascript/app.js"></script>
   
    <?php require "includes/footer.php"; ?>

  </body>
</html>
