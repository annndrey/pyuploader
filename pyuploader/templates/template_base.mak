<!DOCTYPE html>
<html lang="${request.locale_name}">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="pyramid web application">
    ##<link rel="shortcut icon" href="${request.static_url('pyuploader:static/pyramid-16x16.png')}">

    <title>FileUploader</title>

    <!-- Bootstrap core CSS -->
    <link href="//oss.maxcdn.com/libs/twitter-bootstrap/3.0.3/css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom styles for this scaffold -->
    <link href="${request.static_url('pyuploader:static/theme.css')}" rel="stylesheet">
    <script src="//oss.maxcdn.com/libs/jquery/1.10.2/jquery.min.js"></script>
    <script src="//oss.maxcdn.com/libs/twitter-bootstrap/3.0.3/js/bootstrap.min.js"></script>
    <script src="${request.static_url('pyuploader:static/bootstrap.file-input.js')}"></script>

    <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="//oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
      <script src="//oss.maxcdn.com/libs/respond.js/1.3.0/respond.min.js"></script>
    <![endif]-->
    <script type="text/javascript">
      $(document).ready(function() {
      $('input[type=file]').bootstrapFileInput();
      });    
    </script>
  </head>

  <body>
<div class="outer">
<div class="middle">
<div class="inner">

    <div class="jumbotron">
      <div class="center">    
      <h1>Тут можно загрузить файл бесплатно без регистрации без СМС!!!1</h1>
      
      % if len(mess) > 0:
        <p>${mess}</p>
      % endif

      <form action="/upload" method="post" accept-charset="utf-8"
            enctype="multipart/form-data">
        <div class="form-group">
          <input type="checkbox" value=""> сохранить НАВСЕГДА!!1 (или будет удален через 30 дней)<br>
          <input class="alert alert-info" data-filename-placement="inside" id="anyfile" name="anyfile" type="file" value="" title="Выберите ваш файл"/></br>
          <input type="submit" class="btn btn-default" value="Отправить" />
        </div>
      </form>
      </div>
      <!-- Bootstrap core JavaScript
      ================================================== -->
      <!-- Placed at the end of the document so the pages load faster -->
    </div>
</div>
</div>
</div>
  </body>
</html>
