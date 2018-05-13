<!DOCTYPE html>
<html>
<head>

	<title>To Do Listi</title>
	<link rel="stylesheet" type="text/css" href="/static/style.css"/>
</head>
<body>
	<div id="wrapper">


		<div id="header">

			<h1>Todo Listi</h1>

		</div>

		<div id="navigation">
			<ul>
				<li><a href="/">Heim</a></li>
				<li><a href="/new">Bæta við</a></li>
				<li><a href="/upp">Upplýsingar</a></li>

			</ul>
		</div>
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

<div id="footer">
	2018 - <strong>Lokaverkefni</strong>
	</div>
</div>

</body>
</html>