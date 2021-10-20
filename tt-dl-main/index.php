<!DOCTYPE HTML>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="Download video tiktok anti watermark">
    <meta name="author" content="putri">
    <title>Tiktok Downloader</title>
    <link rel="icon" href="https://i.ibb.co/0JmCRL1/97fe5e8c-4cae-4de7-ba34-6e8b967441d7.png">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <style type="text/css">
      @import url('https://fonts.googleapis.com/css2?family=Baloo+Chettan+2:wght@500&display=swap');
      * {font-family: 'Baloo Chettan 2', Sans-Serif;}body {background: #d3d3d3;}
    </style>
  </head>
<body>
  <div class="container mb-4">
    <div class="card mt-4">
      <div class="card-header">
        Tiktok Downloader No Watermark
      </div>
      <div class="card-body">
        <form action="" method="post">
          <div class="form-group">
            <input type="text" name="url" placeholder="link video tiktok" class="form-control" />
          </div>
          <div class="form-group text-center mt-2">
            <button type="submit" name="submit" class="btn btn-sm btn-warning">download</button>
          </div>
        </form>
      </div>
    </div>
    <?php
         if(isset($_POST["submit"])){
           ?>
             <div class="card mt-4">
             <div class="card-header">
              Hasil
              </div>
            <div class="card-body justify-content-center text-center">
           <?php
           $url = $_POST["url"];
           if(empty($url)){
             ?>
               <div class="alert alert-danger mb-3">
                isi link video tiktoknya
               </div>
             <?php
           }else {
             $cek = file_get_contents("https://tt-dl.herokuapp.com/?url=".$url);
             $dec = json_decode($cek, true);
             $cari = strpos($cek, "status");
             if($cari){
               ?>
                 <div class="alert alert-danger mb-3">
                  <?= $dec["message"]; ?>
                 </div>
                </div>
               <?php
             } else {
               ?>
                  <video width="300" height="200" controls>
                    <source src="<?= $dec["download"]; ?>" type="video/mp4">
                   </video>
                </div>
                <div class="mt-2 text-center mb-4">
                  <a href="<?= $dec["src-dl"]; ?>" class="btn btn-primary text-uppercase" target="_blank">Download</a>
                </div>
               <?php
             }
           }
           ?>
            </div>
           <?php
         }
        ?>
  </div>
</body>
</html>