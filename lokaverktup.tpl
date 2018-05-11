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
    <td><a href="/item{{row[0]}}">{{col}}</a></td>
  %end
  </tr>
%end
</table>

</body>
</html>