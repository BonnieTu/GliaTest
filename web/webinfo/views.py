import random
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
	excuse = [
		"That feature was slated for phase two",
		"I told you yesterday it would be done by the end of today",
		"You must have done something wrong",
		"It's a browser compatibility issue",
		"Why do you want to do it that way"
	]

	output = """
	<!DOCTYPE html>
	<html>
	<head>
		<title>Excuses For Lazy Coders</title>
	</head>
	<body style="height= 100%; background: black ">
	<div style="text-align: center;height: 90vh; color: white">
		<a href="/" style="text-decoration:none; color:white; font-size: 2em; line-height: 100vh;">{sen}</a>
	</div>
	<div sytle="text-align:center; color: white; background: white; height: 10vh; font-size: 1em">
		© Copyright 2012 - 2016 programmingexcuses.com - All Rights Reserved
	</div>
	</body>
	</html>
	""".format(sen=random.choice(excuse))

	return HttpResponse(output)