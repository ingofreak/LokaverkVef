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
	<p>{{ttitle}}</p>


<button onClick="goBack()">Back</button> <button  onClick="location.href='/edit/{{todoid}}'"type="button">Edit</button>
<script>
	function goBack() {
		window.history.back();
	}
</script>

<div id="footer">
	2018 - <strong>Lokaverkefni</strong>
	</div>
</div>

</body>
</html>