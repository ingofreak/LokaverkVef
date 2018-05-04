<!DOCTYPE html>
<html>
<head>
	<title></title>
</head>
<body>
	<a href="/new">Bæta Við</a>
	<p>Hlutir til að gera:</p>
<table border="1">
%for row in rows:
  <tr>
  %for col in row:
    <td>{{col}}</td>
  %end
  </tr>
%end
</table>

</body>
</html>