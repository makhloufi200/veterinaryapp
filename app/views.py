from django.shortcuts import render
import os, errno, shutil
from django.contrib import messages
from datetime import datetime
# Create your views here.

def home(request):

    context = {
        "name": "Home"
    }

    return render(request, 'index.html', context)

	
def exportdatabase(request):
	command = "python manage.py"
	#create folder for exporting database
	dirname = datetime.now().strftime('%Y.%m.%d')
	#os.mkdir(os.path.join('save'))
	try:
		os.mkdir(os.path.join('save/'+dirname))
	except OSError as e:
		if e.errno != errno.EEXIST:
			pass
		else:
			print(e)
	#lanch export database script		
	run_script = fr"""call export_database.bat"""

	os.system(run_script)
	messages.add_message(request,messages.INFO,'Export Database avec Success')
	#move file to folder save
	try:
		shutil.move('db.json','save/'+dirname)
	except OSError as e:
		if e.errno != errno.EEXIST:
			pass
		else:
			print(e)
	context = {
        "name": "Home"
    }

	return render(request, 'index.html', context)
	
def importdatabase(request):
	command = "python manage.py"
	run_script = fr"""call import_database.bat"""

	os.system(run_script)
	messages.add_message(request,messages.INFO,'Import Database avec Success')
	context = {
        "name": "Home"
    }

	return render(request, 'index.html', context)	