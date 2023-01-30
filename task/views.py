from django.shortcuts import render
from .models import File


def view_(request):
    counter = 0
    filename = ''
    list_of_word = []
    wordcount = ''
    if request.method == 'POST':
        try:
            filename = request.POST['filename']
            with open(filename, 'r') as file:
                text = file.read()
            text_list = text.lower().split(' ')
            list_of_word = []
            for word in text_list:
                word = word.strip()
                list_of_word.append(word)
            File.objects.create(file=filename, list_of_word=list_of_word)
        except:
            filename = File.objects.order_by().last().file

    if request.method == 'GET':
        try:
            filename = File.objects.order_by().last().file
            wordcount = request.GET['wordcount']

            with open(filename, 'r') as file:
                text = file.read()
            text_list = text.lower().split(' ')
            list_of_word = []
            for word in text_list:
                word = word.strip()
                list_of_word.append(word)

            for word in list_of_word:
                if word == wordcount:
                    counter += 1

            if request.GET['delete_'] == 'Delete':
                File.objects.order_by().last().delete()
                filename = File.objects.order_by().last().file

        except:
            wordcount = ''

    return render(request, 'view_.html', {'filename': filename, "list_of_word": list_of_word, 'wordcount': wordcount, "counter": counter,})
