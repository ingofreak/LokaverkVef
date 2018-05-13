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
<p>Edit the task with ID = {{no}}</p>
<form action="/edit/{{no}}" method="get">
  <input type="text" name="task" value="{{old[0]}}" size="100" maxlength="100">
  <select name="status">
    <option>open</option>
    <option>closed</option>
  </select>
  <br>
  <input type="submit" name="save" value="save">
</form>

<div id="footer">
	2018 - <strong>Lokaverkefni</strong>
	</div>
</div>

</body>
</html>