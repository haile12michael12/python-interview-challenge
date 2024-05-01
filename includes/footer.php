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
  
    <link rel="stylesheet" href="./assets/css/font-awesome.min.css" type="text/css">
    <link rel="stylesheet" href="./assets/css/themify-icons.css" type="text/css">
    <link rel="stylesheet" href="./assets/css/elegant-icons.css" type="text/css">

    <link rel="stylesheet" href="./assetscss/nice-select.css" type="text/css">
    <link rel="stylesheet" href="./assetscss/jquery-ui.min.css" type="text/css">
    <link rel="stylesheet" href="./assetscss/slicknav.min.css" type="text/css">

    <link rel="stylesheet" href="./assets/assets/css/bootstrap.min@5.2.0.css.css" />
    <link rel="stylesheet" href="./assets/assets/css/boxicons.min.css" />
    <link rel="stylesheet" href="./assets/css/owl.carousel.min.css" />
    <link rel="stylesheet" href="./assets/css/owl.theme.default.min.css" />
    <link rel="stylesheet" href="./assets/css/styles.css" />
    
    <title>yonatanbt furniture</title>
  </head>
  <body>


    <!-- Footer Start -->
    <div class="container-fluid bg-dark text-light footer mt-5 pt-5 wow fadeIn" data-wow-delay="0.1s">
        <div class="container py-5">
            <div class="row g-5">
                <div class="col-lg-3 col-md-6">
                    <div class="widget widget-company">
                            <a href="index.php"><img src="./assets/images/klogo.jpg" width="36" height="70"alt="image"></a>
                    <h2 class="text-light mb-5"> YonatanBT Furniture</h2>
                    <h4 class="text-light mb-4">Address</h4>
                    <p class="mb-2"darkclass="fa fa-map-marker-alt me-3"></i>123 Street, New York, USA</p>
                    <p class="mb-2"><i class="fa fa-phone-alt me-3"></i>+012 345 67890</p>
                    <p class="mb-2"><i class="fa fa-envelope me-3"></i>info@example.com</p>
                    <div class="d-flex pt-2">
                        <a class="btn btn-outline-light btn-social" href=""><i class="fab fa-twitter"></i></a>
                        <a class="btn btn-outline-light btn-social" href=""><i class="fab fa-facebook-f"></i></a>
                        <a class="btn btn-outline-light btn-social" href=""><i class="fab fa-youtube"></i></a>
                        <a class="btn btn-outline-light btn-social" href=""><i class="fab fa-linkedin-in"></i></a>
                    </div>
                </div>
            </div>
                <div class="col-lg-3 col-md-6">
                    <h4 class="text-light mb-4">Services</h4>
                    <a class="btn btn-link" href="">General Carpentry</a>
                    <a class="btn btn-link" href="">Furniture Remodeling</a>
                    <a class="btn btn-link" href="">Wooden Floor</a>
                    <a class="btn btn-link" href="">Wooden Furniture</a>
                    <a class="btn btn-link" href="">Custom Carpentry</a>
                </div>
                <div class="col-lg-3 col-md-6">
                    <h4 class="text-light mb-4">Quick Links</h4>
                    <a class="btn btn-link" href="about.php">About Us</a>
                    <a class="btn btn-link" href="contact.php">Contact Us</a>
                    <a class="btn btn-link" href="service.php">Our Services</a>
                    <a class="btn btn-link" href="term.php">Terms & Condition</a>
                    <a class="btn btn-link" href="support.php">Support</a>
                </div>
                <div class="col-lg-3 col-md-6">
                    <h4 class="text-light mb-4">Newsletter</h4>
                    <p>Dolor amet .</p>
                    <div class="position-relative mx-auto" style="max-width: 400px;">
                        <input class="form-control border-0 w-100 py-3 ps-4 pe-5" type="text" placeholder="Your email">
                        <button type="button" class="btn btn-primary py-2 position-absolute top-0 end-0 mt-2 me-2">SignUp</button>
                    </div>
                </div>
            </div>
        </div>
        <div class="container">
            <div class="copyright">
                <div class="row">
                    <div class="col-md-6 text-center text-md-start mb-3 mb-md-0">
                        &copy; <a class="border-bottom" href="index.hp">YonatanBT Furniture</a>, All Right Reserved.
                    </div>
                    <div class="col-md-6 text-center text-md-end">
                        Designed By <a class="border-bottom" href="index.php">IT</a>
                    </div>
                </div>
            </div>
        </div>

    </div>

  <script src=".assets/javascript/jquery-3.3.1.min.js"></script>
    <script src=".assets/javascript/bootstrap.min.js"></script>
    <script src=".assets/javascript/jquery-ui.min.js"></script>
    <script src=".assets/javascript/jquery.countdown.min.js"></script>
    <script src=".assets/javascript/jquery.nice-select.min.js"></script>
    <script src=".assets/javascript/jquery.zoom.min.js"></script>
    <script src=".assets/javascript/jquery.dd.min.js"></script>
    <script src=".assets/javascript/jquery.slicknav.js"></script>
    <script src=".assets/javascript/owl.carousel.min.js"></script>
    <script src=".assets/javascript/main.js"></script>
     <script src=".assets/javascript/jquery-3.6.0.js"></script>
    <script src=".assets/javascript/bootstrap@5.2.0.min.js"></script>
    <script src=".assets/javascript/owl.carousel.min.js"></script>
    <script src=".assets/javascript/app.js"></script>
  </body>
  </html>